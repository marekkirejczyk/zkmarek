from manim import DOWN, UP, Code, Text, Write

from zkmarek.video.slides.slide_base import SlideBase


class CodeSlide(SlideBase):
    title: Text
    code: Code

    def __init__(self, title, code_path):
        super().__init__(title)
        self.title = Text(title)
        self.code = Code(code_path)
        self.title.to_edge(UP, buff=1)
        self.code.next_to(self.title, DOWN, buff=1)

    def animate_in(self, scene):
        scene.play(Write(self.title))
        scene.play(Write(self.code))

