from manim import DOWN, UP, Code, FadeOut, Text, Write

from zkmarek.video.slides.common.slide_base import SlideBase


class CodeSlide(SlideBase):
    title_text: Text
    code: Code

    def __init__(self, title, code_path, **kwargs):
        super().__init__(f"{title} (CODE)")
        self.title_text = Text(title)
        self.code = Code(
            code_path,
            background="rectangle",
            insert_line_no=True,
            font="Monospace",
            font_size=14,
            margin=0.2,
            style="fruity",
            line_no_buff=0.2,
            **kwargs
        )
        self.title_text.to_edge(UP, buff=1)
        self.code.next_to(self.title_text, DOWN, buff=1)

    def animate_in(self, scene):
        scene.play(Write(self.title_text))
        scene.play(Write(self.code))

    def animate_out(self, scene):
        scene.play(FadeOut(self.code))
        scene.play(FadeOut(self.title_text))
