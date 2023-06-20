from manim import RED, FadeIn, FadeOut

from zkmarek.crypto.subgroup import Subgroup
from zkmarek.crypto.weierstrass_curve import Secp256k1_41, WeierstrassCurve
from zkmarek.video.mobjects.discreet_elliptic_chart import DiscreteEllipticChart
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.ec.animate_subgroup import AnimateSubgroups


class Subgroups(SlideBase):
    chart: DiscreteEllipticChart

    curve: WeierstrassCurve
    subgroups: list[Subgroup]

    def __init__(self, curve: WeierstrassCurve = Secp256k1_41):
        super().__init__(title="Subgroups")
        self.curve = curve
        self.labels = []

    def construct(self):
        self.chart = DiscreteEllipticChart(self.curve)
        self.subgroups = Subgroup.generate_all(self.curve)

    def animate_in(self, scene):
        scene.play(FadeIn(self.chart))
        subgroup = self.subgroups[0]


        self.new_subsection(scene, "Subgroup 1")
        animation1 = AnimateSubgroups(self.chart)
        animation1.animate_subgroup(scene, subgroup, subgroup.generator)
        animation1.animate_out_labels(scene)

        self.new_subsection(scene, "Subgroup 2")
        animation2 = AnimateSubgroups(self.chart)
        animation2.target_color = RED
        animation2.runtime_per_step = 0.5
        animation2.animate_subgroup(scene, subgroup, subgroup.all_generators[1])
        animation2.animate_out_labels(scene)
        animation1.animate_out_dots(scene)
        animation2.animate_out_dots(scene)

    def animate_out(self, scene):
        scene.play(FadeOut(self.chart))
