import cv2


class Altitude:
    def __init__(self):
        pass

    drawing_area = ((510, 100), (600, 360))

    @staticmethod
    def draw(img, hud, color):
        cv2.rectangle(img, Altitude.drawing_area[0], Altitude.drawing_area[1], color, 1, cv2.CV_AA)

        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(img, "est alt: ", (510, 60), font, 1, color, 1, cv2.CV_AA)
        cv2.putText(img, "{:4.1f}".format(hud.est_alt).rjust(10), (530, 60), font, 1, color, 1, cv2.CV_AA)
        cv2.putText(img, "bar alt:", (510, 75), font, 1, color, 1, cv2.CV_AA)
        cv2.putText(img, "{:4.1f}".format(hud.bar_alt).rjust(10), (530, 75), font, 1, color, 1, cv2.CV_AA)
        cv2.putText(img, "ver spd:", (510, 90), font, 1, color, 1, cv2.CV_AA)
        cv2.putText(img, "{:4.1f}".format(hud.vertical_speed).rjust(10), (530, 90), font, 1, color, 1, cv2.CV_AA)
