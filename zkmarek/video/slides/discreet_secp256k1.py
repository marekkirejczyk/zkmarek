from manim import LEFT, FadeIn, FadeOut, Flash, Line, Wait

from zkmarek.crypto.weierstrass_curve import Secp256k1_41, WeierstrassCurve
from zkmarek.video.mobjects.discreet_elliptic_chart import DiscreetEllipticChart
from zkmarek.video.mobjects.sidebar import Sidebar

from .slide_base import SlideBase


class DiscreetSecp256k1(SlideBase):
    curve: WeierstrassCurve
    chart: DiscreetEllipticChart

    def __init__(self):
        self.curve = Secp256k1_41
        self.chart = DiscreetEllipticChart(self.curve)

    def create_symmetry_line(self):
        mid_y = self.curve.p / 2
        s = self.chart.ax.c2p(-10, mid_y)
        e = self.chart.ax.c2p(self.curve.p + 10, mid_y)
        return Line(s, e, color="red")

    def create_vertical_line(self, x):
        s = self.chart.ax.c2p(x, 0)
        e = self.chart.ax.c2p(x, self.curve.p)
        return Line(s, e, color="red")

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
        line = self.create_vertical_line(9)
        scene.play(FadeIn(line))
        dots = list(filter(lambda d: d.point.x.value == 9, self.chart.dots))
        scene.play(Flash(dots[0]))
        sline = self.create_symmetry_line()
        scene.play(FadeIn(sline), Wait())
        scene.play(Flash(dots[1]))
        scene.play(FadeOut(sline))
        scene.play(FadeOut(line))

    def animate_in(self, scene):
        scene.play(self.chart.animate_appear())
        self.animate_symmetry(scene)
        self.animate_vertical(scene)
        self.animate_negate(scene)

    def animate_out(self, scene):
        scene.play(self.chart.animate_disappear())
