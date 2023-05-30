from manim import RED, RIGHT, Dot, FadeOut, Indicate, Line, Tex, FadeIn

from zkmarek.crypto.weierstrass_curve import Secp256k1_41
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
        self.chart = DiscreteEllipticChart(Secp256k1_41)
        self.chart.center()
        self.label1 = Tex("A", font_size=28)
        self.label2 = Tex("-A", font_size=28)
        self.dots = self.chart.find_dots_by_x(9)
        self.sidebar = Sidebar(
            "Negation", tex_path="data/cec/neg.tex", code_path="data/ec/neg.py"
        )

    def indicate_dot(self, scene, dot, label):
        scene.play(Indicate(dot, scale_factor=2))
        dot.set_color(RED)
        label.next_to(dot, RIGHT)
        self.chart.add(dot)
        self.chart.animate_add(scene, label)

    def animate_in(self, scene):
        scene.play(FadeIn(self.chart))
        self.v_line = self.chart.create_vertical_line(9)
        self.chart.animate_add(scene, self.v_line)
        self.indicate_dot(scene, self.dots[0], self.label1)

        self.h_line = self.chart.create_horizontal_line()
        self.chart.animate_add(scene, self.h_line)
        self.indicate_dot(scene, self.dots[1], self.label2)

        self.chart.animate_align_left(scene)
        self.sidebar.animate_appear(scene, self)
        self.sidebar.animate_disappear(scene)
        self.chart.animate_align_center(scene)

    def animate_out(self, scene):
        self.chart.animate_remove(
            scene,
            self.v_line,
            self.h_line,
            self.label1,
            self.label2,
            self.dots[0],
            self.dots[1],
        )
        scene.play(FadeOut(self.chart))
