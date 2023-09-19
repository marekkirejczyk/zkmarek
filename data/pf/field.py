class Field:
    value: int # BigInteger
    order: int # BigInteger

    def __init__(self, value: int, order: int):
        self.value = value % order
        self.order = order

    def __eq__(self, other: Field) -> bool:
        assert self.order == other.order
        return self.value == other.value

    def __add__(self, other: Field) -> Field:
        assert self.order == other.order
        return Field(self.value + other.value, self.order)

    def __sub__(self, other: Field) -> Field:
        assert self.order == other.order
        return Field(self.value - other.value, self.order)

    def __mul__(self, other: Field) -> Field:
        assert self.order == other.order
        return Field(self.value * other.value, self.order)

    def inv(self) -> Field:
        return ...
