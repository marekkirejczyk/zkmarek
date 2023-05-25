def __add__(self, other: ECAffine) -> ECAffine:
    assert self.curve == other.curve
    slope = (other.y - self.y) / (other.x - self.x)
    x = slope**2 - self.x - other.x
    y = slope * (self.x - x) - self.y
    return ECAffine(x, y, self.curve)
