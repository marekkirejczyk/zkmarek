from elliptic.crypto.ec_point_affine import ECPointAffine


class WeierstrassCurve:
    p = None
    a = None
    b = None

    def __init__(self, a: int, b: int, p: int) -> None:
        self.a = a
        self.b = b
        self.p = p

    def evaluate_at(self, point: ECPointAffine):
        x = point.x.value
        y = point.y.value
        return (y**2 - x**3 - self.a * x - self.b) % self.p

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.p == other.p


Secp256k_Order = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1
Secp256k1 = WeierstrassCurve(0, 7, Secp256k_Order)
Secp256k1_13 = WeierstrassCurve(0, 7, 13)
Secp256k1_29 = WeierstrassCurve(0, 7, 29)
