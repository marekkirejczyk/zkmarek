from unittest import TestCase
from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.crypto.subgroup import Subgroup

from zkmarek.crypto.weierstrass_curve import WeierstrassCurve


class TestSubgroup(TestCase):
    def test_from_generator(self):
        curve = WeierstrassCurve(0, 7, 3)
        points = ECAffine.generate_points(curve)
        expected = [ECAffine(0, 2, curve), ECAffine(0, 1, curve), ECAffine(0, 0, curve)]

        subgroup = Subgroup.from_generator(points[0])
        self.assertEqual(set(subgroup.points), set(expected))

        subgroup = Subgroup.from_generator(points[1])
        self.assertEqual(set(subgroup.points), set(expected))

        subgroup = Subgroup.from_generator(ECAffine(0, 0, curve))
        self.assertEqual(set(subgroup.points), set([ECAffine(0, 0, curve)]))

    def test_generate_all(self):
        curve = WeierstrassCurve(0, 7, 3)
        points = ECAffine.generate_points(curve)
        expected1 = [
            ECAffine(0, 2, curve),
            ECAffine(0, 1, curve),
            ECAffine(0, 0, curve),
        ]
        expected2 = [ECAffine(2, 0, curve), ECAffine(0, 0, curve)]
        subgroups = Subgroup.generate_all(points)
        self.assertEqual(len(subgroups), 2)
        self.assertEqual(set(subgroups[0].points), set(expected1))
        self.assertEqual(set(subgroups[1].points), set(expected2))
