from zkmarek.video.mobjects.clock import Clock

from .common.slide_base import SlideBase

class PrimeFields(SlideBase):
    clock: Clock

    def __init__(self):
        super().__init__(title="Prime Fields")

    def construct(self):
        self.clock = Clock()

    def animate_in(self, scene):
        self.clock.animate_in(scene)
