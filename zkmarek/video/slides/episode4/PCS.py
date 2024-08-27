from manim import (
    DOWN,
    LEFT,
    UP,
    RIGHT,
    FadeIn,
    FadeOut,
    MathTex,
    Write,
    VGroup,
    ReplacementTransform,
    Indicate,
    MoveToTarget,
    Text,
)

from zkmarek.video.constant import (
    PRIMARY_COLOR,
    HIGHLIGHT_COLOR,
    SECONDARY_COLOR,
    PRIMARY_FONT,
)
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.e4.discreete_polynomial_chart import (
    DiscreetePolynomialChart,
)


def poly(x):
    return x * x * x - x * x * 2 + x * 3 + 4


class PolynomialCommitment(SlideBase):
    chart: DiscreetePolynomialChart
    polynomial: MathTex
    equation: MathTex
    commitment: MathTex
    proof: MathTex
    verification: MathTex

    def __init__(self):
        super().__init__("Polynomial Commitment Scheme")

    def construct(self):
        self.title = Text(
            "Polynomial Commitment Scheme", color=PRIMARY_COLOR, font=PRIMARY_FONT
        ).to_edge(UP)
        self.chart = DiscreetePolynomialChart(41, poly).scale(0.85)
        self.chart.to_edge(LEFT)
        self.polynomial = MathTex(r"p(x) = \sum_{i=0}^n p_i x^i", color=PRIMARY_COLOR)
        self.polynomial2 = (
            MathTex(r"p(x) = p_n x^n + \cdots + p_1 x + p_0", color=PRIMARY_COLOR)
            .scale(0.9)
            .next_to(self.chart, RIGHT)
        )

        self.commitment = MathTex(
            r"C = P(\tau) \cdot G_1", color=HIGHLIGHT_COLOR
        ).next_to(self.polynomial2, DOWN)
        self.tau = self.commitment[0][4:5]

    def animate_in(self, scene):
        scene.play(FadeIn(self.title))
        self.new_subsection(scene, "intro KZG", "data/sound/episode4/slide10-0.mp3")
        scene.play(Write(self.polynomial))
        scene.wait(3)
        scene.play(Indicate(self.polynomial), color=SECONDARY_COLOR, run_time=0.5)
        scene.wait(1.5)
        self.polynomial.generate_target()
        self.polynomial.target.next_to(self.chart, RIGHT)
        scene.play(MoveToTarget(self.polynomial))
        scene.play(ReplacementTransform(self.polynomial, self.polynomial2))
        scene.wait(10)
        self.chart.gen_points()
        scene.play(FadeIn(self.chart))
        dots = VGroup(*self.chart.dots)
        scene.play(Indicate(dots, color=HIGHLIGHT_COLOR, scale=1.05))
        self.new_subsection(
            scene, "commiting poly", "data/sound/episode4/slide10-1.mp3"
        )
        self.new_subsection(scene, "commitment", "data/sound/episode4/slide10-2.mp3")
        scene.wait(3)
        scene.play(FadeIn(self.commitment))
        scene.wait(2)
        scene.play(Indicate(self.tau), color=SECONDARY_COLOR)
        scene.wait(4)
        self.play_sound(scene, "data/sound/episode4/slide10-3.mp3")
        scene.wait(1)
        scene.play(Indicate(self.tau), color=SECONDARY_COLOR)
        scene.wait(3.5)
        self.new_subsection(scene, "quotient", "data/sound/episode4/slide10-4.mp3")

    def animate_out(self, scene):
        scene.play(
            FadeOut(self.polynomial2), FadeOut(self.commitment), FadeOut(self.chart)
        )
