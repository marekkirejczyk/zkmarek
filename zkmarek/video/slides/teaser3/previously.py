from manim import FadeIn, Text, UP, DOWN, LEFT, RIGHT, Indicate, Write, FadeOut

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
        self.signatory = (
            Text("Signatory", color=PRIMARY_COLOR, font=PRIMARY_FONT)
            .to_edge(UP + LEFT)
            .shift(RIGHT)
        )
        self.verifier = (
            Text("Verifier", color=PRIMARY_COLOR, font=PRIMARY_FONT)
            .to_edge(UP + RIGHT)
            .shift(LEFT)
        )
        self.msg_box = EquationBoxWithIcons.create(
            "✉", 'msg =hash("...")', HIGHLIGHT_COLOR
        ).shift(UP)
        self.key_box2 = (
            EquationBoxWithIcons.create(
                "⚿",
                "K_{Priv} = random()",
                PRIMARY_COLOR,
                "⚿",
                "K_{Pub} = {{K_{Priv} \cdot G}}",
                PRIMARY_COLOR,
            )
            .next_to(self.signatory, DOWN, buff=0.5)
            .scale(0.8)
        )

        self.key_box = (
            EquationBoxWithIcons.create(
                "⚿",
                "K_{Pub} = {{K_{Priv} \cdot G}}",
                SECONDARY_COLOR,
            )
            .next_to(self.verifier, DOWN, buff=0.8)
            .scale(0.8)
        )

        self.signature_verifier = (
            EquationBoxWithIcons.create(
                "⎘",
                "{{r = R_x \mod n}}",
                SECONDARY_COLOR,
                "⎘",
                "{{s =  (msg + r \cdot K_{Priv}) \cdot secret^{-1}  \mod n}}",
                SECONDARY_COLOR,
            )
            .next_to(self.key_box, DOWN, buff=1)
            .scale(0.8)
            .shift(DOWN)
        )
        self.signature = (
            EquationBoxWithIcons.create(
                "⚂",
                "R = {{secret \cdot G}}",
                PRIMARY_COLOR,
                "⎘",
                "{{r = R_x \mod n}}",
                PRIMARY_COLOR,
                "⎘",
                "{{s =  (msg + r \cdot K_{Priv}) \cdot secret^{-1}  \mod n}}",
                PRIMARY_COLOR,
                "⚂",
                "{{secret = random()}}",
                PRIMARY_COLOR,
            )
            .next_to(self.key_box2, DOWN, buff=1)
            .scale(0.8)
        )

    def animate_in(self, scene):
        self.new_subsection(
            scene, "we last talked about", "data/sound/teaser3/slide1-0.mp3"
        )
        scene.play(
            Write(self.signatory),
            Write(self.verifier),
            run_time=1.5,
        )
        self.new_subsection(scene, "recall", "data/sound/teaser3/slide1-1.mp3")
        scene.play(Write(self.msg_box), run_time=0.1)
        scene.wait(4.5)
        scene.play(Indicate(self.verifier, color=SECONDARY_COLOR), run_time=0.5)
        scene.wait(0.5)
        scene.play(Indicate(self.msg_box, color=SECONDARY_COLOR), run_time=0.5)
        scene.wait(0.5)
        scene.play(Indicate(self.signatory, color=SECONDARY_COLOR), run_time=0.5)

        self.new_subsection(scene, "signature", "data/sound/teaser3/slide1-2.mp3")
        scene.play(
            FadeIn(self.signature),
            FadeIn(self.key_box),
            FadeIn(self.signature_verifier),
            Write(self.key_box2),
            run_time=0.7,
        )
        scene.wait(3)
        scene.play(Indicate(self.key_box[1], color=HIGHLIGHT_COLOR), run_time=1)
        scene.wait(3.5)
        scene.play(Indicate(self.msg_box, color=SECONDARY_COLOR), run_time=0.7)
        scene.wait(0.5)
        scene.play(
            Indicate(self.signature_verifier[1], color=HIGHLIGHT_COLOR), run_time=0.5
        )
        scene.play(
            Indicate(self.signature_verifier[3], color=HIGHLIGHT_COLOR), run_time=0.5
        )

        self.new_subsection(scene, "signature", "data/sound/teaser3/slide1-3.mp3")
        scene.wait(2.7)
        scene.play(Indicate(self.signature[3], color=SECONDARY_COLOR), run_time=0.5)
        scene.play(Indicate(self.signature[5]), color=SECONDARY_COLOR, run_time=0.5)

        scene.wait(1.8)
        scene.play(Indicate(self.signature[3], color=SECONDARY_COLOR), run_time=0.5)
        scene.wait(1.8)
        scene.play(Indicate(self.signature[1], color=SECONDARY_COLOR), run_time=0.5)
        scene.wait(4.3)
        scene.play(Indicate(self.signature[5], color=SECONDARY_COLOR), run_time=1)
        self.new_subsection(
            scene, "summary the action of signature", "data/sound/teaser3/slide1-4.mp3"
        )
        scene.wait(3)
        # scene.play(Indicate(self.signature, color=SECONDARY_COLOR), run_time=0.7)
        scene.play(Indicate(self.key_box2[1], color=SECONDARY_COLOR), run_time=0.5)
        scene.wait(7)
        scene.play(Indicate(self.verifier, color=SECONDARY_COLOR), run_time=0.7)
        scene.wait(3)
        scene.play(
            Indicate(self.signature_verifier[1], color=PRIMARY_COLOR),
            Indicate(self.signature_verifier[3], color=PRIMARY_COLOR),
            run_time=1,
        )
        scene.wait(3)
        scene.play(Indicate(self.key_box2[1], color=SECONDARY_COLOR))

        scene.wait(4)

    def animate_out(self, scene):
        scene.play(
            FadeOut(self.signature),
            FadeOut(self.signature_verifier),
            FadeOut(self.key_box),
            FadeOut(self.key_box2),
            FadeOut(self.msg_box),
            FadeOut(self.verifier),
            FadeOut(self.signatory),
        )
