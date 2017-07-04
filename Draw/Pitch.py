import cv2
import numpy

from Draw.Rotate import Rotate


class Pitch:
    def __init__(self):
        pass

    @staticmethod
    def draw(img, hud, color):

        pitch_line_offset = int(hud.angy * 10)
        img_width = img.shape[1]
        img_height = img.shape[0]
        center_point = (img_width // 2, img_height // 2)

        Pitch.child_line(img, color, pitch_line_offset, hud.angx, 50)
        Pitch.child_line(img, color, pitch_line_offset, hud.angx, 40)
        Pitch.child_line(img, color, pitch_line_offset, hud.angx, 30)
        Pitch.child_line(img, color, pitch_line_offset, hud.angx, 20)
        Pitch.child_line(img, color, pitch_line_offset, hud.angx, 10)
        Pitch.child_line(img, color, pitch_line_offset, hud.angx, 0)
        Pitch.child_line(img, color, pitch_line_offset, hud.angx, -10)
        Pitch.child_line(img, color, pitch_line_offset, hud.angx, -20)
        Pitch.child_line(img, color, pitch_line_offset, hud.angx, -30)
        Pitch.child_line(img, color, pitch_line_offset, hud.angx, -40)
        Pitch.child_line(img, color, pitch_line_offset, hud.angx, -50)

        # cv2.rectangle(img, (384, 0), (510, 128), color, 3)

        pts = numpy.array([[10, 5], [20, 30], [70, 20], [50, 10]], numpy.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, color)

        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(img, 'OpenCV', (10, 460), font, 1, color, 1, cv2.CV_AA)
        cv2.putText(img, "{:4.1f}".format(hud.angx).rjust(10), (40, 60), font, 1, color, 1, cv2.CV_AA)
        cv2.putText(img, "{:4.1f}".format(hud.angy).rjust(10), (40, 75), font, 1, color, 1, cv2.CV_AA)
        cv2.putText(img, "{:4.1f}".format(hud.heading).rjust(10), (38, 90), font, 1, color, 1, cv2.CV_AA)

    @staticmethod
    def child_line(img, color, pitch_line_offset, angx, angle):
        pitch_line_offset = pitch_line_offset - angle * 10
        line_points_1 = Rotate.rotate((230, 240 + pitch_line_offset), (320, 240), angx)
        line_points_2 = Rotate.rotate((270, 240 + pitch_line_offset), (320, 240), angx)
        cv2.line(img, line_points_1, line_points_2, color, 1, cv2.CV_AA)

        line_points_1 = Rotate.rotate((370, 240 + pitch_line_offset), (320, 240), angx)
        line_points_2 = Rotate.rotate((410, 240 + pitch_line_offset), (320, 240), angx)
        cv2.line(img, line_points_1, line_points_2, color, 1, cv2.CV_AA)

        if angle > 0:
            Pitch.top(img, color, pitch_line_offset, angx)
            line_points_1 = Rotate.rotate((400, 240 + pitch_line_offset - 5), (320, 240), angx)
            cv2.putText(img, "{:2.0f}".format(angle).rjust(3), line_points_1,
                        cv2.FONT_HERSHEY_PLAIN, 1, color, 1, cv2.CV_AA)
        elif angle < 0:
            Pitch.bottom(img, color, pitch_line_offset, angx)
            line_points_1 = Rotate.rotate((400, 240 + pitch_line_offset + 15), (320, 240), angx)
            cv2.putText(img, "{:2.0f}".format(angle).rjust(3), line_points_1,
                        cv2.FONT_HERSHEY_PLAIN, 1, color, 1, cv2.CV_AA)

    @staticmethod
    def top(img, color, pitch_line_offset, angx):
        line_points_1 = Rotate.rotate((410, 240 + pitch_line_offset), (320, 240), angx)
        line_points_2 = Rotate.rotate((410, 250 + pitch_line_offset), (320, 240), angx)
        cv2.line(img, line_points_1, line_points_2, color, 1, cv2.CV_AA)
        line_points_1 = Rotate.rotate((230, 240 + pitch_line_offset), (320, 240), angx)
        line_points_2 = Rotate.rotate((230, 250 + pitch_line_offset), (320, 240), angx)
        cv2.line(img, line_points_1, line_points_2, color, 1, cv2.CV_AA)

    @staticmethod
    def bottom(img, color, pitch_line_offset, angx):
        line_points_1 = Rotate.rotate((410, 240 + pitch_line_offset), (320, 240), angx)
        line_points_2 = Rotate.rotate((410, 230 + pitch_line_offset), (320, 240), angx)
        cv2.line(img, line_points_1, line_points_2, color, 1, cv2.CV_AA)
        line_points_1 = Rotate.rotate((230, 240 + pitch_line_offset), (320, 240), angx)
        line_points_2 = Rotate.rotate((230, 230 + pitch_line_offset), (320, 240), angx)
        cv2.line(img, line_points_1, line_points_2, color, 1, cv2.CV_AA)
