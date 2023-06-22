from manim import DOWN, UP, Code, FadeIn, Tex, Text

from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.utils import load


class ECRecoverSlide(SlideBase):
    title_text: Text
    code: Code
    docs: Tex

    def __init__(self):
        super().__init__("ECRecover")

    def construct(self):
        self.title_text = Text("ECRecover")
        self.code = Code(
            file_name="data/eth/ecrecover.sol",
            tab_width=2,
            background="rectangle",
            language="Solidity",
            font="Monospace",
            font_size=18,
            margin=0.2,
            line_no_buff=0.2,
            insert_line_no=False
        )
        self.docs = Tex(
            load("data/eth/ecrecover.tex"),
            font_size=32)
        self.title_text.to_edge(UP)
        self.code.next_to(self.title_text, DOWN, buff=0.5)
        self.docs.next_to(self.code, DOWN, buff=0.5)

    def animate_in(self, scene):
        scene.play(FadeIn(self.title_text))
        scene.play(FadeIn(self.code))
        scene.play(FadeIn(self.docs))
