class Curve:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @staticmethod
    def from_x(x, sgn = 1):
        y = 4.26713027e-09 * x ** (15)  -5.00493029e-07 * x ** (14) +  2.67032132e-05 * x ** (13) -8.57314665e-04* x ** (12) +1.84604634e-02 * x ** (11)
        -2.81249901e-01* x ** (10) +  3.11615153e+00 * x ** (9) 
        -2.54062977e+01 * x ** (8) +1.52442624e+02 * x ** (7) 
        -6.66027523e+02 * x ** (6) +  2.07111066e+03 * x ** (5) 
        -4.40664678e+03 * x ** (4) +5.99848486e+03 * x ** (3) 
        -4.60965478e+03 * x ** (2) + 1.47784469e+03 * x ** (1)
        + 7.99999698e+00 * x ** (0) 
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
