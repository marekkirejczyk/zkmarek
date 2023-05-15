import unittest

from zkmarek.crypto.ec_point_affine import ECPointAffine
from zkmarek.crypto.field import Field
from zkmarek.crypto.weierstrass_curve import Secp256k1_13, WeierstrassCurve
from zkmarek.test.constant import TEST_PRIMES_WITHOUT_2


def naive_generate_points(curve: WeierstrassCurve):
    p = curve.p
    for x in range(0, p):
        for y in range(0, p):
            point = ECPointAffine(x, y, curve)
            if curve.evaluate_at(x, y) == 0:
                yield point

class TestECPointAffine(unittest.TestCase):
    curve = Secp256k1_13
    p = 0

    def setup(self):
        self.p = self.curve.p

    def test_init_with_int(self):
        p = ECPointAffine(1, 2, self.curve)
        self.assertEqual(p.x, Field(1, 13))
        self.assertEqual(p.y, Field(2, 13))

    def test_init_with_field(self):
        p = ECPointAffine(Field(1, 13), Field(2, 13), self.curve)
        self.assertEqual(p.x, Field(1, 13))
        self.assertEqual(p.y, Field(2, 13))

    def test_eq(self):
        curve = self.curve
        self.assertTrue(ECPointAffine(1, 2, curve) == ECPointAffine(1, 2, curve))
        self.assertFalse(ECPointAffine(1, 2, curve) == ECPointAffine(2, 1, curve))

    def test_neg(self):
        p = ECPointAffine(1, 2, self.curve)
        self.assertEqual(-p, ECPointAffine(1, 11, self.curve))

    def test_double_neg(self):
        for i in range(1, 13):
            for j in range(1, 13):
                p = ECPointAffine(i, j, self.curve)
                self.assertEqual(--p, p)

    def test_add(self):
        p = ECPointAffine(1, 2, self.curve)
        q = ECPointAffine(2, 1, self.curve)
        self.assertEqual(p + q, ECPointAffine(11, 8, self.curve))

    def test_from_x(self):
        for p in TEST_PRIMES_WITHOUT_2:
            for x in range(1, p):
                curve = WeierstrassCurve(0, 7, p)
                fe = ECPointAffine.from_x(x, 0, curve)
                if fe is not None:
                    self.assertEqual(curve.evaluate_at(fe.x.value, fe.y.value), 0)
                    if fe.y.value != 0:
                        fe2 = ECPointAffine.from_x(x, 1, curve)
                        self.assertNotEqual(fe, -fe)
                        self.assertEqual(curve.evaluate_at(fe2.x.value, fe2.y.value), 0)

    def test_from_x_sgn(self):
        curve = WeierstrassCurve(0, 7, 41)
        for x in range(1, curve.p):
            fe0 = ECPointAffine.from_x(x, 0, curve)
            if fe0 is not None:
                self.assertEqual(fe0.y.value % 2, 0)
                if fe0.y.value != 0:
                    fe1 = ECPointAffine.from_x(x, 1, curve)
                    self.assertEqual(fe1.y.value % 2, 1)

    def test_generate_points(self):
        for p in [3, 5, 7, 11, 13, 17, 97, 137, 211, 499]:
            curve = WeierstrassCurve(0, 7, p)
            expected = set(naive_generate_points(curve))
            actual = set(ECPointAffine.generate_points(curve))
            self.assertEqual(actual, expected)
