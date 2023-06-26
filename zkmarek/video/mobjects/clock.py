
import numpy as np
from manim import GREEN, ORIGIN, DOWN, Circle, Create, Line, VGroup, Text, UP
from typing import Optional


class Clock(VGroup):
    circle: Circle
    markings: VGroup
    use_zero: bool
    modulus: int
    radius: float
    hour: Optional[float]
    hour_hand: Optional[Line] = None

    def __init__(self, use_zero=False, modulus=12, hour = None):
        super().__init__()
        self.use_zero = use_zero
        self.modulus = modulus
        self.circle = Circle(radius=3)
        self.hour = hour
        self.markings = self.create_markings(modulus)
        if hour is not None:
            self.hour_hand = self.create_hand(hour)
            self.add(self.hour_hand)
        self.add(self.circle)
        self.add(self.markings)


    def label_at(self, index):
        if index == 0 and not self.use_zero:
            return str(self.modulus)
        return str(index % self.modulus)

    def create_hand(self, hour, length=2):
        angle = hour * 360 / self.modulus
        line = Line(ORIGIN, length*UP, z_index=2)
        line.rotate(-np.deg2rad(angle), about_point=ORIGIN)
        return line


    def create_markings(self, n):
        result = VGroup()
        for i in range(n):
            angle = i * 360 / n
            line = Line(2.8 * UP, 3 * UP, color=GREEN)
            number = Text(self.label_at(i)).scale(0.4)
            number.next_to(line.get_center(), direction=DOWN, buff=0.5)
            line.rotate(-np.deg2rad(angle), about_point=ORIGIN)
            number.rotate(-np.deg2rad(angle), about_point=ORIGIN)
            result.add(line)
            result.add(number)
        return result

    def animate_in(self, scene):
        scene.play(Create(self.circle))
        scene.play(Create(self.markings))
        if self.hour_hand:
            scene.play(Create(self.hour_hand))
