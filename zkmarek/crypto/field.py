import secrets
from typing import Optional, Union

from zkmarek.crypto.algo.extended_euclid import extended_euclid


class Field:
    value: int
    order: int

    def __init__(self, value: int, order: int):
        self.value = value % order
        self.order = order

    def __eq__(self, other: "Field") -> bool:
        assert self.order == other.order
        return self.value == other.value

    def __add__(self, rhs: "FieldLike") -> "Field":
        other = Field.create_from(rhs, self.order)
        assert self.order == other.order
        return Field(self.value + other.value, self.order)

    def __sub__(self, rhs: "FieldLike") -> "Field":
        other = Field.create_from(rhs, self.order)
        assert self.order == other.order
        return Field(self.value - other.value, self.order)

    def __mul__(self, rhs: "FieldLike") -> "Field":
        other = Field.create_from(rhs, self.order)
        assert self.order == other.order
        return Field(self.value * other.value, self.order)

    def __pow__(self, rhs: int) -> "Field":
        return Field(pow(self.value, rhs, self.order), self.order)

    def __neg__(self) -> "Field":
        return Field(-self.value % self.order, self.order)

    def inv(self) -> "Field":
        if self.value == 0:
            raise ZeroDivisionError(
                "Division by zero (in field modulo {self.order})}))"
            )
        (_, _, _, a, _) = extended_euclid(self.order, self.value)
        return Field(a % self.order, self.order)

    def __str__(self) -> str:
        return f"({self.value} % {self.order})"

    def __repr__(self) -> str:
        return f"({self.value} % {self.order})"

    def __truediv__(self, other) -> "Field":
        return self * other.inv()

    def __hash__(self):
        return hash((self.value, self.order))

    @staticmethod
    def random(p) -> "Field":
        return Field(secrets.randbelow(p), p)

    @staticmethod
    def create_from(other: "FieldLike", modulus: Optional[int] = None) -> "Field":
        if isinstance(other, int):
            assert modulus is not None
            return Field(other, modulus)
        return other


FieldLike = Union[int, Field]
