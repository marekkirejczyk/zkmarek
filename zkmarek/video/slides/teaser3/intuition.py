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
    ImageMobject,
    Arrow, GrowArrow,
)
from zkmarek.video.mobjects.verkle_tree import VerkleTree
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
            .scale(0.9)
        )
        self.line1 = Line(LEFT * 5, RIGHT * 5)
        self.line = Line(LEFT * 6.5, RIGHT * 5)
        self.u1 = (
            MathTex(r"u_1 = -{{msg}} \cdot {{r^{-1}}}", color=PRIMARY_COLOR)
            .next_to(self.line1, UP)
            .shift(LEFT * 4)
            .scale(1.2)
        )
        self.u2 = (
            MathTex(r"u_2 = {{s}} \cdot {{r^{-1}}}", color=PRIMARY_COLOR).next_to(
                self.line1, UP
            ).shift(RIGHT*0.5)
        ).scale(1.2)
        self.u1_enc = (
            MathTex(r"u_1 \cdot {{G}}", color=SECONDARY_COLOR)
            .next_to(self.line1, DOWN)
            .shift(LEFT * 4.5)
            .scale(1.2)
        )
        self.u2_enc = (
            MathTex(r"u_2 \cdot {{R}}", color=SECONDARY_COLOR)
            .next_to(self.line1, DOWN)
            .scale(1.2)
        )

        self.arrow = (
            CurvedArrow(self.line1.get_end() + UP, self.line1.get_end() + DOWN)
            .scale([-1, 1, 1])
            .scale(0.7)
            .shift(RIGHT * 0.7)
        )
        self.label = MathTex(r"\cdot G").next_to(self.arrow, RIGHT).scale(1.2)
        self.arrow2 = (
            CurvedArrow(self.line1.get_start() + UP, self.line1.get_start() + DOWN)
            .rotate(PI)
            .scale([-1, 1, 1])
            .scale(0.7)
        )
        self.label2 = MathTex(r"\log _G").next_to(self.arrow2, LEFT).scale(1.2)
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
        self.lock = ImageMobject("data/images/Locked@2x.png").to_edge(RIGHT).shift(2*DOWN+LEFT).scale(1/2.5)

    def animate_in(self, scene):
        self.new_subsection(scene, "G encrypts", "data/sound/teaser3/slide2-0.mp3")
        scene.play(FadeIn(self.line1), FadeIn(self.title), run_time=0.7)
        number1 = (
            MathTex("176", color=PRIMARY_COLOR).next_to(self.line1, UP).shift(LEFT * 4).scale(1.2)
        )
        number2 = MathTex("815", color=PRIMARY_COLOR).next_to(self.line1, UP).scale(1.2)

        scene.play(
            FadeIn(number1),
            FadeIn(number2),
            FadeIn(self.arrow),
            FadeIn(self.label),
            run_time=0.7,
        )
        number_encrypted = (
            MathTex(r"176\cdot G", color=SECONDARY_COLOR)
            .next_to(self.line1, DOWN)
            .shift(LEFT * 4).scale(1.2)
        )
        number_encrypted2 = MathTex(r"815\cdot G", color=SECONDARY_COLOR).next_to(
            self.line1, DOWN
        ).scale(1.2)
        scene.wait(1)
        scene.play(Indicate(self.label, color = SECONDARY_COLOR), run_time=0.7)
        scene.wait(1.5)
        scene.play(FadeIn(number_encrypted), FadeIn(number_encrypted2))
        scene.play(FadeIn(self.lock), run_time = 0.1)
        scene.play(FadeIn(self.arrow2), FadeIn(self.label2))
        scene.play(Create(self.cross_line), Create(self.cross_line2))
        scene.play(
            FadeOut(self.arrow2),
            FadeOut(self.cross_line),
            FadeOut(self.cross_line2),
            FadeOut(self.label2),
            FadeOut(self.lock),
        )

        self.new_subsection(scene, "addition", "data/sound/teaser3/slide2-1.mp3")
        plus_up = (
            MathTex("+", color=PRIMARY_COLOR).next_to(self.line1, UP).shift(LEFT * 2)
        )
        plus_down = (
            MathTex("+", color=SECONDARY_COLOR).next_to(self.line1, DOWN).shift(LEFT * 2)
        )
        scene.play(Write(plus_up))
        sum_up = (
            MathTex("991", color=PRIMARY_COLOR).next_to(self.line1, UP).shift(RIGHT * 4)
        ).scale(1.2)
        sum_down = (
            MathTex(r"991\cdot G", color=SECONDARY_COLOR)
            .next_to(self.line1, DOWN)
            .shift(RIGHT * 4)
        ).scale(1.2)
        equal_sign_up = (
            MathTex("=", color=PRIMARY_COLOR)
            .next_to(self.line1, UP * 1.5)
            .shift(RIGHT * 2)
        )
        equal_sign_down = (
            MathTex("=", color=SECONDARY_COLOR)
            .next_to(self.line1, DOWN * 1.5)
            .shift(RIGHT * 2)
        )
        scene.wait(1)
        scene.play(
            Write(sum_up),
            Write(equal_sign_up),
            ReplacementTransform(self.line1, self.line)
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
        scene.play(Write(self.u1), Write(self.u2),  run_time=1)
        scene.wait(3.3)
        scene.play(Indicate(self.u1, color = HIGHLIGHT_COLOR), run_time= 0.5)
        scene.play(Indicate(self.u2, color = HIGHLIGHT_COLOR), run_time = 0.5)
        public_key = (
            MathTex(r"K_{\mathrm{Priv}}\cdot G", color=SECONDARY_COLOR)
            .next_to(self.line, DOWN)
            .shift(RIGHT * 4)
        ).scale(1.2)
        plus_down = (
            MathTex("+", color=SECONDARY_COLOR).next_to(self.line, DOWN).shift(LEFT * 2.15)
        )
        equal_sign_up = (
            MathTex("=", color=PRIMARY_COLOR)
            .next_to(self.line, UP * 1.5)
            .shift(RIGHT * 2)
        )
        equal_sign_down = (
            MathTex("=", color=SECONDARY_COLOR)
            .next_to(self.line, DOWN * 1.5)
            .shift(RIGHT * 2.3)
        )
        scene.wait(1.6)
        plus_up = (
            MathTex("+", color=PRIMARY_COLOR).next_to(self.line, UP).shift(LEFT * 2)
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
        scene.wait(1.2)
        scene.play(Indicate(self.u1_enc[1], color = HIGHLIGHT_COLOR), Indicate(self.label, color = HIGHLIGHT_COLOR))
        scene.wait(2.75)
        scene.play(Indicate(self.u2_enc[1], color = HIGHLIGHT_COLOR))
        scene.play(Indicate(self.label, color = HIGHLIGHT_COLOR), run_time=0.7)
        self.u2_enc2 = (
            MathTex(r"{{u_2 \cdot secret}} \cdot G", color=SECONDARY_COLOR)
            .next_to(self.line, DOWN)
            .scale(1.2)
        )
        priv_pub = (
            MathTex(r"K_{\mathrm{Pub}}", color=SECONDARY_COLOR)
            .next_to(self.line, DOWN)
            .shift(RIGHT * 4).scale(1.2)
        )
        scene.wait(1.9)
        scene.play(ReplacementTransform(self.u2_enc, self.u2_enc2))
        scene.wait(4.8)
        scene.play(Indicate(self.signature[1], color=HIGHLIGHT_COLOR), run_time=0.8)
        scene.wait(3.6)
        scene.play(Indicate(self.u2_enc2[0], color = HIGHLIGHT_COLOR), run_time=0.8)
        scene.wait(3.5)
        scene.play(Indicate(self.u1, color = HIGHLIGHT_COLOR), Indicate(self.u2, color = HIGHLIGHT_COLOR))
        scene.wait(3)
        scene.play(FadeIn(plus_down))
        scene.wait(1)
        scene.play(FadeIn(public_key), FadeIn(equal_sign_down))
        scene.wait(4.5)
        scene.play(Indicate(public_key, color = HIGHLIGHT_COLOR), run_time=0.7)
        scene.wait(5)
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
            priv_pub,
            plus_down,
            equal_sign_down
        )

        scene.wait(1)
        scene.play(FadeOut(addition))
        number1 = (
            MathTex("176", color=PRIMARY_COLOR).next_to(self.line, UP).shift(LEFT * 4)
        ).scale(1.2)
        number2 = MathTex(r"815", color=PRIMARY_COLOR).next_to(self.line, UP).scale(1.2)
        number_encrypted = (
            MathTex(r"176\cdot G", color=SECONDARY_COLOR)
            .next_to(self.line, DOWN)
            .shift(LEFT * 4)
        ).scale(1.2)
        number_encrypted2 = MathTex(r"815\cdot G", color=SECONDARY_COLOR).next_to(
            self.line, DOWN
        ).scale(1.2)
        sum_up = (
            MathTex(r"991", color=PRIMARY_COLOR).next_to(self.line, UP).shift(RIGHT * 4)
        ).scale(1.2)
        sum_down = (
            MathTex(r"991\cdot G", color=SECONDARY_COLOR)
            .next_to(self.line, DOWN)
            .shift(RIGHT * 4)
        ).scale(1.2)
        numbers = VGroup(
            number1,
            number2,
            number_encrypted,
            number_encrypted2,
            equal_sign_down,
            equal_sign_up,
            sum_up,
            sum_down,
            plus_up,
            plus_down,
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
        scene.play(Write(numbers), run_time=1.2)
        scene.wait(3.3)
        addition.generate_target()
        addition.target.move_to(UP * 1.5)
        scene.play(MoveToTarget(addition), run_time=1)
        self.line_multiplication = (
            Line(LEFT * 6, RIGHT * 5)
            .set_color(SECONDARY_COLOR)
            .move_to(DOWN * 2 + LEFT * 0.5)
        )

        self.multiplication_down = (
            Text("?").next_to(self.line_multiplication, DOWN).shift(LEFT * 2).scale(1.5)
        )
        self.multiplication_up = (
            MathTex(r"\times").next_to(self.line_multiplication, UP).shift(LEFT * 2)
        )

        self.new_subsection(scene, "pairings", "data/sound/teaser3/slide2-4_2.mp3")
        scene.play(FadeIn(self.line_multiplication), run_time=0.7)
        scene.play(
            Write(self.multiplication_up),
            Write(self.multiplication_down),
        )
        number_enc_multi = (
            number_encrypted.copy()
            .next_to(self.line_multiplication, UP)
            .shift(4 * LEFT)
            .set_color(HIGHLIGHT_COLOR).scale(0.88)
        )

        number_enc_multi2 = (
            number_encrypted2.copy()
            .next_to(self.line_multiplication, UP)
            .set_color(HIGHLIGHT_COLOR).scale(0.88)
        )
        scene.play(Write(number_enc_multi), Write(number_enc_multi2))
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
            FadeOut(equal_sign_down),
            FadeOut(number_enc_multi2),
            FadeOut(number_enc_multi),
            FadeOut(self.pairings),
            FadeOut(self.label),
            FadeOut(self.line),
            FadeOut(plus_up),
        )
        self.animtion_commitment(scene)
        self.animate_tree(scene)

    def animate_out(self, scene):
        scene.play(FadeOut(self.title))

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
            MathTex(r"?= 14256 \cdot G", color=HIGHLIGHT_COLOR)
            .next_to(self.line_multiplication, UP)
            .shift(3 * RIGHT)
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
            MathTex(r"= e(14256 \cdot G, G)", color=SECONDARY_COLOR)
            .next_to(self.line_multiplication, DOWN)
            .shift(RIGHT * 3)
        )
        scene.play(ReplacementTransform(self.multiplication_down, result))
        scene.play(FadeIn(result_of_result), Indicate(pairing_label, color = SECONDARY_COLOR))
        scene.wait(3.5)
        self.pairings = VGroup(
            self.line_multiplication,
            self.arrow,
            pairing_label,
            self.multiplication_up,
            result,
            result_up,
            result_of_result,
            arrow_pairing,
        )


    def animate_tree(self, scene):
        tree = VerkleTree().scale(0.8).shift(UP)
        scene.play(Create(tree))
        scene.wait(3)
        scene.play(FadeOut(tree))

    def animtion_commitment(self, scene):
        committer = ImageMobject("data/images/person.png").shift(LEFT*3).scale(0.5)
        verifier = ImageMobject("data/images/person.png").shift(RIGHT * 3).scale(0.5)
        committer_label = Text("Committer", font = PRIMARY_COLOR, font_size=40, color = PRIMARY_COLOR).next_to(committer, DOWN)
        verifier_label = Text("Verifier", font = PRIMARY_COLOR, font_size=40, color = PRIMARY_COLOR).next_to(verifier, DOWN)
        commitment = ImageMobject("data/images/Docs.png").scale(0.5)
        
        scene.play(FadeIn(committer, committer_label, verifier, verifier_label, commitment))
        
        arrow1 = Arrow(committer.get_right(), verifier.get_left(), color = HIGHLIGHT_COLOR).shift(DOWN)
        
        scene.play(GrowArrow(arrow1))
        
        scene.wait(2)
        scene.play(FadeOut(arrow1, commitment, committer, committer_label, verifier, verifier_label))