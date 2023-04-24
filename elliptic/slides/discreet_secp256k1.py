from manim import *

from .slide_base import SlideBase
from crypto.field import Field

def secp256k1(x, y):
    return y**2 - x**3 - 7

class DiscreetEllipticChart(VGroup):
    def __init__(self, prime=19, equation=secp256k1):
        VGroup.__init__(self)
        self.equation = equation
        self.prime = prime

        self.ax = Axes(
            x_range=[0, prime+1, 1],
            y_range=[0, prime+1, 1],
            x_length=7,
            axis_config={"include_numbers": True},
        )
        self.add(self.ax)
        self.gen_points()


    def gen_points(self):
        for (x, y) in [(x, y) for x in range(0, self.prime+1) for y in range(0, self.prime+1)]:
            if self.equation(Field(x, self.prime), Field(y, self.prime)) == Field(0, self.prime):
                self.add(Dot(self.ax.c2p(x, y), color=YELLOW))


    def animate_appear(self):
        return Create(self)

    def animate_disappear(self):
        return FadeOut(self.ax)

class DiscreetSecp256k1(SlideBase):
    def __init__(self):
        self.chart = DiscreetEllipticChart()

    def animate_in(self, scene):
        scene.play(self.chart.animate_appear())

    def animate_out(self, scene):
        scene.play(self.chart.animate_disappear())
