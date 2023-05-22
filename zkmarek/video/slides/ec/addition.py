from manim import Dot, Line

from zkmarek.video.mobjects.discreet_elliptic_chart import \
    DiscreteEllipticChart
from zkmarek.video.slides.slide_base import SlideBase


class Addition(SlideBase):
    line: Line
    chart: DiscreteEllipticChart
    start: Dot
    end: Dot
    result: Dot

    def __init__(self, chart: DiscreteEllipticChart):
        super().__init__(title="Discrete elliptic curves - addition")
        self.chart = chart
        start = self.chart.find_dots_by_x(5)[1].to_coords(self.chart.ax)
        end = self.chart.find_dots_by_x(10)[0].to_coords(self.chart.ax)
        self.line = Line(start, end)

    def animate_in(self, scene):
        self.chart.animate_add(scene, self.line)
        scene.play(self.line.animate.scale(3))

    def animate_out(self, scene):
        self.chart.animate_remove(scene,  self.line)
