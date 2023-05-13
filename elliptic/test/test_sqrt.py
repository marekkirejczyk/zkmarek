import unittest
from elliptic.crypto.field import Field
from elliptic.crypto.sqrt import (
    find_pow2_divisor,
    has_sqrt,
    find_non_residue,
    tonelli_shanks_sqrt,
)
from elliptic.test.constant import TEST_PRIMES


def naive_find_sqrt(a, p):
    for i in range(p):
        if i * i % p == a:
            return i
    return None


class TestSqrt(unittest.TestCase):
    def test_has_sqrt(self):
        for p in TEST_PRIMES:
            for i in range(1, p):
                self.assertEqual(has_sqrt(i, p), naive_find_sqrt(i, p) is not None)

    def test_find_pow2_divisor(self):
        self.assertEqual(find_pow2_divisor(17), (0, 17))
        self.assertEqual(find_pow2_divisor(28), (2, 7))
        self.assertEqual(find_pow2_divisor(256), (8, 1))
        with self.assertRaises(AssertionError):
            find_pow2_divisor(0)

    def test_tonelli_shanks_sqrt_none(self):
        for p in TEST_PRIMES:
            for i in range(1, p):
                expected = naive_find_sqrt(i, p)
                if expected is None:
                    result = tonelli_shanks_sqrt(Field(i, p))
                    self.assertIsNone(result)

    def test_find_non_residue(self):
        test_primes_without_2 = filter(lambda v: v != 2, TEST_PRIMES)
        for p in test_primes_without_2:
            for i in range(1, 1000):
                z = find_non_residue(p)
                self.assertFalse(has_sqrt(z.value, p))
