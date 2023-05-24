from typing import Optional, Sequence
from manim import (DARK_GREY, RIGHT, Dot, FadeIn, FadeOut, GrowFromPoint, Line,
                   Scene, Tex, line_intersection)

from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.crypto.line import line_through_collinear, is_collinear, lines_through_affine
from zkmarek.video.mobjects.discreet_elliptic_chart import \
    DiscreteEllipticChart



class AnimateAddition:
    chart: DiscreteEllipticChart
    start: Dot
    end: Dot
    result: Dot
    lines: list[Line] = []
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

        (s, e) = line_through_collinear([p[0], p[1], p[2]])

        scene.play(FadeIn(self.labels[0]))
        scene.play(FadeIn(self.labels[1]))
        lines = lines_through_affine(c[0], c[1], c[2])
        for l in lines:
            [s, e] = self.chart.ax.c2p(l)
            line = Line(s, e, color=DARK_GREY)
            self.lines.append(line)
            scene.play(GrowFromPoint(line, point=s, run_time=5))

        scene.play(FadeIn(self.labels[2]))
        self.line2 = Line(p[2], p[3], color=DARK_GREY)
        scene.play(GrowFromPoint(self.line2, point=p[2], run_time=5))
        scene.play(FadeIn(self.labels[3]))

    def animate_out(self, scene):
        scene.play(FadeOut(self.line2, *self.lines, *self.labels))
