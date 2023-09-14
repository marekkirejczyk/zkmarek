import secrets

from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.crypto.weierstrass_curve import WeierstrassCurve, Secp256k1


class Standard:
    curve: WeierstrassCurve
    generator: ECAffine
    group_order: int

    def __init__(self, curve: WeierstrassCurve, generator_x: int, generator_sgn: int,
                 group_order: int):
        self.curve = curve
        generator = ECAffine.from_x(generator_x, generator_sgn, Secp256k1)
        if generator is None:
            raise ValueError("Invalid generator")
        else:
            self.generator = generator
        self.group_order = group_order

    def generate_secret_key(self) -> int:
        return secrets.randbelow(self.group_order)

    def generate_public_key(self, secret: int) -> ECAffine:
        return self.generator * secret

    # Based on https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm#Signature_generation_algorithm
    def sign_raw(self, secret_key: int, msg_hash: int, k: int):
        n = self.group_order
        r: int = (self.generator * k).x.value
        # r = r % n unnecessary for secp256k1
        # s = k⁻¹(z + rdₐ) mod n
        s = (pow(k, -1, n) * (msg_hash + (r * int(hex(secret_key), 16)))) % n
        return r, s


Secp256 = Standard(Secp256k1,
    0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798, 0,
    0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141)
