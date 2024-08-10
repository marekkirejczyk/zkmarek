from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    FadeIn,
    MathTex,
    Indicate,
    TransformMatchingShapes,
    Write,
    Text
)

from zkmarek.crypto.field_element import FieldElement
from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR, PRIMARY_FONT
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.episode4.discreete_polynomial_chart import (
    DiscreetePolynomialChart,
)


def poly(x):
    return x * x * x - x * x * 2 + x * 3 + 4


class Proof1(SlideBase):
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
        self.polynomial = MathTex("p(x) = x^3 - 2x^2 + 3x + 4", color=PRIMARY_COLOR)
        self.equation = MathTex(r"{{q(\tau)}}({{\tau}} - {{z}}) = {{p(\tau)}} - {{y}}", color=PRIMARY_COLOR)

        self.opening = MathTex(r"p(z)=y", color = SECONDARY_COLOR, font_size=40)
        self.opening2 = MathTex(r"p(x) - y = 0", color = SECONDARY_COLOR, font_size=40)
        self.opening3 = MathTex(r"\frac{  p(x) - y }{x - z} = ...", color = SECONDARY_COLOR, font_size=40)
        self.opening4 = MathTex(r"\frac{p(x) - y}{x - z} = q(x)", color = SECONDARY_COLOR, font_size=40)
        self.opening5 = MathTex(r"p(x) - y = (x - z)\cdot q(x)", color = SECONDARY_COLOR, font_size=40)
        self.opening6 = MathTex(r"p(z) - y = (z - z)\cdot q(x)", color = SECONDARY_COLOR, font_size=40)
        self.opening7 = MathTex(r"0 = 0\cdot q(x)", color = SECONDARY_COLOR, font_size=40)

        self.not_infty = Text("If the quotient isn't infinity for z", font = PRIMARY_FONT, color = PRIMARY_COLOR).to_edge(DOWN)

        self.chart.to_edge(LEFT).scale(0.8)
        self.polynomial.to_edge(DOWN + LEFT).scale(0.8)
        self.equation.next_to(self.polynomial, DOWN)
        self.opening.to_edge(UP + RIGHT).shift(LEFT*2)
        self.opening2.next_to(self.opening, DOWN)
        self.opening3.next_to(self.opening, DOWN)
        self.opening4.next_to(self.opening, DOWN)
        self.opening5.next_to(self.opening, DOWN)
        self.opening6.next_to(self.opening, DOWN)
        self.opening7.next_to(self.opening, DOWN)

        self.tau = FieldElement(33, 41)
        self.value_at_tau = poly(self.tau)
        self.z = FieldElement(13, 41)
        self.y = poly(self.z)

    def animate_in(self, scene):
        self.new_subsection(
            scene, "polynomial", "data/sound/e4/slide3-0.mp3"
        )
        self.chart.gen_points()
        scene.play(FadeIn(self.chart))
        scene.play(FadeIn(self.polynomial))
        scene.wait(2)

        self.new_subsection(scene, "challange - w/o revealing p", "data/sound/e4/slide3-1.mp3")
        scene.play(FadeIn(self.opening))
        scene.play(Indicate(self.opening, color = SECONDARY_COLOR))

        self.chart.add_xaxis_label(self.z.value, r"z")

        self.new_subsection(scene, "divisibility", "data/sound/e4/slide3-2.mp3")
        scene.wait(2)
        scene.play(Write(self.opening2))
        scene.play(Indicate(self.opening))
        scene.wait(4.5)
        scene.play(TransformMatchingShapes(self.opening2, self.opening3))

        self.new_subsection(scene, "quotient", "data/sound/e4/slide3-3.mp3")
        scene.wait(2)
        # scene.play(Indicate(self.opening))

        self.new_subsection(scene, "can be divided", "data/sound/e4/slide3-4.mp3")
        scene.wait(4)
        scene.play(Indicate(self.opening3, color = PRIMARY_COLOR))
        scene.wait(1)
        # scene.play(Indicate(self.opening3[3], color = PRIMARY_COLOR))
        scene.play(TransformMatchingShapes(self.opening3, self.opening4))

        self.new_subsection(scene, "why is it crucial", "data/sound/e4/slide3-5.mp3")
        scene.wait(2)
        scene.play(TransformMatchingShapes(self.opening4, self.opening5))
        scene.wait(2)
        scene.play(TransformMatchingShapes(self.opening5, self.opening6))
        scene.wait(4)
        scene.play(TransformMatchingShapes(self.opening6, self.opening7))


