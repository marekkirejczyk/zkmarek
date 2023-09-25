import unittest

from zkmarek.crypto.field_element import FieldElement
from zkmarek.crypto.weierstrass_curve import Secp256k_Order
from zkmarek.test.constant import TEST_PRIMES


class TestFieldElement(unittest.TestCase):
    def test_init(self):
        f = FieldElement(1, 13)
        self.assertEqual(f.value, 1)
        self.assertEqual(f.order, 13)

        f = FieldElement(-1, 13)
        self.assertEqual(f.value, 12)
        self.assertEqual(f.order, 13)

        f = FieldElement(20, 13)
        self.assertEqual(f.value, 7)
        self.assertEqual(f.order, 13)

    def test_eq(self):
        self.assertTrue(FieldElement(1, 13) == FieldElement(1, 13))
        self.assertTrue(FieldElement(28, 29) == FieldElement(28, 29))
        self.assertTrue(FieldElement(13, 1) == FieldElement(13, 1))
        self.assertTrue(FieldElement(12, 13) == FieldElement(-1, 13))
        self.assertTrue(FieldElement(2, 1) == FieldElement(1, 1))

    def test_eq_diff_value(self):
        self.assertFalse(FieldElement(3, 29) == FieldElement(4, 29))
        self.assertFalse(FieldElement(-1, 29) == FieldElement(1, 29))

    def test_eq_diff_order(self):
        with self.assertRaises(AssertionError):
            self.assertFalse(FieldElement(3, 13) == FieldElement(3, 29))
        with self.assertRaises(AssertionError):
            FieldElement(1, 2) == FieldElement(1, 1)

    def test_add(self):
        self.assertEqual(FieldElement(1, 13) + FieldElement(10, 13), FieldElement(11, 13))
        self.assertEqual(FieldElement(10, 13) + FieldElement(10, 13), FieldElement(7, 13))
        self.assertEqual(FieldElement(1, 13) + 10, FieldElement(11, 13))
        self.assertEqual(FieldElement(10, 13) + 10, FieldElement(7, 13))
        with self.assertRaises(AssertionError):
            FieldElement(2, 13) + FieldElement(2, 2)

    def test_sub(self):
        self.assertEqual(FieldElement(0, 13) - FieldElement(1, 13), FieldElement(12, 13))
        self.assertEqual(FieldElement(10, 13) - FieldElement(20, 13), FieldElement(3, 13))
        self.assertEqual(FieldElement(0, 13) - 1, FieldElement(12, 13))
        self.assertEqual(FieldElement(10, 13) - 20, FieldElement(3, 13))
        with self.assertRaises(AssertionError):
            FieldElement(2, 13) - FieldElement(2, 2)

    def test_mul(self):
        self.assertEqual(FieldElement(2, 13) * FieldElement(2, 13), FieldElement(4, 13))
        self.assertEqual(FieldElement(4, 13) * FieldElement(4, 13), FieldElement(3, 13))
        self.assertEqual(FieldElement(2, 13) * 2, FieldElement(4, 13))
        self.assertEqual(FieldElement(4, 13) * 4, FieldElement(3, 13))
        with self.assertRaises(AssertionError):
            FieldElement(2, 13) * FieldElement(2, 2)

    def test_pow_simple(self):
        self.assertEqual(FieldElement(2, 13) ** 2, FieldElement(4, 13))
        self.assertEqual(FieldElement(2, 13) ** 4, FieldElement(3, 13))

    def test_pow_to_prime_order_small(self):
        for p in TEST_PRIMES:
            for i in range(1, p):
                self.assertEqual(FieldElement(i, p) ** p, FieldElement(i, p))
                self.assertEqual(FieldElement(i, p) ** (p - 1), FieldElement(1, p))

    def test_pow_to_prime_order_big(self):
        p = Secp256k_Order
        for i in [1, 2, 3, 7, 100, 1024, 2**128, 2**254]:
            self.assertEqual(FieldElement(i, p) ** p, FieldElement(i, p))
            self.assertEqual(FieldElement(i, p) ** (p - 1), FieldElement(1, p))

    def test_neg(self):
        self.assertEqual(-FieldElement(1, 3), FieldElement(2, 3))
        self.assertEqual(-FieldElement(2, 3), FieldElement(1, 3))
        self.assertEqual(-FieldElement(17, 29), FieldElement(12, 29))

    def test_neg_add(self):
        for p in TEST_PRIMES:
            for i in range(1, p):
                self.assertEqual(--FieldElement(i, p), FieldElement(i, p))

    def test_inv_simple(self):
        self.assertEqual(FieldElement(2, 5).inv(), FieldElement(3, 5))

    def test_inv_zero(self):
        with self.assertRaises(ZeroDivisionError):
            FieldElement(0, 5).inv()

    def test_inv(self):
        for p in TEST_PRIMES:
            for i in range(1, p):
                self.assertEqual(FieldElement(i, p).inv() * FieldElement(i, p), FieldElement(1, p))

    def test_div(self):
        self.assertEqual(FieldElement(2, 5) / FieldElement(2, 5), FieldElement(1, 5))
        self.assertEqual(FieldElement(4, 5) / FieldElement(2, 5), FieldElement(2, 5))
        self.assertEqual(FieldElement(2, 5) / FieldElement(3, 5), FieldElement(4, 5))

    def test_rand(self):
        for p in TEST_PRIMES:
            for _ in range(-p*2, p*2):
                self.assertTrue(0 <= FieldElement.random(p).value < p)
