import unittest

from zkmarek.crypto.cec_affine import INFINITY, CECAffine

class TestCecAffine(unittest.TestCase):
    def test_neg(self):
        self.assertEqual(-CECAffine(1, 2), CECAffine(1, -2))
        self.assertEqual(-CECAffine(0, 0), CECAffine(0, 0))
        self.assertEqual(-CECAffine(1, 0), CECAffine(1, 0))
        self.assertEqual(-CECAffine(-1, -2), CECAffine(-1, 2))

    def test_add_infinite(self):
        a = CECAffine.from_x(1)
        self.assertEqual(a + -a, INFINITY)
        self.assertEqual(a + INFINITY, a)
        self.assertEqual(INFINITY + a, a)
        self.assertEqual(INFINITY + INFINITY, INFINITY)

    def test_double(self):
        a = CECAffine.from_x(1)
        self.assertEqual(a.double(), a + a)
