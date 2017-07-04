import math


class Rotate:
    def __init__(self):
        pass

    @staticmethod
    def rotate(point, origin, angle_deg):
        """
        Rotate.py a point counterclockwise by a given angle around a given origin.

        The angle should be given in degrees.
        """
        ox, oy = origin
        px, py = point
        angle = Rotate.deg_to_rad(angle_deg)

        px_ox_diff = px - ox
        py_oy_diff = py - oy
        sin_angle = math.sin(angle)
        cos_angle = math.cos(angle)

        qx = ox + cos_angle * px_ox_diff - sin_angle * py_oy_diff
        qy = oy + sin_angle * px_ox_diff + cos_angle * py_oy_diff
        return int(qx), int(qy)

    @staticmethod
    def deg_to_rad(deg):
        return deg * math.pi / 180

    @staticmethod
    def rotated_line(p1, p2, center, angle):
        p1rotated = Rotate.rotate(p1, center, angle)
        p2rotated = Rotate.rotate(p2, center, angle)

        return p1rotated, p2rotated
