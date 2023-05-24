from manim import Scene

from zkmarek.video.mobjects.discreet_elliptic_chart import DiscreteEllipticChart
from zkmarek.video.slides.ec.animate_addition import AnimateAddition
from zkmarek.video.slides.slide_base import SlideBase


class Addition(SlideBase):
    chart: DiscreteEllipticChart

    def __init__(self, chart: DiscreteEllipticChart):
        super().__init__(title="Discrete elliptic curves - addition")
        self.chart = chart

    def animate_addition(
        self, scene: Scene, a1_x: int, a1_odd: int, a2_x: int, a2_odd: int
    ):
        a1 = self.chart.find_affine_by_x(a1_x, a1_odd)
        a2 = self.chart.find_affine_by_x(a2_x, a2_odd)
        anim = AnimateAddition(self.chart)
        anim.animate_in(scene, a1, a2)
        anim.animate_out(scene)

    def animate_in(self, scene):
        self.animate_addition(scene, 5, 1, 10, 0)
        self.animate_addition(scene, 5, 1, 9, 1)

    def animate_out(self, scene):
        pass

    @staticmethod
    def play(scene: Scene, chart: DiscreteEllipticChart):
        instance = Addition(chart)
        instance.animate_in(scene)
        instance.animate_out(scene)
