import math

class CECAffine:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @staticmethod
    def from_compressed(x, sgn = 1):
        y_squared = x ** 3 + 7
        y = math.sqrt(y_squared)
        return CECAffine(x, -y) if sgn < 0 else CECAffine(x, y)

    def __neg__(self):
        return CECAffine(self.x, -self.y)

    def __add__(self, other):
        # if self.x == other.x and self.y == other.y:
        #     return self.double()
        # elif self.x == other.x and self.y == -other.y:
        #     return CPoint(0, 0)
        # else:
        slope = (other.y - self.y) / (other.x - self.x)
        x = slope ** 2 - self.x - other.x
        y = slope * (self.x - x) - self.y
        return CECAffine(x, y)
