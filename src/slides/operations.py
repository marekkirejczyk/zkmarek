from manim import *

from ..cpoint import CPoint
from ..mobjects.continuous_elliptic_chart import ContinuousEllipticChart
from ..mobjects.point_on_curve import PointOnCurve
from ..mobjects.sidebar import Sidebar
from .slide_base import NewSection, SlideBase


class OperationsSlide(SlideBase):
    def __init__(self):
        SlideBase.__init__(self, title="Operations")
        self.chart = ContinuousEllipticChart()
        a = CPoint.from_compressed(1)
        self.p1 = PointOnCurve(self.chart.ax, "A(x, y)", a)
        self.p2 = PointOnCurve(self.chart.ax, "A", a, include_coords=True)
        self.sidebar = Sidebar("Operations", tex_filename="data/operations.tex")

    def animate_in(self):
        return [
            self.chart.animate_appear(),
            self.p1.animate_appear(),
            ReplacementTransform(self.p1, self.p2),
            NewSection("Sidebar"),
            VGroup(self.p2, self.chart).animate.align_on_border(LEFT),
            lambda : self.p2.position_update(),
            Write(self.sidebar),
        ]

    def animate_out(self):
        return [FadeOut(self.p2), FadeOut(self.chart), FadeOut(self.sidebar)]
