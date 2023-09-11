from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.crypto.weierstrass_curve import WeierstrassCurve, Secp256k1


class Standard:
    curve: WeierstrassCurve
    generator: ECAffine

    def __init__(self, curve: WeierstrassCurve, generator_x: int, generator_sgn: int):
        self.curve = curve
        generator = ECAffine.from_x(generator_x, generator_sgn, Secp256k1)
        if generator is None:
            raise ValueError("Invalid generator")
        else:
            self.generator = generator



Secp256 = Standard(Secp256k1,
    0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798, 0)

