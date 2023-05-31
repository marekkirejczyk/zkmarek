from manim import FadeOut, Text, Write

from .slide_base import SlideBase


class TitleSlide(SlideBase):
    title_text: Text

    def __init__(self, title) -> None:
        super().__init__(title)

    def __str__(self):
        return f"{self.title} (TITLE)"

    def construct(self):
        self.title_text = Text(self.title_str)
        self.add(self.title_text)

    def animate_in(self, scene):
        scene.play(Write(self.title_text))

    def animate_out(self, scene):
        scene.play(FadeOut(self.title_text))
