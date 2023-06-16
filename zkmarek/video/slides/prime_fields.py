from manim import LEFT, Transform
from zkmarek.video.mobjects.clock import Clock
from zkmarek.video.mobjects.sidebar import Sidebar

from .common.slide_base import SlideBase

class PrimeFields(SlideBase):
    clock: Clock
    sidebar: Sidebar

    def __init__(self):
        super().__init__(title="Prime Fields")

    def construct(self):
        self.clock = Clock()
        self.clock2 = Clock(use_zero=False)
        self.clock3 = Clock(use_zero=False, modulus=41)
        self.sidebar = Sidebar("Prime Field", code_path="data/pf/field.py")

    def animate_in(self, scene):
        self.clock.animate_in(scene)
        scene.play(Transform(self.clock, self.clock2))
        scene.remove(self.clock)
        scene.play(Transform(self.clock2, self.clock3))
        scene.remove(self.clock2)
        scene.play(self.clock3.animate.align_on_border(LEFT, buff=0.2))
        self.sidebar.animate_in(scene)
