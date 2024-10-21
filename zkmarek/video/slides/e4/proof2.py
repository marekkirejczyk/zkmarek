from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    MathTex,
    Indicate,
    Write,
    FadeIn,
    TransformMatchingShapes,
    VGroup,
    FadeOut,
    TransformMatchingTex,
    ImageMobject,
    Text,
    Create,
    Polygon,
    MoveToTarget,
    Tex,
    RoundedRectangle,
    Arrow,
    StealthTip
)

from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR, HIGHLIGHT_COLOR, PRIMARY_FONT
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.e4.discreete_polynomial_chart import DiscreetePolynomialChart

def poly(x):
    return x * x * x - x * x * 2 + x * 3 + 7


class Proof2(SlideBase):
    polynomial: MathTex
    equation: MathTex
    commitment: MathTex
    proof: MathTex
    verification: MathTex

    def __init__(self):
        super().__init__("Verification")

    def construct(self):
        self.title = Text("Verification", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 40).to_edge(UP)
        self.verifier = ImageMobject("data/images/person.png").to_corner(RIGHT+UP).scale(0.6).shift(LEFT)
        self.commiter = ImageMobject("data/images/person_blue.png").to_corner(LEFT+UP).scale(0.6).shift(RIGHT)

        self.commiter_label = Text("Committer", color = PRIMARY_COLOR, font=PRIMARY_FONT).scale(0.6).next_to(self.commiter, DOWN, buff = 0.4)
        self.verifier_label = Text("Verifier", color = PRIMARY_COLOR, font=PRIMARY_FONT).scale(0.6).next_to(self.verifier, DOWN, buff = 0.4)

        self.chart = DiscreetePolynomialChart(41, poly)

        self.definition2 = MathTex(r"e({{G_1}}, {{G_2}}) \rightarrow {{G_T}}", color=PRIMARY_COLOR)
        self.polynomial = MathTex("p(x) = x^3 - 2x^2 + 3x + 4", color=PRIMARY_COLOR)
        self.equation = MathTex(r"{{q(\tau)}}\cdot {{(\tau - x_0)}} = {{p(\tau)}} - {{y_0}}", color=PRIMARY_COLOR)
        self.equation2 = MathTex(r"{{q(x)}}\cdot {{(x - x_0)}} = {{p(x)}} - {{y_0}}", color=PRIMARY_COLOR)
        self.commitment = MathTex(r"{{C}} = {{p(\tau)}} \cdot {{G_1}}", font_size = 32, color=PRIMARY_COLOR)
        self.proof = MathTex(r"{{\pi}} = {{q(\tau)}} \cdot {{G_1}}", color=PRIMARY_COLOR)

        self.verification = MathTex(
            r"e( {{\pi}}, {{(\tau-x_0)}} {{\cdot G_2}} ) = e({{C}} - {{y_0}} {{\cdot G_1}}, {{G_2}})",
            color=PRIMARY_COLOR,
        )
        self.verification0b = MathTex(
            r"e( {{\pi}}, {{(\tau-x_0)}} {{\cdot G_2}} ) = e({{C}} {{}} - {{y_0}} {{\cdot G_1}}, {{G_2}})",
            color=PRIMARY_COLOR,
        )
        self.verification0a = MathTex(
            r"e( {{\pi}}, ({{\tau}} -{{x_0}}) {{\cdot G_2}} ) = e({{C}} - {{y_0}} {{\cdot G_1}}, {{G_2}})",
            color=PRIMARY_COLOR,
        )
        self.verification1 = MathTex(
            r"e( {{\pi}}{{}}, {{(\tau-x_0)}} {{\cdot G_2}} ) = e({{p(\tau)}} \cdot {{G_1}} - {{y_0}} {{\cdot G_1}}, {{G_2}})",
            color=PRIMARY_COLOR,
        )

        self.verification2 = MathTex(
            r"e( {{q(\tau)}}{{\cdot G_1}}, {{(\tau-x_0)}} {{\cdot G_2}} ) = e({{p(\tau)}} \cdot {{G_1}} - {{y_0}} {{\cdot G_1}}, {{G_2}})",
            color=PRIMARY_COLOR,
        ).to_edge(DOWN)
        self.verification2a = MathTex(
            r"e( {{q(\tau)}}{{\cdot G_1}}, {{(\tau-x_0)}} {{\cdot}} {{G_2}} ) = e({{p(\tau)}} \cdot {{G_1}} - {{y_0}} {{\cdot G_1}}, {{G_2}})",
            color = PRIMARY_COLOR
        ).to_edge(DOWN)
        self.verification3 = MathTex(
            r"e({{q(\tau)}}{{\cdot}} {{(\tau-x_0)}} {{\cdot G_1}}, {{G_2}}) = e([{{p(\tau)}} - {{y_0}}] {{\cdot G_1}}, {{G_2}})",
            color=PRIMARY_COLOR,
        ).to_edge(DOWN)
        self.verification3a = MathTex(
            r"{{e(}} {{q(\tau)}} {{\cdot}} {{(\tau-x_0)}} {{\cdot G_1}} , {{G_2)}} = {{e(}}[ {{p(\tau)}} - {{y_0}}] {{\cdot G_1}}, {{G_2}})",
            color=PRIMARY_COLOR,
        ).to_edge(DOWN)
        self.verification4 = MathTex(
            r"{{q(\tau)}} {{\cdot}} {{(\tau-x_0)}} = {{p(\tau)}} - {{y_0}}",
            color=PRIMARY_COLOR,
        ).to_edge(DOWN)
        self.verification5 = MathTex(
            r"q({{\tau}}) {{\cdot}} ({{\tau}}-x_0) = p({{\tau}}) - {{y_0}}",
            color=PRIMARY_COLOR,
        ).to_edge(DOWN)

        self.polynomial.to_edge(LEFT + DOWN).scale(0.8)
        self.proof.next_to(self.verifier_label, DOWN)
        self.definition2.next_to(self.title, DOWN, buff = 1.0)
        self.commitment.next_to(self.commiter, RIGHT, buff = 0)
        self.opening = MathTex(r"p(x_0)=y_0", font_size=32, color = SECONDARY_COLOR).next_to(self.commitment, DOWN)
        self.thumb_up = ImageMobject("data/images/Thumb_up.png").scale(0.2).next_to(self.opening, LEFT, buff = 0.3)
        self.opening2 = MathTex(r"{{q(x)}} {{}} {{}} = {{\frac{p(x)- y}{x-x_0} }}", color = PRIMARY_COLOR)
        self.equation.next_to(self.commitment, DOWN)
        self.opening2.next_to(self.commitment, DOWN)
        self.equation2.next_to(self.commitment, DOWN)
        self.verification.to_edge(DOWN).shift(UP*0.5)
        self.verification0a.to_edge(DOWN).shift(UP*0.5)
        self.verification0b.to_edge(DOWN).shift(UP*0.5)
        self.verification1.to_edge(DOWN).shift(UP*0.5)
        self.verification2.to_edge(DOWN).shift(UP*0.5)
        self.verification2a.to_edge(DOWN).shift(UP*0.5)
        self.verification3.to_edge(DOWN).shift(UP*0.5)
        self.verification3a.to_edge(DOWN).shift(UP*0.5)
        self.verification4.to_edge(DOWN).shift(UP*0.5)
        self.verification5.to_edge(DOWN).shift(UP*0.5)
        self.chart.next_to(self.commiter_label, DOWN, buff = -1).scale(0.4)
        self.envelope_body_closed = Polygon(
            [-3, -1, 0], [3, -1, 0], [3, 1, 0], [-3, 1, 0],
            fill_color=PRIMARY_COLOR, fill_opacity=0.5
        ).scale(0.4)

        self.envelope_flap_closed = Polygon(
            [-3, 1, 0], [3, 1, 0], [0, -0.6, 0],
            fill_color=HIGHLIGHT_COLOR, fill_opacity=0.5
        ).scale(0.39)

        self.envelope_body = Polygon(
            [-3, -1, 0], [3, -1, 0], [3, 1, 0], [-3, 1, 0],
            fill_color=PRIMARY_COLOR, fill_opacity=0.5
        ).scale(0.4)
        self.envelope_flap = Polygon(
            [-3, 1, 0], [3, 1, 0], [0, 3, 0], 
            fill_color=HIGHLIGHT_COLOR, fill_opacity=0.5
        ).scale(0.395)
        self.envelope_body.next_to(self.commiter, RIGHT+DOWN, buff = 0.4)
        self.envelope_body_closed.next_to(self.commiter, RIGHT+DOWN, buff = 0.4)

        self.envelope_flap.next_to(self.envelope_body, UP, buff= 0)
        self.envelope_flap_closed.next_to(self.envelope_body_closed, UP, buff = -0.63)
        self.lock = ImageMobject("data/images/Locked@2x.png").scale(0.2)

        self.final_verification = MathTex(r"{{p(x_0)}} = {{y_0}} {{}}", color = PRIMARY_COLOR).shift(UP*2)
        self.final_verification2 = MathTex(r"{{}} {{}} {{p(x_0)}} - {{y_0}} = {{0}}", color = PRIMARY_COLOR).shift(UP*1)
        self.final_verification3 = MathTex(r"{{q(x)}} \cdot {{(x-x_0)}} = {{p(x)}} - {{y_0}}", color = PRIMARY_COLOR)
        self.arrow = Arrow(self.final_verification3.get_bottom(), self.verification4.get_top(), color = HIGHLIGHT_COLOR, tip_shape=StealthTip)

    def animate_in(self, scene):
        self.new_subsection(scene, "one last time", "data/sound/e4/slide4-2a.mp3")
        scene.play(Write(self.title), run_time=2)

        self.new_subsection(scene, "committer", "data/sound/e4/slide4-2b.mp3")
        scene.play(FadeIn(self.commiter), Write(self.commiter_label), run_time=0.6)
        self.chart.gen_points()
        self.lock.next_to(self.chart, RIGHT, buff = 0).shift(UP)
        scene.play(Create(self.chart), FadeIn(self.lock), run_time=1.3)
        scene.play(FadeIn(self.verifier), Write(self.verifier_label), run_rime=0.6)

        scene.play(FadeIn(self.envelope_body_closed, self.envelope_flap_closed))
        scene.play(FadeOut(self.envelope_flap_closed), FadeIn(self.envelope_flap))
        self.dots = VGroup(*self.chart.dots).copy()
        self.commitment.generate_target()
        self.commitment.target.move_to(self.envelope_body_closed.get_center())

        scene.play(TransformMatchingShapes(VGroup(self.dots.scale(0.7)), self.envelope_flap_closed), FadeOut(self.envelope_flap), MoveToTarget(self.commitment), run_time=2)
        commitment_sent = VGroup(self.envelope_body_closed, self.envelope_flap_closed, self.commitment)
        commitment_sent.generate_target()
        commitment_sent.target.shift(6.5*RIGHT+DOWN*2)
        self.envelope_flap.shift(6.5*RIGHT+DOWN*2)

        scene.play(MoveToTarget(commitment_sent), run_time=1)

        self.new_subsection(scene, "verfier", "data/sound/e4/slide4-2c.mp3")
        speech_text_verifier = Tex(r"$p(x_0) = \ ?$", font_size=32, color = SECONDARY_COLOR)
        bubble_verifier = RoundedRectangle(corner_radius=0.5, width=speech_text_verifier.width + 1, height=speech_text_verifier.height + 1.2, color = SECONDARY_COLOR).next_to(self.verifier, DOWN+LEFT, buff = -1).shift(1.3*LEFT+DOWN*0.5)
        bubble_verifier.shift(UP) 
        speech_text_verifier.move_to(bubble_verifier.get_center())
        tail_verifier = Polygon(
            [0, 0, 0], 
            [0, -0.9, 0], 
            [0.78, 0.1, 0], 
            color=SECONDARY_COLOR,
            fill_opacity=0.4
        ).next_to(bubble_verifier, RIGHT, buff=-0.8).scale(0.4).shift(0.58*RIGHT)

        scene.play(Create(bubble_verifier), Create(tail_verifier))
        scene.play(Create(speech_text_verifier))

        self.new_subsection(scene, "one last time", "data/sound/e4/slide4-2d.mp3")
        scene.play(FadeOut(bubble_verifier, speech_text_verifier, tail_verifier))
        self.proof = MathTex(r"{{\pi}} = {{q(\tau)}} {{\cdot G_1}}", font_size=32, color = PRIMARY_COLOR)
        bubble_opening = RoundedRectangle(corner_radius=0.5, width=self.opening.width + 0.7, height=self.opening.height + 1.5, color = PRIMARY_COLOR).next_to(self.commiter, RIGHT, buff = -0.3).shift(RIGHT*0.7+DOWN*0.5)
        tail = Polygon(
            [0, 0.03, 0], 
            [-0.9, 0.2, 0], 
            [0, -1, 0], 
            color=PRIMARY_COLOR,
            fill_opacity=0.4
        ).next_to(bubble_opening, LEFT, buff=-0.8).scale(0.4).shift(LEFT*0.54)

        self.opening.move_to(bubble_opening.get_center())
        self.opening.shift(UP*0.3)
        self.proof.next_to(self.opening, DOWN, buff = 0.3)
        scene.play(Create(bubble_opening), Create(tail))
        scene.play(FadeIn(self.opening, self.proof))
        scene.wait(0.7)
        scene.play(Indicate(self.proof, color = HIGHLIGHT_COLOR))
        scene.play(Indicate(self.proof[2], color = HIGHLIGHT_COLOR))
        scene.play(FadeOut(self.envelope_body_closed, self.envelope_flap_closed))
        self.chart.generate_target()
        self.chart.target.scale(0.6).shift(UP*0.7)
        self.lock.generate_target()
        self.lock.target.scale(0.6).shift(UP*0.4+LEFT*0.4)
        scene.play(MoveToTarget(self.chart), MoveToTarget(self.lock))

        self.commitment.generate_target()
        self.commitment.target.next_to(self.verifier_label, DOWN)
        self.opening.generate_target()
        self.opening.target.next_to(self.verifier_label, DOWN).shift(DOWN*0.7)
        self.proof.generate_target()
        self.proof.target.next_to(self.verifier_label, DOWN).shift(DOWN*1.4)
        scene.play(MoveToTarget(self.opening), MoveToTarget(self.proof), MoveToTarget(self.commitment), FadeOut(bubble_opening, tail))

        self.new_subsection(scene, "we use eqn", "data/sound/e4/slide4-2.mp3")
        scene.play(Write(self.verification))
        scene.wait(2.5)
        scene.play(Indicate(self.proof, color = SECONDARY_COLOR), Indicate(self.verification[1], color = SECONDARY_COLOR), run_time=1)
        scene.play(Indicate(self.opening, color = HIGHLIGHT_COLOR), Indicate(self.verification[9], color = HIGHLIGHT_COLOR), Indicate(self.verification[3], color = HIGHLIGHT_COLOR), run_time=1)
        scene.play(Indicate(self.commitment, color = SECONDARY_COLOR), Indicate(self.verification[7], color = SECONDARY_COLOR), run_time=1)

        self.new_subsection(scene, "LHS", "data/sound/e4/slide4-3.mp3")
        scene.wait(1.5)
        scene.play(Indicate(self.verification[1], color = SECONDARY_COLOR))
        scene.wait(1)
        scene.play(Indicate(self.verification[3], color = SECONDARY_COLOR))
        scene.wait(2.3)
        scene.play(Indicate(self.verification[5], color = SECONDARY_COLOR))
        scene.wait(1.5)

        self.new_subsection(scene, "how the prover knows LHS", "data/sound/e4/slide4-3a.mp3")
        scene.wait(1)
        scene.play(TransformMatchingShapes(self.verification, self.verification0a), run_time=1.2)
        scene.wait(0.5)
        scene.play(Indicate(self.verification0a[3], color = HIGHLIGHT_COLOR), Indicate(self.verification0a[7], color = HIGHLIGHT_COLOR), run_time=0.8)
        scene.wait(3.8)

        scene.play(Indicate(self.verification0a[5], color = HIGHLIGHT_COLOR), run_time=0.8)
        scene.play(Indicate(self.opening, color = HIGHLIGHT_COLOR))
        scene.play(TransformMatchingShapes(self.verification0a, self.verification))

        self.new_subsection(scene, "RHS", "data/sound/e4/slide4-4.mp3")
        scene.wait(4)
        scene.play(Indicate(self.verification[7], color = SECONDARY_COLOR))
        scene.wait(0.8)
        scene.play(Indicate(self.verification[9], color = SECONDARY_COLOR))

        scene.play(Indicate(self.verification[11], color = SECONDARY_COLOR))
        scene.wait(2)

        self.new_subsection(scene, "why the equation?", "data/sound/e4/slide4-4a.mp3")
        scene.play(TransformMatchingShapes(self.verification, self.verification0b))

        self.new_subsection(scene, "commitment and pi", "data/sound/e4/slide4-5.mp3")

        scene.play(FadeOut(self.verification0b[0], self.verification0b[1], self.verification0b[2], self.verification0b[3], self.verification0b[4], self.verification0b[5], self.verification0b[6], self.verification0b[10], self.verification0b[11], self.verification0b[12], self.verification0b[13], self.verification0b[14], self.verification0b[15]), TransformMatchingShapes(VGroup(self.commitment[2].copy(), self.commitment[3].copy(), self.commitment[4].copy(), self.verification0b[9], self.verification0b[8], self.verification0b[7]), VGroup(self.verification1[8], self.verification1[9], self.verification1[10], self.verification1[7])), FadeIn(self.verification1[0], self.verification1[1], self.verification1[2], self.verification1[3], self.verification1[4], self.verification1[5], self.verification1[6], self.verification1[11], self.verification1[12], self.verification1[13], self.verification1[14], self.verification1[15], self.verification1[16]), run_time=2)
        # scene.play(TransformMatchingShapes(VGroup(self.commitment[2].copy(), self.commitment[3].copy(), self.commitment[4].copy(), self.verification0b), self.verification1), run_time=2)
        scene.wait(1)
        scene.play(FadeOut(self.verification1[1], self.verification1[0], self.verification1[3], self.verification1[4], self.verification1[5], self.verification1[6], self.verification1[7], self.verification1[8], self.verification1[9], self.verification1[10], self.verification1[11], self.verification1[12], self.verification1[13], self.verification1[14], self.verification1[15], self.verification1[16]), TransformMatchingShapes(VGroup(self.proof[2].copy(), self.proof[3].copy(), self.proof[4].copy(), self.verification1[2]), VGroup(self.verification2[1], self.verification2[2])), FadeIn(self.verification2[0], self.verification2[3], self.verification2[4], self.verification2[5], self.verification2[6], self.verification2[7], self.verification2[8], self.verification2[9], self.verification2[10], self.verification2[11], self.verification2[12], self.verification2[13], self.verification2[14], self.verification2[15], self.verification2[16]), run_time=2)
        scene.wait(1.5)

        self.new_subsection(scene, "bilinear", "data/sound/e4/slide4-6.mp3")
        scene.play(TransformMatchingShapes(self.verification2, self.verification2a))
        scene.wait(2)
        scene.play(TransformMatchingTex(self.verification2a, self.verification3), run_time=1.8)
        scene.wait(2)
        scene.play(TransformMatchingShapes(self.verification3, self.verification3a))

        self.new_subsection(scene, "verificaion", "data/sound/e4/slide4-7.mp3")
        scene.play(TransformMatchingShapes(self.verification3a, self.verification4))
        scene.wait(1)
        scene.play(Write(self.final_verification))
        scene.wait(1)
        scene.play(TransformMatchingShapes(self.final_verification.copy(), self.final_verification2))
        scene.wait(2.6)
        scene.play(Write(self.final_verification3))
        scene.wait(1)


        self.new_subsection(scene, "verificaion", "data/sound/e4/slide4-8.mp3")
        scene.wait(2)
        scene.play(TransformMatchingShapes(self.verification4, self.verification5))
        scene.wait(1.5)
        scene.play(Create(self.arrow), Indicate(self.verification5[1], color = HIGHLIGHT_COLOR), Indicate(self.verification5[5], color = HIGHLIGHT_COLOR), Indicate(self.verification5[7], color = HIGHLIGHT_COLOR))
        scene.wait(0.5)
        scene.play(TransformMatchingShapes(self.verification5, self.verification4))
        scene.play(Indicate(self.verification4[0], color = HIGHLIGHT_COLOR), Indicate(self.final_verification3[0], color = HIGHLIGHT_COLOR))
        scene.play(Indicate(self.verification4[4], color = HIGHLIGHT_COLOR), Indicate(self.final_verification3[2], color = HIGHLIGHT_COLOR))
        scene.play(Indicate(self.verification4[6], color = HIGHLIGHT_COLOR), Indicate(self.final_verification3[4], color = HIGHLIGHT_COLOR))
        scene.play(Indicate(self.verification4[8], color = HIGHLIGHT_COLOR), Indicate(self.final_verification3[4], color = HIGHLIGHT_COLOR))


    def animate_out(self, scene):
        scene.play(FadeOut(self.commitment, self.lock, self.opening, self.chart, self.commiter, self.commiter_label, self.verifier, self.verifier_label, self.title, self.proof, self.verification4, self.final_verification3, self.arrow, self.final_verification, self.final_verification2))