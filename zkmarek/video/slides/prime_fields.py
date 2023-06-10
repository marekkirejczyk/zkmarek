import numpy as np
from manim import GREEN, ORIGIN, DOWN, Circle, Create, Line, VGroup, Text, UP, IN

from .common.slide_base import SlideBase

class Clock(VGroup):
    circle: Circle
    markings: VGroup
    use_zero: bool
    modulus: int

    def __init__(self, use_zero=True, modulus=12):
        self.circle = Circle(radius=3)
        self.use_zero = use_zero
        self.modulus = modulus

    def label_at(self, index):
        if self.use_zero and index == 0:
            return str(self.modulus)
        return str(index % 12)

    def create_markings(self, n):
        result = VGroup()
        for i in range(n):
            angle = i * 360 / n
            line = Line(2.8 * UP, 3 * UP, color=GREEN)
            number = Text(self.label_at(i)).scale(0.5)
            number.next_to(line.get_center(), direction=DOWN, buff=0.5)
            line.rotate(-np.deg2rad(angle), about_point=ORIGIN)
            number.rotate(-np.deg2rad(angle), about_point=ORIGIN)
            result.add(line)
            result.add(number)
        return result

    def animate_in(self, scene):
        scene.play(Create(self.circle))
        self.markings = self.create_markings(12)
        scene.play(Create(self.markings))

class PrimeFields(SlideBase):
    clock: Clock

    def __init__(self):
        super().__init__(title="Prime Fields")

    def construct(self):
        self.clock = Clock()

    def animate_in(self, scene):
        self.clock.animate_in(scene)
