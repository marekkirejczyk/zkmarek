from manim import Scene

from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.video.mobjects.discreet_elliptic_chart import \
    DiscreteEllipticChart
from zkmarek.video.slides.ec.animate_addition import AnimateAddition
from zkmarek.video.slides.slide_base import SlideBase


class Addition(SlideBase):
    chart: DiscreteEllipticChart

    def __init__(self, chart: DiscreteEllipticChart):
        super().__init__(title="Discrete elliptic curves - addition")
        self.chart = chart

    def animate_addition(self, scene: Scene, a1: ECAffine, a2: ECAffine):
        anim = AnimateAddition(self.chart)
        anim.animate_in(scene, a1, a2)
        anim.animate_out(scene)

    def animate_in(self, scene):
        start = self.chart.find_affine_by_x(5)[1]
        end = self.chart.find_affine_by_x(10)[0]
        self.animate_addition(scene, start, end)

    def animate_out(self, scene):
        pass
