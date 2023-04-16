from manim import *
from manim_editor import PresentationSectionType


class NewSection():
    def __init__(self, title, type=PresentationSectionType.NORMAL):
        self.title = title
        self.type = type

class SlideBase(VGroup):
    def __init__(self) -> None:
        VGroup.__init__(self)

    def animate_in(self):
        return []

    def animate_out(self):
        return [FadeOut(self)]
