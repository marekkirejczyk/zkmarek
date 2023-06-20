    def __add__(self, other: "ECAffine") -> "ECAffine":
        assert self.curve == other.curve
        if self.x == other.x and self.y == -other.y:
            return self.infinity()
        elif self.is_infinity():
            return other
        elif other.is_infinity():
            return self
        else:
            slope = (other.y - self.y) / (other.x - self.x)
            x = slope**2 - self.x - other.x
            y = slope * (self.x - x) - self.y
            return ECAffine(x, y, self.curve)
