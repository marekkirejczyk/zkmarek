from manim import *

from .slide_base import NewSection, SlideBase


class TitleSlide(SlideBase):
    def __init__(self, title) -> None:
        SlideBase.__init__(self)
        self.title = Text(title)
        self.add(self.title)

    def animate_in(self):
        return [Write(self.title)]
