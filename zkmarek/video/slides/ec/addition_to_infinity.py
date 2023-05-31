from manim import DARK_GREY, FadeOut, GrowFromPoint, Line

from zkmarek.crypto.weierstrass_curve import Secp256k1_41
from zkmarek.video.mobjects.discreet_elliptic_chart import \
    DiscreteEllipticChart
from zkmarek.video.mobjects.point_at_infinity import PointAtInfinity
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
        self.chart.center()
        self.point_at_infinity = PointAtInfinity(self.chart.ax, 9, 43)

    def animate_in(self, scene):
        scene.add(self.chart)
        dots = self.chart.find_dots_by_x(9)
        self.line = Line(
            dots[1].get_center(),
            self.point_at_infinity.dot.get_center(),
            color=DARK_GREY,
            z_index=0,
        )
        scene.play(GrowFromPoint(self.line, point=dots[1].get_center(), run_time=3))
        self.point_at_infinity.animate_in(scene)

    def animate_out(self, scene):
        scene.play(FadeOut(self.line))
        self.point_at_infinity.animate_out(scene)
        scene.play(FadeOut(self.chart))
