from manim import (
    DOWN,
    RIGHT,
    FadeIn,
    Indicate,
    VGroup,
)

from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR
from zkmarek.video.mobjects.equation_box import EquationBox, EquationBoxWithIcons
from zkmarek.video.slides.common.code_slide import CodeSlide
from zkmarek.video.utils import find_in_code


class EthereumTransaction(CodeSlide):
    def __init__(self):
        super().__init__(
            "Ethereum Transaction", "data/eth/transaction.py", language="python"
        )

    def animate_in(self, scene):
        self.new_subsection(
            scene, "Ethereum Transaction", sound="data/sound/teaser2/slide1-1.mp3"
        )

        super().animate_in(scene)

        fragments1 = [
            '"from"',
            '"to"',
            '"value"',
            '"nonce"',
            '"chainId"',
            '"hash"',
            "...",
        ]

        indications = []
        for fragment in fragments1:
            chars = find_in_code(self.code, fragment)
            indications.append(Indicate(*chars, color=SECONDARY_COLOR))

        scene.play(*indications)

        scene.wait(4)

        fragments2 = [
            '"s": "0x4a94e0265f31fd90dc414433d5acdaf28d3ebf0a7657841c4edc7564808b078b"',
            '"r": "0xa99c1ac8787f592251ae67055afaeab9ade2e36eea47a2db213aa5f76f00ba49"',
            '"v": "0x0"',
        ]

        for fragment in fragments2:
            chars = find_in_code(self.code, fragment)
            scene.play(Indicate(*chars, color=SECONDARY_COLOR, run_time=0.4))

        scene.wait(4.5)
        self.new_subsection(scene, "rsv values", "data/sound/teaser2/slide1-2.mp3")
        fragments3 = [" 0", " 1", " 27", " 28"]
        for fragment in fragments3:
            chars = find_in_code(self.code, fragment)
            scene.play(Indicate(*chars, color=SECONDARY_COLOR, run_time=0.5))

        self.signature = EquationBoxWithIcons.create(
            "⎘",
            "r = R_x \mod n",
            PRIMARY_COLOR,
            "⎘",
            "s = (msg + r \cdot K_{Priv}) \cdot secret^{-1} \mod n",
            PRIMARY_COLOR,
        )
        scene.wait(2)
        self.signature.arrange(RIGHT, buff=1).next_to(self.code, DOWN, buff=0.5)

        scene.play(FadeIn(self.signature))
        scene.play(Indicate(self.signature[1], color=SECONDARY_COLOR))

    def animate_out(self, scene):
        pass
