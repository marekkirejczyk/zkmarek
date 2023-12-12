from manim import (DOWN, DashedLine, FadeIn, FadeOut,
                   ReplacementTransform, Text)

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
    dsa_key_box: EquationBoxWithIcons
    dsa_msg_box: EquationBoxWithIcons
    dsa_signature: EquationBoxWithIcons
    dsa_variable_box: EquationBox
    dsa_q_box: EquationBox

    schnorr_key_box: EquationBoxWithIcons
    schnorr_signature: EquationBoxWithIcons
    schnorr_signature2: EquationBoxWithIcons
    schnorr_msg_box: EquationBoxWithIcons


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

        self.dsa_key_box = EquationBoxWithIcons.create(
            "⚿", "K_{Priv} = random()", PRIV_COLOR,
            "⚿", "K_{Pub} = {{K_{Priv} \cdot G}}", PUB_COLOR
        ).next_to(self.left_label, DOWN, buff=0.5)

        self.dsa_msg_box = EquationBoxWithIcons.create(
            "✉", "msg =hash(\"...\")", PUB_COLOR
            ).next_to(self.dsa_key_box, DOWN, buff=0.5)

        self.dsa_signature = EquationBoxWithIcons.create(
            "⚂", "secret = random()", PRIV_COLOR,
            "⚂", "R = {{secret \cdot G}}", PRIMARY_COLOR,
            "⎘", "r = R_x \mod n", PUB_COLOR,
            "⎘", "s = {{ (msg + r \cdot K_{Priv}) \cdot secret^{-1} }} \mod n",
            PUB_COLOR
        ).next_to(self.dsa_msg_box, DOWN, buff=0.5)

        self.dsa_variable_box = EquationBox(
            "u_1 = {{-msg \cdot r^{-1} }}",
            "u_2 = {{s \cdot r^{-1} }}",
        ).next_to(self.dsa_signature, DOWN, buff=0.5)

        self.dsa_q_box = EquationBox(
            "Q = u_1 \cdot G + u_2 \cdot {{R}} \stackrel{?}{=} K_{Pub}"
        ).next_to(self.dsa_variable_box, DOWN, buff=0.5)



        self.schnorr_key_box = EquationBoxWithIcons.create(
            "⚿", "K_{Priv} = random()", PRIV_COLOR,
            "⚿", "K_{Pub} = {{K_{Priv} \cdot G}}", PUB_COLOR
        ).next_to(self.right_label, DOWN, buff=0.5)

        self.schnorr_signature = EquationBoxWithIcons.create(
            "⚂", "secret = random()", PRIV_COLOR,
            "⚂", "R = {{secret \cdot G}}", PRIMARY_COLOR
        ).next_to(self.schnorr_key_box, DOWN, buff=0.5)

        self.schnorr_msg_box = EquationBoxWithIcons.create(
            "✉", "msg =hash(r || \"...\")", PUB_COLOR
            ).next_to(self.schnorr_signature, DOWN, buff=0.5)

        self.schnorr_signature2 = EquationBoxWithIcons.create(
            "⚂", "secret = random()", PRIV_COLOR,
            "⚂", "R = {{secret \cdot G}}", PRIMARY_COLOR,
            "⎘", "s = {{secret - K_{Priv} \cdot msg}}", PRIMARY_COLOR
        ).next_to(self.schnorr_key_box, DOWN, buff=0.5)



        # DSA Signature
        scene.play(FadeIn(self.dsa_key_box))
        scene.play(FadeIn(self.dsa_msg_box))
        scene.play(FadeIn(self.dsa_signature))

        # Schnorr Signature
        scene.play(FadeIn(self.schnorr_key_box))
        scene.play(FadeIn(self.schnorr_signature))
        scene.play(FadeIn(self.schnorr_msg_box))
        scene.play(ReplacementTransform(self.schnorr_signature, self.schnorr_signature2))
        scene.play(self.schnorr_msg_box.animate.next_to(self.schnorr_signature2, DOWN, buff=0.5))

        # Transition
        scene.play(FadeOut(self.dsa_key_box))
        scene.play(FadeOut(self.schnorr_key_box))
        scene.play(self.dsa_msg_box.animate.next_to(self.left_label, DOWN, buff=0.5))
        scene.play(self.dsa_signature.animate.next_to(self.dsa_msg_box, DOWN, buff=0.5))
        self.dsa_variable_box.next_to(self.dsa_signature, DOWN, buff=0.5)
        self.dsa_q_box.next_to(self.dsa_variable_box, DOWN, buff=0.5)

        scene.play(self.schnorr_signature2.animate.next_to(self.right_label, DOWN, buff=0.5))
        scene.play(self.schnorr_msg_box.animate.next_to(self.schnorr_signature2, DOWN, buff=0.5))

        # DSA Recover
        scene.play(FadeIn(self.dsa_variable_box))
        scene.play(FadeIn(self.dsa_q_box))

        # DSA Recover


# TODO
# Add note about ECRecover
# Add ECVerify

# Add solidity implementation
# Add slide with Solidity implementation
