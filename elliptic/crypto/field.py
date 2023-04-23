class Field:
    value = None
    modulus = None

    def __init__(self, value, modulus):
        self.value = value
        self.modulus = modulus

    def __eq__(self, other) -> bool:
        assert(self.modulus == other.modulus)
        return self.value == other.value

    def __add__(self, other):
        assert(self.modulus == other.modulus)
        return Field((self.value + other.value) % self.modulus, self.modulus)

    def __mul__(self, other):
        assert(self.modulus == other.modulus)
        return Field((self.value * other.value) % self.modulus, self.modulus)

    def __pow__(self, other):
        return Field(pow(self.value, other, self.modulus), self.modulus)

