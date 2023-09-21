from manim import RIGHT, Dot, FadeOut, Indicate, MathTex, Scene, Write, Circle, \
    Circumscribe

from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.crypto.subgroup import Subgroup
from zkmarek.video.constant import HIGHLIGHT_COLOR
from zkmarek.video.mobjects.discreet_elliptic_chart import \
    DiscreteEllipticChart


class AnimateSubgroups:
    chart: DiscreteEllipticChart
    runtime_per_step: float
    labels: list[MathTex]
    duplicates: list[Dot]
    target_color: str

    def __init__(self, chart: DiscreteEllipticChart, target_color=HIGHLIGHT_COLOR,
        runtime_per_step=0.75):
        self.chart = chart
        self.labels = []
        self.runtime_per_step = runtime_per_step
        self.target_color = target_color
        self.duplicates = []

    def animate_affine(self, scene: Scene, affine: ECAffine, label: str,
        split_animation=False):
        self.animate_dot(scene, self.chart.find_dot_by_affine(affine),
            label, split_animation=split_animation)

    def animate_dot(self, scene: Scene, dot: Dot, label: str, split_animation=False):
        dup_dot = dot.copy()
        scene.add(dup_dot)
        self.duplicates.append(dup_dot)
        dup_dot.set_color(self.target_color)
        self.labels.append(MathTex(label, font_size=20, color=self.target_color))
        self.labels[-1].next_to(dup_dot, direction=RIGHT, buff=0.15)
        if split_animation:
            scene.play(Indicate(dup_dot))
            scene.wait(1)
            scene.play(Write(self.labels[-1]), run_time=self.runtime_per_step)
        else:
            scene.play(Indicate(dup_dot), Write(self.labels[-1]),
                run_time=self.runtime_per_step)

    def animate_subgroup(self, scene: Scene, subgroup: Subgroup, generator: ECAffine):
        self.animate_generator(scene, generator)
        self.animate_subgroup_end(scene, subgroup, generator)

    def animate_generator(self, scene, generator, split_animation=False):
        self.animate_affine(scene, generator, "G", split_animation=split_animation)

    def animate_subgroup_mid(self, scene: Scene, subgroup: Subgroup,
        generator: ECAffine, start=2, end=None):
        end = subgroup.order() if end is None else end
        for i in range(start, end):
            self.animate_affine(scene, generator * i, f"{i} \cdot G")

    def animate_subgroup_end(self, scene: Scene, subgroup: Subgroup,
        generator: ECAffine, start=2, end=None):
        self.animate_subgroup_mid(scene, subgroup, generator, start, end)

        if self.chart.point_at_infinity is None:
            self.chart.create_point_at_infinity(9, 43, "", dot_color=self.target_color)

        infinity_label = f"{subgroup.order()} \cdot G = \mathcal{{O}}"
        scene.play(Circumscribe(self.chart.point_at_infinity.dot, Circle))
        self.animate_dot(scene, self.chart.point_at_infinity.dot, infinity_label)

        gen_dot = self.chart.find_dot_by_affine(generator)
        scene.wait(1)
        scene.play(Circumscribe(gen_dot, Circle))
        scene.play(Indicate(gen_dot), Indicate(self.labels[0]))

    def animate_out_labels(self, scene: Scene):
        scene.play(FadeOut(*self.labels))

    def animate_out_dots(self, scene: Scene):
        scene.play(FadeOut(*self.duplicates))
        scene.remove(*self.duplicates)

