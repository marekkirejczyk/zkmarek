from manim import LEFT, FadeOut, Indicate, ReplacementTransform, Scene, VGroup

from zkmarek.crypto.cec_affine import CECAffine
from zkmarek.video.constant import HIGHLIGHT_COLOR
from zkmarek.video.mobjects.continuous_elliptic_chart import \
    ContinuousEllipticChart
from zkmarek.video.mobjects.dot_on_curve import DotOnCurve
from zkmarek.video.mobjects.sidebar import Sidebar
from zkmarek.video.slides.common.slide_base import SlideBase


class Operations(SlideBase):
    sidebar: Sidebar
    p1: DotOnCurve
    p2: DotOnCurve
    copy: DotOnCurve

    def __init__(self):
        super().__init__("Elliptic Curves Operations")

    def construct(self):
        self.chart = ContinuousEllipticChart()
        a = CECAffine.from_x(1)
        self.p1 = DotOnCurve(self.chart.ax, "A(x, y)", a)
        self.p2 = DotOnCurve(self.chart.ax, "A", a, include_coords=True)
        self.sidebar = Sidebar("Operations", tex_path="data/cec/operations.tex")

    def animate_in(self, scene: Scene):
        self.new_subsection(scene,
            "Operations",
            sound="data/sound/episode/s6-1.wav")

        self.chart.animate_in(scene)
        self.p1.animate_in(scene)
        scene.wait(0.5)
        scene.play(ReplacementTransform(self.p1, self.p2))

        scene.wait(3)
        scene.play(VGroup(self.p2, self.chart).animate.align_on_border(LEFT),
            run_time=2)
        self.sidebar.animate_show_label(scene)
        scene.wait(2)

        self.copy = self.p2.dot.copy()
        scene.play(Indicate(self.copy))

        self.sidebar.animate_show_math(scene)

        self.new_subsection(scene,
            "Operations",
            sound="data/sound/episode/s6-2.wav")
        scene.wait(3)
        list = self.sidebar.math
        list[0][0:12].set_color(HIGHLIGHT_COLOR)
        scene.wait(2)
        list[0][12:25].set_color(HIGHLIGHT_COLOR)
        scene.wait(2)
        list[0][25:38].set_color(HIGHLIGHT_COLOR)
        scene.wait(1)

    def animate_out(self, scene: Scene):
        scene.play(FadeOut(self.p2),
            FadeOut(self.copy),
            FadeOut(self.chart))
        scene.play(FadeOut(self.sidebar))
