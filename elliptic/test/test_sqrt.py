import unittest
from elliptic.crypto.sqrt import find_pow2_divisor, has_sqrt
from elliptic.test.constant import TEST_PRIMES

def naive_find_sqrt(a, p):
    for i in range(p):
        if i*i % p == a:
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

