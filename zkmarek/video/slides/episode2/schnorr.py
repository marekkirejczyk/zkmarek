from manim import DOWN, LEFT, RIGHT, UP, Create, DashedLine, FadeIn, Text

from zkmarek.video.constant import (HIGHLIGHT_COLOR, PRIMARY_COLOR,
                                    PRIMARY_FONT, SECONDARY_COLOR)
from zkmarek.video.mobjects.equation_box import (EquationBox,
                                                 EquationBoxWithIcons)
from zkmarek.video.slides.common.split_slide import SplitSlide

PUB_COLOR = HIGHLIGHT_COLOR
PRIV_COLOR = SECONDARY_COLOR

class SchnorrSlide(SplitSlide):
    left_label: Text
    right_label: Text
    h_line: DashedLine
    key_box: EquationBoxWithIcons
    msg_box: EquationBoxWithIcons
    signature: EquationBoxWithIcons
    variable_box: EquationBox

    def __init__(self):
        super().__init__("DSA vs Schnorr")

    def construct(self):
        self.title = "DSA vs Schnorr"
        self.left_label = Text("DSA", font=PRIMARY_FONT,
            color=PRIMARY_COLOR)
        self.right_label = Text("Schnorr", font=PRIMARY_FONT,
            color=PRIMARY_COLOR)

    def animate_in(self, scene):
        self.new_subsection(scene, "DSA")
        self.fade_in_board(scene)

        self.key_box = EquationBoxWithIcons.create(
            "⚿", "K_{Priv} = random()", PRIV_COLOR,
            "⚿", "K_{Pub} = {{K_{Priv} \cdot G}}", PUB_COLOR
        ).next_to(self.left_label, DOWN, buff=0.5)

        self.msg_box = EquationBoxWithIcons.create(
            "✉", "msg =hash(\"...\")", PUB_COLOR
            ).next_to(self.key_box, DOWN, buff=0.5)

        self.signature = EquationBoxWithIcons.create(
            "⚂", "secret = random()", PRIV_COLOR,
            "⚂", "R = {{secret \cdot G}}", PRIMARY_COLOR,
            "⎘", "r = R_x \mod n", PUB_COLOR,
            "⎘", "s = {{ (msg + r \cdot K_{Priv}) \cdot secret^{-1} }} \mod n",
            PUB_COLOR
        ).next_to(self.msg_box, DOWN, buff=0.5)

        self.variable_box = EquationBox(
            "u_1 = {{-msg \cdot r^{-1} }}",
            "u_2 = {{s \cdot r^{-1} }}",
        ).next_to(self.signature, DOWN, buff=0.5)

        scene.play(FadeIn(self.key_box))
        scene.play(FadeIn(self.msg_box))
        scene.play(FadeIn(self.signature))
        scene.play(FadeIn(self.variable_box))




