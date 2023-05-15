from typing import List, Optional

from zkmarek.crypto.algo.sqrt import tonelli_shanks_sqrt
from zkmarek.crypto.field import Field, FieldLike
from zkmarek.crypto.weierstrass_curve import WeierstrassCurve


class ECPointAffine:
    x: Field
    y: Field

    def __init__(self, x: FieldLike, y: FieldLike, curve: WeierstrassCurve):
        self.curve = curve
        self.x = Field.create_from(x, curve.p)
        self.y = Field.create_from(y, curve.p)
        assert self.x.order > 0 and self.x.order == self.y.order

    def __neg__(self) -> "ECPointAffine":
        return ECPointAffine(self.x, -self.y, self.curve)

    def __eq__(self, other: "ECPointAffine") -> bool:
        assert self.curve == other.curve
        return self.x == other.x and self.y == other.y

    def __add__(self, other: "ECPointAffine") -> "ECPointAffine":
        assert self.curve == other.curve
        slope = (other.y - self.y) / (other.x - self.x)
        x = slope**2 - self.x - other.x
        y = slope * (self.x - x) - self.y
        return ECPointAffine(x, y, self.curve)

    def __str__(self) -> str:
        return f"({self.x.value}, {self.y.value})[%{self.curve.p}]"

    def __repr__(self) -> str:
        return f"({self.x.value}, {self.y.value})[%{self.curve.p}]"

    def __hash__(self):
        return hash((self.x, self.y))

    @staticmethod
    def from_x(x: int, sgn: int, curve: WeierstrassCurve) -> "Optional[ECPointAffine]":
        fx = Field(x, curve.p)
        fy = tonelli_shanks_sqrt(fx**3 + fx * curve.a + curve.b)
        if fy is None:
            return None
        r = ECPointAffine(fx, fy, curve)
        return r if r.y.value % 2 == sgn % 2 else -r

    @staticmethod
    def generate_points(curve: WeierstrassCurve) -> "List[ECPointAffine]":
        points = []
        for x in range(0, curve.p):
            point = ECPointAffine.from_x(x, 0, curve)
            if point is not None:
                points.append(point)
                if point.y.value != 0:
                    points.append(-point)
        return points
