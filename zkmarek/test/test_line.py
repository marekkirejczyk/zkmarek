import unittest

from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.crypto.line import (calculate_line_coefficients, line_through_collinear,
                                       is_collinear, lines_through_affine)
from zkmarek.crypto.weierstrass_curve import Secp256k1_41


class TestLine(unittest.TestCase):

    def test_find_x_min_max(self):
        actual = line_through_collinear([(1, 2), (3, 4)])
        self.assertEqual(actual, [(1, 2), (3, 4)])
        actual = line_through_collinear([(1, 2), (3, 4), (2, 1)])
        self.assertEqual(actual, [(1, 2), (3, 4)])
        actual = line_through_collinear([(1, 2), (3, 4), (0, 1)])
        self.assertEqual(actual, [(0, 1), (3, 4)])

    def test_calculate_line_coefficients(self):
        actual = calculate_line_coefficients((0, 0), (1, 1))
        self.assertEqual(actual, (1, 0))
        actual = calculate_line_coefficients((0, 0), (-1, 1))
        self.assertEqual(actual, (-1, 0))
        actual = calculate_line_coefficients((1, 2), (3, 4))
        self.assertEqual(actual, (1, 1))
        actual = calculate_line_coefficients((1, 2), (2, 1))
        self.assertEqual(actual, (-1, 3))

    def test_is_collinear(self):
        self.assertTrue(is_collinear([(1., 1.), (2., 2.), (3., 3.)]))
        self.assertFalse(is_collinear([(1., 1.), (2., 2.), (2., 3.)]))

    def test_lines_through_points_mod_one_line(self):
        p1 = ECAffine.from_x(5, 1, Secp256k1_41)
        p2 = ECAffine.from_x(10, 0, Secp256k1_41)
        p3 = -(p1 + p2)
        actual = lines_through_affine(p1, p2, p3)
        self.assertEqual(actual, [[[5., 3., 0.], [27., 25., 0.]]])

    def test_lines_through_points_mod_two_lines(self):
        p1 = ECAffine.from_x(5, 1, Secp256k1_41)
        p2 = ECAffine.from_x(15, 0, Secp256k1_41)
        p3 = -(p1 + p2)
        actual = lines_through_affine(p1, p2, p3)
        expected = [
            [[5.0, 3.0, 0.0], [21.08695652173913, 40.,  0.]],
            [[21.08695652173913, 0.0, 0.0], [39.0, 32.0, 0.0]]
        ]
        self.assertEqual(actual, expected)
