from manim import Text, Write, FadeOut

from .slide_base import  SlideBase


class TitleSlide(SlideBase):
    def __init__(self, title) -> None:
        super().__init__(title=title)
        self.title_label = Text(title)
        self.add(self.title_label)

    def animate_in(self, scene):
        scene.play(Write(self.title_label))

    def animate_out(self, scene):
        scene.play(FadeOut(self.title_label))
