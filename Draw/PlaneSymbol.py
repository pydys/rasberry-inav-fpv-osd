import cv2
from Draw.Rotate import Rotate


class PlaneSymbol:
    # Draw Center pointer
    def __init__(self):
        pass

    @staticmethod
    def draw(img, hud):
        center_point = (img.shape[1] // 2, img.shape[0] // 2)

        cv2.circle(img, center_point, 15, (0, 255, 0), 1, cv2.CV_AA)
        p1 = (270, 240)
        p2 = (370, 240)
        # rotated_line = Rotate.rotated_line(p1, p2, center_point, hud.angx)
        cv2.line(img, p1, p2, (50, 255, 20), 1, cv2.CV_AA)

        p1 = (290, 240)
        p2 = (290, 250)
        # rotated_line = Rotate.rotated_line(p1, p2, center_point, hud.angx)
        cv2.line(img, p1, p2, (50, 255, 20), 1, cv2.CV_AA)

        p1 = (350, 240)
        p2 = (350, 250)
        # rotated_line = Rotate.rotated_line(p1, p2, center_point, hud.angx)
        cv2.line(img, p1, p2, (50, 255, 20), 1, cv2.CV_AA)


