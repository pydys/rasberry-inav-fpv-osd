#!/usr/bin/python

import math
import numpy
import time

import cv2

from Connector.MspConnector import MspConnector
from DataModel.Hud import Hud
from Draw.Pitch import Pitch
from Draw.PlaneSymbol import PlaneSymbol

cap = cv2.VideoCapture(0)
frameNumber = numpy.int64(0)
start = time.time()
color = (0, 255, 0)
hud = Hud()
msp = MspConnector("/dev/ttyACM0", hud)

while True:
    frameNumber += 1
    # Capture frame-by-frame
    ret, img = cap.read()

    # Our operations on the frame come here
    # img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Draw Center pointer
    PlaneSymbol.draw(img, hud)

    # Draw a pich line
    Pitch.draw(img, hud, color)

    # End time
    end = time.time()

    # Time elapsed
    seconds = end - start

    font = cv2.FONT_HERSHEY_PLAIN
    fps = "%10.2f fps" % (frameNumber / seconds)
    cv2.putText(img, fps, (10, 450), font, 1, color, 1, cv2.CV_AA)
    cv2.putText(img, frameNumber.astype('|S10'), (10, 440), font, 1, color, 1, cv2.CV_AA)

    # cv2.ellipse(img, (256, 256), (100, 100), 0, 40 + frameNumber, 160 + frameNumber, 255, 0)

    # Display the resulting frame
    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
