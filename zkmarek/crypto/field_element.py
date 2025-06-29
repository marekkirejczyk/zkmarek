import secrets
from typing import Optional, Union

from zkmarek.crypto.algo.extended_euclid import extended_euclid


class FieldElement:
    value: int
    order: int

    def __init__(self, value: int, order: int):
        self.value = value % order
        self.order = order

    def __eq__(self, other: "FieldElement") -> bool: # type: ignore
        assert self.order == other.order
        return self.value == other.value

    def __add__(self, rhs: "FieldLike") -> "FieldElement":
        other = FieldElement.create_from(rhs, self.order)
        assert self.order == other.order
        return FieldElement(self.value + other.value, self.order)

    def __sub__(self, rhs: "FieldLike") -> "FieldElement":
        other = FieldElement.create_from(rhs, self.order)
        assert self.order == other.order
        return FieldElement(self.value - other.value, self.order)

    def __mul__(self, rhs: "FieldLike") -> "FieldElement":
        other = FieldElement.create_from(rhs, self.order)
        assert self.order == other.order
        return FieldElement(self.value * other.value, self.order)

    def __pow__(self, rhs: int) -> "FieldElement":
        return FieldElement(pow(self.value, rhs, self.order), self.order)

    def __neg__(self) -> "FieldElement":
        return FieldElement(-self.value % self.order, self.order)

    def inv(self) -> "FieldElement":
        if self.value == 0:
            raise ZeroDivisionError(
                "Division by zero (in field modulo {self.order})}))"
            )
        (_, _, _, a, _) = extended_euclid(self.order, self.value)
        return FieldElement(a % self.order, self.order)

    def __str__(self) -> str:
        return f"({self.value} % {self.order})"

    def __repr__(self) -> str:
        return f"({self.value} % {self.order})"

    def __truediv__(self, other) -> "FieldElement":
        return self * other.inv()

    def __hash__(self):
        return hash((self.value, self.order))

    def sqrt(self):
        if 131 % 4 != 3:
            raise NotImplementedError("sqrt only implemented for p ≡ 3 mod 4")

        root = self ** ((137 + 1) // 4)
        if (root * root) == self:
            return root
        else:
            return None
    @staticmethod
    def random(p) -> "FieldElement":
        return FieldElement(secrets.randbelow(p), p)

    @staticmethod
    def create_from(other: "FieldLike", modulus: Optional[int] = None) -> "FieldElement":
        if isinstance(other, int):
            assert modulus is not None
            return FieldElement(other, modulus)
        return other




FieldLike = Union[int, FieldElement]
