from manim import (DEGREES, GREEN, ORIGIN, UP, Angle, Line,
                   VMobject)
from numpy import concatenate
from zkmarek.video.constant import BACKGROUND_COLOR

class FillAngle(VMobject):
    def __init__(self, length = 2, fillcolor = BACKGROUND_COLOR, deg1 = 0, deg2 = 90):
        super().__init__()
        l1 = Line(ORIGIN, length * UP).rotate(-deg1 * DEGREES, about_point=ORIGIN)
        l2 = Line(ORIGIN, length * UP).rotate(-deg2 * DEGREES, about_point=ORIGIN)
        norm = l1.get_length()
        a1 = Angle(l1, l2, other_angle=True, radius=norm - 0.5).set_color(GREEN)
        a2 = Angle(l1, l2, other_angle=True, radius=norm).set_color(GREEN)
        q1 = a1.points
        q2 = a2.reverse_direction().points
        pnts = concatenate([q1, q2, q1[0].reshape(1, 3)])
        self.set_color(fillcolor)
        self.set_points_as_corners(pnts).set_fill(fillcolor, opacity=1)
