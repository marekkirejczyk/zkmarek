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
        return CECAffine(x, y)
