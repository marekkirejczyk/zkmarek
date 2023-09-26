from manim import (DOWN, LEFT, UP, Code, FadeIn, FadeOut, Indicate, Rectangle,
                   Succession, Tex, Text)

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.utils import find_in_code, load


class ECRecoverSlideTeaser(SlideBase):
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
            tex_environment=None,
            font_size=32)
        self.title_text.to_edge(UP)
        self.code.next_to(self.title_text, DOWN, buff=0.5)
        self.docs.next_to(self.code, DOWN, buff=0.5)

    def animate_in(self, scene):
        self.play_sound(scene, "data/sound/teaser/s5.wav")
        scene.play(FadeIn(self.title_text))
        scene.play(FadeIn(self.code))
        scene.play(FadeIn(self.docs))
        fragments = ["bytes32 s", "bytes32 r", "uint8 v", ]

        scene.wait(3)

        for fragment in fragments:
            chars = find_in_code(self.code, fragment)
            scene.play(Indicate(*chars), run_time=0.5)

    def animate_miniature(self, scene):
        rectangle = Rectangle(color=PRIMARY_COLOR, width=15, height=8)
        text = Text("Learning motivation", color=SECONDARY_COLOR,
            font=PRIMARY_FONT, font_size=70).scale(0.4)
        self.add(rectangle, self.title_text, self.code, self.docs)
        self.scale(0.4)
        self.move_to(LEFT * 3.4)
        text.next_to(rectangle, DOWN, buff=0.4)
        scene.play(FadeIn(self.title_text), FadeIn(rectangle), FadeIn(text),
            FadeIn(self.code), FadeIn(self.docs))
        self.add(text)

    def animate_out(self, scene):
        scene.play(FadeOut(self), run_time=0.5)
        self.wait_for_sound(scene)
