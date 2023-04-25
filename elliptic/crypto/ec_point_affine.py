from elliptic.crypto.field import Field

class ECPointAffine:
    x = 0
    y = 0

    def __init__(self, x, y, field_order = None):
        self.x = x if isinstance(x, Field) else Field(x, field_order)
        self.y = y if isinstance(y, Field) else Field(y, field_order)
        assert isinstance(self.x.order, int) and self.x.order == self.y.order

    def __neg__(self):
        return ECPointAffine(self.x, -self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
