from manim import LEFT, FadeIn
from zkmarek.crypto.cec_affine import CECAffine
from zkmarek.video.mobjects.continuous_elliptic_chart import \
    ContinuousEllipticChart
from zkmarek.video.mobjects.dot_on_curve import DotOnCurve
from zkmarek.video.mobjects.sidebar import Sidebar
from zkmarek.video.slides.common.slide_base import SlideBase


class Negation(SlideBase):
    def __init__(self):
        super().__init__("Elliptic Curves Negation")

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
        self.new_subsection(scene,
            "Negation",
            sound="data/sound/episode/s7-1.wav")

        scene.play(FadeIn(self.chart), FadeIn(self.p1))
        self.sidebar.animate_show_label(scene)
        self.p2.animate_in(scene)
        self.sidebar.animate_show_math(scene)
        self.play_sound(scene, "data/sound/episode/s7-2.wav")
        self.sidebar.animate_show_code(scene)
        scene.wait(2)
        # self.play_sound(scene, "data/sound/episode/s7-3.wav")
        # self.play_sound(scene, "data/sound/episode/s7-4.wav")
        # self.play_sound(scene, "data/sound/episode/s7-5.wav")
        # self.play_sound(scene, "data/sound/episode/s7-6.wav")

