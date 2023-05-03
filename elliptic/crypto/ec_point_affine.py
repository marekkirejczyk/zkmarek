from elliptic.crypto.field import Field
from elliptic.crypto.weierstrass_curve import WeierstrassCurve
from typing import Union

FieldLike = Union[int, Field]

class ECPointAffine:
    x: Field
    y: Field

    def __init__(self, x: FieldLike, y: FieldLike, curve:WeierstrassCurve):
        self.curve = curve
        self.x = x if isinstance(x, Field) else Field(x, curve.p)
        self.y = y if isinstance(y, Field) else Field(y, curve.p)
        assert self.x.order > 0 and self.x.order == self.y.order

    def __neg__(self):
        return ECPointAffine(self.x, -self.y, self.curve)

    def __eq__(self, other: "ECPointAffine") -> bool:
        assert(self.curve == other.curve)
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        assert(self.curve == other.curve)
        slope = (other.y - self.y) / (other.x - self.x)
        x = slope ** 2 - self.x - other.x
        y = slope * (self.x - x) - self.y
        return ECPointAffine(x, y, self.curve)

    def __str__(self):
        return f"({self.x.value}, {self.y.value})"

