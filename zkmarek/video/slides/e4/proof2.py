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
    MoveToTarget
)

from zkmarek.crypto.field_element import FieldElement
from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR, HIGHLIGHT_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.e4.discreete_polynomial_chart import (
    DiscreetePolynomialChart,
)


def poly(x):
    return x * x * x - x * x * 2 + x * 3 + 7


class Proof2(SlideBase):
    chart: DiscreetePolynomialChart
    polynomial: MathTex
    equation: MathTex
    commitment: MathTex
    proof: MathTex
    verification: MathTex

    def __init__(self):
        super().__init__("Proof2")

    def construct(self):
        self.chart = DiscreetePolynomialChart(41, poly)

        self.definition2 = MathTex(r"e({{G_1}}, {{G_2}}) \rightarrow {{G_T}}", color=PRIMARY_COLOR)
        self.polynomial = MathTex("p(x) = x^3 - 2x^2 + 3x + 4", color=PRIMARY_COLOR)
        self.equation = MathTex(r"{{q(\tau)}}({{\tau}} - {{z}}) = {{p(\tau)}} - {{y}}", color=PRIMARY_COLOR)
        self.equation2 = MathTex(r"{{q(\tau)}}({{x}} - {{z}}) = {{p(x)}} - {{y}}", color=PRIMARY_COLOR)
        self.commitment = MathTex(r"{{C}} = {{ p(\tau)}} \cdot {{G_1}}", color=PRIMARY_COLOR)
        self.proof = MathTex(r"{{\pi}} = {{q(\tau)}} \cdot {{G_1}}", color=PRIMARY_COLOR)
        self.verification = MathTex(
            r"e( {{\pi}}, {{(\tau-z)}} {{\cdot G_2}}) ) = e({{C}} - {{y}} {{\cdot G_1}}, {{G_2}})",
            color=PRIMARY_COLOR,
        )
        self.verification2 = MathTex(
            r"e( {{q(\tau)\cdot G_1}}, ({{\tau-z}}) \cdot G_2) ) = e({{p(\tau)\cdot G_1}} - y \cdot G_1, G_2)",
            color=PRIMARY_COLOR,
        ).to_edge(DOWN)
        self.verification3 = MathTex(
            r"e({{q(\tau) \cdot (\tau-z) \cdot G_1}}, G_2) = e({{[p(\tau) -y]\cdot G_1}}, G_2)",
            color=PRIMARY_COLOR,
        ).to_edge(DOWN)
        self.verification4 = MathTex(
            r"q(\tau)\cdot (\tau-z) = p(\tau) -y",
            color=PRIMARY_COLOR,
        ).to_edge(DOWN)

        self.chart.to_edge(LEFT)
        self.polynomial.to_edge(LEFT + DOWN).scale(0.8)
        self.proof.to_edge(UP + RIGHT).shift(LEFT*2)
        self.definition2.to_edge(UP + RIGHT).shift(LEFT+DOWN)
        self.commitment.next_to(self.proof, DOWN)
        self.equation.next_to(self.commitment, DOWN)
        self.equation2.next_to(self.commitment, DOWN)
        self.verification.to_edge(DOWN)

        self.tau = FieldElement(33, 41)
        self.value_at_tau = poly(self.tau)
        self.z = FieldElement(13, 41)
        self.y = poly(self.z)

    def animate_in(self, scene):
        self.new_subsection(
            scene, "pairings", "data/sound/e4/slide4-0.mp3"
        )
        self.chart.gen_points()
        scene.play(FadeIn(self.chart))
        scene.wait(2)
        scene.play(FadeIn(self.definition2))
        scene.wait(4.7)
        scene.play(Indicate(self.definition2[1], color = SECONDARY_COLOR))
        scene.wait(1)
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
        scene.wait(1)
        scene.play(Indicate(self.commitment[4], color = HIGHLIGHT_COLOR))

        self.new_subsection(scene, "we use eqn", "data/sound/e4/slide4-2.mp3")
        self.chart.generate_target()
        self.chart.target.scale(0.8)
        scene.play(Write(self.verification), MoveToTarget(self.chart))
        scene.play(Write(self.equation2))


        self.new_subsection(scene, "LHS", "data/sound/e4/slide4-3.mp3")
        scene.play(TransformMatchingShapes(self.equation2, self.equation))
        scene.wait(1)
        scene.play(Indicate(self.verification[1], color = SECONDARY_COLOR))
        scene.wait(1)
        scene.play(Indicate(self.verification[3], color = SECONDARY_COLOR))
        scene.wait(2)
        scene.play(Indicate(self.verification[5], color = SECONDARY_COLOR))

        self.chart.add_xaxis_label(self.tau.value, r"\tau")
        line_tau = self.chart.animate_create_vertical_line(
            scene, self.tau.value, self.value_at_tau.value
        )
        line_tau_y = self.chart.animate_create_vertical_line(
            scene, self.tau.value, self.value_at_tau.value - self.y.value
        )

        self.chart.add_xaxis_label(self.z.value, r"z")
        line_z = self.chart.animate_create_vertical_line(
            scene, self.z.value, self.y.value
        )
        self.new_subsection(scene, "RHS", "data/sound/e4/slide4-4.mp3")
        self.chart.add(line_tau_y)
        self.chart.add(line_z)

        self.chart.animate_shift_dots(scene, self.y.value)
        self.chart.animate_shift_dots_wrap_fix(scene, self.y.value)
        scene.play(FadeOut(line_z, line_tau, line_tau_y))

        scene.play(Indicate(self.verification[7], color = SECONDARY_COLOR))
        scene.play(Indicate(self.verification[9], color = SECONDARY_COLOR))

        scene.play(Indicate(self.verification[11], color = SECONDARY_COLOR))

        self.new_subsection(scene, "commitment and pi", "data/sound/e4/slide4-5.mp3")

        scene.play(TransformMatchingShapes(VGroup(self.proof.copy(), self.verification, self.commitment.copy()), self.verification2), run_time=2)

        self.new_subsection(scene, "commitment and pi", "data/sound/e4/slide4-6.mp3")
        scene.wait(2)
        scene.play(TransformMatchingShapes(self.verification2, self.verification3))
        scene.wait(2)
        scene.play(TransformMatchingShapes(self.verification3, self.verification4))
        scene.wait(4)