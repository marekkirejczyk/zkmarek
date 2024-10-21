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
    FadeOut,
    VGroup,
    ImageMobject,
    Text,
)

from zkmarek.crypto.field_element import FieldElement
from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR, HIGHLIGHT_COLOR, HIGHLIGHT2_COLOR, PRIMARY_FONT

from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.e4.discreete_polynomial_chart import (
    DiscreetePolynomialChart,
)


def poly(x):
    return x * x * x - x * x * 2 + x * 3 + 7
def poly2(x):
    if isinstance(x, FieldElement):
        output = FieldElement(4, x.order) * x * x * x - FieldElement(8, x.order) * x * x  - FieldElement(17, x.order) * x + FieldElement(30, x.order)
    else:
        output = 4 * x * x * x - 8 * x * x * 2 - 17 * x + 30
    return output


class Proof1(SlideBase):
    chart: DiscreetePolynomialChart
    polynomial: MathTex
    verification: MathTex

    def __init__(self):
        super().__init__("Proof")

    def construct(self):
        self.chart = DiscreetePolynomialChart(41, poly)
        self.chart2 = DiscreetePolynomialChart(41, poly2)
        self.polynomial = MathTex("{{p(x)}} = {{x^3}} - {{2x^2}} + {{3x}} + {{4}}", color=PRIMARY_COLOR)
        self.r_of_x = MathTex("{{r(x)}} = {{p(x)}} - {{y_0}}", color=PRIMARY_COLOR)

        self.opening = MathTex(r"{{p(x_0)}} {{}} = {{y_0}}", color = PRIMARY_COLOR)
        self.opening2 = MathTex(r"{{}} {{p(x_0)}} {{- y_0}} = {{0}}", color = PRIMARY_COLOR)
        self.opening3 = MathTex(r"{{r(x)}}= {{p(x)}} {{- y_0}} {{}}", color = PRIMARY_COLOR)
        self.opening4 = MathTex(r"{{r(x_0)=}}{{p(x_0)}} {{- y_0}} {{=0}}", color = PRIMARY_COLOR)
        self.opening5 = MathTex(r"{{(x-x_0)}} {{(...)=}}{{p(x)}} {{- y_0}} {{}} ", color = PRIMARY_COLOR)
        self.opening6 = MathTex(r"{{(x-x_0)}} \cdot {{ q(x)}}={{p(x)}} {{- y_0}} {{}} ", color = PRIMARY_COLOR)
        self.opening7 = MathTex(r"{{}} {{q(x)=}}\frac{  p(x) - y_0 }{ (x-x_0) } {{}}", color = PRIMARY_COLOR)

        self.verifier = ImageMobject("data/images/person.png").to_corner(RIGHT+UP).scale(0.6).shift(LEFT)
        self.commiter = ImageMobject("data/images/person_blue.png").to_corner(LEFT+UP).scale(0.6).shift(RIGHT)

        self.commiter_label = Text("Committer", color = PRIMARY_COLOR, font=PRIMARY_FONT).scale(0.6).next_to(self.commiter, DOWN, buff = 0.4)
        self.verifier_label = Text("Verifier", color = PRIMARY_COLOR, font=PRIMARY_FONT).scale(0.6).next_to(self.verifier, DOWN, buff = 0.4)

        self.chart = DiscreetePolynomialChart(41, poly)

        self.chart.to_edge(LEFT).scale(0.8).shift(UP*0.5)
        self.chart2.to_edge(LEFT).scale(0.8).shift(UP*0.5)
        self.polynomial.to_edge(DOWN + LEFT).scale(0.8).shift(RIGHT)
        self.r_of_x.to_edge(DOWN + LEFT).scale(0.8).shift(RIGHT*2.3)
        self.opening.to_edge(RIGHT).shift(LEFT*2+UP*2)
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
        self.new_subsection(scene, "opening", "data/sound/e4/slide3-3.mp3")
        self.chart.gen_points()
        scene.play(FadeIn(self.chart))
        scene.play(FadeIn(self.polynomial))

        self.x_0_label = self.chart.add_xaxis_label(self.z.value, r"x_0")
        scene.wait(1)
        line_z = self.chart.animate_create_vertical_line(
            scene, self.z.value, self.y.value
        )
        self.chart.add(line_z)
        scene.wait(1)
        scene.play(Write(self.opening))
        scene.wait(2.5)
        scene.play(TransformMatchingShapes(self.opening.copy(), self.opening2), run_time=1.5)

        self.new_subsection(scene, "p(x)-y as polynomial", "data/sound/e4/slide3-4.mp3")
        scene.wait(1.5)
        scene.play(TransformMatchingShapes(self.opening2, self.opening3), run_time=1.5)
        scene.wait(1.2)
        scene.play(Indicate(self.opening3[0], color = HIGHLIGHT_COLOR))
        scene.wait(6.5)

        self.new_subsection(scene, "r(x) in a chart", "data/sound/e4/slide3-4a.mp3")

        scene.wait(3.5)
        self.dots = VGroup(*self.chart.dots)
        scene.play(Indicate(self.dots, color=HIGHLIGHT2_COLOR, scale=1.05))
        scene.wait(2)
        scene.play(Indicate(line_z, color = HIGHLIGHT2_COLOR), run_time=1)
        self.chart.animate_shift_dots_with_fade(scene, self.y.value)
        scene.play(FadeOut(line_z))
        self.chart.remove(line_z)
        
        self.new_subsection(scene, "modulo operation", "data/sound/e4/slide3-4b.mp3")
        scene.wait(3.2)
        self.chart.animate_shift_dots_wrap_fix(scene, self.y.value)
        scene.play(TransformMatchingShapes(self.polynomial, self.r_of_x))
        scene.wait(2.8)

        self.new_subsection(scene, "rewriting it with roots", "data/sound/e4/slide3-5.mp3")
        scene.wait(3.5)
        scene.play(TransformMatchingShapes(self.opening3, self.opening4), run_time=1.7)
        self.chart.indicate_xaxis_label(scene, self.x_0_label)

        scene.play(TransformMatchingShapes(self.opening4, self.opening5), run_time=1.5)
        scene.wait(2.2)
        scene.play(Indicate(self.opening5[5], color = HIGHLIGHT_COLOR))
        scene.wait(2.5)

        self.new_subsection(scene, "divisability will prove opening", "data/sound/e4/slide3-6.mp3")
        scene.wait(1.5)

        scene.play(Indicate(self.opening, color = HIGHLIGHT_COLOR), run_time=0.8)
        scene.play(TransformMatchingShapes(self.opening5, self.opening6), run_time=1.5)

        scene.wait(2)

        self.new_subsection(scene, "and this is quotient", "data/sound/e4/slide3-7.mp3")
        scene.wait(2)
        scene.play(Indicate(self.opening6[2], color = SECONDARY_COLOR))
        scene.play(TransformMatchingShapes(self.opening6, self.opening7))
        self.quotient_text = Text("quotient polynomial", color = SECONDARY_COLOR, font_size=20, font=PRIMARY_FONT).next_to(self.opening7, DOWN).shift(LEFT*0.1)
        scene.play(FadeIn(self.quotient_text), run_time=1)
        scene.wait(4.2)

        self.new_subsection(scene, "how quotient help us?", "data/sound/e4/slide3-8.mp3")
        scene.wait(8.5)

    def animate_out(self, scene):
        scene.play(FadeOut(self.chart, self.r_of_x, self.opening, self.quotient_text, self.opening7))