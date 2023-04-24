from manim import *

from .slide_base import SlideBase
from mobjects.discreet_elliptic_chart import DiscreetEllipticChart

class DiscreetSecp256k1(SlideBase):
    def __init__(self):
        self.chart = DiscreetEllipticChart()

    def animate_in(self, scene):
        scene.play(self.chart.animate_appear())

    def animate_out(self, scene):
        scene.play(self.chart.animate_disappear())
