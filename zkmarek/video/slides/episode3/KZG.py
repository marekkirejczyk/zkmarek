
from manim import DOWN, LEFT, RIGHT, UP, FadeIn, FadeOut, MathTex

from zkmarek.crypto.field_element import FieldElement
from zkmarek.video.constant import PRIMARY_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.episode3.discreete_polynomial_chart import \
    DiscreetePolynomialChart


def poly(x):
    return x*x*x - x*x*2 + x*3 + 4

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
        self.verification = MathTex(r"e( \pi, (s-z) \cdot G_2) ) = e(C - y \cdot G_1, G_2)",
            color=PRIMARY_COLOR)

        self.chart.to_edge(LEFT)
        self.polynomial.to_edge(RIGHT + UP)
        self.equation.next_to(self. polynomial, DOWN)
        self.commitment.next_to(self.equation, DOWN)
        self.proof.next_to(self.commitment, DOWN)
        self.verification.to_edge(DOWN)

        self.tau = FieldElement(33, 41)
        self.value_at_tau = poly(self.tau)
        self.z = FieldElement(13, 41)
        self.y = poly(self.z)

    def animate_in(self, scene):
        self.chart.gen_points()
        scene.play(FadeIn(self.chart))
        scene.play(FadeIn(self.polynomial))

        self.chart.add_xaxis_label(self.tau.value, r"\tau")
        line_tau = self.chart.animate_create_vertical_line(scene, self.tau.value, self.value_at_tau.value)
        line_tau_y = self.chart.animate_create_vertical_line(scene, self.tau.value,
            self.value_at_tau.value-self.y.value)

        self.chart.add_xaxis_label(self.z.value, r"z")
        line_z = self.chart.animate_create_vertical_line(scene, self.z.value, self.y.value)
        self.chart.add(line_tau_y)

        self.chart.animate_shift_dots(scene, self.y.value)
        scene.play(FadeOut(line_z))
        scene.play(FadeOut(line_tau))
        self.chart.animate_shift_dots_wrap_fix(scene, self.y.value)

        scene.play(FadeIn(self.equation))
        scene.play(FadeIn(self.commitment))
        scene.play(FadeIn(self.proof))

        scene.play(self.chart.animate.scale(0.9))
        scene.play(self.chart.animate.to_edge(UP))

        scene.play(FadeIn(self.verification))
