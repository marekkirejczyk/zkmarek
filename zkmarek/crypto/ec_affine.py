from typing import List, Optional, Sequence

from zkmarek.crypto.algo.sqrt import tonelli_shanks_sqrt
from zkmarek.crypto.bits import bits, bits_lsb
from zkmarek.crypto.field_element import FieldElement, FieldLike
from zkmarek.crypto.weierstrass_curve import WeierstrassCurve


class ECAffine:
    x: FieldElement
    y: FieldElement
    curve: WeierstrassCurve

    def __init__(self, x: FieldLike, y: FieldLike, curve: WeierstrassCurve):
        self.curve = curve
        self.x = FieldElement.create_from(x, curve.p)
        self.y = FieldElement.create_from(y, curve.p)
        assert self.x.order > 0 and self.x.order == self.y.order
        assert curve.is_at(
            self.x.value, self.y.value
        ), f"Point ({x}, {y}) is not on curve"

    def __neg__(self) -> "ECAffine":
        return ECAffine(self.x, -self.y, self.curve)

    def __eq__(self, other: "ECAffine") -> bool: # type: ignore
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
        elif other.is_infinity():
            return self
        else:
            slope = (other.y - self.y) / (other.x - self.x)
            x = slope**2 - self.x - other.x
            y = slope * (self.x - x) - self.y
            return ECAffine(x, y, self.curve)

    def __sub__(self, other: "ECAffine") -> "ECAffine":
        return self + (-other)

    def slope(self) -> Optional[FieldElement]:
        if self.is_infinity() or self.y.value == 0:
            return None
        return ((self.x**2) * 3) / (self.y * 2)

    def double(self) -> "ECAffine":
        if self.is_infinity():
            return self
        if self.y.value == 0:
            return self.infinity()
        slope = ((self.x**2) * 3) / (self.y * 2)
        x = slope**2 - self.x * 2
        y = slope * (self.x - x) - self.y
        return ECAffine(x, y, self.curve)

    def __str__(self) -> str:
        if self.is_infinity():
            return "(INF)"
        return f"({self.x.value}, {self.y.value})"

    def __repr__(self) -> str:
        if self.is_infinity():
            return f"INF[%{self.curve.p}]"
        return f"({self.x.value}, {self.y.value})[%{self.curve.p}]"

    def __format__(self, format_spec):
        return format(str(self), format_spec)

    def __hash__(self):
        return hash((self.x, self.y))

    def to_coords(self) -> Sequence[float]:
        return [float(self.x.value), float(self.y.value), 0.0]

    def infinity(self) -> "ECAffine":
        return ECAffine(0, 0, self.curve)

    def is_infinity(self):
        return self.x.value == 0 and self.y.value == 0

    def __mul__(self, k: int) -> "ECAffine":
        if k == 0:
            return self.infinity()
        elif k == 1:
            return self
        else:
            return self.double_and_add(k)

    def double_and_add(self, k: int):
        result = self.infinity()
        tmp = self
        for bit in bits(k):
            if bit == 1:
                result = result + tmp
            tmp = tmp.double()
        return result

    # Note: This is not constant time multiplication, as
    # underlying Elliptic Curve operations are not constant time
    def double_and_always_add(self, k: int):
        tmp = self
        result = self.infinity()
        for bit in bits_lsb(k):
            result = result.double()
            tmp = result + self
            one = result * (1-bit)
            two = tmp * bit
            result =  one + two
        return result

    def serialize_uncompressed(self) -> str:
        return (f'{self.x.value:x}' + f'{self.y.value:x}').upper()

    @staticmethod
    def infinity_point(curve: WeierstrassCurve) -> "ECAffine":
        return ECAffine(0, 0, curve)

    @staticmethod
    def from_x(x: int, sgn: int, curve: WeierstrassCurve) -> "Optional[ECAffine]":
        fx = FieldElement(x, curve.p)
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
            if point is not None and not point.is_infinity():
                points.append(point)
                if point.y.value != 0:
                    points.append(-point)
        return points

