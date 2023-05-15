from manim import FadeIn, FadeOut, Line, Wait

from zkmarek.crypto.weierstrass_curve import Secp256k1_41
from zkmarek.video.mobjects.discreet_elliptic_chart import DiscreetEllipticChart

from .slide_base import SlideBase


class DiscreetSecp256k1(SlideBase):
    def __init__(self):
        self.curve = Secp256k1_41
        self.chart = DiscreetEllipticChart(self.curve)

    def animate_symmetry(self, scene):
        mid_y = self.curve.p / 2
        print(f"mid_y: {mid_y}")
        s = self.chart.ax.c2p(-10, mid_y)
        e = self.chart.ax.c2p(self.curve.p + 10, mid_y)
        line = Line(s, e, color="red")
        scene.play(FadeIn(line), Wait())
        scene.play(FadeOut(line))

    def animate_vertical(self, scene):
        def line_for(x):
            s = self.chart.ax.c2p(x, 0)
            e = self.chart.ax.c2p(x, self.curve.p)
            return Line(s, e, color="red")

        for x in range(0, 5):
            line = line_for(x)
            scene.play(FadeIn(line), Wait())
            scene.play(FadeOut(line))

        for x in range(5, 11):
            line = line_for(x)
            scene.play(FadeIn(line))
            scene.play(FadeOut(line))

    def animate_in(self, scene):
        scene.play(self.chart.animate_appear())
        self.animate_symmetry(scene)
        self.animate_vertical(scene)

    def animate_out(self, scene):
        scene.play(self.chart.animate_disappear())
