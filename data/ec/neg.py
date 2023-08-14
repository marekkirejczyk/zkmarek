class ECAffine:
    x: Field
    y: Field

    ...

    def __neg__(self) -> ECAffine:
        return ECAffine(self.x, -self.y)
