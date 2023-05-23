from manim import RED, RIGHT, Dot, Indicate, Line, Tex

from zkmarek.video.mobjects.discreet_elliptic_chart import DiscreteEllipticChart
from zkmarek.video.slides.slide_base import SlideBase


class Negation(SlideBase):
    chart: DiscreteEllipticChart
    label1: Tex
    label2: Tex
    dots: list[Dot]
    h_line: Line
    v_line: Line

    def __init__(self, chart: DiscreteEllipticChart) -> None:
        super().__init__("Negation")
        self.chart = chart
        self.label1 = Tex("A", font_size=28)
        self.label2 = Tex("-A", font_size=28)
        self.dots = self.chart.find_dots_by_x(9)

    def indicate_dot(self, scene, dot, label):
        scene.play(Indicate(dot, scale_factor=2))
        dot.set_color(RED)
        label.next_to(dot, RIGHT)
        self.chart.add(dot)
        self.chart.animate_add(scene, label)

    def animate_in(self, scene):
        self.v_line = self.chart.create_vertical_line(9)
        self.chart.animate_add(scene, self.v_line)
        self.indicate_dot(scene, self.dots[0], self.label1)

        self.h_line = self.chart.create_horizontal_line()
        self.chart.animate_add(scene, self.h_line)
        self.indicate_dot(scene, self.dots[1], self.label2)

    def animate_out(self, scene):
        self.chart.animate_remove(
            scene,
            self.v_line,
            self.h_line,
            self.label1,
            self.label2,
            self.dots[0],
            self.dots[1],
        )
