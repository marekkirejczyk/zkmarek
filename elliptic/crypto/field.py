from .extended_euclid import extended_euclid
from typing import Union, Optional

class Field:
    value: int
    order: int

    def __init__(self, value: int, order: int):
        self.value = value % order
        self.order = order

    def __eq__(self, other) -> bool:
        assert self.order == other.order
        return self.value == other.value

    def __add__(self, rhs):
        other = Field.create_from(rhs, self.order)
        assert self.order == other.order
        return Field((self.value + other.value) % self.order, self.order)

    def __sub__(self, rhs):
        other = Field.create_from(rhs, self.order)
        assert self.order == other.order
        return Field((self.value - other.value) % self.order, self.order)

    def __mul__(self, rhs):
        other = Field.create_from(rhs, self.order)
        assert self.order == other.order
        return Field((self.value * other.value) % self.order, self.order)

    def __pow__(self, rhs):
        other = Field.create_from(rhs, self.order)
        assert self.order == other.order
        return Field(pow(self.value, other.value, self.order), self.order)

    def __str__(self):
        return f"({self.value} % {self.order})"

    def __repr__(self):
        return f"({self.value} % {self.order})"

    def __neg__(self):
        return Field(-self.value % self.order, self.order)

    def inv(self):
        (_, _, _, a, _) = extended_euclid(self.order, self.value)
        return Field(a % self.order, self.order)

    def __truediv__(self, other):
        return self * other.inv()

    @staticmethod
    def create_from(other: "FieldLike", modulus: Optional[int] = None):
        if isinstance(other, int):
            return Field(other, modulus)
        return other

FieldLike = Union[int, Field]
