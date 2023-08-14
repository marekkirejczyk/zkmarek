from manim import RED, RIGHT, Dot, Indicate, Line, Tex

from zkmarek.crypto.weierstrass_curve import Secp256k1_41
from zkmarek.video.constant import HIGHLIGHT_COLOR, PRIMARY_COLOR
from zkmarek.video.mobjects.discreet_elliptic_chart import \
    DiscreteEllipticChart
from zkmarek.video.mobjects.sidebar import Sidebar
from zkmarek.video.slides.common.slide_base import SlideBase


class Negation(SlideBase):
    chart: DiscreteEllipticChart
    label1: Tex
    label2: Tex
    dots: list[Dot]
    h_line: Line
    v_line: Line

    def __init__(self) -> None:
        super().__init__("Negation")

    def construct(self):
        self.chart = DiscreteEllipticChart(Secp256k1_41)
        self.chart.center()
        self.label1 = Tex("A", font_size=28, color=PRIMARY_COLOR)
        self.label2 = Tex("-A", font_size=28, color=PRIMARY_COLOR)
        self.dots = self.chart.find_dots_by_x(9)
        self.sidebar = Sidebar(
            "Negation", tex_path="data/cec/neg.tex", code_path="data/ec/neg.py"
        )

    def indicate_dot(self, scene, dot, label):
        scene.play(Indicate(dot, scale_factor=2, color=HIGHLIGHT_COLOR))
        dot.set_color(HIGHLIGHT_COLOR)
        label.next_to(dot, RIGHT)
        self.chart.add(dot)
        self.chart.animate_add(scene, label, run_time=0.5)

    def animate_in(self, scene):
        self.new_subsection(scene, "Elliptic Curve Negation",
            sound="data/sound/episode/s14-1.wav")
        scene.add(self.chart)
        scene.wait(4)

        self.v_line = self.chart.create_vertical_line(9)
        self.chart.animate_add(scene, self.v_line)
        self.indicate_dot(scene, self.dots[0], self.label1)

        self.h_line = self.chart.create_horizontal_line()
        self.chart.animate_add(scene, self.h_line)
        self.indicate_dot(scene, self.dots[1], self.label2)

        self.chart.animate_align_left(scene, run_time=0.5)
        self.sidebar.animate_fast_show_math(scene)
        self.sidebar.math_set_color(10, 12)
        scene.wait(2)

        self.new_subsection(scene, "Elliptic Curve class",
            sound="data/sound/episode/s14-2.wav")
        self.sidebar.animate_show_code(scene)
        scene.wait(2)
        self.sidebar.indicate_code(scene, "class ECAffine")

        self.new_subsection(scene, "Elliptic Curve coordinates",
            sound="data/sound/episode/s14-3.wav")
        self.sidebar.indicate_code(scene, "x: Field")
        self.sidebar.indicate_code(scene, "y: Field")
        scene.wait(1.5)
        self.sidebar.indicate_code(scene, "Field", 0)
        self.sidebar.indicate_code(scene, "Field", 1)

        self.new_subsection(scene, "Elliptic Curve negation operator",
            sound="data/sound/episode/s14-4.wav")
        scene.wait(3)
        self.sidebar.indicate_code(scene, "__neg__")
        scene.wait(3)
        self.sidebar.indicate_code(scene, "ECAffine", 2)
        scene.wait(1)
        self.sidebar.indicate_code(scene, "-self.y")


    def animate_out(self, scene):
        self.sidebar.animate_out(scene)
        self.chart.animate_align_center(scene)
        self.chart.animate_remove(
            scene,
            self.v_line,
            self.h_line,
            self.label1,
            self.label2,
            self.dots[0],
            self.dots[1],
        )
        scene.remove(self.chart)
