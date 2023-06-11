from manim import LEFT
from zkmarek.crypto.cec_affine import CECAffine
from zkmarek.video.mobjects.continuous_elliptic_chart import \
    ContinuousEllipticChart
from zkmarek.video.mobjects.dot_on_curve import DotOnCurve
from zkmarek.video.mobjects.sidebar import Sidebar
from zkmarek.video.slides.common.slide_base import SlideBase


class Negation(SlideBase):
    def __init__(self):
        super().__init__("Negation")

    def construct(self):
        self.chart = ContinuousEllipticChart()
        self.chart.align_on_border(LEFT)
        self.sidebar = Sidebar(
            "Negation", tex_path="data/cec/neg.tex", code_path="data/cec/neg.py"
        )
        a = CECAffine.from_x(2)
        self.p1 = DotOnCurve(self.chart.ax, "A", a, include_lines=True)
        self.p2 = DotOnCurve(self.chart.ax, "-A", -a, include_lines=True)
        self.add(self.p1, self.p2, self.chart, self.sidebar)

    def animate_in(self, scene):
        self.chart.animate_in(scene)
        self.p1.animate_in(scene)
        self.p2.animate_in(scene)
        self.sidebar.animate_in(scene, self)
