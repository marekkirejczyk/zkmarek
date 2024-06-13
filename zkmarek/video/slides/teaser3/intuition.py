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
            MathTex(r"u_2 \cdot {{R}}", color=SECONDARY_COLOR)
            .next_to(self.line, DOWN)
            .scale(0.8)
        )

        self.arrow = (
            CurvedArrow(self.line.get_end() + UP, self.line.get_end() + DOWN)
            .scale([-1, 1, 1])
            .scale(0.7)
            .shift(RIGHT * 0.3)
        )
        self.label = MathTex(r"\times G").next_to(self.arrow, RIGHT)
        self.arrow2 = (
            CurvedArrow(self.line.get_start() + UP, self.line.get_start() + DOWN)
            .rotate(PI)
            .scale([-1, 1, 1])
            .shift(0.3 * RIGHT)
            .scale(0.7)
        )
        self.label2 = MathTex(r"\div G").next_to(self.arrow2, LEFT)
        self.cross_line = Line(
            start=self.arrow2.get_start() + LEFT * 2,
            end=self.arrow2.get_end() + RIGHT * 0.8,
            color="red",
        ).scale(0.4)
        self.cross_line2 = Line(
            start=self.arrow2.get_end() + LEFT * 2,
            end=self.arrow2.get_start() + RIGHT * 0.8,
            color="red",
        ).scale(0.4)
        self.signature = EquationBoxWithIcons.create(
            "⎘",
            "{{r = R_x \mod n}}",
            SECONDARY_COLOR,
            "⎘",
            "{{s =  (msg + r \cdot K_{Priv}) \cdot secret^{-1}  \mod n}}",
            SECONDARY_COLOR,
        ).to_edge(DOWN + LEFT)

    def animate_in(self, scene):
        self.new_subsection(scene, "G encrypts", "data/sound/teaser3/slide2-0.mp3")
        scene.play(FadeIn(self.line), FadeIn(self.title), run_time=0.7)
        number1 = (
            MathTex("176", color=PRIMARY_COLOR).next_to(self.line, UP).shift(LEFT * 4)
        )
        number2 = MathTex("815", color=PRIMARY_COLOR).next_to(self.line, UP)

        scene.play(
            FadeIn(number1),
            FadeIn(number2),
            FadeIn(self.arrow),
            FadeIn(self.label),
            run_time=0.7,
        )
        number_encrypted = (
            MathTex(r"176\cdot G", color=SECONDARY_COLOR)
            .next_to(self.line, DOWN)
            .shift(LEFT * 4)
        )
        number_encrypted2 = MathTex(r"815\cdot G", color=SECONDARY_COLOR).next_to(
            self.line, DOWN
        )
        scene.wait(2.2)
        scene.play(FadeIn(number_encrypted), FadeIn(number_encrypted2))
        scene.wait(1)
        scene.play(FadeIn(self.arrow2), FadeIn(self.label2))
        scene.play(Create(self.cross_line), Create(self.cross_line2))
        scene.play(
            FadeOut(self.arrow2),
            FadeOut(self.cross_line),
            FadeOut(self.cross_line2),
            FadeOut(self.label2),
        )

        self.new_subsection(scene, "addition", "data/sound/teaser3/slide2-1.mp3")
        plus_up = (
            MathTex("+", color=PRIMARY_COLOR).next_to(self.line, UP).shift(LEFT * 2)
        )
        plus_down = (
            MathTex("+", color=SECONDARY_COLOR).next_to(self.line, DOWN).shift(LEFT * 2)
        )
        scene.play(Write(plus_up))
        sum_up = (
            MathTex("991", color=PRIMARY_COLOR).next_to(self.line, UP).shift(RIGHT * 4)
        )
        sum_down = (
            MathTex(r"991\cdot G", color=SECONDARY_COLOR)
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
        scene.wait(4.2)
        plus_up = (
            MathTex("+", color=PRIMARY_COLOR).next_to(self.line, UP).shift(LEFT * 2)
        )
        scene.play(
            Write(plus_up),
            Write(equal_sign_up),
            Write(sum_u),
        )
        scene.play(
            Indicate(self.u1[1], color=SECONDARY_COLOR),
            run_time=0.7,
        )
        scene.play(FadeIn(self.signature), run_time=1)
        self.new_subsection(scene, "r", "data/sound/teaser3/slide2-r.mp3")
        scene.play(
            Indicate(self.signature[1], color=HIGHLIGHT_COLOR),
            Indicate(self.u1[3], color=SECONDARY_COLOR),
            Indicate(self.u2[3], color=SECONDARY_COLOR),
            run_Time=0.7,
        )
        self.new_subsection(scene, "and s", "data/sound/teaser3/slide2-s.mp3")
        scene.play(
            Indicate(self.signature[3], color=HIGHLIGHT_COLOR),
            Indicate(self.u2[1], color=SECONDARY_COLOR),
            run_time=0.7,
        )
        self.new_subsection(scene, "secret", "data/sound/teaser3/slide2-3.mp3")
        scene.play(FadeIn(self.u1_enc), FadeIn(self.u2_enc))
        scene.play(Indicate(self.u2_enc[1]))
        self.u2_enc2 = (
            MathTex(r"u_2 \cdot secret \cdot G", color=SECONDARY_COLOR)
            .next_to(self.line, DOWN)
            .scale(0.8)
        )
        scene.wait(14)
        priv_pub = (
            MathTex(r"K_{\mathrm{Pub}}", color=SECONDARY_COLOR)
            .next_to(self.line, DOWN)
            .shift(RIGHT * 4)
        )
        scene.play(ReplacementTransform(self.u2_enc, self.u2_enc2))
        scene.wait(7)
        scene.play(FadeIn(public_key), FadeIn(plus_down), FadeIn(equal_sign_down))
        scene.wait(10)
        scene.play(ReplacementTransform(public_key, priv_pub))
        scene.wait(2)
        self.new_subsection(
            scene, "add and multiply", "data/sound/teaser3/slide2-4.mp3"
        )
        addition = VGroup(
            self.u1,
            self.u2,
            self.u1_enc,
            self.u2_enc2,
            self.signature,
            sum_u,
            priv_pub,
        )

        scene.wait(2)
        scene.play(FadeOut(addition))
        number1 = (
            MathTex("176", color=PRIMARY_COLOR).next_to(self.line, UP).shift(LEFT * 4)
        )
        number2 = MathTex(r"815", color=PRIMARY_COLOR).next_to(self.line, UP)
        number_encrypted = (
            MathTex(r"176\cdot G", color=SECONDARY_COLOR)
            .next_to(self.line, DOWN)
            .shift(LEFT * 4)
        )
        number_encrypted2 = MathTex(r"815\cdot G", color=SECONDARY_COLOR).next_to(
            self.line, DOWN
        )
        sum_up = (
            MathTex(r"991", color=PRIMARY_COLOR).next_to(self.line, UP).shift(RIGHT * 4)
        )
        sum_down = (
            MathTex(r"991\cdot G", color=SECONDARY_COLOR)
            .next_to(self.line, DOWN)
            .shift(RIGHT * 4)
        )
        numbers = VGroup(
            number1,
            number2,
            number_encrypted,
            number_encrypted2,
            plus_up,
            plus_down,
            equal_sign_down,
            equal_sign_up,
            sum_up,
            sum_down,
        )
        addition = VGroup(
            self.line,
            self.label,
            self.arrow,
            number1,
            number2,
            plus_up,
            plus_down,
            equal_sign_down,
            equal_sign_up,
            number_encrypted,
            number_encrypted2,
            sum_up,
            sum_down,
        )
        scene.play(Write(numbers), run_time=0.7)
        addition.generate_target()
        addition.target.move_to(UP * 1.5)
        scene.play(MoveToTarget(addition), run_time=1)
        self.line_multiplication = (
            Line(LEFT * 7, RIGHT * 4).set_color(SECONDARY_COLOR).move_to(DOWN * 2)
        )

        self.multiplication_down = (
            Text("?").next_to(self.line_multiplication, DOWN).shift(LEFT * 2).scale(1.5)
        )
        self.multiplication_up = (
            MathTex(r"\times").next_to(self.line_multiplication, UP).shift(LEFT * 2)
        )
        scene.play(FadeIn(self.line_multiplication), run_time=0.7)
        scene.play(
            Write(self.multiplication_up),
            Write(self.multiplication_down),
        )
        number_enc_multi = (
            number_encrypted.copy()
            .next_to(self.line_multiplication, UP)
            .move_to(LEFT * 4 + DOWN * 2)
            .set_color(HIGHLIGHT_COLOR)
        )

        number_enc_multi2 = (
            number_encrypted2.copy()
            .next_to(self.line_multiplication, UP)
            .set_color(HIGHLIGHT_COLOR)
        )
        scene.play(Write(number_enc_multi), Write(number_enc_multi2))
        self.new_subsection(scene, "pairings", "data/sound/teaser3/slide2-5.mp3")
        self.pairings_animation(scene)
        scene.play(
            FadeOut(number_encrypted),
            FadeOut(number_encrypted2),
            FadeOut(sum_down),
            FadeOut(number1),
            FadeOut(number2),
            FadeOut(sum_up),
            FadeOut(plus_down),
            FadeOut(plus_down),
            FadeOut(equal_sign_up),
            FadeOut(number_enc_multi2),
            FadeOut(number_enc_multi),
        )

    def animate_out(self, scene):
        scene.play(FadeOut(self.title), FadeOut(self.line), FadeOut(self.label))

    def pairings_animation(self, scene):
        arrow_pairing = (
            CurvedArrow(
                self.line_multiplication.get_end() + UP,
                self.line_multiplication.get_end() + DOWN,
            )
            .scale([-1, 1, 1])
            .scale(0.7)
            .shift(RIGHT * 0.3)
        )
        pairing_label = MathTex(r"e(\cdot, \cdot)").next_to(arrow_pairing, RIGHT)
        result_up = (
            MathTex(r"= \quad 14256 \cdot G", color=HIGHLIGHT_COLOR)
            .next_to(self.line_multiplication, UP)
            .move_to(3 * RIGHT)
        )
        scene.play(FadeIn(result_up))
        scene.play(Write(arrow_pairing), Write(pairing_label), run_time=0.7)
        scene.wait(2)
        result = (
            MathTex(r"e(176\cdot G, 815\cdot G)", color=SECONDARY_COLOR)
            .next_to(self.line_multiplication, DOWN)
            .shift(LEFT * 2)
        )
        result_of_result = (
            MathTex(r"= \quad e(14256 \cdot G, G)", color=SECONDARY_COLOR)
            .next_to(self.line_multiplication, DOWN)
            .move_to(RIGHT * 3)
        )
        scene.play(ReplacementTransform(self.multiplication_down, result))
        scene.wait(3)
        scene.play(FadeIn(result_of_result))
        scene.wait(5)
        pairings = VGroup(
            self.line_multiplication,
            self.arrow,
            pairing_label,
            self.multiplication_up,
            result,
            result_up,
            result_of_result,
        )
        scene.play(FadeOut(pairings))
