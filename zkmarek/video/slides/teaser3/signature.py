from manim import (
    FadeIn,
    FadeOut,
    MathTex,
    UP,
    DOWN,
    ReplacementTransform,
    Text,
    TransformMatchingTex,
    VGroup,
)

from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.mobjects.equation_box import EquationBox
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR


class SignatureMath(SlideBase):
    def __init__(self) -> None:
        super().__init__("Signature reminder")

    def construct(self):
        self.title = Text(
            "Previously on zkMarek", font=PRIMARY_FONT, color=PRIMARY_COLOR
        )

        self.signature_box = EquationBox(
            "s = {{ (msg + r \cdot K_{Priv}) \cdot secret^{-1} }} \mod n",
            "u_1 = {{-msg \cdot r^{-1} \mod n }}",
            "u_2 = {{s \cdot r^{-1} \mod n }}",
        ).next_to(self.title, DOWN)
        self.equation2 = MathTex(
            "Q = ({{u_1}} + {{u_2}} {{\cdot secret}}) {{\cdot  G}}",
            color=SECONDARY_COLOR,
        ).next_to(self.signature_box, UP * 2)
        self.equation4 = MathTex(
            "Q = (-msg \cdot r^{-1} + {{s}} {{\cdot r^{-1} secret) \cdot  G}}",
            color=SECONDARY_COLOR,
        ).next_to(self.signature_box, UP * 2)
        self.equation5 = MathTex(
            "Q = (-msg \cdot r^{-1} + {{ (msg + r \cdot K_{Priv}) \cdot secret^{-1} }} {{\cdot r^{-1} secret) \cdot  G}}",  # noqa: E501 # pyright: ignore
            color=SECONDARY_COLOR,
        ).next_to(self.signature_box, UP * 2)
        self.equation6 = MathTex(
            "Q = (-msg \cdot r^{-1} + (msg + r \cdot K_{\mathrm{Priv}}) {{\cdot secret^{-1}}}  \cdot r^{-1} {{secret}}) \cdot  G}}",  # noqa: E501 # pyright: ignore
            color=SECONDARY_COLOR,
        ).next_to(self.signature_box, UP * 2)
        self.equation7 = MathTex(
            "Q = (-msg \cdot r^{-1} + (msg + r \cdot K_{Priv}) {{}}  \cdot r^{-1} {{}}) \cdot G}}",  # noqa: E501 # pyright: ignore
            color=SECONDARY_COLOR,
        ).next_to(self.signature_box, UP * 2)
        self.equation8 = MathTex(
            "Q = (-msg \cdot r^{-1} + ({{msg}} {{ }} + {{r \cdot}} K_{Priv}) {{\cdot r^{-1})}} \cdot G}}",  # noqa: E501 # pyright: ignore
            color=SECONDARY_COLOR,
        ).next_to(self.signature_box, UP * 2)
        self.equation9 = MathTex(
            "Q = (-msg \cdot r^{-1} + ({{msg}} {{\cdot r^{-1} }} + {{ }} K_{Priv}) ) {{ }} \cdot G}}",  # noqa: E501 # pyright: ignore
            color=SECONDARY_COLOR,
        ).next_to(self.signature_box, UP * 2)
        self.equation10 = MathTex(
            "Q = (-msg \cdot r^{-1} + (msg \cdot r^{-1} + K_{Priv}) ) \cdot G}}",
            color=SECONDARY_COLOR,
        ).next_to(self.signature_box, UP * 2)
        self.equation11 = MathTex(
            "Q = {{(-msg \cdot r^{-1} + }} {{(}}{{msg \cdot r^{-1} + }} K_{Priv} {{)}} {{ ) }} \cdot G}}",  # noqa: E501 # pyright: ignore
            color=SECONDARY_COLOR,
        ).next_to(self.signature_box, UP * 2)
        self.equation12 = MathTex(
            "Q = {{(-msg \cdot r^{-1} + }} {{ }}{{msg \cdot r^{-1} + }}  K_{Priv} {{ }} {{ ) }} \cdot G}}",  # noqa: E501 # pyright: ignore
            color=SECONDARY_COLOR,
        ).next_to(self.signature_box, UP * 2)
        self.equation13 = MathTex(
            "Q = {{}} {{ }}{{ }} K_{Priv} {{ }} {{ }} \cdot G}}",
            color=SECONDARY_COLOR,
        ).next_to(self.signature_box, UP * 2)

    def animate_in(self, scene):
        scene.play(FadeIn(self.title.to_edge(UP)))
        scene.play(FadeIn(self.equation2), FadeIn(self.signature_box))
        scene.wait(1)
        scene.play(
            TransformMatchingTex(
                VGroup(self.equation2, self.signature_box[1].copy()), self.equation4
            ),
            TransformMatchingTex(
                VGroup(self.equation2, self.signature_box[2].copy()), self.equation4
            ),
        )
        scene.wait(1)
        scene.play(
            TransformMatchingTex(
                VGroup(self.equation4, self.signature_box[0].copy()), self.equation5
            ),
        )
        scene.wait(2)
        scene.play(ReplacementTransform(self.equation5, self.equation6), run_time=0.5)
        scene.wait(2)
        scene.play(ReplacementTransform(self.equation6, self.equation7), run_time=0.5)
        scene.wait(2)
        scene.play(ReplacementTransform(self.equation7, self.equation8), run_time=0.5)
        scene.wait(2)
        scene.play(ReplacementTransform(self.equation8, self.equation9), run_time=0.5)
        scene.wait(2)
        scene.play(ReplacementTransform(self.equation9, self.equation10), run_time=0.5)
        scene.wait(2)
        scene.play(ReplacementTransform(self.equation10, self.equation11), run_time=0.5)
        scene.wait(2)
        scene.play(ReplacementTransform(self.equation11, self.equation12), run_time=0.5)
        scene.wait(2)
        scene.play(ReplacementTransform(self.equation12, self.equation13), run_time=0.5)

    def animate_out(self, scene):
        scene.play(
            FadeOut(self.title),
            FadeOut(self.equation13),
            FadeOut(self.signature_box),
        )
