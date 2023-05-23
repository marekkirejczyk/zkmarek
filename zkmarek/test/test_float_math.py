import unittest

from zkmarek.crypto.float_math import calculate_line, find_x_min_max, is_collinear

class TestFloatMath(unittest.TestCase):

    def test_find_x_min_max(self):
        actual = find_x_min_max([(1, 2), (3, 4)])
        self.assertEqual(actual, ((1, 2), (3, 4)))
        actual = find_x_min_max([(1, 2), (3, 4), (2, 1)])
        self.assertEqual(actual, ((1, 2), (3, 4)))
        actual = find_x_min_max([(1, 2), (3, 4), (0, 1)])
        self.assertEqual(actual, ((0, 1), (3, 4)))

    def test_calculate_line(self):
        actual = calculate_line((0, 0), (1, 1))
        self.assertEqual(actual, (1, 0))
        actual = calculate_line((0, 0), (-1, 1))
        self.assertEqual(actual, (-1, 0))
        actual = calculate_line((1, 2), (3, 4))
        self.assertEqual(actual, (1, 1))
        actual = calculate_line((1, 2), (2, 1))
        self.assertEqual(actual, (-1, 3))

    def test_is_collinear(self):
        self.assertTrue(is_collinear([(1., 1.), (2., 2.), (3., 3.)]))
        self.assertFalse(is_collinear([(1., 1.), (2., 2.), (2., 3.)]))
