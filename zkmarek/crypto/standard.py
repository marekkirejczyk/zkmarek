import hashlib
import secrets
from typing import Optional

from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.crypto.ecdsa import ECDSASignature
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
    def sign(self, secret_key: int, msg_hash: int, k: int):
        n = self.group_order
        r: int = (self.generator * k).x.value % n
        # s = k⁻¹(z + rdₐ) mod n
        s = (pow(k, -1, n) * (msg_hash + (r * int(hex(secret_key), 16)))) % n
        return r, s

    def sign_with_random_k(self, secret_key: int, msg: bytes) -> ECDSASignature:
        msg_hash = hashlib.sha256(msg).digest()
        r = 0
        s = 0
        while r == 0 or s == 0:
            k = secrets.randbits(256)
            r, s = self.sign(secret_key, int.from_bytes(msg_hash, 'big'), k)
        return ECDSASignature(r, s)

    # Based on https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm#Signature_verification_algorithm
    def verify(self, z: int, r: int, s: int, public_key: ECAffine) -> bool:
        if public_key.is_infinity() or not (public_key * self.group_order).is_infinity():
            return False

        if r < 1 or r >= self.group_order or s < 1 or s >= self.group_order:
            return False

        n = self.group_order
        s_inverse = pow(s, -1, n)
        u1 = z * s_inverse % n
        u2 = r * s_inverse % n

        Q = self.generator * u1 + public_key * u2
        x = Q.x.value % n
        return x == r

    def recover(self, z: int, r: int, s: int, v: int) -> Optional[ECAffine]:
        n = self.group_order
        R = ECAffine.from_x(r, v, self.curve)
        if R is None:
            return None
        else:
            r_inverse = pow(r, -1, n)
            u1 = -z * r_inverse % n
            u2 = s * r_inverse % n
            QA = self.generator * u1 + R * u2
            return QA


Secp256 = Standard(
    Secp256k1,
    0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798, 0,
    0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141)
