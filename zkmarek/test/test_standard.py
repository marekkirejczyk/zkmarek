from dataclasses import dataclass
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

    def test_sign_raw(self):
        @dataclass
        class SignTestCase:
            sk: int
            hash: int
            k: int
            expected_r: int
            expected_s: int

        test_parameters = [
            # data from https://learnmeabitcoin.com/technical/ecdsa
            SignTestCase(
                sk=0xf94a840f1e1a901843a75dd07ffcc5c84478dc4f987797474c9393ac53ab55e6,
                hash=0xe46bf164b0960d3a3b5612cbac4a691c31b71e26d45c7f8ade7be23727809775,
                k=12345,
                expected_r=108607064596551879580190606910245687803607295064141551927605737287325610911759,
                expected_s=73791001770378044883749956175832052998232581925633570497458784569540878807131,
            ),
            # data from https://crypto.stackexchange.com/a/41339
            SignTestCase(
                sk=0xebb2c082fd7727890a28ac82f6bdf97bad8de9f5d7c9028692de1a255cad3e0f,
                hash=0x4b688df40bcedbe641ddb16ff0a1842d9c67ea1c3bf63f3e0471baa664531d1a,
                k=0x49a0d7b786ec9cde0d0721d72804befd06571c974b191efb42ecf322ba9ddd9a,
                expected_r=0x241097efbf8b63bf145c8961dbdf10c310efbb3b2676bbc0f8b08505c9e2f795,
                expected_s=0x021006b7838609339e8b415a7f9acb1b661828131aef1ecbc7955dfb01f3ca0e,
            )
        ]

        for p in test_parameters:
            with self.subTest('Test raw signature sign'):
                standard = Secp256
                r, s = standard.sign_raw(p.sk, p.hash, p.k)

                self.assertEqual(p.expected_r, r)
                self.assertEqual(p.expected_s, s)
