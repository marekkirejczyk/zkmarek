from typing import List

from zkmarek.crypto.ec_affine import ECAffine


class Subgroup:
    generator: ECAffine
    points: List[ECAffine]

    def __init__(self, generator: ECAffine):
        self.generator = generator
        self.points = []

    def __repr__(self) -> str:
        points = ", ".join([str(point) for point in self.points])
        return f"Subgroup(generator={self.generator}, points=[{points}])"

    def __eq__(self, other: object) -> bool:
        return set(self.points) == set(other.points)

    @staticmethod
    def generate_all(points: List[ECAffine]) -> "List[Subgroup]":
        result = []
        for point in points:
            subgroup = Subgroup.from_generator(point)
            if subgroup not in result:
                result.append(subgroup)
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
