class Curve:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @staticmethod
    def from_x(x, sgn = 1):
        y = (-0.013005328649673187  * x ** (4) + 0.44002953745582507 * x ** (3) 
                                                                  -4.368305697782954 * x ** (2) + 15.731787164922928 * x ** (1)
                                                                  +4.2790892673006296 * x ** (0))
        return Curve(x, -y) if sgn < 0 else Curve(x, y)

    def __neg__(self):
        return Curve(self.x, -self.y)


    def __eq__(self, __value: "Curve") -> bool: # type: ignore
        return self.x == __value.x and self.y == __value.y

    def __repr__(self):
        return f"Curve({self.x}, {self.y})"


INFINITY = Curve(0, 0)
