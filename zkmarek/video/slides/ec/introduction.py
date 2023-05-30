from manim import FadeIn, FadeOut, Wait

from zkmarek.crypto.weierstrass_curve import Secp256k1_41, WeierstrassCurve
from zkmarek.video.mobjects.discreet_elliptic_chart import \
    DiscreteEllipticChart
from zkmarek.video.mobjects.sidebar import Sidebar
from zkmarek.video.slides.common.slide_base import SlideBase


class Introduction(SlideBase):
    curve: WeierstrassCurve
    chart: DiscreteEllipticChart
    sidebar: Sidebar

    def __init__(self):
        super().__init__("Discrete elliptic curves chart")
        self.curve = Secp256k1_41
        self.chart = DiscreteEllipticChart(self.curve)
        self.chart.center()

    def animate_symmetry(self, scene):
        line = self.chart.create_horizontal_line()
        scene.play(FadeIn(line), Wait())
        scene.play(FadeOut(line))

    def animate_vertical(self, scene):
        for x in range(1, 5):
            line = self.chart.create_vertical_line(x)
            scene.play(FadeIn(line), Wait())
            scene.play(FadeOut(line))

        for x in range(5, 9):
            line = self.chart.create_vertical_line(x)
            scene.play(FadeIn(line))
            scene.play(FadeOut(line))

    def animate_in(self, scene):
        self.chart.animate_appear(scene)
        self.animate_symmetry(scene)
        self.animate_vertical(scene)

    def animate_out(self, scene):
        scene.remove(self.chart)
