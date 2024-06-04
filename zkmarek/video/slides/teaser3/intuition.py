from manim import (
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    LEFT,
    RIGHT,
    DOWN,
    UP,
    Create,
    Write,
    Unwrite,
    VGroup,
    Indicate,
    ImageMobject,
    ReplacementTransform,
    PI,
)

from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR, HIGHLIGHT_COLOR


class Intuition(SlideBase):
    def __init__(self) -> None:
        super().__init__(title="Intuition")

    def construct(self):
        self.line = Line(LEFT * 6, RIGHT * 5)

        self.u1 = (
            MathTex(r"u_1 = -{{msg}} \cdot {{r^{-1}}}", color=PRIMARY_COLOR)
            .next_to(self.line, UP)
            .shift(LEFT * 4)
            .scale(0.8)
        )
        self.u2 = (
            MathTex(r"u_2 = {{s}} \cdot {{r^{-1}}}", color=PRIMARY_COLOR).next_to(
                self.line, UP
            )
        ).scale(0.8)
        self.u1_enc = (
            MathTex(r"u_1 \cdot G", color=SECONDARY_COLOR)
            .next_to(self.line, DOWN)
            .shift(LEFT * 4)
            .scale(0.8)
        )
        self.u2_enc = (
            MathTex(r"u_2 \cdot R", color=SECONDARY_COLOR)
            .next_to(self.line, DOWN)
            .scale(0.8)
        )
        self.arrow = (
            ImageMobject("zkmarek/video/slides/teaser3/arrow_right.png")
            .next_to(self.line, RIGHT)
            .scale(3.5)
        )
        self.label = MathTex(r"\times G").next_to(self.arrow, RIGHT)
        self.arrow2 = (
            ImageMobject("zkmarek/video/slides/teaser3/arrow_left.png")
            .next_to(self.line, LEFT)
            .scale(3.5)
        ).rotate(2 * PI / 3)
        self.label2 = MathTex(r"\times G").next_to(self.arrow2, LEFT)
        self.cross_line = Line(
            start=self.arrow2.get_start() + LEFT,
            end=self.arrow2.get_end() + RIGHT,
            color="red",
        ).scale(0.5)

    def animate_in(self, scene):
        self.new_subsection(scene, "G encrypts", "data/sound/teaser3/slide2-0.mp3")
        scene.play(FadeIn(self.line), run_time=0.7)
        number1 = (
            MathTex("17624", color=PRIMARY_COLOR).next_to(self.line, UP).shift(LEFT * 4)
        )
        number2 = MathTex("81526", color=PRIMARY_COLOR).next_to(self.line, UP)

        scene.play(Write(number1), Write(number2))
        scene.wait(1)
        scene.play(FadeIn(self.arrow), FadeIn(self.label), run_time=0.5)
        number_encrypted = (
            MathTex(r"17624\times G", color=SECONDARY_COLOR)
            .next_to(self.line, DOWN)
            .shift(LEFT * 4)
        )
        number_encrypted2 = MathTex(r"81526\times G", color=SECONDARY_COLOR).next_to(
            self.line, DOWN
        )
        scene.play(Write(number_encrypted), Write(number_encrypted2))
        scene.play(FadeIn(self.arrow2))
        scene.play(Create(self.cross_line))
        scene.wait(0.5)
        scene.play(FadeOut(self.arrow2), FadeOut(self.cross_line))

        self.new_subsection(scene, "", "data/sound/teaser3/slide2-1.mp3")
        plus_up = (
            MathTex("+", color=PRIMARY_COLOR).next_to(self.line, UP).shift(LEFT * 2)
        )
        plus_down = (
            MathTex("+", color=SECONDARY_COLOR).next_to(self.line, DOWN).shift(LEFT * 2)
        )
        scene.play(Write(plus_up))
        sum_up = (
            MathTex("99150", color=PRIMARY_COLOR)
            .next_to(self.line, UP)
            .shift(RIGHT * 4)
        )
        sum_down = (
            MathTex(r"99150\times G", color=SECONDARY_COLOR)
            .next_to(self.line, DOWN)
            .shift(RIGHT * 4)
        )
        equal_sign_up = (
            MathTex("=", color=PRIMARY_COLOR)
            .next_to(self.line, UP * 1.5)
            .shift(RIGHT * 2)
        )
        equal_sign_down = (
            MathTex("=", color=SECONDARY_COLOR)
            .next_to(self.line, DOWN * 1.5)
            .shift(RIGHT * 2)
        )
        scene.wait(1)
        scene.play(
            Write(sum_up),
            Write(equal_sign_up),
        )
        self.new_subsection(scene, "addition", "data/sound/teaser3/slide2-2.mp3")
        scene.wait(2)
        scene.play(Write(plus_down), Write(equal_sign_down), Write(sum_down))
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
        )
        scene.play(
            Unwrite(numbers),
            Unwrite(equal_sign_down),
            Unwrite(equal_sign_up),
        )
        self.new_subsection(scene, "u1 and u2", "data/sound/teaser3/slide2-3.mp3")
        scene.play(Write(self.u1), Write(self.u2))
        public_key = (
            MathTex(r"K_{\mathrm{Priv}}\cdot G", color=SECONDARY_COLOR)
            .next_to(self.line, DOWN)
            .shift(RIGHT * 4)
        )
        sum_u = (
            MathTex("u_1 + u_2", color=PRIMARY_COLOR)
            .next_to(self.line, UP)
            .shift(RIGHT * 4)
        )
        plus_down = (
            MathTex("+", color=SECONDARY_COLOR).next_to(self.line, DOWN).shift(LEFT * 2)
        )
        equal_sign_up = (
            MathTex("=", color=PRIMARY_COLOR)
            .next_to(self.line, UP * 1.5)
            .shift(RIGHT * 2)
        )
        equal_sign_down = (
            MathTex("=", color=SECONDARY_COLOR)
            .next_to(self.line, DOWN * 1.5)
            .shift(RIGHT * 2)
        )
        scene.wait(5)
        scene.play(
            Write(self.u1_enc),
            Write(self.u2_enc),
            Write(plus_down),
            Write(equal_sign_down),
            Write(public_key),
        )
        self.new_subsection(scene, "s, r, mess hash", "data/sound/teaser3/slide2-4.mp3")
        scene.wait(3.2)
        scene.play(Indicate(self.u2[1], color=HIGHLIGHT_COLOR))
        scene.play(Indicate(self.u1[1], color=HIGHLIGHT_COLOR))
        scene.play(
            Indicate(self.u1[3], color=HIGHLIGHT_COLOR),
            Indicate(self.u2[3], color=HIGHLIGHT_COLOR),
        )

        self.new_subsection(scene, "encrypted", "data/sound/teaser3/slide2-5.mp3")
        scene.wait(1)
        self.u2_enc2 = (
            MathTex(r"u_2 \cdot secret \cdot G", color=SECONDARY_COLOR)
            .next_to(self.line, DOWN)
            .scale(0.8)
        )
        scene.play(ReplacementTransform(self.u2_enc, self.u2_enc2))
        plus_up = (
            MathTex("+", color=PRIMARY_COLOR).next_to(self.line, UP).shift(LEFT * 2)
        )

        scene.play(
            Write(equal_sign_up),
            Write(sum_u),
        )
        self.new_subsection(scene, "private key", "data/sound/teaser3/slide2-6.mp3")
        multiplication_down = (
            MathTex(r"\stackrel{?}{\times}").next_to(self.line, DOWN).shift(LEFT * 2)
        )
        multiplication_up = (
            MathTex(r"\stackrel{?}{\times}")
            .next_to(self.line, UP * 1.5)
            .shift(LEFT * 2)
        )
        scene.play(
            Unwrite(sum_u),
            Unwrite(public_key),
            Unwrite(equal_sign_down),
            Unwrite(equal_sign_up),
        )
        scene.wait(2.8)
        scene.play(
            ReplacementTransform(plus_up, multiplication_up),
            ReplacementTransform(plus_down, multiplication_down),
        )
        self.new_subsection(scene, "pairings", "data/sound/teaser3/slide2-7.mp3")
        all_u = VGroup(
            multiplication_down,
            multiplication_up,
            self.u1,
            self.u2,
            self.u1_enc,
            self.u2_enc2,
            self.label,
        )
        self.new_subsection(scene, "next episode", "data/sound/teaser3/slide2-8.mp3")
        scene.wait(4)
        scene.play(
            Unwrite(all_u),
            FadeOut(self.arrow),
        )

    def animate_out(self, scene):
        scene.play(FadeOut(self.line))
