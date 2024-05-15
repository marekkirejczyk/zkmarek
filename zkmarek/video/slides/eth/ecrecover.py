from manim import (
    DOWN,
    UP,
    Code,
    FadeIn,
    FadeOut,
    Indicate,
    ReplacementTransform,
    Tex,
    Text,
)

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT
from zkmarek.video.mobjects.equation_box import EquationBoxWithIcons
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.utils import find_in_code, load


class ECRecoverSlide(SlideBase):
    title_text: Text
    code: Code
    docs: Tex
    signature: EquationBoxWithIcons
    signature2: EquationBoxWithIcons

    def __init__(self):
        super().__init__("ECRecover")

    def construct(self):
        self.title_text = Text("ECRecover", color=PRIMARY_COLOR, font=PRIMARY_FONT)
        self.code = Code(
            file_name="data/eth/ecrecover.sol",
            tab_width=2,
            background="rectangle",
            language="Solidity",
            font="Monospace",
            font_size=18,
            margin=0.2,
            line_no_buff=0.2,
            insert_line_no=False,
        )
        self.docs = Tex(
            load("data/eth/ecrecover.tex"), tex_environment=None, font_size=32
        )
        self.title_text.to_edge(UP)
        self.code.next_to(self.title_text, DOWN, buff=0.5)
        self.docs.next_to(self.code, DOWN, buff=0.5)

        self.signature = EquationBoxWithIcons.create(
            "⎘",
            "r = R_x \mod n",
            PRIMARY_COLOR,
            "⎘",
            "s = (msg + r \cdot K_{Priv}) \cdot secret^{-1} \mod n",
            PRIMARY_COLOR,
        ).next_to(self.docs, DOWN, buff=1)

        self.signature2 = EquationBoxWithIcons.create(
            "⎘",
            "r = R_x \mod n",
            PRIMARY_COLOR,
            "⎘",
            "s = (msg + r \cdot K_{Priv}) \cdot secret^{-1} \mod n",
            PRIMARY_COLOR,
            "⎘",
            "v = ?",
            PRIMARY_COLOR,
        ).next_to(self.docs, DOWN, buff=1)

    def animate_in(self, scene):
        self.new_subsection(
            scene, "ECRecover", sound="data/sound/episode2/slide9-0.mp3"
        )

        scene.play(FadeIn(self.title_text))
        scene.play(FadeIn(self.code))
        scene.play(FadeIn(self.docs))
        fragments = [
            "bytes32 s",
            "bytes32 r",
            "uint8 v",
        ]

        scene.wait(1.5)

        for fragment in fragments:
            chars = find_in_code(self.code, fragment)
            scene.play(Indicate(*chars), run_time=0.5)

        scene.wait(1)
        scene.play(FadeIn(self.signature))
        scene.wait(1)
        scene.play(ReplacementTransform(self.signature, self.signature2))

    def animate_out(self, scene):
        scene.play(FadeOut(self), run_time=0.5)
        self.wait_for_sound(scene)
