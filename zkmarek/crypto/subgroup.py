from typing import List

from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.crypto.weierstrass_curve import WeierstrassCurve


class Subgroup:
    generator: ECAffine
    all_generators: List[ECAffine]
    points: List[ECAffine]

    def __init__(self, generator: ECAffine):
        self.generator = generator
        self.points = []
        self.all_generators = [generator]

    def __repr__(self) -> str:
        points = ", ".join([str(point) for point in self.points])
        all_gen = ", ".join([str(point) for point in self.all_generators])
        n = len(self.points)
        return f"Subgroup(order={n}\n generator={self.generator}\n" \
               f"allgen=[{all_gen}]\n points=[{points}])"

    def __eq__(self, other: "Subgroup") -> bool:
        return set(self.points) == set(other.points)

    def order(self) -> int:
        return len(self.points)

    @staticmethod
    def generate_all(curve: WeierstrassCurve) -> "List[Subgroup]":
        return Subgroup.generate_all_from_points(ECAffine.generate_points(curve))

    @staticmethod
    def generate_all_from_points(points: List[ECAffine]) -> "List[Subgroup]":
        result = []
        for point in points:
            subgroup = Subgroup.from_generator(point)
            if subgroup not in result:
                result.append(subgroup)
            else:
                result[result.index(subgroup)].all_generators.append(point)
        return result

    @staticmethod
    def from_generator(generator: ECAffine) -> "Subgroup":
        point = generator
        result = Subgroup(generator)
        while True:
            result.points.append(point)
            point = point + generator
            if point == generator:
                break
        return result
