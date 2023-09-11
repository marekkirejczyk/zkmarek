from math import sqrt
from unittest import TestCase

from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.crypto.standard import Secp256, Standard
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

    def test_init_invalid_generator(self):
        with self.assertRaises(ValueError):
            Standard(Secp256k1, 0, 0,
                     0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141)

    def test_generate_secret_key(self):
        for i in range(1000):
            secrete_key = Secp256.generate_secret_key()
            sqrt_n = sqrt(Secp256.group_order)
            self.assertTrue(secrete_key >= sqrt_n)
            self.assertTrue(secrete_key < Secp256.group_order - sqrt_n)

    def test_generate_secret_keys_unique(self):
        self.assertNotEqual(
            Secp256.generate_secret_key(),
            Secp256.generate_secret_key())

    def test_generate_public_key(self):
        secret = 0xeb7a1cd9f8163e6d7e51a7ca72db2b9d08df9f5114942a133a8497c945aa7d13
        expected = ECAffine(
            0xc2460e55d14c9c0008013160559ec814b7b327e7b6eb1dbc0cc6d5eba4b0caa0,
            0x45a77f71637e70ccb0a28e09bdf7e0bd6fb55a71194564cdb07473630e326f29,
            Secp256k1)
        self.assertEqual(expected, Secp256.generate_public_key(secret))
