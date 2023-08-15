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
        self.new_subsection(scene, "Elliptic Curve Addition",
            sound="data/sound/episode/s15-0.wav")
        scene.add(self.chart)

        self.new_subsection(scene, "Elliptic Curve Addition example",
            sound="data/sound/episode/s15-1.wav")
        scene.wait(5)
        AnimateAddition.play(scene, self.chart, 5, 1, 10, 0,
            wait_time_between=3)

        self.new_subsection(scene, "Elliptic Curve - Addition overflow the field",
            sound="data/sound/episode/s15-2.wav")

        anim = AnimateAddition.play(scene, self.chart, 5, 1, 9, 1,
            animate_out=False)

        self.new_subsection(scene, "Elliptic Curve - Addition math",
            sound="data/sound/episode/s15-3.wav")

        self.chart.animate_align_left(scene)
        self.sidebar.animate_show_label(scene)
        self.sidebar.animate_show_math(scene)
        scene.wait(7)
        self.sidebar.animate_show_code(scene)
        scene.wait(1)

        anim.animate_out(scene)

    def animate_out(self, scene):
        self.sidebar.animate_out(scene)
        self.chart.animate_align_center(scene)
        scene.play(FadeOut(self.chart))

