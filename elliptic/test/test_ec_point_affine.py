import unittest

from elliptic.crypto.ec_point_affine import ECPointAffine
from elliptic.crypto.field import Field

class TestECPointAffine(unittest.TestCase):
    def test_init_with_int(self):
        p = ECPointAffine(1, 2, 13)
        self.assertEqual(p.x, Field(1, 13))
        self.assertEqual(p.y, Field(2, 13))

    def test_init_with_field(self):
        p = ECPointAffine(Field(1,13), Field(2,13))
        self.assertEqual(p.x, Field(1, 13))
        self.assertEqual(p.y, Field(2, 13))

    def test_eq(self):
        self.assertTrue(ECPointAffine(1, 2, 13) == ECPointAffine(1, 2, 13))
        self.assertFalse(ECPointAffine(1, 2, 13) == ECPointAffine(2, 1, 13))

    def test_neg(self):
        p = ECPointAffine(1, 2, 13)
        self.assertEqual(-p, ECPointAffine(1, 11, 13))

    def test_double_neg(self):
        for i in range(1, 13):
            p = ECPointAffine(Field(i, 13), Field(i, 13))
            self.assertEqual(--p, p)

if __name__ == "__main__":
    unittest.main()
