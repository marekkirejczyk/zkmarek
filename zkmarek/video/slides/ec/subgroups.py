from manim import RED, FadeIn, FadeOut
from zkmarek.crypto.ec_affine import ECAffine

from zkmarek.crypto.subgroup import Subgroup
from zkmarek.crypto.weierstrass_curve import Secp256k1_41, WeierstrassCurve
from zkmarek.video.mobjects.discreet_elliptic_chart import DiscreteEllipticChart
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.ec.animate_subgroup import AnimateSubgroups


class Subgroups(SlideBase):
    chart: DiscreteEllipticChart

    curve: WeierstrassCurve
    # subgroups: list[Subgroup]

    def __init__(self, curve: WeierstrassCurve = Secp256k1_41):
        super().__init__(title="Subgroups")
        self.curve = curve
        self.labels = []

    def construct(self):
        self.chart = DiscreteEllipticChart(self.curve)
        # self.subgroups = Subgroup.generate_all(self.curve)

    def animate_in(self, scene):
        scene.play(FadeIn(self.chart))
        # subgroup = self.subgroups[0]

        generator1 = ECAffine(10, 8, self.curve)
        subgroup1 = Subgroup.from_generator(generator1)

        self.new_subsection(scene, "Subgroup 1")
        animation2a = AnimateSubgroups(self.chart)
        animation2a.animate_subgroup(scene, subgroup1, generator1)
        animation2a.animate_out_labels(scene)
        animation2a.animate_out_dots(scene)

        generator2a = ECAffine(1, 34, self.curve)
        generator2b = ECAffine(1, 7, self.curve)
        subgroup2 = Subgroup.from_generator(generator2a)

        self.new_subsection(scene, "Subgroup 2a")
        animation2a = AnimateSubgroups(self.chart)
        animation2a.animate_subgroup(scene, subgroup2, generator2a)
        animation2a.animate_out_labels(scene)

        self.new_subsection(scene, "Subgroup 2b")
        animation2b = AnimateSubgroups(self.chart)
        animation2b.target_color = RED
        animation2b.runtime_per_step = 0.5
        animation2b.animate_subgroup(scene, subgroup2, generator2b)
        animation2b.animate_out_labels(scene)
        animation2a.animate_out_dots(scene)
        animation2b.animate_out_dots(scene)

    def animate_out(self, scene):
        scene.play(FadeOut(self.chart))
