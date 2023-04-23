import unittest

from elliptic.crypto.ec_point_affine import ECPointAffine

class TestECPointAffine(unittest.TestCase):
    def test_init(self):
        p = ECPointAffine(1, 2)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)

if __name__ == "__main__":
    unittest.main()
