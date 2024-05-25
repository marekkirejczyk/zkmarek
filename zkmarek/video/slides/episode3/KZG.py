from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    FadeIn,
    FadeOut,
    MathTex,
    TransformMatchingTex,
    VGroup,
    ReplacementTransform,
)

from zkmarek.crypto.field_element import FieldElement
from zkmarek.video.constant import PRIMARY_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.episode3.discreete_polynomial_chart import (
    DiscreetePolynomialChart,
)


def poly(x):
    return x * x * x - x * x * 2 + x * 3 + 4


class KZG(SlideBase):
    chart: DiscreetePolynomialChart
    polynomial: MathTex
    equation: MathTex
    commitment: MathTex
    proof: MathTex
    verification: MathTex

    def __init__(self):
        super().__init__("KZG")

    def construct(self):
        self.chart = DiscreetePolynomialChart(41, poly)
        self.polynomial = MathTex("p(x) = x^3 - 2x^2 + 3x + 4", color=PRIMARY_COLOR)
        self.equation = MathTex(r"q(\tau)(\tau - z) = p(\tau) - y", color=PRIMARY_COLOR)
        self.commitment = MathTex(r"C = P(\tau) \cdot G_1", color=PRIMARY_COLOR)
        self.proof = MathTex(r"\pi = q(\tau) \cdot G_1", color=PRIMARY_COLOR)
        self.verification = MathTex(
            r"e( \pi, (\tau-z) \cdot G_2) ) = e(C - y \cdot G_1, G_2)",
            color=PRIMARY_COLOR,
        )
        self.verification2 = MathTex(
            r"e( q(\tau)\cdot G_1, (\tau-z) \cdot G_2) ) = e(P(\tau\cdot G_1) - y \cdot G_1, G_2)",
            color=PRIMARY_COLOR,
        ).to_edge(DOWN)
        self.verification3 = MathTex(
            r"q(\tau), (\tau-z) \cdot e(G_1, G_2) = (P(\tau -y)\cdot e(G_1, G_2)",
            color=PRIMARY_COLOR,
        ).to_edge(DOWN)
        self.verification4 = MathTex(
            r"q(\tau), (\tau-z) = P(\tau) -y",
            color=PRIMARY_COLOR,
        ).to_edge(DOWN)

        self.chart.to_edge(LEFT)
        self.polynomial.to_edge(RIGHT + UP)
        self.equation.next_to(self.polynomial, DOWN)
        self.commitment.next_to(self.equation, DOWN)
        self.proof.next_to(self.commitment, DOWN)
        self.verification.to_edge(DOWN)

        self.tau = FieldElement(33, 41)
        self.value_at_tau = poly(self.tau)
        self.z = FieldElement(13, 41)
        self.y = poly(self.z)

    def animate_in(self, scene):
        self.new_subsection(
            scene, "verify the proof", "data/sound/episode4/slide11-0.mp3"
        )
        self.chart.gen_points()
        scene.play(FadeIn(self.chart))
        scene.play(FadeIn(self.polynomial))

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
        self.play_sound(scene, "data/sound/episode4/slide11-1.mp3")
        scene.play(FadeIn(self.equation))
        self.chart.add(line_tau_y)

        self.chart.animate_shift_dots(scene, self.y.value)
        self.chart.animate_shift_dots_wrap_fix(scene, self.y.value)
        scene.play(FadeOut(line_z))
        scene.play(FadeOut(line_tau))
        self.new_subsection(scene, "equation", "data/sound/episode4/slide11-2.mp3")
        scene.play(self.chart.animate.scale(0.9))
        scene.play(self.chart.animate.to_edge(UP))
        scene.play(FadeIn(self.verification))

        scene.play(FadeIn(self.commitment))
        scene.play(FadeIn(self.proof))

        self.new_subsection(scene, "verify proof", "data/sound/episode4/slide11-3.mp3")
        scene.play(
            TransformMatchingTex(
                VGroup(self.verification, self.proof.copy()), self.verification2
            )
        )
        scene.play(
            TransformMatchingTex(
                VGroup(self.verification2, self.commitment.copy()), self.verification3
            )
        )
        scene.play(ReplacementTransform(self.verification3, self.verification4))
