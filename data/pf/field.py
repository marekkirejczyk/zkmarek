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
        return Field((self.value + other.value) % self.order, self.order)

    def __sub__(self, rhs: "FieldLike") -> "Field":
        other = Field.create_from(rhs, self.order)
        assert self.order == other.order
        return Field((self.value - other.value) % self.order, self.order)

    def __mul__(self, rhs: "FieldLike") -> "Field":
        other = Field.create_from(rhs, self.order)
        assert self.order == other.order
        return Field((self.value * other.value) % self.order, self.order)
