def double(self):
    if self == INFINITY:
        return INFINITY
    slope = (3 * self.x ** 2) / (2 * self.y)
    x = slope ** 2 - 2 * self.x
    y = slope * (self.x - x) - self.y
    return CECAffine(x, y)
