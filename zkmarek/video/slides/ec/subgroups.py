from manim import FadeIn, FadeOut
from zkmarek.crypto.ec_affine import ECAffine

from zkmarek.crypto.subgroup import Subgroup
from zkmarek.crypto.weierstrass_curve import Secp256k1_41, WeierstrassCurve
from zkmarek.video.constant import BACKGROUND_COLOR, PRIMARY_COLOR, SECONDARY_COLOR
from zkmarek.video.mobjects.discreet_elliptic_chart import DiscreteEllipticChart
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.ec.animate_subgroup import AnimateSubgroups


class Subgroups(SlideBase):
    chart: DiscreteEllipticChart
    curve: WeierstrassCurve

    def __init__(self, curve: WeierstrassCurve = Secp256k1_41):
        super().__init__(title="Subgroups")
        self.curve = curve
        self.labels = []

    def construct(self):
        self.chart = DiscreteEllipticChart(self.curve, dot_color=BACKGROUND_COLOR)

    def animate_in(self, scene):
        self.new_subsection(scene, "Subgroups",
            sound="data/sound/episode/s22-1.m4a")

        scene.play(FadeIn(self.chart))

        generator1 = ECAffine(10, 8, self.curve)
        subgroup1 = Subgroup.from_generator(generator1)
        animation1 = AnimateSubgroups(self.chart, runtime_per_step=0.6)

        animation1.animate_generator(scene, generator1, split_animation=True)
        scene.wait(2)
        animation1.animate_subgroup_mid(scene, subgroup1, generator1, 2, 5)
        self.new_subsection(scene, "Subgroups",
            sound="data/sound/episode/s22-2.wav")

        animation1.animate_subgroup_end(scene, subgroup1, generator1, 5)
        animation1.animate_out_labels(scene)

        generator2 = ECAffine(1, 34, self.curve)
        generator3 = ECAffine(1, 7, self.curve)
        subgroup2 = Subgroup.from_generator(generator2)

        self.new_subsection(scene, "Subgroups of a subgroup",
            sound="data/sound/episode/s22-3.wav")

        animation2 = AnimateSubgroups(self.chart, target_color=SECONDARY_COLOR)
        animation2.animate_subgroup(scene, subgroup2, generator2)
        scene.wait(3)
        animation1.animate_out_dots(scene)
        animation2.animate_out_labels(scene)

        animation3 = AnimateSubgroups(self.chart, target_color=PRIMARY_COLOR)
        animation3.runtime_per_step = 0.5
        animation3.animate_subgroup(scene, subgroup2, generator3)

        animation3.animate_out_labels(scene)
        animation2.animate_out_dots(scene)
        animation3.animate_out_dots(scene)

    def animate_out(self, scene):
        scene.play(FadeOut(self.chart))
