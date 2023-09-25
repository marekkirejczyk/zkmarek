class FieldElement:
    value: int # BigInteger
    order: int # BigInteger

    def __init__(self, value: int, order: int):
        self.value = value % order
        self.order = order

    def __eq__(self, other: FieldElement) -> bool:
        assert self.order == other.order
        return self.value == other.value

    def __add__(self, other: FieldElement) -> FieldElement:
        assert self.order == other.order
        return FieldElement(self.value + other.value, self.order)

    def __sub__(self, other: FieldElement) -> FieldElement:
        assert self.order == other.order
        return FieldElement(self.value - other.value, self.order)

    def __mul__(self, other: FieldElement) -> FieldElement:
        assert self.order == other.order
        return FieldElement(self.value * other.value, self.order)

    def inv(self) -> FieldElement:
        return ...
