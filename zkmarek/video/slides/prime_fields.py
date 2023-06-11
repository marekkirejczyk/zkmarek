from manim import LEFT
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
        self.sidebar = Sidebar("Prime Field", code_path="data/pf/field.py")

    def animate_in(self, scene):
        self.clock.animate_in(scene)
        scene.play(self.clock.animate.align_on_border(LEFT, buff=0.2))
        self.sidebar.animate_in(scene)
