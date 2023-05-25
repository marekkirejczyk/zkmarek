from typing import List, Optional, Sequence

from zkmarek.crypto.algo.sqrt import tonelli_shanks_sqrt
from zkmarek.crypto.field import Field, FieldLike
from zkmarek.crypto.weierstrass_curve import WeierstrassCurve


class ECAffine:
    x: Field
    y: Field
    curve: WeierstrassCurve

    def __init__(self, x: FieldLike, y: FieldLike, curve: WeierstrassCurve):
        self.curve = curve
        self.x = Field.create_from(x, curve.p)
        self.y = Field.create_from(y, curve.p)
        assert self.x.order > 0 and self.x.order == self.y.order

    def __neg__(self) -> "ECAffine":
        return ECAffine(self.x, -self.y, self.curve)

    def __eq__(self, other: "ECAffine") -> bool:
        assert self.curve == other.curve
        return self.x == other.x and self.y == other.y

    def __add__(self, other: "ECAffine") -> "ECAffine":
        assert self.curve == other.curve
        if self.x == other.x and self.y == other.y:
            return self.double()
        elif self.x == other.x and self.y == -other.y:
            return self.infinity()
        elif self.is_infinity():
            return other
        elif self.is_infinity():
            return self
        else:
            slope = (other.y - self.y) / (other.x - self.x)
            x = slope**2 - self.x - other.x
            y = slope * (self.x - x) - self.y
            return ECAffine(x, y, self.curve)

    def __sub__(self, other: "ECAffine") -> "ECAffine":
        return self + (-other)

    def double(self) -> "ECAffine":
        if self.is_infinity():
            return self
        slope = ((self.x ** 2)*3) / (self.y * 2)
        x = slope ** 2 - self.x * 2
        y = slope * (self.x - x) - self.y
        return ECAffine(x, y, self.curve)

    def __str__(self) -> str:
        return f"({self.x.value}, {self.y.value})[%{self.curve.p}]"

    def __repr__(self) -> str:
        return f"({self.x.value}, {self.y.value})[%{self.curve.p}]"

    def __format__(self, format_spec):
        return format(str(self), format_spec)


    def __hash__(self):
        return hash((self.x, self.y))

    def to_coords(self) -> Sequence[float]:
        return [float(self.x.value), float(self.y.value), 0.]

    def infinity(self) -> "ECAffine":
        return ECAffine(0, 0, self.curve)

    def is_infinity(self):
        return self.x.value == 0 and self.y.value == 0

    @staticmethod
    def infinity_point(curve: WeierstrassCurve) -> "ECAffine":
        return ECAffine(0, 0, curve)

    @staticmethod
    def from_x(x: int, sgn: int, curve: WeierstrassCurve) -> "Optional[ECAffine]":
        fx = Field(x, curve.p)
        fy = tonelli_shanks_sqrt(fx**3 + fx * curve.a + curve.b)
        if fy is None:
            return None
        r = ECAffine(fx, fy, curve)
        return r if r.y.value % 2 == sgn % 2 else -r

    @staticmethod
    def generate_points(curve: WeierstrassCurve) -> "List[ECAffine]":
        points = []
        for x in range(0, curve.p):
            point = ECAffine.from_x(x, 0, curve)
            if point is not None:
                points.append(point)
                if point.y.value != 0:
                    points.append(-point)
        return points


INFINITY = ECAffine(0, 0, WeierstrassCurve(0, 0, 1))
