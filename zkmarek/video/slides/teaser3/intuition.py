from manim import (
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    LEFT,
    RIGHT,
    Arrow,
    DOWN,
    UP,
    Create,
    Write,
    Unwrite,
    VGroup,
    Indicate,
)

from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR, HIGHLIGHT2_COLOR


class Intuition(SlideBase):
    def __init__(self) -> None:
        super().__init__(title="Intuition")

    def construct(self):
        self.line = Line(LEFT * 6, RIGHT * 6)

        self.u1 = (
            MathTex(r"u_1 = -{{msg}} \cdot {{r^{-1}}}", color=PRIMARY_COLOR)
            .next_to(self.line, UP)
            .shift(LEFT * 1.5)
            .scale(0.8)
        )
        self.u2 = (
            MathTex(r"u_2 = {{s}} \cdot {{r^{-1}}}", color=PRIMARY_COLOR)
            .next_to(self.line, UP)
            .shift(RIGHT * 1.5)
        ).scale(0.8)
        self.u1_enc = (
            MathTex(r"u_1 \cdot G", color=PRIMARY_COLOR)
            .next_to(self.line, DOWN)
            .shift(LEFT * 1.5)
            .scale(0.8)
        )
        self.u2_enc = (
            MathTex(r"u_2 \times \cdot secret \cdot G", color=PRIMARY_COLOR)
            .next_to(self.line, DOWN)
            .shift(RIGHT * 1.5)
            .scale(0.8)
        )
        self.arrow = Arrow(
            start=self.line.get_end() + UP * 0.5,
            end=self.line.get_end() + DOWN * 2,
            color=HIGHLIGHT2_COLOR,
        )
        self.label = MathTex(r"\times G").next_to(self.arrow, RIGHT)
        self.arrow2 = Arrow(
            start=self.line.get_start() + DOWN, end=self.line.get_start() + UP * 2
        )
        self.label2 = MathTex(r"\times G").next_to(self.arrow2, LEFT)
        self.cross_line = Line(
            start=self.arrow2.get_start() + LEFT,
            end=self.arrow2.get_end() + RIGHT,
            color="red",
        )

    def animate_in(self, scene):
        self.new_subsection(scene, "G encrypts", "data/sound/teaser3/slide2-0.mp3")
        scene.play(FadeIn(self.line), run_time=0.7)
        number1 = (
            MathTex("17624", color=PRIMARY_COLOR).next_to(self.line, UP).shift(LEFT * 2)
        )
        number2 = (
            MathTex("81526", color=PRIMARY_COLOR)
            .next_to(self.line, UP)
            .shift(RIGHT * 1.5)
        )

        scene.play(Write(number1), Write(number2))
        scene.wait(1)
        scene.play(FadeIn(self.arrow), FadeIn(self.label), run_time=0.5)
        number_encrypted = (
            MathTex(r"17624\times G", color=HIGHLIGHT2_COLOR)
            .next_to(self.line, DOWN)
            .shift(LEFT * 1.5)
        )
        number_encrypted2 = (
            MathTex(r"81526\times G", color=HIGHLIGHT2_COLOR)
            .next_to(self.line, DOWN)
            .shift(RIGHT * 1.5)
        )
        scene.play(Write(number_encrypted), Write(number_encrypted2))
        scene.play(FadeIn(self.arrow2))
        scene.play(Create(self.cross_line))
        scene.wait(2.5)
        scene.play(FadeOut(self.arrow2), FadeOut(self.cross_line))

        self.new_subsection(scene, "", "data/sound/teaser3/slide2-1.mp3")
        plus_up = MathTex("+", color=PRIMARY_COLOR).next_to(self.line, UP)
        plus_down = MathTex("+", color=HIGHLIGHT2_COLOR).next_to(self.line, DOWN)
        scene.play(Write(plus_up), Write(plus_down))
        sum_up = (
            MathTex("99150", color=SECONDARY_COLOR)
            .next_to(self.line, UP)
            .shift(RIGHT * 4)
        )
        sum_down = (
            MathTex(r"99150\times G", color=HIGHLIGHT2_COLOR)
            .next_to(self.line, DOWN)
            .shift(RIGHT * 4)
        )
        equal_sign_up = (
            MathTex("=", color=PRIMARY_COLOR).next_to(self.line, UP).shift(RIGHT * 3)
        )
        equal_sign_down = (
            MathTex("=", color=HIGHLIGHT2_COLOR)
            .next_to(self.line, DOWN)
            .shift(RIGHT * 3)
        )
        self.new_subsection(scene, "addition", "data/sound/teaser3/slide2-2.mp3")
        scene.play(
            Write(sum_up), Write(sum_down), Write(equal_sign_up), Write(equal_sign_down)
        )
        scene.wait(2)
        numbers = VGroup(
            number1,
            number2,
            number_encrypted,
            number_encrypted2,
            plus_down,
            plus_up,
            sum_up,
            sum_down,
            equal_sign_down,
            equal_sign_up,
        )
        scene.play(Unwrite(numbers))
        self.new_subsection(scene, "u1 and u2", "data/sound/teaser3/slide2-3.mp3")
        scene.play(Write(self.u1), Write(self.u2))
        self.new_subsection(scene, "s, r, mess hash", "data/sound/teaser3/slide2-4.mp3")
        scene.play(Indicate(self.u2[1], color=SECONDARY_COLOR))
        scene.play(Indicate(self.u1[1], color=SECONDARY_COLOR))
        scene.play(
            Indicate(self.u1[3], color=SECONDARY_COLOR),
            Indicate(self.u2[3], color=SECONDARY_COLOR),
        )

        scene.wait(1)
        self.new_subsection(scene, "encrypted", "data/sound/teaser3/slide2-5.mp3")
        scene.play(Write(self.u1_enc), Write(self.u2_enc))
        scene.wait(1)
        scene.play(Write(plus_up), Write(plus_down))
        public_key = (
            MathTex(r"K_{\mathrm{Priv}}\cdot G", color=HIGHLIGHT2_COLOR)
            .next_to(self.line, DOWN)
            .shift(RIGHT * 4)
        )
        sum_u = (
            MathTex("u_1 + u_2", color=PRIMARY_COLOR)
            .next_to(self.line, UP)
            .shift(RIGHT * 4)
        )
        self.new_subsection(scene, "private key", "data/sound/teaser3/slide2-6.mp3")
        scene.play(
            Write(equal_sign_up),
            Write(equal_sign_down),
            Write(public_key),
            Write(sum_u),
        )
        self.new_subsection(scene, "pairings", "data/sound/teaser3/slide2-7.mp3")

        self.new_subsection(scene, "", "data/sound/teaser3/slide2-8.mp3")

    def animate_out(self, scene):
        scene.play(FadeOut(self.line))
