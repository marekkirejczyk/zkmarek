from manim import Create, Rectangle

from zkmarek.video.constant import PRIMARY_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase


class Commitment(SlideBase):

    def __init__(self):
        super().__init__("Commitment")

    def construct(self):
        self.rectangle = Rectangle(height=3, width=5, color = PRIMARY_COLOR)
        
    def animate_in(self, scene):
        self.new_subsection(scene, "envelope", "data/sound/e4/slide2-1.mp3")
        scene.play(Create(self.rectangle))

        self.new_subsection(scene, "another party", "data/sound/e4/slide2-3.mp3")
