import numpy as np
class Curve:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @staticmethod
    def from_x(x, sgn = 1):
        y = sum(((x+1)**k*np.sin(k*np.pi*(x+1)/3)+0.3) / np.math.factorial(k)/k**k/np.math.factorial(k)/k**k/k for k in range(1, 101))
        return Curve(x, -y) if sgn < 0 else Curve(x, y)

    def __neg__(self):
        return Curve(self.x, -self.y)

    def double(self):
        if self == INFINITY:
            return INFINITY
        slope = (3 * self.x ** 2) / (2 * self.y)
        x = slope ** 2 - 2 * self.x
        y = slope * (self.x - x) - self.y
        return Curve(x, y)

    def __add__(self, other):
        if self.x == other.x and self.y == other.y:
            return self.double()
        elif self.x == other.x and self.y == -other.y:
            return INFINITY
        elif self == INFINITY:
            return other
        elif other == INFINITY:
            return self
        else:
            slope = (other.y - self.y) / (other.x - self.x)
            x = slope ** 2 - self.x - other.x
            y = slope * (self.x - x) - self.y
            return Curve(x, y)

    def __eq__(self, __value: "Curve") -> bool: # type: ignore
        return self.x == __value.x and self.y == __value.y

    def __repr__(self):
        return f"Curve({self.x}, {self.y})"


INFINITY = Curve(0, 0)
