from manim import DOWN, UP, Code, FadeIn, Tex, Text, Indicate

from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.utils import find_in_code, load


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
            tex_environment=None,
            font_size=32)
        self.title_text.to_edge(UP)
        self.code.next_to(self.title_text, DOWN, buff=0.5)
        self.docs.next_to(self.code, DOWN, buff=0.5)

    def animate_in(self, scene):
        self.play_sound(scene, "data/sound/teaser/s6.wav")
        scene.play(FadeIn(self.title_text))
        scene.play(FadeIn(self.code))
        scene.play(FadeIn(self.docs))
        fragments = ["bytes32 r", "bytes32 s", "uint8 v", ]

        for fragment in fragments:
            chars = find_in_code(self.code, fragment)
            scene.play(Indicate(*chars))

        scene.wait(3)

        for i in range(1, 8, 2):
            scene.play(Indicate(self.docs[i]), run_time=0.5)
        self.play_sound(scene, "data/sound/teaser/s7.wav")
