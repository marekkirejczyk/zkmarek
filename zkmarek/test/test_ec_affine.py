import unittest

from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.crypto.field import Field
from zkmarek.crypto.weierstrass_curve import (Secp256k1_13, Secp256k1_41,
                                              WeierstrassCurve)
from zkmarek.test.constant import SMALL_PRIMES, TEST_PRIMES_WITHOUT_2


def naive_generate_points(curve: WeierstrassCurve):
    p = curve.p
    for x in range(0, p):
        for y in range(0, p):
            if curve.is_at(x, y) and not curve.is_infinity(x, y):
                yield ECAffine(x, y, curve)


def naive_mul(p: ECAffine, k: int) -> ECAffine:
    res = p.infinity()
    for _ in range(k):
        res += p
    return res


class TestECAffine(unittest.TestCase):
    curve = Secp256k1_13
    p = 0

    def setup(self):
        self.p = self.curve.p

    def test_init_with_int(self):
        p = ECAffine(7, 8, self.curve)
        self.assertEqual(p.x, Field(7, 13))
        self.assertEqual(p.y, Field(8, 13))
        p = ECAffine(20, -5, self.curve)
        self.assertEqual(p.x, Field(7, 13))
        self.assertEqual(p.y, Field(8, 13))


    def test_init_not_on_curve(self):
        with self.assertRaises(AssertionError):
            ECAffine(7, 7, self.curve)

    def test_init_with_field(self):
        p = ECAffine(Field(7, 13), Field(8, 13), self.curve)
        self.assertEqual(p.x, Field(7, 13))
        self.assertEqual(p.y, Field(8, 13))

    def test_infinity(self):
        p = ECAffine.infinity_point(self.curve)
        self.assertTrue(p.is_infinity())
        for p in p.generate_points(self.curve):
            self.assertFalse(p.is_infinity())
            self.assertNotEqual(p, ECAffine.infinity_point(self.curve))
            self.assertEqual(p.infinity(), ECAffine.infinity_point(self.curve))

    def test_eq(self):
        curve = self.curve
        self.assertTrue(ECAffine(7, 8, curve) == ECAffine(7, 8, curve))
        self.assertFalse(ECAffine(8, 8, curve) == ECAffine(7, 8, curve))

    def test_neg_simple(self):
        p = ECAffine(7, 8, self.curve)
        self.assertEqual(-p, ECAffine(7, 5, self.curve))

    def test_neg_double(self):
        points = ECAffine.generate_points(self.curve)
        for p in points:
            self.assertEqual(--p, p)

    def test_add_simple(self):
        p = ECAffine(7, 8, self.curve)
        q = ECAffine(8, 8, self.curve)
        self.assertEqual(p + q, ECAffine(11, 5, self.curve))

    def test_add_infinity(self):
        p = ECAffine(7, 8, self.curve)
        self.assertEqual(p + p.infinity(), p)
        p = ECAffine(7, 8, self.curve)
        self.assertEqual(p.infinity() + p, p)

    def test_double(self):
        for prime in TEST_PRIMES_WITHOUT_2:
            curve = WeierstrassCurve(0, 7, prime)
            points = ECAffine.generate_points(curve)
            for p in points:
                self.assertEqual(p.double()-p, p)

    def test_double_infinity(self):
        p = ECAffine.infinity_point(self.curve)
        self.assertEqual(p.double(), p.infinity())
        p = ECAffine(17, 0, Secp256k1_41)
        self.assertEqual(p.double(), p.infinity())

    def test_from_x(self):
        for p in TEST_PRIMES_WITHOUT_2:
            for x in range(1, p):
                curve = WeierstrassCurve(0, 7, p)
                fe = ECAffine.from_x(x, 0, curve)
                if fe is not None:
                    self.assertEqual(curve.evaluate_at(fe.x.value, fe.y.value), 0)
                    if fe.y.value != 0:
                        fe2 = ECAffine.from_x(x, 1, curve)
                        self.assertNotEqual(fe, -fe)
                        self.assertEqual(curve.evaluate_at(fe2.x.value, fe2.y.value), 0)

    def test_from_x_sgn(self):
        curve = WeierstrassCurve(0, 7, 41)
        for x in range(1, curve.p):
            fe0 = ECAffine.from_x(x, 0, curve)
            if fe0 is not None:
                self.assertEqual(fe0.y.value % 2, 0)
                if fe0.y.value != 0:
                    fe1 = ECAffine.from_x(x, 1, curve)
                    self.assertEqual(fe1.y.value % 2, 1)

    def test_generate_points(self):
        for p in [3, 5, 7, 11, 13, 17, 97, 137, 211, 499]:
            curve = WeierstrassCurve(0, 7, p)
            expected = set(naive_generate_points(curve))
            actual = set(ECAffine.generate_points(curve))
            self.assertEqual(actual, expected)

    def test_double_and_add(self):
        for prime in SMALL_PRIMES:
            points = ECAffine.generate_points(WeierstrassCurve(0, 7, prime))
            for p in points:
                for i in range(prime + 2):
                    expected = naive_mul(p, i)
                    actual = p.double_and_add(i)
                    if p.y.value != 0:
                        self.assertEqual(expected, actual)
