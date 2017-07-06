import cv2
import numpy

from Draw.InRectangle import InRectangle
from Draw.Rotate import Rotate


class Pitch:
    def __init__(self):
        pass

    drawing_area = ((140, 100), (500, 360))

    @staticmethod
    def draw(img, hud, color):

        pitch_line_offset = int(hud.ang_y * 7)
        img_width = img.shape[1]
        img_height = img.shape[0]
        center_point = (img_width // 2, img_height // 2)

        cv2.rectangle(img, Pitch.drawing_area[0], Pitch.drawing_area[1], color, 1, cv2.CV_AA)

        for i in range(-90, 90, 10):
            Pitch.child_line(img, color, pitch_line_offset, hud.ang_x, i)

        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(img, "roll: ", (25, 60), font, 1, color, 1, cv2.CV_AA)
        cv2.putText(img, "{:4.1f}".format(hud.ang_x).rjust(10), (40, 60), font, 1, color, 1, cv2.CV_AA)
        cv2.putText(img, "pitch:", (15, 75), font, 1, color, 1, cv2.CV_AA)
        cv2.putText(img, "{:4.1f}".format(hud.ang_y).rjust(10), (40, 75), font, 1, color, 1, cv2.CV_AA)
        cv2.putText(img, "head: ", (20, 90), font, 1, color, 1, cv2.CV_AA)
        cv2.putText(img, "{:4.1f}".format(hud.heading).rjust(10), (38, 90), font, 1, color, 1, cv2.CV_AA)

    @staticmethod
    def child_line(img, color, pitch_line_offset, ang_x, angle):
        pitch_line_offset = pitch_line_offset - angle * 7
        line_points_1 = Rotate.rotate((230, 240 + pitch_line_offset), (320, 240), ang_x)
        line_points_2 = Rotate.rotate((270, 240 + pitch_line_offset), (320, 240), ang_x)
        Pitch.draw_line(img, line_points_1, line_points_2, color)

        line_points_1 = Rotate.rotate((370, 240 + pitch_line_offset), (320, 240), ang_x)
        line_points_2 = Rotate.rotate((410, 240 + pitch_line_offset), (320, 240), ang_x)
        Pitch.draw_line(img, line_points_1, line_points_2, color)

        if angle > 0:
            Pitch.top(img, color, pitch_line_offset, ang_x)
            line_points_1 = Rotate.rotate((400, 240 + pitch_line_offset - 5), (320, 240), ang_x)
            if InRectangle.contains(Pitch.drawing_area, line_points_1):
                cv2.putText(img, "{:2.0f}".format(angle).rjust(3), line_points_1,
                            cv2.FONT_HERSHEY_PLAIN, 1, color, 1, cv2.CV_AA)
        elif angle < 0:
            Pitch.bottom(img, color, pitch_line_offset, ang_x)
            line_points_1 = Rotate.rotate((400, 240 + pitch_line_offset + 15), (320, 240), ang_x)
            if InRectangle.contains(Pitch.drawing_area, line_points_1):
                cv2.putText(img, "{:2.0f}".format(angle).rjust(3), line_points_1,
                            cv2.FONT_HERSHEY_PLAIN, 1, color, 1, cv2.CV_AA)

    @staticmethod
    def top(img, color, pitch_line_offset, ang_x):
        line_points_1 = Rotate.rotate((410, 240 + pitch_line_offset), (320, 240), ang_x)
        line_points_2 = Rotate.rotate((410, 250 + pitch_line_offset), (320, 240), ang_x)
        Pitch.draw_line(img, line_points_1, line_points_2, color)

        line_points_1 = Rotate.rotate((230, 240 + pitch_line_offset), (320, 240), ang_x)
        line_points_2 = Rotate.rotate((230, 250 + pitch_line_offset), (320, 240), ang_x)
        Pitch.draw_line(img, line_points_1, line_points_2, color)

    @staticmethod
    def bottom(img, color, pitch_line_offset, ang_x):
        line_points_1 = Rotate.rotate((410, 240 + pitch_line_offset), (320, 240), ang_x)
        line_points_2 = Rotate.rotate((410, 230 + pitch_line_offset), (320, 240), ang_x)
        Pitch.draw_line(img, line_points_1, line_points_2, color)

        line_points_1 = Rotate.rotate((230, 240 + pitch_line_offset), (320, 240), ang_x)
        line_points_2 = Rotate.rotate((230, 230 + pitch_line_offset), (320, 240), ang_x)
        Pitch.draw_line(img, line_points_1, line_points_2, color)

    @staticmethod
    def draw_line(img, line_points_1, line_points_2, color, ):
        if InRectangle.contains(Pitch.drawing_area, line_points_1) or \
                InRectangle.contains(Pitch.drawing_area, line_points_2):
            cv2.line(img, line_points_1, line_points_2, color, 1, cv2.CV_AA)
