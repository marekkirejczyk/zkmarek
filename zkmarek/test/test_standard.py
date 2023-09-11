from math import sqrt
from unittest import TestCase

from zkmarek.crypto.standard import Secp256
from zkmarek.crypto.weierstrass_curve import Secp256k1


class TestStandard(TestCase):
    def test_init(self):
        generator = Secp256.generator
        self.assertEqual(Secp256.curve, Secp256k1)
        self.assertEqual(
            0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
            generator.x.value
        )
        self.assertEqual(
            0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8,
            generator.y.value
        )

    def test_generate_secret_key(self):
        for i in range(1000):
            secrete_key = Secp256.generate_secret_key()
            sqrt_n = sqrt(Secp256.group_order)
            self.assertTrue(secrete_key >= sqrt_n)
            self.assertTrue(secrete_key < Secp256.group_order - sqrt_n)

    def test_generate_secret_keys_are_different(self):
        self.assertNotEquals(
            Secp256.generate_secret_key(),
            Secp256.generate_secret_key())
