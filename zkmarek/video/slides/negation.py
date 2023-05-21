from manim import LEFT, Create

from zkmarek.crypto.cec_affine import CECAffine
from zkmarek.video.mobjects.continuous_elliptic_chart import \
    ContinuousEllipticChart
from zkmarek.video.mobjects.dot_on_curve import DotOnCurve
from zkmarek.video.mobjects.sidebar import Sidebar

from .slide_base import SlideBase


class NegationSlide(SlideBase):
    def __init__(self):
        super().__init__(title="Negation")
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
        scene.play(Create(self.chart))
        scene.play(self.p1.animate_appear())
        scene.play(self.p2.animate_appear())
        self.sidebar.animate_appear(scene, self)
