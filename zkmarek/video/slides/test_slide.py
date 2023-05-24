from manim import Tex
from utils import load
from zkmarek.video.slides.slide_base import SlideBase

class TestSlide(SlideBase):
    def __init__(self):
        super().__init__("Test slide")

    def animate_in(self, scene):
        tex_path = "data/cec/add_double.tex"
        self.add(Tex(load(tex_path), font_size=32))


