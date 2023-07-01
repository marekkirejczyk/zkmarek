from manim import Indicate
from zkmarek.video.constant import SECONDARY_COLOR
from zkmarek.video.slides.common.code_slide import CodeSlide
from zkmarek.video.utils import find_in_code


class EthereumTransaction(CodeSlide):
    def __init__(self):
        super().__init__(
            "Ethereum Transaction",
            "data/eth/transaction.py",
            language="python")

    def animate_in(self, scene):
        super().animate_in(scene)
        fragments = [
            '"from"',
            '"to"',
            '"value"',
            '"nonce"',
            '"chainId"',
            '"hash"',
            '...',
            '"r": "0xa99c1ac8787f592251ae67055afaeab9ade2e36eea47a2db213aa5f76f00ba49"',
            '"s": "0x4a94e0265f31fd90dc414433d5acdaf28d3ebf0a7657841c4edc7564808b078b"',
            '"v": "0x0"'
        ]

        for fragment in fragments:
            chars = find_in_code(self.code, fragment)
            scene.play(Indicate(*chars, color=SECONDARY_COLOR))

