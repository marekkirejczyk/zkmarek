from manim import *

from cpoint import CPoint
from mobjects.continuous_elliptic_chart import ContinuousEllipticChart
from mobjects.point_on_curve import PointOnCurve
from mobjects.sidebar import Sidebar
from .slide_base import SlideBase


class NegationSlide(SlideBase):
    def __init__(self):
        SlideBase.__init__(self, title="Negation")
        self.chart = ContinuousEllipticChart()
        self.chart.align_on_border(LEFT)
        self.sidebar = Sidebar(
            "Negation", tex_filename="data/neg.tex", code_filename="data/neg.py"
        )
        a = CPoint.from_compressed(2)
        self.p1 = PointOnCurve(self.chart.ax, "A", a, include_lines=True)
        self.p2 = PointOnCurve(self.chart.ax, "-A", -a, include_lines=True)
        self.add(self.p1, self.p2, self.chart, self.sidebar)

    def animate_in(self, scene):
        scene.play(Create(self.chart))
        scene.play(self.p1.animate_appear())
        scene.play(self.p2.animate_appear())
        scene.play(Write(self.sidebar))
