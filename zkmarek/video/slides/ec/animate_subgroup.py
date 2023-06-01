from manim import BLUE, RIGHT, Dot, FadeOut, Flash, MathTex, Scene, Write

from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.crypto.subgroup import Subgroup
from zkmarek.video.mobjects.discreet_elliptic_chart import \
    DiscreteEllipticChart


class AnimateSubgroups:
    chart: DiscreteEllipticChart
    runtime_per_step: float
    labels: list[MathTex]
    duplicates: list[Dot]
    target_color: str

    def __init__(self, chart: DiscreteEllipticChart):
        self.chart = chart
        self.labels = []
        self.runtime_per_step = 1
        self.target_color = BLUE
        self.duplicates = []

    def animate_dot(self, scene: Scene, dot: Dot, label: str):
        dup_dot = dot.copy()
        scene.add(dup_dot)
        self.duplicates.append(dup_dot)
        dup_dot.set_color(self.target_color)
        scene.play(Flash(dup_dot), run_time=self.runtime_per_step)
        self.labels.append(MathTex(label, font_size=20))
        self.labels[-1].next_to(dup_dot, direction=RIGHT, buff=0.15)
        scene.play(Write(self.labels[-1]), run_time=self.runtime_per_step)

    def animate_subgroup(self, scene: Scene, subgroup: Subgroup, generator: ECAffine):
        self.animate_affine(scene, generator, "G")
        for i in range(2, subgroup.order()):
            self.animate_affine(scene, generator * i, f"{i} \cdot G")

        if self.chart.point_at_infinity is None:
            self.chart.create_point_at_infinity(9, 43)
            self.chart.point_at_infinity.animate_in(scene)
        self.animate_dot(scene, self.chart.point_at_infinity.dot, "")
        gen_dot = self.chart.find_dot_by_affine(generator)
        scene.play(Flash(gen_dot), run_time=self.runtime_per_step)

    def animate_out_labels(self, scene: Scene):
        scene.play(FadeOut(*self.labels))

    def animate_out_dots(self, scene: Scene):
        scene.play(FadeOut(*self.duplicates))
        scene.remove(*self.duplicates)


    def animate_affine(self, scene: Scene, affine: ECAffine, label: str):
        self.animate_dot(scene, self.chart.find_dot_by_affine(affine), label)
