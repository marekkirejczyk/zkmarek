from manim import *
from ..mobjects.sidebar import Sidebar
from ..mobjects.continuous_elliptic_chart import ContinuousEllipticChart
from ..mobjects.point_on_curve import PointOnCurve
from ..cpoint import CPoint


class OperationsSlide(VGroup):
    def __init__(self):
        VGroup.__init__(self)
        self.chart = ContinuousEllipticChart()
        self.a = CPoint.from_compressed(1)
        self.p1 = PointOnCurve(self.chart.ax, "A(x, y)", self.a)
        self.p2 = PointOnCurve(self.chart.ax, "A", self.a, include_coords=True)
        self.sidebar = Sidebar("Operations", tex_filename="data/operations.tex")

    def animate_in(self):
        return [
            self.chart.animate_appear(),
            self.p1.animate_appear(),
            VGroup(self.p1, self.chart).animate.align_on_border(LEFT),
            lambda : self.p2.position_update(),
            ReplacementTransform(self.p1, self.p2),
            Write(self.sidebar),
        ]

    def animate_out(self):
        return [FadeOut(self.p2), FadeOut(self.sidebar)]
