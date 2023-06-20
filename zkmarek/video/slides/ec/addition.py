from manim import FadeOut

from zkmarek.crypto.weierstrass_curve import Secp256k1_41
from zkmarek.video.mobjects.discreet_elliptic_chart import \
    DiscreteEllipticChart
from zkmarek.video.mobjects.sidebar import Sidebar
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.ec.animate_addition import AnimateAddition


class Addition(SlideBase):
    chart: DiscreteEllipticChart
    sidebar: Sidebar

    def __init__(self):
        super().__init__("Discrete elliptic curves - addition")

    def construct(self):
        self.curve = Secp256k1_41
        self.chart = DiscreteEllipticChart(self.curve)
        self.chart.center()
        self.sidebar = Sidebar(
            title="Addition", code_path="data/ec/add.py", tex_path="data/ec/add.tex"
        )

    def animate_in(self, scene):
        scene.add(self.chart)
        AnimateAddition.play(scene, self.chart, 5, 1, 10, 0)
        self.new_subsection(scene, "Overflow the field")
        anim = AnimateAddition.play(scene, self.chart, 5, 1, 9, 1, animate_out=False)
        self.new_subsection(scene, "Sidebar")
        self.chart.animate_align_left(scene)
        self.sidebar.animate_in(scene, self)
        anim.animate_out(scene)

    def animate_out(self, scene):
        self.sidebar.animate_out(scene)
        self.chart.animate_align_center(scene)
        scene.play(FadeOut(self.chart))

