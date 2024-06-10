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
    PI,
    Write,
    Unwrite,
    VGroup,
    Indicate,
    ReplacementTransform,
    Text,
    CurvedArrow,
    MoveToTarget,
)

from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import (
    PRIMARY_COLOR,
    SECONDARY_COLOR,
    HIGHLIGHT_COLOR,
    PRIMARY_FONT,
)
from zkmarek.video.mobjects.equation_box import EquationBoxWithIcons


class Intuition(SlideBase):
    def __init__(self) -> None:
        super().__init__(title="Understanding the digital signature")

    def construct(self):
        self.title = (
            Text(
                "Understanding the digital signature",
                color=PRIMARY_COLOR,
                font=PRIMARY_FONT,
            )
            .to_edge(UP)
            .scale(0.8)
        )
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

        self.arrow = CurvedArrow(
            self.line.get_end() + UP, self.line.get_end() + DOWN
        ).scale([-1, 1, 1])
        self.label = MathTex(r"\times G").next_to(self.arrow, RIGHT)
        self.arrow2 = (
            CurvedArrow(self.line.get_start() + UP, self.line.get_start() + DOWN)
            .rotate(PI)
            .scale([-1, 1, 1])
        )
        self.label2 = MathTex(r"\times G").next_to(self.arrow2, RIGHT)
        self.cross_line = Line(
            start=self.arrow2.get_start() + LEFT * 2,
            end=self.arrow2.get_end() + RIGHT,
            color="red",
        ).scale(0.4)
        self.signature = EquationBoxWithIcons.create(
            "⎘",
            "{{r = R_x \mod n}}",
            SECONDARY_COLOR,
            "⎘",
            "{{s =  (msg + r \cdot K_{Priv}) \cdot secret^{-1}  \mod n}}",
            SECONDARY_COLOR,
            "⎘",
            '{{msg = hash("...")}}',
            SECONDARY_COLOR,
        ).to_edge(DOWN + LEFT)

    def animate_in(self, scene):
        self.new_subsection(scene, "G encrypts", "data/sound/teaser3/slide2-0.mp3")
        scene.play(FadeIn(self.line), FadeIn(self.title), run_time=0.7)
        number1 = (
            MathTex("17624", color=PRIMARY_COLOR).next_to(self.line, UP).shift(LEFT * 4)
        )
        number2 = MathTex("81526", color=PRIMARY_COLOR).next_to(self.line, UP)

        scene.play(Write(number1), Write(number2))
        scene.wait(1)
        scene.play(FadeIn(self.arrow), FadeIn(self.label), run_time=0.5)
        number_encrypted = (
            MathTex(r"17624\cdot G", color=SECONDARY_COLOR)
            .next_to(self.line, DOWN)
            .shift(LEFT * 4)
        )
        number_encrypted2 = MathTex(r"81526\cdot G", color=SECONDARY_COLOR).next_to(
            self.line, DOWN
        )
        scene.play(Write(number_encrypted), Write(number_encrypted2))
        scene.play(FadeIn(self.arrow2), FadeIn(self.label2))
        scene.play(Create(self.cross_line))
        scene.wait(0.5)
        scene.play(FadeOut(self.arrow2), FadeOut(self.cross_line), FadeOut(self.label2))

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
            MathTex(r"99150\cdot G", color=SECONDARY_COLOR)
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
        self.new_subsection(scene, "u1 and u2", "data/sound/teaser3/slide2-2.mp3")
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
            FadeIn(self.signature),
        )
        scene.wait(3.2)
        scene.play(Indicate(self.u2[1], color=HIGHLIGHT_COLOR))
        scene.play(Indicate(self.u1[1], color=HIGHLIGHT_COLOR))
        scene.play(
            Indicate(self.u1[3], color=HIGHLIGHT_COLOR),
            Indicate(self.u2[3], color=HIGHLIGHT_COLOR),
        )
        scene.play(Indicate(self.signature[1], color=HIGHLIGHT_COLOR), run_time=0.5)
        scene.play(Indicate(self.signature[5], color=HIGHLIGHT_COLOR), run_Time=0.7)
        scene.play(Indicate(self.signature[3], color=HIGHLIGHT_COLOR), run_time=0.7)
        self.new_subsection(scene, "secret", "data/sound/teaser3/slide2-3.mp3")
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
            Write(plus_up),
            Write(equal_sign_up),
            Write(sum_u),
        )
        scene.wait(5)
        scene.play(Indicate(public_key), run_time=0.7)

        self.new_subsection(scene, "pairings", "data/sound/teaser3/slide2-4.mp3")
        addition = VGroup(
            self.u1,
            self.u2,
            self.u1_enc,
            self.u2_enc2,
            self.signature,
            plus_down,
            plus_up,
            equal_sign_down,
            equal_sign_up,
            sum_u,
            public_key,
        )
        self.line_multiplication = Line(LEFT * 6, RIGHT * 5).set_color(SECONDARY_COLOR)
        scene.play(Unwrite(addition), run_time=1.5)
        scene.play(
            ReplacementTransform(self.line, self.line_multiplication), run_time=0.7
        )

        self.multiplication_down = (
            Text("?").next_to(self.line, DOWN).shift(LEFT * 2).scale(1.5)
        )
        self.multiplication_up = (
            MathTex(r"\stackrel{?}{\times}")
            .next_to(self.line, UP * 1.5)
            .shift(LEFT * 2)
        )
        scene.wait(2)
        scene.play(
            Write(self.multiplication_up),
            Write(self.multiplication_down),
        )
        self.pairings_animation(scene)

    def animate_out(self, scene):
        scene.play(FadeOut(self.title))

    def pairings_animation(self, scene):
        self.pairing = (
            Text("Pairings:", color=PRIMARY_COLOR, font=PRIMARY_FONT)
            .next_to(self.u1_enc, DOWN * 4)
            .scale(0.8)
        )
        self.operation = (
            MathTex(r"e: G_1 \times G_2 \rightarrow G_T")
            .next_to(self.pairing, RIGHT)
            .scale(0.8)
        )
        component1 = MathTex(r"P\in G_1").next_to(self.operation, DOWN)
        component2 = MathTex(r"Q\in G_2").next_to(component1, DOWN)
        pairing_label = MathTex("e()").next_to(self.arrow, RIGHT)
        scene.play(
            Write(self.pairing),
            Write(self.operation),
            Write(component1),
            Write(component2),
            ReplacementTransform(self.label, pairing_label),
            run_time=1,
        )
        scene.wait(2)
        component1.generate_target()
        component1.target.next_to(self.line_multiplication, UP).shift(LEFT * 4)
        component2.generate_target()
        component2.target.next_to(self.line_multiplication, UP)
        scene.play(MoveToTarget(component1), MoveToTarget(component2), run_time=0.8)
        result = MathTex("e(P,Q)").next_to(self.line_multiplication, DOWN)
        scene.play(ReplacementTransform(self.multiplication_down, result), run_time=0.7)

        scene.wait(7)
        pairings = VGroup(
            self.pairing,
            self.operation,
            component1,
            component2,
            result,
            self.line_multiplication,
            self.arrow,
            pairing_label,
            self.multiplication_up,
        )
        scene.play(FadeOut(pairings))
