from manim import GREEN

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
        self.chart.center()
        self.subgroups = Subgroup.generate_all(self.curve)

    def animate_in(self, scene):
        scene.add(self.chart)
        subgroup = self.subgroups[0]

        animation1 = AnimateSubgroups(self.chart)
        animation1.animate_subgroup(scene, subgroup, subgroup.generator)
        animation1.animate_out_labels(scene)

        animation2 = AnimateSubgroups(self.chart)
        animation2.target_color = GREEN
        animation2.runtime_per_step = 0.5
        animation2.animate_subgroup(scene, subgroup, subgroup.all_generators[1])
        animation2.animate_out_labels(scene)
        animation1.animate_out_dots(scene)
        animation2.animate_out_dots(scene)

    def animate_out(self, scene):
        scene.remove(self.chart)
