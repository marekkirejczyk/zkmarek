import unittest

from zkmarek.crypto.cec.linear_function import LinearFunction, Point




class TestLinearFunction(unittest.TestCase):
    def test_from_points(self):
        f = LinearFunction.from_points(Point(2, 1), Point(3, 2))
        self.assertEqual((f.a, f.b), (1, -1))
        f = LinearFunction.from_points(Point(1, 0), Point(2, 2))
        self.assertEqual((f.a, f.b), (2., -2.))

    def test_get_points_a_zero(self):
        f = LinearFunction(0, 0)
        self.assertEqual(f.get_points(), [Point(-10, 0), Point(10, 0)])
        f = LinearFunction(0, 1)
        self.assertEqual(f.get_points(), [Point(-10, 1), Point(10, 1)])
        f = LinearFunction(0, -1)
        self.assertEqual(f.get_points(), [Point(-10, -1), Point(10, -1)])
        f = LinearFunction(0, 2)
        self.assertEqual(f.get_points(), [Point(-10, 2), Point(10, 2)])

    def test_get_points_a_non_zero(self):
        f = LinearFunction(1, 0)
        self.assertEqual(f.get_points(), [Point(-10, -10), Point(10, 10)])
        f = LinearFunction(1, 1)
        self.assertEqual(f.get_points(), [Point(-10, -9), Point(9, 10)])
        f = LinearFunction(1, -1)
        self.assertEqual(f.get_points(), [Point(10, 9), Point(-9, -10)])
        f = LinearFunction(2, 0)
        self.assertEqual(f.get_points(), [Point(-5, -10), Point(5, 10)])
        f = LinearFunction(-2, -1)
        self.assertEqual(f.get_points(), [Point(4.5, -10), Point(-5.5, 10)])
