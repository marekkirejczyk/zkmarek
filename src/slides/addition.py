from manim import *

from ..cpoint import CPoint
from ..mobjects.continuous_elliptic_chart import ContinuousEllipticChart
from ..mobjects.line_through_points import LineThroughPoints
from ..mobjects.point_on_curve import PointOnCurve
from ..mobjects.sidebar import Sidebar
from .slide_base import NewSection, SlideBase


class AdditionSlide(SlideBase):
    def __init__(self):
        SlideBase.__init__(self)
        self.chart = ContinuousEllipticChart()
        self.chart.align_on_border(LEFT)

        a = CPoint.from_compressed(2)
        b = CPoint.from_compressed(3)
        c = a + b
        self.p1 = PointOnCurve(self.chart.ax, "A", a)
        self.p2 = PointOnCurve(self.chart.ax, "B", b)
        self.p3 = PointOnCurve(self.chart.ax, "A + B", c, label_direction=LEFT)
        self.p4 = PointOnCurve(self.chart.ax, "-(A + B)", -c, label_direction=LEFT)
        self.line1 = LineThroughPoints(self.p2, self.p4)
        self.line2 = LineThroughPoints(self.p4, self.p3)
        self.sidebar = Sidebar(
            "Addition", tex_filename="data/add.tex", code_filename="data/add.py"
        )
        self.add(self.chart, self.p1, self.p2, self.p3, self.p4, self.line1, self.line2, self.sidebar)

    def animate_in(self):
        return [
            NewSection("Addition"),
            Create(self.chart),
            self.p1.animate_appear(),
            self.p2.animate_appear(),
            Write(self.line1),
            self.p4.animate_appear(),
            Write(self.line2),
            self.p3.animate_appear(),
            Write(self.sidebar)
        ]
