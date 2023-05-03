from .extended_euclid import extended_euclid


class Field:
    value = None
    order = None

    def __init__(self, value, order):
        assert isinstance(order, int)
        self.value = value
        self.order = order

    def __eq__(self, other) -> bool:
        assert self.order == other.order
        return self.value == other.value

    def __add__(self, rhs):
        other = Field.from_int_or_self(rhs, self.order)
        assert self.order == other.order
        return Field((self.value + other.value) % self.order, self.order)

    def __sub__(self, rhs):
        other = Field.from_int_or_self(rhs, self.order)
        assert self.order == other.order
        return Field((self.value - other.value) % self.order, self.order)

    def __mul__(self, rhs):
        other = Field.from_int_or_self(rhs, self.order)
        assert self.order == other.order
        return Field((self.value * other.value) % self.order, self.order)

    def __pow__(self, rhs):
        other = Field.from_int_or_self(rhs, self.order)
        assert self.order == other.order
        return Field(pow(self.value, other.value, self.order), self.order)

    def __str__(self):
        return f"({self.value} % {self.order})"

    def __repr__(self):
        return f"({self.value} % {self.order})"

    def __neg__(self):
        return Field(-self.value % self.order, self.order)

    def from_int_or_self(other, modulus):
        if isinstance(other, int):
            return Field(other, modulus)
        return other

    def inv(self):
        (_, _, _, a, _) = extended_euclid(self.order, self.value)
        return Field(a % self.order, self.order)
