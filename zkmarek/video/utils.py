from typing import Sequence


def load(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

def get_slides_from_names(slide_names, globals=globals()):
    if slide_names is None:
        return None
    return [globals[name.strip()]() for name in slide_names.split(",")]


def find_x_min_max(points: Sequence[Sequence[float]]) -> tuple[float, float]:
    sorted_points = sorted(points, key=lambda d: d[0])
    return (sorted_points[0], sorted_points[-1])
