from manim import Text, Write, FadeOut

from .slide_base import  SlideBase


class TitleSlide(SlideBase):
    title_text: Text
    def __init__(self, title) -> None:
        super().__init__(title=f"{title} (TITLE)")
        self.title_text = Text(title)
        self.add(self.title_text)

    def animate_in(self, scene):
        scene.play(Write(self.title_text))

    def animate_out(self, scene):
        scene.play(FadeOut(self.title_text))
