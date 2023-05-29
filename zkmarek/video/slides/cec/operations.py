from manim import LEFT, FadeOut, ReplacementTransform, Scene, VGroup, Write

from zkmarek.crypto.cec_affine import CECAffine
from zkmarek.video.mobjects.continuous_elliptic_chart import \
    ContinuousEllipticChart
from zkmarek.video.mobjects.dot_on_curve import DotOnCurve
from zkmarek.video.mobjects.sidebar import Sidebar
from zkmarek.video.slides.common.slide_base import SlideBase



class Operations(SlideBase):
    def __init__(self):
        super().__init__(title="Operations")
        self.chart = ContinuousEllipticChart()
        a = CECAffine.from_x(1)
        self.p1 = DotOnCurve(self.chart.ax, "A(x, y)", a)
        self.p2 = DotOnCurve(self.chart.ax, "A", a, include_coords=True)
        self.sidebar = Sidebar("Operations", tex_path="data/cec/operations.tex")

    def animate_in(self, scene: Scene):
        scene.play(self.chart.animate_appear())
        scene.play(self.p1.animate_appear())
        scene.play(ReplacementTransform(self.p1, self.p2))
        scene.next_section("Sidebar"),
        scene.play(VGroup(self.p2, self.chart).animate.align_on_border(LEFT))
        scene.play(Write(self.sidebar))

    def animate_out(self, scene: Scene):
        scene.play(FadeOut(self.p2))
        scene.play(FadeOut(self.chart))
        scene.play(FadeOut(self.sidebar))
