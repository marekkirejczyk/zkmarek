from manim import RIGHT, Axes, Create, Dot, MathTex, VGroup, Write

from zkmarek.video.slides.common.slide_base import SlideBase


class TrustedSetup(SlideBase):
    label: MathTex
    def __init__(self):
        super().__init__("Trusted setup")

    def construct(self):
        self.label = MathTex(r"\tau")

    def animate_in(self, scene):
        scene.play(Write(self.label))
