from manim import *

from ..cpoint import CPoint
from ..mobjects.point_on_curve import PointOnCurve
from ..mobjects.sidebar import Sidebar
from ..mobjects.continuous_elliptic_chart import ContinuousEllipticChart


class NegationSlide(VGroup):
    def __init__(self):
        VGroup.__init__(self)
        self.chart = ContinuousEllipticChart()
        self.chart.align_on_border(LEFT)
        self.sidebar = Sidebar("Negation", tex_filename="data/neg.tex", code_filename="data/neg.py")
        a = CPoint.from_compressed(2)
        self.p1 = PointOnCurve(self.chart.ax, "A", a, include_lines=True)
        self.p2 = PointOnCurve(self.chart.ax, "-A", -a, include_lines=True)
        self.add(self.p1, self.p2, self.chart, self.sidebar)

    def animate_in(self):
        return [Create(self.chart), self.p1.animate_appear(), self.p2.animate_appear(), Write(self.sidebar)]

    def animate_out(self):
        return [FadeOut(self)]
