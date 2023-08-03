from manim import LEFT, FadeOut, ReplacementTransform, Scene, VGroup, Write

from zkmarek.crypto.cec_affine import CECAffine
from zkmarek.video.mobjects.continuous_elliptic_chart import \
    ContinuousEllipticChart
from zkmarek.video.mobjects.dot_on_curve import DotOnCurve
from zkmarek.video.mobjects.sidebar import Sidebar
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import HIGHLIGHT_COLOR


class Operations(SlideBase):
    sidebar: Sidebar
    p1: DotOnCurve
    p2: DotOnCurve

    def __init__(self):
        super().__init__("Elliptic Curves Operations")

    def construct(self):
        self.chart = ContinuousEllipticChart()
        a = CECAffine.from_x(1)
        self.p1 = DotOnCurve(self.chart.ax, "A(x, y)", a)
        self.p2 = DotOnCurve(self.chart.ax, "A", a, include_coords=True)
        self.sidebar = Sidebar("Operations", tex_path="data/cec/operations.tex")

    def animate_in(self, scene: Scene):
        self.play_sound(scene, "data/sound/episode/s6-1.wav")
        self.chart.animate_in(scene)
        self.p1.animate_in(scene)
        scene.play(ReplacementTransform(self.p1, self.p2))
        self.new_subsection(scene,
            "Operations",
            sound="data/sound/episode/s6-2.wav")
        scene.play(VGroup(self.p2, self.chart).animate.align_on_border(LEFT))
        scene.play(Write(self.sidebar))

        list = self.sidebar.math
        list.set_color_by_tex("Negation", HIGHLIGHT_COLOR)
        scene.wait(2)
        list.set_color_by_tex("Addition", HIGHLIGHT_COLOR)
        scene.wait(2)
        list.set_color_by_tex("Doubling", HIGHLIGHT_COLOR)


    def animate_out(self, scene: Scene):
        scene.play(FadeOut(self.p2))
        scene.play(FadeOut(self.chart))
        scene.play(FadeOut(self.sidebar))
