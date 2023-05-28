import unittest

from zkmarek.crypto.field import Field
from zkmarek.crypto.weierstrass_curve import Secp256k_Order
from zkmarek.test.constant import TEST_PRIMES


class TestField(unittest.TestCase):
    def test_init(self):
        f = Field(1, 13)
        self.assertEqual(f.value, 1)
        self.assertEqual(f.order, 13)

        f = Field(-1, 13)
        self.assertEqual(f.value, 12)
        self.assertEqual(f.order, 13)

        f = Field(20, 13)
        self.assertEqual(f.value, 7)
        self.assertEqual(f.order, 13)

    def test_eq(self):
        self.assertTrue(Field(1, 13) == Field(1, 13))
        self.assertTrue(Field(28, 29) == Field(28, 29))
        self.assertTrue(Field(13, 1) == Field(13, 1))
        self.assertTrue(Field(12, 13) == Field(-1, 13))
        self.assertTrue(Field(2, 1) == Field(1, 1))

    def test_eq_diff_value(self):
        self.assertFalse(Field(3, 29) == Field(4, 29))
        self.assertFalse(Field(-1, 29) == Field(1, 29))

    def test_eq_diff_order(self):
        with self.assertRaises(AssertionError):
            self.assertFalse(Field(3, 13) == Field(3, 29))
        with self.assertRaises(AssertionError):
            Field(1, 2) == Field(1, 1)

    def test_add(self):
        self.assertEqual(Field(1, 13) + Field(10, 13), Field(11, 13))
        self.assertEqual(Field(10, 13) + Field(10, 13), Field(7, 13))
        self.assertEqual(Field(1, 13) + 10, Field(11, 13))
        self.assertEqual(Field(10, 13) + 10, Field(7, 13))
        with self.assertRaises(AssertionError):
            Field(2, 13) + Field(2, 2)

    def test_sub(self):
        self.assertEqual(Field(0, 13) - Field(1, 13), Field(12, 13))
        self.assertEqual(Field(10, 13) - Field(20, 13), Field(3, 13))
        self.assertEqual(Field(0, 13) - 1, Field(12, 13))
        self.assertEqual(Field(10, 13) - 20, Field(3, 13))
        with self.assertRaises(AssertionError):
            Field(2, 13) - Field(2, 2)

    def test_mul(self):
        self.assertEqual(Field(2, 13) * Field(2, 13), Field(4, 13))
        self.assertEqual(Field(4, 13) * Field(4, 13), Field(3, 13))
        self.assertEqual(Field(2, 13) * 2, Field(4, 13))
        self.assertEqual(Field(4, 13) * 4, Field(3, 13))
        with self.assertRaises(AssertionError):
            Field(2, 13) * Field(2, 2)

    def test_pow_simple(self):
        self.assertEqual(Field(2, 13) ** 2, Field(4, 13))
        self.assertEqual(Field(2, 13) ** 4, Field(3, 13))

    def test_pow_to_prime_order_small(self):
        for p in TEST_PRIMES:
            for i in range(1, p):
                self.assertEqual(Field(i, p) ** p, Field(i, p))
                self.assertEqual(Field(i, p) ** (p-1), Field(1, p))

    def test_pow_to_prime_order_big(self):
        p = Secp256k_Order
        for i in [1, 2, 3, 7, 100, 1024, 2**128, 2**254]:
            self.assertEqual(Field(i, p) ** p, Field(i, p))
            self.assertEqual(Field(i, p) ** (p-1), Field(1, p))

    def test_neg(self):
        self.assertEqual(-Field(1, 3), Field(2, 3))
        self.assertEqual(-Field(2, 3), Field(1, 3))
        self.assertEqual(-Field(17, 29), Field(12, 29))

    def test_neg_add(self):
        for p in TEST_PRIMES:
            for i in range(1, p):
                self.assertEqual(--Field(i, p), Field(i, p))

    def test_inv_simple(self):
        self.assertEqual(Field(2, 5).inv(), Field(3, 5))

    def test_inv_zero(self):
        with self.assertRaises(ZeroDivisionError):
            Field(0, 5).inv()

    def test_inv(self):
        for p in TEST_PRIMES:
            for i in range(1, p):
                self.assertEqual(Field(i, p).inv() * Field(i, p), Field(1, p))

    def test_div(self):
        self.assertEqual(Field(2, 5) / Field(2, 5), Field(1, 5))
        self.assertEqual(Field(4, 5) / Field(2, 5), Field(2, 5))
        self.assertEqual(Field(2, 5) / Field(3, 5), Field(4, 5))

    def test_rand(self):
        for p in TEST_PRIMES:
            for _ in range(-p*2, p*2):
                self.assertTrue(0 <= Field.random(p).value < p)
