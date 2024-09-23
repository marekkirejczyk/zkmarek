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
    Unwrite,
    FadeOut,
    VGroup,
    ImageMobject,
    Text,
    MoveToTarget,
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
    equation: MathTex
    commitment: MathTex
    proof: MathTex
    verification: MathTex

    def __init__(self):
        super().__init__("Proof2")

    def construct(self):
        self.chart = DiscreetePolynomialChart(41, poly)
        self.chart2 = DiscreetePolynomialChart(41, poly2)
        self.polynomial = MathTex("p(x) = x^3 - 2x^2 + 3x + 4", color=PRIMARY_COLOR)
        self.equation = MathTex(r"{{q(\tau)}}({{\tau}} - {{z}}) = {{p(\tau)}} - {{y_0}}", color=PRIMARY_COLOR)

        self.equality_quotient = MathTex(r"{{q(\tau)}} \stackrel{?}{=} {{p(\tau)}}", color = SECONDARY_COLOR).to_edge(RIGHT).shift(LEFT*2)
        self.commitment_quotient = MathTex(r"{{C}} = {{p(\tau)}}\cdot {{G_1}}", color = SECONDARY_COLOR).to_edge(RIGHT).shift(LEFT*2)
        self.commitment_quotient2 = MathTex(r"{{C}} \stackrel{?}{=} {{q(\tau)}}\cdot {{G_1}}", color = SECONDARY_COLOR).to_edge(RIGHT).shift(LEFT*2)

        self.opening = MathTex(r"{{p(x_0)}} {{}} = {{y_0}}", color = PRIMARY_COLOR)
        self.opening2 = MathTex(r"{{p(x_0)}} {{- y_0}} = {{0}}", color = PRIMARY_COLOR)
        self.opening3 = MathTex(r"{{p(x)}} {{- y_0}} = {{r(x)}} {{}}", color = PRIMARY_COLOR)
        self.opening4 = MathTex(r"{{p(x_0)}} {{- y_0}} = {{r(x_0)}} {{=0}}", color = PRIMARY_COLOR)
        self.opening5 = MathTex(r"{{p(x)}} {{- y_0}} {{}} {{=(x-x_0)}} {{(...)}}", color = PRIMARY_COLOR)
        self.opening6 = MathTex(r"{{p(x)}} {{- y_0}} {{}} {{=(x-x_0)}} \cdot {{ q(x)}}", color = PRIMARY_COLOR)
        self.opening7 = MathTex(r"\frac{p(x)- y_0}{x-x_0} = {{}} {{}} {{q(x)}}", color = PRIMARY_COLOR)

        self.verifier = ImageMobject("data/images/person.png").to_corner(RIGHT+UP).scale(0.6).shift(LEFT)
        self.commiter = ImageMobject("data/images/person_blue.png").to_corner(LEFT+UP).scale(0.6).shift(RIGHT)

        self.commiter_label = Text("Committer", color = PRIMARY_COLOR, font=PRIMARY_FONT).scale(0.6).next_to(self.commiter, DOWN, buff = 0.4)
        self.verifier_label = Text("Verifier", color = PRIMARY_COLOR, font=PRIMARY_FONT).scale(0.6).next_to(self.verifier, DOWN, buff = 0.4)

        self.chart = DiscreetePolynomialChart(41, poly)

        self.equation2 = MathTex(r"{{q(x)}}\cdot {{(x - x_0)}} = {{p(x)}} - {{y_0}}", color=PRIMARY_COLOR)
        self.commitment = MathTex(r"{{C}} = {{ p(\tau)}} \cdot {{G_1}}", color=PRIMARY_COLOR)
        self.proof = MathTex(r"{{\pi}} = {{q(\tau)}} \cdot {{G_1}}", color=PRIMARY_COLOR)


        self.chart.to_edge(LEFT).scale(0.8).shift(UP*0.5)
        self.chart2.to_edge(LEFT).scale(0.8).shift(UP*0.5)
        self.polynomial.to_edge(DOWN + LEFT).scale(0.8).shift(RIGHT)
        self.opening.to_edge(RIGHT).shift(LEFT*2+UP*2)
        self.equation.next_to(self.opening, DOWN)
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
        self.new_subsection(scene, "challange - secret tau", "data/sound/e4/slide3-1.mp3")
        self.chart.gen_points()
        scene.play(FadeIn(self.chart))
        scene.play(FadeIn(self.polynomial))

        self.chart.add_xaxis_label(self.tau.value, r"\tau")

        self.new_subsection(scene, "contructing q via tau", "data/sound/e4/slide3-2.mp3")
        scene.wait(2)
        self.chart2.gen_points2()
        scene.play(FadeIn(self.chart2))

        scene.play(Write(self.equality_quotient))
        scene.wait(1.5)
        self.equality_quotient.generate_target()
        self.equality_quotient.target.shift(UP*1.5)
        scene.play(Write(self.commitment_quotient), MoveToTarget(self.equality_quotient))
        scene.wait(1)
        scene.play(TransformMatchingShapes(VGroup(self.equality_quotient[0].copy(), self.commitment_quotient), self.commitment_quotient2))
        scene.wait(3.7)

        self.new_subsection(scene, "possibility for attack", "data/sound/e4/slide3-2a.mp3")
        scene.play(FadeOut(self.commitment_quotient2), run_time=0.7)
        scene.wait(3.8)

        self.new_subsection(scene, "opening", "data/sound/e4/slide3-3.mp3")
        scene.play(FadeOut(self.chart2), Unwrite(self.equality_quotient), run_time=3)
        self.chart.add_xaxis_label(self.z.value, r"x_0")
        scene.wait(1)
        line_z = self.chart.animate_create_vertical_line(
            scene, self.z.value, self.y.value
        )
        self.chart.add(line_z)
        scene.wait(1)
        scene.play(Write(self.opening))
        scene.wait(1)
        scene.play(FadeOut(self.equality_quotient), run_time=1)
        scene.wait(0.5)
        scene.play(TransformMatchingShapes(self.opening.copy(), self.opening2), run_time=1.5)

        self.new_subsection(scene, "p(x)-y as polynomial", "data/sound/e4/slide3-4.mp3")
        scene.wait(1.5)
        scene.play(TransformMatchingShapes(self.opening2, self.opening3), run_time=1.5)
        scene.wait(1.5)
        scene.play(TransformMatchingShapes(self.opening3, self.opening4), run_time=1.5)
        scene.wait(1.2)

        self.new_subsection(scene, "r(x) in a chart", "data/sound/e4/slide3-4a.mp3")

        scene.play(TransformMatchingShapes(self.opening4, self.opening3))
        line_tau = self.chart.animate_create_vertical_line(
            scene, self.tau.value, self.value_at_tau.value
        )
        line_tau_y = self.chart.animate_create_vertical_line(
            scene, self.tau.value, self.value_at_tau.value - self.y.value
        )   
        self.chart.add(line_tau_y)
        scene.wait(1)
        dots = VGroup(*self.chart.dots)
        scene.play(Indicate(dots, color=HIGHLIGHT2_COLOR, scale=1.05))
        scene.wait(2)
        scene.play(Indicate(line_z, color = HIGHLIGHT2_COLOR), run_time=1)
        self.chart.animate_shift_dots(scene, self.y.value)
        
        self.new_subsection(scene, "modulo operation", "data/sound/e4/slide3-4b.mp3")
        scene.play(FadeOut(line_z, line_tau, line_tau_y), run_time=0.3)
        scene.wait(1.8)

        self.new_subsection(scene, "rewriting it with roots", "data/sound/e4/slide3-5.mp3")
        scene.wait(3.5)
        scene.play(TransformMatchingShapes(self.opening3, self.opening5), run_time=1.5)
        scene.wait(0.2)
        scene.play(Indicate(self.opening5[6], color = HIGHLIGHT_COLOR))
        scene.wait(2.5)

        self.new_subsection(scene, "there exist a q(x)", "data/sound/e4/slide3-6.mp3")
        scene.wait(2)
        scene.play(Indicate(self.opening5[4], color = HIGHLIGHT_COLOR), run_time=0.8)

        scene.wait(0.7)
        scene.play(TransformMatchingShapes(self.opening5, self.opening6), run_time=1.5)
        scene.wait(1.5)
        scene.play(Indicate(self.opening, color = HIGHLIGHT_COLOR), run_time=0.8)

        self.new_subsection(scene, "security", "data/sound/e4/slide3-7.mp3")
        scene.wait(0.5)
        scene.play(Indicate(self.chart.labels[0], color = HIGHLIGHT_COLOR))

        scene.play(TransformMatchingShapes(self.opening6, self.opening7), run_time=1.3)
        scene.wait(3)


    def animate_out(self, scene):
        scene.play(FadeOut(self.chart, self.polynomial, self.opening7))