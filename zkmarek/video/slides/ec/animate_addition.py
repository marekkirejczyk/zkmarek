from manim import (DARK_GREY, RIGHT, Dot, FadeIn, FadeOut, GrowFromPoint, Line,
                   Scene, Tex)

from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.crypto.float_math import find_x_min_max
from zkmarek.video.mobjects.discreet_elliptic_chart import \
    DiscreteEllipticChart


class AnimateAddition:
    chart: DiscreteEllipticChart
    start: Dot
    end: Dot
    result: Dot
    line1: Line
    line2: Line
    labels: list[Tex]

    def __init__(self, chart: DiscreteEllipticChart) -> None:
        self.chart = chart
        self.labels = [
            Tex(c, font_size=24) for i, c in enumerate(["A", "B", "-(A+B)", "A+B"])
        ]

    def animate_in(self, scene: Scene, c0: ECAffine, c1: ECAffine):
        c = [c0, c1, -(c0 + c1), c0 + c1]
        p = list(map(lambda i: self.chart.affine_to_point(c[i]), range(4)))
        for i in range(4):
            self.labels[i].next_to(self.chart.find_dot_by_affine(c[i]), RIGHT)

        (s, e) = find_x_min_max([p[0], p[1], p[2]])
        self.line1 = Line(s, e, color=DARK_GREY)
        self.line2 = Line(e, p[3], color=DARK_GREY)
        scene.play(FadeIn(self.labels[0]))
        scene.play(FadeIn(self.labels[1]))
        scene.play(GrowFromPoint(self.line1, point=s, run_time=5))
        scene.play(FadeIn(self.labels[2]))
        scene.play(GrowFromPoint(self.line2, point=e, run_time=5))
        scene.play(FadeIn(self.labels[3]))

    def animate_out(self, scene):
        scene.play(FadeOut(self.line1, self.line2, *self.labels))
