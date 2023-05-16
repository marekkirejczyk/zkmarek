class ECAffine:
    x: Field
    y: Field
    curve: WeierstrassCurve

    ...

    def __neg__(self) -> ECAffine:
        return ECAffine(self.x, -self.y, self.curve)
