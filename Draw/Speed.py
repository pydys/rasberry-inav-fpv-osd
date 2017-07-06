import cv2


class Speed:
    def __init__(self):
        pass

    drawing_area = ((30, 100), (130, 360))

    @staticmethod
    def draw(img, hud, color):
        cv2.rectangle(img, Speed.drawing_area[0], Speed.drawing_area[1], color, 1, cv2.CV_AA)
