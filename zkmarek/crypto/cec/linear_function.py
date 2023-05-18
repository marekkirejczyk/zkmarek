class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

class BoundingBox:
    x_min: float
    x_max: float
    y_min: float
    y_max: float

    def __init__(self, x_min: float, x_max: float, y_min: float, y_max: float):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

default_bounding_box = BoundingBox(-10, 10, -10, 10)

class LinearFunction:
    a: float
    b: float

    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    @staticmethod
    def from_points(p1, p2):
        a = (p2.y - p1.y) / (p2.x - p1.x)
        return LinearFunction(a, p1.y - a * p1.x)

    @staticmethod
    def extend_points(p1, p2, bounding_box=default_bounding_box):
        a = (p2.y - p1.y) / (p2.x - p1.x)
        return LinearFunction(a, p1.y - a * p1.x).get_points(bounding_box)

    def get_points(self, bounding_box=default_bounding_box):
        points = []
        if self.a == 0:
            points.append(Point(bounding_box.x_min, self.b))
            points.append(Point(bounding_box.x_max, self.b))
            return points
        for x in [bounding_box.x_min, bounding_box.x_max]:
            p = Point(x, self.a * x + self.b)
            if p.y >= bounding_box.y_min and p.y <= bounding_box.y_max:
                points.append(p)
        for y in [bounding_box.y_min, bounding_box.y_max]:
            p = Point((y - self.b) / self.a, y)
            if p.x >= bounding_box.x_min and p.x <= bounding_box.x_max:
                points.append(p)
        return points[0:2]


