from manim import (
    FadeIn,
    FadeOut,
    MathTex,
    UP,
    LEFT,
    DOWN,
    Text,
    VGroup,
    Indicate,
    Write,
    Unwrite,
)

from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.mobjects.strike_line import StrikeLine
from zkmarek.video.mobjects.equation_box import EquationBox
from zkmarek.video.constant import (
    PRIMARY_COLOR,
    PRIMARY_FONT,
    SECONDARY_COLOR,
    HIGHLIGHT_COLOR,
)


class SignatureMath(SlideBase):
    def __init__(self) -> None:
        super().__init__("Signature reminder")

    def construct(self):
        self.title = Text(
            "Digital signature", font=PRIMARY_FONT, color=PRIMARY_COLOR
        ).to_edge(UP)

        self.signature_box = EquationBox(
            "s = {{ (msg + r \cdot K_{Priv}) \cdot secret^{-1} }} \mod n",
            "u_1 = {{-msg \cdot r^{-1} \mod n }}",
            "u_2 = {{s \cdot r^{-1} \mod n }}",
        ).to_edge(DOWN + LEFT)
        self.equation2 = (
            MathTex(
                "Q = ({{u_1}} + {{u_2}} {{\cdot secret}}) {{\cdot  G}}",
                color=SECONDARY_COLOR,
            )
            .next_to(self.title, DOWN, buff=0.3)
            .scale(0.8)
        )
        self.equation4 = (
            MathTex(
                "Q = (-msg \cdot r^{-1} + {{s}} {{\cdot r^{-1} secret) \cdot  G}}",
                color=SECONDARY_COLOR,
            )
            .next_to(self.equation2, DOWN, buff=0.2)
            .scale(0.8)
        )
        self.equation5 = (
            MathTex(
                "Q = (-msg \cdot r^{-1} +  (msg + r \cdot K_{Priv}) \cdot {{secret^{-1} }} \cdot r^{-1} {{secret}}) \cdot  G}}",  # noqa: E501 # pyright: ignore
                color=SECONDARY_COLOR,
            )
            .next_to(self.equation4, DOWN, buff=0.2)
            .scale(0.8)
        )
        self.strike1 = StrikeLine(self.equation5[1])
        self.strike2 = StrikeLine(self.equation5[3])
        self.equation8 = (
            MathTex(
                "Q = (-msg \cdot r^{-1} + ({{msg}}  + {{r \cdot}} K_{Priv}) {{\cdot r^{-1})}} \cdot G}}",  # noqa: E501 # pyright: ignore
                color=SECONDARY_COLOR,
            )
            .next_to(self.equation5, DOWN, buff=0.2)
            .scale(0.8)
        )
        self.strike3 = StrikeLine(self.equation8[3])
        self.strike4 = StrikeLine(self.equation8[5])
        self.equation10 = (
            MathTex(
                "Q = (-msg \cdot r^{-1} + msg \cdot r^{-1} + K_{Priv}) \cdot G}}",
                color=SECONDARY_COLOR,
            )
            .next_to(self.equation8, DOWN, buff=0.2)
            .scale(0.8)
        )
        self.equation13 = (
            MathTex(
                "Q = {{}} {{ }}{{ }} K_{Priv} {{ }} {{ }} \cdot G}}",
                color=SECONDARY_COLOR,
            )
            .next_to(self.equation10, DOWN, buff=0.2)
            .scale(0.8)
        )

    def animate_in(self, scene):
        self.new_subsection(scene, "Intro", "data/sound/teaser3/slide1-4.mp3")
        scene.play(
            FadeIn(self.title),
            FadeIn(self.equation2),
            FadeIn(self.signature_box),
            run_time=0.5,
        )
        scene.wait(5.7)
        scene.play(Indicate(self.equation2[1], color=PRIMARY_COLOR), run_time=0.5)
        scene.play(Indicate(self.equation2[3], color=PRIMARY_COLOR), run_time=0.5)
        scene.wait(0.1)
        scene.play(Write(self.equation4))
        scene.wait(1)
        scene.play(
            Indicate(self.signature_box[0], color=HIGHLIGHT_COLOR),
            Indicate(self.equation4[1], color=HIGHLIGHT_COLOR),
        )
        scene.wait(0.1)

        scene.play(Write(self.equation5))
        scene.wait(1)
        self.play_sound(scene, "data/sound/teaser3/slide1-5.mp3")
        scene.play(Write(self.strike1), Write(self.strike2))
        scene.wait(0.1)
        scene.play(
            Unwrite(self.strike1),
            Unwrite(self.strike2),
            Write(self.equation8),
            run_time=0.5,
        )
        scene.wait(1)
        scene.play(Write(self.strike3), Write(self.strike4))
        scene.play(
            Unwrite(self.strike3),
            Unwrite(self.strike4),
            Write(self.equation10),
            run_time=0.5,
        )
        scene.wait(1)
        scene.play(Write(self.equation13))
        scene.wait(5)

    def animate_out(self, scene):
        self.equations = VGroup(
            self.equation10,
            self.equation13,
            self.equation2,
            self.equation4,
            self.equation5,
            self.equation8,
        )
        scene.play(
            FadeOut(self.equations),
            FadeOut(self.title),
            FadeOut(self.equation13),
            FadeOut(self.signature_box),
        )
