from manim import FadeIn, Indicate, FadeOut

from zkmarek.video.constant import SECONDARY_COLOR
from zkmarek.video.slides.common.code_slide import CodeSlide
from zkmarek.video.utils import find_in_code


class EthereumTransaction(CodeSlide):
    def __init__(self):
        super().__init__(
            "Ethereum Transaction", "data/eth/transaction.py", language="python"
        )

    def animate_in(self, scene):

        scene.play(FadeIn(self.title_text), FadeIn(self.code), run_time=0.7)
        self.new_subsection(
            scene, "Ethereum Transaction", sound="data/sound/teaser2/slide1-2.mp3"
        )
        fragments1 = [
            '"from"',
            '"to"',
            '"value"',
            '"nonce"',
            '"chainId"',
            '"hash"',
            "...",
        ]
        scene.wait(1.5)
        indications = []
        for fragment in fragments1:
            chars = find_in_code(self.code, fragment)
            indications.append(Indicate(*chars, color=SECONDARY_COLOR))

        scene.play(*indications)

        scene.wait(2)
        fragments2 = [
            '"s": "0x4a94e0265f31fd90dc414433d5acdaf28d3ebf0a7657841c4edc7564808b078b"',
            '"r": "0xa99c1ac8787f592251ae67055afaeab9ade2e36eea47a2db213aa5f76f00ba49"',
            '"v": "0x0"',
        ]

        for fragment in fragments2:
            chars = find_in_code(self.code, fragment)
            scene.play(Indicate(*chars, color=SECONDARY_COLOR, run_time=0.4))

        scene.wait(4.5)

        fragments3 = [" 0", " 1", " 27", " 28"]
        for fragment in fragments3:
            chars = find_in_code(self.code, fragment)
            scene.play(Indicate(*chars, color=SECONDARY_COLOR, run_time=0.7))

    def animate_out(self, scene):
        scene.play(FadeOut(self.code), FadeOut(self.title_text))
