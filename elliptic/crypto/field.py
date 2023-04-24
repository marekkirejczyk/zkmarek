class Field:
    value = None
    modulus = None

    def __init__(self, value, modulus):
        self.value = value
        self.modulus = modulus

    def __eq__(self, other) -> bool:
        assert(self.modulus == other.modulus)
        return self.value == other.value

    def __add__(self, rhs):
        other = Field.from_int_or_self(rhs, self.modulus)
        assert(self.modulus == other.modulus)
        return Field((self.value + other.value) % self.modulus, self.modulus)

    def __sub__(self, rhs):
        other = Field.from_int_or_self(rhs, self.modulus)
        assert(self.modulus == other.modulus)
        return Field((self.value - other.value) % self.modulus, self.modulus)

    def __mul__(self, rhs):
        other = Field.from_int_or_self(rhs, self.modulus)
        assert(self.modulus == other.modulus)
        return Field((self.value * other.value) % self.modulus, self.modulus)

    def __pow__(self, rhs):
        other = Field.from_int_or_self(rhs, self.modulus)
        assert(self.modulus == other.modulus)
        return Field(pow(self.value, other.value, self.modulus), self.modulus)

    def __str__(self):
        return f'({self.value} % {self.modulus})'

    def from_int_or_self(other, modulus):
        if isinstance(other, int):
            return Field(other, modulus)
        return other
