import unittest

from elliptic.crypto.ec_point_affine import ECPointAffine
from elliptic.crypto.field import Field
from elliptic.crypto.weierstrass_curve import Secp256k1_13

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
        p = ECPointAffine(Field(1,13), Field(2,13), self.curve)
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

if __name__ == "__main__":
    unittest.main()
