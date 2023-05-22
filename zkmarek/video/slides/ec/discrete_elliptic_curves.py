from manim import LEFT, FadeIn, FadeOut, Wait

from zkmarek.crypto.weierstrass_curve import Secp256k1_41, WeierstrassCurve
from zkmarek.video.mobjects.discreet_elliptic_chart import \
    DiscreteEllipticChart
from zkmarek.video.mobjects.sidebar import Sidebar
from zkmarek.video.slides.ec.negation import Negation
from zkmarek.video.slides.slide_base import SlideBase


class DiscreteEllipticCurves(SlideBase):
    curve: WeierstrassCurve
    chart: DiscreteEllipticChart
    sidebar: Sidebar

    def __init__(self):
        super().__init__("Discrete elliptic curves chart")
        self.curve = Secp256k1_41
        self.chart = DiscreteEllipticChart(self.curve)
        self.chart.set_z_index(1, family=True)
        self.sidebar = Sidebar(
            "Negation", tex_path="data/cec/neg.tex", code_path="data/ec/neg.py"
        )

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

    def animate_negate(self, scene):
        negation_slide = Negation(self.chart)
        negation_slide.animate_in(scene)
        scene.play(self.chart.animate.align_on_border(LEFT, buff=0.2))
        self.sidebar.animate_appear(scene, self)
        negation_slide.animate_out(scene)

    def animate_in(self, scene):
        self.chart.animate_appear(scene)
        self.animate_symmetry(scene)
        self.animate_vertical(scene)
        self.animate_negate(scene)

    def animate_out(self, scene):
        self.sidebar.animate_disappear(scene)
        self.chart.animate_disappear(scene)
