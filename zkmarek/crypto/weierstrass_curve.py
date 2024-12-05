
class WeierstrassCurve:
    p: int
    a: int
    b: int

    def __init__(self, a: int, b: int, p: int) -> None:
        self.a = a
        self.b = b
        self.p = p

    def evaluate_at(self, x: int, y: int) -> int:
        return (y**2 - x**3 - self.a * x - self.b) % self.p

    def is_at(self, x: int, y: int) -> int:
        return self.evaluate_at(x, y) == 0 or self.is_infinity(x, y)

    def is_infinity(self, x: int, y: int) -> bool:
        return x == 0 and y == 0

    def __eq__(self, other: "WeierstrassCurve") -> bool: # type: ignore
        return self.a == other.a and self.b == other.b and self.p == other.p


Secp256k_prime_field_p = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1
Secp256k_Order = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
Secp256k1 = WeierstrassCurve(0, 7, Secp256k_prime_field_p)
Secp256k1_13 = WeierstrassCurve(0, 7, 13)
Secp256k1_29 = WeierstrassCurve(0, 7, 29)
Secp256k1_41 = WeierstrassCurve(0, 7, 41)
BLS12381 = WeierstrassCurve(0, 4, 41)
BN254 = WeierstrassCurve(0, 3, 41)

