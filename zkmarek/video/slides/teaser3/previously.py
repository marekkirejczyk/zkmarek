from manim import FadeIn, Text, UP, DOWN, LEFT, RIGHT, Indicate, ReplacementTransform

from zkmarek.video.constant import (
    PRIMARY_COLOR,
    PRIMARY_FONT,
    SECONDARY_COLOR,
    HIGHLIGHT_COLOR,
)
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.mobjects.equation_box import EquationBoxWithIcons


class Episode2Reference(SlideBase):

    def __init__(self):
        super().__init__("Signature algorithm reference")

    def construct(self):
        self.signatory = Text(
            "Signatory", color=PRIMARY_COLOR, font=PRIMARY_FONT
        ).to_edge(UP + LEFT)
        self.verifier = Text(
            "Verifier", color=PRIMARY_COLOR, font=PRIMARY_FONT
        ).to_edge(UP + RIGHT)
        self.msg_box1 = EquationBoxWithIcons.create(
            "✉", "Lorem\ ipsum\ dolor\ sit\ amet...", HIGHLIGHT_COLOR
        ).next_to(self.signatory, DOWN, buff=0.5)
        self.msg_box2 = EquationBoxWithIcons.create(
            "✉", 'msg =hash("...")', HIGHLIGHT_COLOR
        ).next_to(self.signatory, DOWN, buff=0.5)
        self.signature = EquationBoxWithIcons.create(
            "⚂",
            "secret = random()",
            SECONDARY_COLOR,
            "⚂",
            "R = {{secret \cdot G}}",
            PRIMARY_COLOR,
            "⎘",
            "r = R_x \mod n",
            SECONDARY_COLOR,
            "⎘",
            "s = {{ (msg + r \cdot K_{\mathrm{Priv}}) \cdot secret^{-1} }} \mod n",
            SECONDARY_COLOR,
        ).next_to(self.msg_box2, DOWN, buff=0.5)

    def animate_in(self, scene):
        scene.play(FadeIn(self.signatory), FadeIn(self.verifier), FadeIn(self.msg_box1))
        scene.wait(2)
        scene.play(Indicate(self.verifier), color=SECONDARY_COLOR)
        scene.play(Indicate(self.msg_box1), color=SECONDARY_COLOR)
        scene.play(ReplacementTransform(self.msg_box2))
        scene.play(FadeIn(self.signature))
