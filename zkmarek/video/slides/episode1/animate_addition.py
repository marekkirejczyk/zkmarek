from manim import RIGHT, Dot, FadeIn, FadeOut, GrowFromPoint, Line, Scene, Tex

from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.crypto.line import line_through_collinear, lines_through_affine
from zkmarek.video.constant import PRIMARY_COLOR
from zkmarek.video.mobjects.discreet_elliptic_chart import \
    DiscreteEllipticChart


class AnimateAddition:
    chart: DiscreteEllipticChart
    start: Dot
    end: Dot
    result: Dot
    lines: list[Line]
    line2: Line
    labels: list[Tex]

    def __init__(self, chart: DiscreteEllipticChart) -> None:
        self.chart = chart
        self.lines = []
        self.labels = [
            Tex(c, font_size=24, color=PRIMARY_COLOR)
                for i, c in enumerate(["A", "B", "-(A+B)", "A+B"])
        ]

    def animate_in(self, scene: Scene, c0: ECAffine, c1: ECAffine,
        wait_time_between = 1):
        c = [c0, c1, -(c0 + c1), c0 + c1]

        p = list(map(lambda i: self.chart.affine_to_point(c[i]), range(4)))
        for i in range(4):
            dot = self.chart.find_dot_by_affine(c[i])
            self.labels[i].next_to(dot, RIGHT)

        (s, e) = line_through_collinear([p[0], p[1], p[2]])

        scene.play(FadeIn(self.labels[0]))
        scene.play(FadeIn(self.labels[1]))
        lines = lines_through_affine(c[0], c[1], c[2])
        for line_coords in lines:
            [s, e] = self.chart.ax.c2p(line_coords)
            line = Line(s, e, color=PRIMARY_COLOR)
            self.lines.append(line)
            scene.play(GrowFromPoint(line, point=s, run_time=2))

        scene.wait(wait_time_between)
        scene.play(FadeIn(self.labels[2]))
        self.line2 = Line(p[2], p[3], color=PRIMARY_COLOR)
        scene.play(GrowFromPoint(self.line2, point=p[2], run_time=5))
        scene.play(FadeIn(self.labels[3]))
        self.chart.add(*self.lines)
        self.chart.add(self.line2)
        self.chart.add(*self.labels)

    def animate_out(self, scene):
        scene.play(FadeOut(*self.labels))
        scene.play(FadeOut(self.line2), FadeOut(*self.lines))
        self.chart.remove(*self.lines)
        self.chart.remove(self.line2)
        self.chart.remove(*self.labels)

    @staticmethod
    def play(
        scene: Scene,
        chart: DiscreteEllipticChart,
        a1_x: int,
        a1_odd: int,
        a2_x: int,
        a2_odd: int,
        animate_out: bool = True,
        wait_time_between=0,
    ):
        a1 = chart.find_affine_by_x(a1_x, a1_odd)
        a2 = chart.find_affine_by_x(a2_x, a2_odd)
        anim = AnimateAddition(chart)
        anim.animate_in(scene, a1, a2, wait_time_between=wait_time_between)
        if animate_out:
            anim.animate_out(scene)
        return anim
