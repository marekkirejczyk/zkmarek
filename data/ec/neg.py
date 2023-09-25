class ECAffine:
    x: FieldElement
    y: FieldElement
    ...

    def __neg__(self) -> ECAffine:
        return ECAffine(self.x, -self.y)
