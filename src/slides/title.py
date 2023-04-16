from manim import *

from .slide_base import NewSection, SlideBase


class TitleSlide(SlideBase):
    def __init__(self, title) -> None:
        SlideBase.__init__(self, title=title)
        self.title_label = Text(title)
        self.add(self.title_label)

    def animate_in(self):
        return [Write(self.title_label)]
