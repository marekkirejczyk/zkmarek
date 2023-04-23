import unittest

from elliptic.crypto.affine_ec_point import ECPointAffine

class TestECPointAffine(unittest.TestCase):
    def test_init(self):
        p = ECPointAffine(1, 2)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)


if __name__ == "__main__":
    unittest.main()
