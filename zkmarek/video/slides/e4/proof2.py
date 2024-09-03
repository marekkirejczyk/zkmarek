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
    Brace,
    Create,
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
        super().__init__("Proof2")

    def construct(self):
        self.title = Text("Proof", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 40).to_edge(UP)
        self.verifier = ImageMobject("data/images/person.png").to_corner(RIGHT+UP).scale(0.6).shift(LEFT)
        self.commiter = ImageMobject("data/images/person_blue.png").to_corner(LEFT+UP).scale(0.6).shift(RIGHT)

        self.commiter_label = Text("Committer", color = PRIMARY_COLOR, font=PRIMARY_FONT).scale(0.6).next_to(self.commiter, DOWN, buff = 0.4)
        self.verifier_label = Text("Verifier", color = PRIMARY_COLOR, font=PRIMARY_FONT).scale(0.6).next_to(self.verifier, DOWN, buff = 0.4)

        self.chart = DiscreetePolynomialChart(41, poly)

        self.definition2 = MathTex(r"e({{G_1}}, {{G_2}}) \rightarrow {{G_T}}", color=PRIMARY_COLOR)
        self.polynomial = MathTex("p(x) = x^3 - 2x^2 + 3x + 4", color=PRIMARY_COLOR)
        self.equation = MathTex(r"{{q(\tau)}}\cdot {{(\tau - x_0)}} = {{p(\tau)}} - {{y}}", color=PRIMARY_COLOR)
        self.equation2 = MathTex(r"{{q(x)}}\cdot {{(x - x_0)}} = {{p(x)}} - {{y}}", color=PRIMARY_COLOR)
        self.commitment = MathTex(r"{{C}} = {{ p(\tau)}} \cdot {{G_1}}", color=PRIMARY_COLOR)
        self.proof = MathTex(r"{{\pi}} = {{q(\tau)}} \cdot {{G_1}}", color=PRIMARY_COLOR)
        self.brace1 = Brace(self.commitment, color=PRIMARY_COLOR, direction=LEFT)

        self.brace1.scale(2)
        self.brace1_label = Text("elliptic curve points", font_size=20, color=PRIMARY_COLOR, font = PRIMARY_FONT)
        self.brace1.put_at_tip(self.brace1_label)

        self.opening = MathTex(r"p(x_0)=y", color = PRIMARY_COLOR).next_to(self.commitment, DOWN, buff = 1.0)
        self.thumb_up = ImageMobject("data/images/Thumb_up.png").scale(0.2).next_to(self.opening, LEFT, buff = -0.8)
        self.opening2 = MathTex(r"{{q(x)}} {{}} {{}} = {{\frac{p(x)- y}{x-x_0} }}", color = PRIMARY_COLOR)

        self.verification = MathTex(
            r"e( {{\pi}}, {{(\tau-x_0)}} {{\cdot G_2}}) ) = e({{C}} - {{y}} {{\cdot G_1}}, {{G_2}})",
            color=PRIMARY_COLOR,
        )
        self.verification0a = MathTex(
            r"e( {{\pi}}, {{\tau\cdot G_2}} {{-x_0 \cdot G_2}} ) = e({{C}} - {{y}} {{\cdot G_1}}, {{G_2}})",
            color=PRIMARY_COLOR,
        )
        self.verification1 = MathTex(
            r"e( {{q(\tau)}}{{\cdot G_1}}, {{(\tau-x_0)}} {{\cdot G_2}}) ) = e({{C}} - {{y}} {{\cdot G_1}}, {{G_2}})",
            color=PRIMARY_COLOR,
        )

        self.verification2 = MathTex(
            r"e( {{q(\tau)}}{{\cdot G_1}}, ({{\tau-x_0}}) \cdot G_2) ) = e({{p(\tau)\cdot G_1}} - y \cdot G_1, G_2)",
            color=PRIMARY_COLOR,
        ).to_edge(DOWN)
        self.verification2a = MathTex(
            r"e( {{q(\tau)\cdot G_1, (\tau-x_0) \cdot G_2) ) = e(}} {{p(\tau)\cdot G_1}} - y \cdot G_1, G_2)",
            color = PRIMARY_COLOR
        ).to_edge(DOWN)
        self.verification3 = MathTex(
            r"e({{q(\tau)}} \cdot (\tau-x_0) {{\cdot G_1}}, G_2) = e({{[p(\tau) -y]\cdot G_1}}, G_2)",
            color=PRIMARY_COLOR,
        ).to_edge(DOWN)
        self.verification4 = MathTex(
            r"q(\tau)\cdot (\tau-x_0) = p(\tau) -y",
            color=PRIMARY_COLOR,
        ).to_edge(DOWN)

        self.polynomial.to_edge(LEFT + DOWN).scale(0.8)
        self.proof.next_to(self.verifier_label, DOWN)
        self.definition2.next_to(self.title, DOWN, buff = 1.0)
        self.commitment.next_to(self.proof, DOWN)
        self.equation.next_to(self.commitment, DOWN)
        self.opening2.next_to(self.commitment, DOWN)
        self.opening.next_to(self.commitment, DOWN)
        self.equation2.next_to(self.commitment, DOWN)
        self.verification.to_edge(DOWN).shift(UP*0.5)
        self.verification0a.to_edge(DOWN).shift(UP*0.5)
        self.verification1.to_edge(DOWN).shift(UP*0.5)
        self.verification2.to_edge(DOWN).shift(UP*0.5)
        self.verification2a.to_edge(DOWN).shift(UP*0.5)
        self.verification3.to_edge(DOWN).shift(UP*0.5)
        self.verification4.to_edge(DOWN).shift(UP*0.5)
        self.chart.next_to(self.commiter_label, DOWN, buff = -0.4).scale(0.3)

    def animate_in(self, scene):
        self.new_subsection(
            scene, "pairings", "data/sound/e4/slide4-0.mp3"
        )
        scene.play(Write(self.title), run_time=1.5)
        scene.wait(0.5)
        scene.play(FadeIn(self.definition2))
        scene.play(FadeIn(self.commiter, self.verifier), run_time=2)
        scene.play(Write(self.verifier_label), Write(self.commiter_label), run_time=2)
        scene.wait(1.9)
        scene.play(Indicate(self.definition2[1], color = SECONDARY_COLOR))
        scene.wait(1.3)
        scene.play(Indicate(self.definition2[3], color = SECONDARY_COLOR))

        self.new_subsection(scene, "pi - proof", "data/sound/e4/slide4-1.mp3")
        scene.play(FadeOut(self.definition2))
        scene.play(Write(self.proof))
        scene.wait(2)
        scene.play(Indicate(self.proof[2], color = HIGHLIGHT_COLOR))
        scene.wait(1)
        scene.play(Indicate(self.proof[4], color = HIGHLIGHT_COLOR))
        scene.wait(1)
        scene.play(Write(self.commitment))
        scene.wait(1)
        scene.play(Indicate(self.commitment[2], color = HIGHLIGHT_COLOR))
        scene.wait(0.5)
        scene.play(Indicate(self.commitment[4], color = HIGHLIGHT_COLOR))

        self.new_subsection(scene, "is opening correct?", "data/sound/e4/slide4-1a.mp3")
        self.chart.gen_points()
        scene.play(Create(self.chart), run_time=1)
        scene.play(Write(self.opening), run_time=1)
        scene.wait(0.4)
        scene.play(FadeIn(self.thumb_up), run_time=0.6)
        scene.wait(1.4)

        self.new_subsection(scene, "verify if p is divisible", "data/sound/e4/slide4-1b.mp3")
        scene.wait(1)
        scene.play(FadeOut(self.thumb_up), run_time=0.7)
        scene.wait(0.8)
        scene.play(TransformMatchingShapes(self.opening, self.opening2), run_time=1.5)
        scene.wait(2)
        scene.play(TransformMatchingShapes(self.opening2, self.equation2), run_time=1.5)

        self.new_subsection(scene, "true for tau", "data/sound/e4/slide4-1c.mp3")
        scene.wait(1)
        scene.play(TransformMatchingShapes(self.equation2, self.equation), run_time=1.5)

        self.new_subsection(scene, "we use eqn", "data/sound/e4/slide4-2.mp3")

        scene.play(Write(self.verification))
        scene.wait(2)

        self.new_subsection(scene, "LHS", "data/sound/e4/slide4-3.mp3")
        scene.wait(1.5)
        scene.play(Indicate(self.verification[1], color = SECONDARY_COLOR))
        scene.wait(1)
        scene.play(Indicate(self.verification[3], color = SECONDARY_COLOR))

        scene.play(Indicate(self.verification[5], color = SECONDARY_COLOR))


        self.new_subsection(scene, "how the prover knows LHS", "data/sound/e4/slide4-3a.mp3")
        scene.wait(1)
        scene.play(TransformMatchingShapes(self.verification, self.verification0a), run_time=1.2)
        scene.wait(0.5)
        scene.play(Indicate(self.verification0a[3], color = HIGHLIGHT_COLOR), run_time=0.8)
        scene.wait(2.5)

        scene.play(Indicate(self.verification0a[5], color = HIGHLIGHT_COLOR), run_time=0.8)
        scene.wait(2)
        scene.play(TransformMatchingShapes(self.verification0a, self.verification))

        self.new_subsection(scene, "RHS", "data/sound/e4/slide4-4.mp3")
        scene.wait(1.5)
        scene.play(Indicate(self.verification[7], color = SECONDARY_COLOR))
        scene.play(Indicate(self.verification[9], color = SECONDARY_COLOR))

        scene.play(Indicate(self.verification[11], color = SECONDARY_COLOR))

        self.new_subsection(scene, "commitment and pi", "data/sound/e4/slide4-5.mp3")

        scene.play(TransformMatchingTex(VGroup(self.proof.copy(), self.verification), self.verification1), run_time=2)
        scene.wait(1)
        scene.play(TransformMatchingTex(VGroup(self.commitment.copy(), self.verification1), self.verification2), run_time=2)
        

        self.new_subsection(scene, "commitment and pi", "data/sound/e4/slide4-6.mp3")
        scene.play(TransformMatchingShapes(self.verification2, self.verification2a), run_time=0.05)
        scene.wait(2)
        scene.play(TransformMatchingTex(self.verification2a, self.verification3))
        scene.wait(2)
        scene.play(TransformMatchingShapes(self.verification3, self.verification4))

        self.new_subsection(scene, "verificaion", "data/sound/e4/slide4-7.mp3")
        scene.wait(4)
        scene.play(Indicate(self.equation, color = HIGHLIGHT_COLOR), Indicate(self.verification4, color = HIGHLIGHT_COLOR))
        scene.wait(3)    

    def animate_out(self, scene):
        scene.play(FadeOut(self.commitment, self.commiter, self.commiter_label, self.verifier, self.verifier_label, self.title, self.chart, self.proof, self.equation, self.verification4))