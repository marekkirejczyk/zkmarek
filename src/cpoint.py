import math

class CPoint:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    @staticmethod
    def from_compressed(x, sgn = 1):
        y_squared = x ** 3 + 7
        y = math.sqrt(y_squared)
        return CPoint(x, -y) if sgn < 0 else CPoint(x, y)

    def x(self):
        return self.x

    def y(self):
        return self.y

    def neg(self):
        return CPoint(self.x, -self.y)

    def __add__(self, other):
        # if self.x == other.x and self.y == other.y:
        #     return self.double()
        # elif self.x == other.x and self.y == -other.y:
        #     return CPoint(0, 0)
        # else:
        slope = (other.y - self.y) / (other.x - self.x)
        x = slope ** 2 - self.x - other.x
        y = slope * (self.x - x) - self.y
        return CPoint(x, y)

    def to_coord(self, ax):
        return ax.c2p(self.x, self.y)
