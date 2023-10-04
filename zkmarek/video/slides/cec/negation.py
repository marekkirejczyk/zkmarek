from manim import LEFT, FadeIn, Indicate

from zkmarek.crypto.cec_affine import CECAffine
from zkmarek.video.constant import SECONDARY_COLOR
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
        scene.play(FadeIn(self.chart), FadeIn(self.p1))
        self.new_subsection(scene,
            "Negation",
            sound="data/sound/episode1/s8-1.wav")
        self.sidebar.animate_show_label(scene)
        self.p2.animate_in(scene)
        self.sidebar.animate_show_math(scene)

        scene.wait(1)
        scene.play(Indicate(self.sidebar.math[1]), color=SECONDARY_COLOR)
        scene.wait(1)
        scene.play(Indicate(self.sidebar.math[3]), color=SECONDARY_COLOR)

        self.new_subsection(scene, "Code", "data/sound/episode1/s8-2.wav")
        scene.wait(0.5)
        self.sidebar.animate_show_code(scene)
        scene.wait(3)

        self.sidebar.indicate_code(scene, "class")
        scene.wait(1.5)

        self.sidebar.indicate_code(scene, "x: float")
        self.sidebar.indicate_code(scene, "y: float")

        self.play_sound(scene, "data/sound/episode1/s8-3.wav")
        scene.wait(1)

        self.sidebar.indicate_code(scene, "CECAffine")
        scene.wait(7)

        self.sidebar.indicate_code(scene, "x: float")
        self.sidebar.indicate_code(scene, "y: float")


        self.play_sound(scene, "data/sound/episode1/s8-4.m4a")
        scene.wait(1)
        self.sidebar.indicate_code(scene, "def __init__(self, x: float, y: float):")
        scene.wait(1)
        self.sidebar.indicate_code(scene, "self.x = x")
        self.sidebar.indicate_code(scene, "self.y = y")
        scene.wait(1)
        self.sidebar.indicate_code(scene, "x: float", 1)
        self.sidebar.indicate_code(scene, "y: float", 1)

        self.play_sound(scene, "data/sound/episode1/s8-5.wav")
        scene.wait(3)
        self.sidebar.indicate_code(scene, "def __neg__(self):")
        self.play_sound(scene, "data/sound/episode1/s8-6.wav")
        scene.wait(2)
        self.sidebar.indicate_code(scene, "CECAffine", 1)
        scene.wait(2)
        self.sidebar.indicate_code(scene, "self.x", 1)
        scene.wait(1.5)
        self.sidebar.indicate_code(scene, "-self.y")

