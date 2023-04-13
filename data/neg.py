class CPoint:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    ...

    def neg(self):
        return CPoint(self.x, -self.y)
