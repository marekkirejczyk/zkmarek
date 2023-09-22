import unittest

from zkmarek.crypto.algo.sqrt import (find_non_residue, find_pow2_divisor,
                                      find_two_pow_order, has_sqrt,
                                      tonelli_shanks_sqrt)
from zkmarek.crypto.field_element import Field
from zkmarek.crypto.weierstrass_curve import Secp256k_Order
from zkmarek.test.constant import TEST_PRIMES, TEST_PRIMES_WITHOUT_2


def naive_find_sqrt(a, p):
    for i in range(p):
        if (i * i) % p == a:
            return i
    return None


class TestSqrt(unittest.TestCase):
    def test_has_sqrt(self):
        for p in TEST_PRIMES:
            for i in range(1, p):
                self.assertEqual(has_sqrt(i, p), naive_find_sqrt(i, p) is not None)

    def test_has_sqrt_big(self):
        p = Secp256k_Order
        for i in [1, 2, 3, 7, 100, 1024, 2**128, 2**254] + list(range(101, 202)):
            nf = Field(i, p)
            self.assertEqual(has_sqrt(i, p), tonelli_shanks_sqrt(nf) is not None)


    def test_find_pow2_divisor(self):
        self.assertEqual(find_pow2_divisor(17), (0, 17))
        self.assertEqual(find_pow2_divisor(28), (2, 7))
        self.assertEqual(find_pow2_divisor(256), (8, 1))
        with self.assertRaises(AssertionError):
            find_pow2_divisor(0)

    def test_find_non_residue(self):
        for p in TEST_PRIMES_WITHOUT_2:
            for i in range(1, 100):
                z = find_non_residue(p)
                self.assertFalse(has_sqrt(z.value, p))

    def test_find_non_residue_big(self):
        p = Secp256k_Order
        for i in range(1, 100):
            z = find_non_residue(p)
            self.assertFalse(has_sqrt(z.value, p))


    def test_find_non_residue_non_zero(self):
        for i in range(1, 100):
            z = find_non_residue(3)
            self.assertNotEqual(z.value, 0)

    def test_find_two_pow_order_simple(self):
        nf = Field(9, 41)
        self.assertEqual(find_two_pow_order(nf, 41), 2)

    def test_find_two_pow_order(self):
        for i in [9, 32, 40]:
            nf = Field(i, 41)
            self.assertEqual(nf **(2 ** find_two_pow_order(nf, 41)), Field(1, 41))

    def test_tonelli_shanks_sqrt_none(self):
        for p in TEST_PRIMES:
            for i in range(1, p):
                expected = naive_find_sqrt(i, p)
                if expected is None:
                    result = tonelli_shanks_sqrt(Field(i, p))
                    self.assertIsNone(result)

    def test_tonelli_shanks_sqrt_small(self):
        for p in TEST_PRIMES_WITHOUT_2:
            for i in range(1, p):
                nf = Field(i, p)
                if has_sqrt(i, p):
                    r = tonelli_shanks_sqrt(nf)
                    self.assertEqual(r * r, nf)

    def test_tonelli_shanks_sqrt_big(self):
        p = Secp256k_Order
        for i in [1, 2, 3, 7, 100, 1024, 2**128, 2**254]:
            nf = Field(i, p)
            if has_sqrt(i, p):
                r = tonelli_shanks_sqrt(nf)
                self.assertEqual(r * r, nf)
