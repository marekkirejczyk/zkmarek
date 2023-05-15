import unittest

from zkmarek.crypto.algo.extended_euclid import extended_euclid
from zkmarek.test.constant import TEST_PRIMES


class TestExtendedEuclid(unittest.TestCase):

    def test_simple_quotients(self):
        self.assertEqual(extended_euclid(4, 2)[:3], (2, 2, 1))
        self.assertEqual(extended_euclid(15, 12)[:3], (3, 5, 4))
        self.assertEqual(extended_euclid(240, 46)[:3], (2, 120, 23))

    def test_simple_bezouts_identity(self):
        (gcd, _, _, a, b) = extended_euclid(4, 2)
        self.assertEqual(gcd, 4 * b + 2 * a)

        (gcd, _, _, a, b) = extended_euclid(15, 12)
        self.assertEqual(gcd, 15 * b + 12 * a)

        (gcd, _, _, a, b) = extended_euclid(240, 46)
        self.assertEqual(gcd, 240 * b + 46 * a)

    def test_arg_equals(self):
        for i in range(1, 1000):
            self.assertEqual(extended_euclid(i, i), (i, 1, 1, 1, 0))

    def test_prime_dividend(self):
        for p in TEST_PRIMES:
            for i in range(1, p):
                (gcd, _, _, a, b) = extended_euclid(p, i)
                self.assertEqual(extended_euclid(p, i)[:3], (1, p, i))
                self.assertEqual(gcd, p * b + i * a)

    def test_raises_if_second_arg_bigger(self):
        with self.assertRaises(AssertionError):
            extended_euclid(3, 4)
