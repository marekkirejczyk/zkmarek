from manim import DOWN, UP, Code, FadeOut, Text, Write
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT

from zkmarek.video.slides.common.slide_base import SlideBase


class CodeSlide(SlideBase):
    title_text: Text
    title: str
    code: Code
    code_path: str
    kwargs: dict

    def __init__(self, title, code_path, **kwargs):
        super().__init__(title)
        self.code_path = code_path
        self.kwargs = kwargs
        self.title = title

    def construct(self):
        self.title_text = Text(self.title, font=PRIMARY_FONT, color=PRIMARY_COLOR)
        code_params = {
            "background_color": "window", 
            "line_no_buff": 0.2,
        }

        code_params.update(self.kwargs)

        self.code = Code(
            self.code_path,
            **code_params
        )
        self.title_text.to_edge(UP, buff=1)
        self.code.next_to(self.title_text, DOWN, buff=0.5)

    def __str__(self):
        return f"{self.title} (CODE)"

    def animate_in(self, scene):
        scene.play(Write(self.title_text))
        scene.play(Write(self.code))

    def animate_out(self, scene):
        scene.play(FadeOut(self.code))
        scene.play(FadeOut(self.title_text))
