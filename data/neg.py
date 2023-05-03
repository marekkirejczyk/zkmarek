class CPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    ...

    def neg(self):
        return CPoint(self.x, -self.y)
