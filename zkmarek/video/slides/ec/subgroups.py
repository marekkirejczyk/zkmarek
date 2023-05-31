from manim import BLUE, RIGHT, Dot, FadeOut, Flash, MathTex, Scene, Write

from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.crypto.subgroup import Subgroup
from zkmarek.crypto.weierstrass_curve import Secp256k1_41, WeierstrassCurve
from zkmarek.video.mobjects.discreet_elliptic_chart import DiscreteEllipticChart
from zkmarek.video.mobjects.point_at_infinity import PointAtInfinity
from zkmarek.video.slides.common.slide_base import SlideBase


class Subgroups(SlideBase):
    chart: DiscreteEllipticChart
    labels: list[MathTex]
    curve: WeierstrassCurve
    subgroups: list[Subgroup]
    point_at_infinity: PointAtInfinity

    def __init__(self, curve: WeierstrassCurve = Secp256k1_41):
        super().__init__(title="Subgroups")
        self.curve = curve
        self.labels = []

    def construct(self):
        self.chart = DiscreteEllipticChart(self.curve)
        self.chart.center()
        self.subgroups = Subgroup.generate_all(self.curve)
        self.point_at_infinity = PointAtInfinity(self.chart.ax, 9, 43)

    def animate_affine(self, scene: Scene, affine: ECAffine, label: str):
        self.animate_dot(scene, self.chart.find_dot_by_affine(affine), label)

    def animate_dot(self, scene: Scene, dot: Dot, label: str, run_time=1):
        scene.play(Flash(dot), run_time=run_time)
        dot.set_color(BLUE)
        scene.play(dot.animate.scale(1.5), run_time=run_time)
        self.labels.append(MathTex(label, font_size=20))
        self.labels[-1].next_to(dot, direction=RIGHT, buff=0.15)
        scene.play(Write(self.labels[-1]), run_time=run_time)

    def animate_subgroup(
        self, scene: Scene, subgroup: Subgroup, generator: ECAffine, run_time=1
    ):
        self.animate_affine(scene, generator, "G")
        for i in range(2, subgroup.order()):
            self.animate_affine(scene, generator * i, f"{i} \cdot G")
        self.point_at_infinity.animate_in(scene)
        self.animate_dot(scene, self.point_at_infinity.dot, "")
        gen_dot = self.chart.find_dot_by_affine(generator)
        scene.play(Flash(gen_dot), run_time=run_time)

    def animate_in(self, scene):
        scene.add(self.chart)
        subgroup = self.subgroups[0]
        self.animate_subgroup(scene, subgroup, subgroup.generator, run_time=1)
        scene.play(FadeOut(*self.labels))

    def animate_out(self, scene):
        scene.remove(self.chart)
