from manim import *

from .slide_base import SlideBase

class DiscreetEllipticChart(VGroup):
    secp256k1 = lambda x, y: y**2 - x**3 - 7

    def __init__(self, prime=13, equation=secp256k1):
        VGroup.__init__(self)
        self.equation = equation
        self.ax = Axes(
            x_range=[0, prime+1, 1],
            y_range=[0, prime+1, 1],
            x_length=7,
            axis_config={"include_numbers": True},
        )
        self.add(self.ax)




    def animate_appear(self):
        return Succession(Create(self.ax))

    def animate_disappear(self):
        return Succession(FadeOut(self.ax))

class DiscreetSecp256k1(SlideBase):
    def __init__(self, prime=13):
        self.chart = DiscreetEllipticChart(prime=13)

    def animate_in(self, scene):
        scene.play(self.chart.animate_appear())

    def animate_out(self, scene):
        scene.play(self.chart.animate_disappear())
