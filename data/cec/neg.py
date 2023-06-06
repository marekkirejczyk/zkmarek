class CECAffine:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    ...

    def __neg__(self):
        return CECAffine(self.x, -self.y)
