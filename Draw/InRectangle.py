class InRectangle:
    def __init__(self):
        pass

    @staticmethod
    def contains(rect, point):
        # (140, 100), (500, 360)
        return (rect[0][0] <= point[0] <= rect[1][0] and
                rect[0][1] <= point[1] <= rect[1][1])
