from typing import Sequence


def find_x_min_max(
    points: Sequence[Sequence[float]],
) -> tuple[Sequence[float], Sequence[float]]:
    sorted_points = sorted(points, key=lambda d: d[0])
    return (sorted_points[0], sorted_points[-1])


def calculate_line(p1: Sequence[float], p2: Sequence[float]) -> tuple[float, float]:
    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    b = p1[1] - m * p1[0]
    return (m, b)


def is_collinear(p: Sequence[Sequence[float]]) -> bool:
    (m, b) = calculate_line(p[0], p[1])
    y2 = m * p[2][0] + b
    return abs(y2 - p[2][1]) < 0.01
