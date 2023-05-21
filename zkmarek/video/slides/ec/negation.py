from manim import (DARK_GREY, LEFT, RED, RIGHT, FadeIn, FadeOut, Indicate,
                   Line, Tex, Wait)

from zkmarek.crypto.weierstrass_curve import Secp256k1_41, WeierstrassCurve
from zkmarek.video.mobjects.discreet_elliptic_chart import \
    DiscreteEllipticChart
from zkmarek.video.mobjects.sidebar import Sidebar
from zkmarek.video.slides.slide_base import SlideBase



class Negation(SlideBase):
    curve: WeierstrassCurve
    chart: DiscreteEllipticChart
    sidebar: Sidebar
    label1: Tex
    label2: Tex


    def __init__(self):
        super().__init__(title="Discrete elliptic curves chart")
        self.curve = Secp256k1_41
        self.chart = DiscreteEllipticChart(self.curve)
        self.chart.set_z_index(1, family=True)
        self.label1 = Tex("A", font_size=28)
        self.label2 = Tex("-A", font_size=28)

    def create_symmetry_line(self):
        mid_y = self.curve.p / 2
        s = self.chart.ax.c2p(-1, mid_y)
        e = self.chart.ax.c2p(self.curve.p, mid_y)
        return Line(s, e, color=DARK_GREY, z_index=0)

    def create_vertical_line(self, x):
        s = self.chart.ax.c2p(x, -1)
        e = self.chart.ax.c2p(x, self.curve.p)
        return Line(s, e, color=DARK_GREY, z_index=0)

    def create_sidebar(self):
        self.sidebar = Sidebar(
            "Negation", tex_path="data/cec/neg.tex", code_path="data/ec/neg.py"
        )

    def animate_symmetry(self, scene):
        line = self.create_symmetry_line()
        scene.play(FadeIn(line), Wait())
        scene.play(FadeOut(line))

    def animate_vertical(self, scene):
        for x in range(1, 5):
            line = self.create_vertical_line(x)
            scene.play(FadeIn(line), Wait())
            scene.play(FadeOut(line))

        for x in range(5, 9):
            line = self.create_vertical_line(x)
            scene.play(FadeIn(line))
            scene.play(FadeOut(line))

    def animate_negate(self, scene):
        self.new_subsection(scene, "Negation")
        scene.play(self.chart.animate.align_on_border(LEFT, buff=0.2))

        line = self.create_vertical_line(9)
        scene.play(FadeIn(line))
        dots = self.chart.find_dots_by_x(9)
        scene.play(Indicate(dots[0], scale_factor=2))
        dots[0].set_color(RED)
        self.label1.next_to(dots[0], RIGHT)
        scene.play(FadeIn(self.label1))
        sline = self.create_symmetry_line()
        scene.play(FadeIn(sline), Wait())
        scene.play(Indicate(dots[1], scale_factor=2))
        dots[1].set_color(RED)
        self.label2.next_to(dots[1], RIGHT)
        scene.play(FadeIn(self.label2))

        self.sidebar.animate_appear(scene, self)
        scene.play(FadeOut(sline))
        scene.play(FadeOut(line))

    def animate_in(self, scene):
        self.create_sidebar()
        scene.play(self.chart.animate_appear())
        self.animate_symmetry(scene)
        self.animate_vertical(scene)
        self.animate_negate(scene)

    def animate_out(self, scene):
        scene.play(FadeOut(self.label1))
        scene.play(FadeOut(self.label2))
        self.sidebar.animate_disappear(scene)
        scene.play(self.chart.animate_disappear())
