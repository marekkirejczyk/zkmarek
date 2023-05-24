from manim import line_intersection
from typing import Sequence
from zkmarek.crypto.ec_affine import ECAffine

Coords = Sequence[float]
Line = Sequence[Coords]


def line_through_collinear(points: Sequence[Coords]) -> Sequence[Coords]:
    sorted_points = sorted(points, key=lambda d: d[0])
    return [sorted_points[0], sorted_points[-1]]


def calculate_line_coefficients(p1: Coords, p2: Coords) -> tuple[float, float]:
    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    b = p1[1] - m * p1[0]
    return (m, b)


def is_collinear(p: Sequence[Coords], threshold=1e-05) -> bool:
    (m, b) = calculate_line_coefficients(p[0], p[1])
    y2 = m * p[2][0] + b
    return abs(y2 - p[2][1]) < threshold


def lines_through_affine(a1: ECAffine, a2: ECAffine, a3: ECAffine) -> Sequence[Line]:
    p1 = a1.to_coords()
    p2 = a2.to_coords()
    p3 = a3.to_coords()

    if is_collinear([p1, p2, p3]):
        return [line_through_collinear([p1, p2, p3])]
    p = float(a1.curve.p+3) #Cheating
    top_line = [[0., p, 0.], [2., p, 0.]]
    top_point = line_intersection([p1, p2], top_line)
    bottom_point = [top_point[0], 0., 0.]
    line1 = [p1, list(top_point)]
    line2 = [list(bottom_point), p3]
    return [line1, line2]
