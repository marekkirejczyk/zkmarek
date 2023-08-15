from manim import DARK_GREY, RIGHT, FadeIn, FadeOut, GrowFromPoint, Line, Tex

from zkmarek.crypto.weierstrass_curve import Secp256k1_41
from zkmarek.video.constant import PRIMARY_COLOR
from zkmarek.video.mobjects.discreet_elliptic_chart import \
    DiscreteEllipticChart
from zkmarek.video.mobjects.point_at_infinity import PointAtInfinity
from zkmarek.video.mobjects.sidebar import Sidebar
from zkmarek.video.slides.common.slide_base import SlideBase


class AdditionToInfinity(SlideBase):
    chart: DiscreteEllipticChart
    point_at_infinity: PointAtInfinity
    line: Line

    def __init__(self):
        super().__init__("Discrete elliptic curves addition - point at infinity")

    def construct(self):
        self.curve = Secp256k1_41
        self.chart = DiscreteEllipticChart(self.curve)
        self.point_at_infinity = PointAtInfinity(self.chart.ax, 9, 43)
        self.sidebar = Sidebar(
            title="Addition",
            code_path="data/ec/add.py",
            tex_path="data/ec/add.tex"
        )

    def animate_in(self, scene):
        self.new_subsection(scene, "Elliptic Curve - Addition code - point at infinity",
            sound="data/sound/episode/s16-1.wav")

        scene.add(self.chart)
        dots = self.chart.find_dots_by_x(9)
        self.line = Line(
            dots[1].get_center(),
            self.point_at_infinity.dot.get_center(),
            color=DARK_GREY,
            z_index=0,
        )
        self.label1 = Tex("A", font_size=24, color=PRIMARY_COLOR).next_to(
            dots[1], RIGHT)
        self.label2 = Tex("-A", font_size=24, color=PRIMARY_COLOR).next_to(
            dots[0], RIGHT)
        scene.play(FadeIn(self.label1))
        scene.play(FadeIn(self.label2))
        self.chart.add(self.label1)
        self.chart.add(self.label2)
        scene.play(GrowFromPoint(self.line, point=dots[1].get_center(), run_time=1))

        self.point_at_infinity.animate_in(scene)
        self.chart.add(self.point_at_infinity)
        self.chart.add(self.line)
        self.chart.animate_align_left(scene)
        self.sidebar.animate_fast_show_math(scene)
        self.sidebar.animate_replace_math(scene, "data/ec/add_inf.tex")
        self.sidebar.math_set_color(0, 16)
        scene.wait(2)

        self.sidebar.animate_hide_math(scene)
        self.sidebar.animate_show_code(scene)
        self.sidebar.animate_replace_code(scene, "data/ec/add_inf.py")

        self.new_subsection(scene, "Elliptic Curve - Addition code",
            sound="data/sound/episode/s16-2.wav")
        scene.wait(3)
        self.sidebar.animate_replace_code(scene, "data/ec/add_double.py")
        scene.wait(2)

    def animate_out(self, scene):
        scene.play(FadeOut(self.sidebar), FadeOut(self.chart))
