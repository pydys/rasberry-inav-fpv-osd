import threading
import logging
from time import sleep

from DataModel.Hud import Hud
from lib.pyMultiwii import MultiWii

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )


class MspConnector:
    board = None
    port = "/dev/ttyACM0"

    def __init__(self, port, hud):
        self.port = port
        self.lock = threading.Lock()
        self.hud = hud
        self.board = MultiWii(self.port)
        # process data
        worker = threading.Thread(target=self.process_data)
        worker.start()

    def process_data(self):
        while True:
            altitude_new = self.board.getData(MultiWii.ALTITUDE)
            print altitude_new
            if isinstance(altitude_new, dict):
                self.lock.acquire()
                try:
                    self.hud.vertical_speed = float(altitude_new['vario'] // 10) / 10
                    self.hud.est_alt = float(altitude_new['estalt'] // 10) / 10
                    self.hud.bar_alt = float(altitude_new['baralt'] // 10) / 10
                finally:
                    self.lock.release()
            sleep(0.05)

            attitude_new = self.board.getData(MultiWii.ATTITUDE)
            print attitude_new
            if isinstance(attitude_new, dict):
                self.lock.acquire()
                try:
                    self.hud.ang_x = attitude_new['angx']
                    self.hud.ang_y = -1 * attitude_new['angy']
                    self.hud.heading = attitude_new['heading']
                finally:
                    self.lock.release()
            sleep(0.05)

            print "Msp loop done"
