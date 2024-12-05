from manim import (FadeOut, Text, LEFT, RIGHT, DOWN, UP, Write, Create, WHITE, ValueTracker, MathTex,
Indicate, Arrow, StealthTip, GrowArrow, Transform, Axes, FadeIn, MoveToTarget, MAROON_A, PURPLE, PINK, TransformMatchingShapes)
from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR, HIGHLIGHT_COLOR, PRIMARY_FONT, HIGHLIGHT2_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.mobjects.dot_on_curve import DotOnCurve
from zkmarek.video.slides.e4.chart import Chart
from zkmarek.video.slides.e4.curve import Curve
import numpy as np
from zkmarek.crypto.field_element import FieldElement
from zkmarek.video.slides.e4.discreete_polynomial_chart import (
    DiscreetePolynomialChart,
)

def poly(x):
    return FieldElement(1, x.order) * x ** 100 + FieldElement(1, x.order) * x ** 99 + FieldElement(1, x.order) * x ** 98 + FieldElement(1, x.order) * x ** 97 + FieldElement(1, x.order) * x ** 96
class VectorCommitments(SlideBase):
    def __init__(self) -> None:
        super().__init__(title="Layer 2")
        
    def construct(self):
        self.title_label = Text("Vector commitments", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 40).to_edge(UP)
        self.chart = Chart(include_details=True).scale(0.7).shift(LEFT*3.5)
        self.chart_discrete = DiscreetePolynomialChart(101, poly, label="p", include_numbers=False).scale(0.7).shift(LEFT*3.5)
        self.number_sequence = MathTex(r"\left[ {{y_0}}, {{y_1}}, {{y_2}}, {{\cdots}}, {{y_{4095}}} \right]", color = SECONDARY_COLOR).shift(RIGHT*3)
        self.number_sequence100 = MathTex(r"\left[ {{y_0}}, {{y_1}}, {{y_2}}, {{\cdots}}, {{y_{100}}} \right]", color = SECONDARY_COLOR).shift(RIGHT*3)
        self.number_sequence_smaller = MathTex(r"\left[ {{30}}, {{9}}, {{-4}}, {{15}} \right]", color = SECONDARY_COLOR).shift(RIGHT*3)
        self.number_sequence_smaller_indeces = MathTex(r" {{\ }}{{0}} \quad {{ \}}{{1}} {{ \quad}}{{ 2}} \quad {{\}}{{3}} ", color = SECONDARY_COLOR).next_to(self.number_sequence_smaller, DOWN).scale(0.6)
        for i in range(4):
            self.number_sequence_smaller_indeces[3*i+2].set_color(PURPLE)
        self.arrow_number_indeces = Arrow(self.number_sequence_smaller_indeces.get_top(), self.number_sequence_smaller.get_bottom(), tip_shape=StealthTip, 
                               stroke_width=2, max_tip_length_to_length_ratio=0.15).set_color_by_gradient([HIGHLIGHT2_COLOR, SECONDARY_COLOR])
        self.p0 = ValueTracker(0)
        a0_1 = Curve.from_x(self.p0.get_value())
        self.p0 = DotOnCurve(self.chart.ax, "({{0}},{{30}})", a0_1)

        self.p1_1 = ValueTracker(1)
        a1_1 = Curve.from_x(self.p1_1.get_value())
        self.p1 = DotOnCurve(self.chart.ax, "({{1}}, {{9}})", a1_1)
        self.p1.label.shift(LEFT*0.1)

        self.p2_10 = ValueTracker(2)
        a2_10 = Curve.from_x(self.p2_10.get_value())
        self.p2 = DotOnCurve(self.chart.ax, "({{2}},{{-4}})", a2_10)
        self.p2.label.shift(LEFT*0.3+DOWN*0.3)

        self.p3_23 = ValueTracker(3)
        a3_23 = Curve.from_x(self.p3_23.get_value())
        self.p3 = DotOnCurve(self.chart.ax, "({{3}}, {{15}})", a3_23)

        self.poly_point0 = MathTex("P(0) = 30", color = PRIMARY_COLOR).to_edge(RIGHT)
        self.poly_point1 = MathTex("P(1) = 9", color = PRIMARY_COLOR).next_to(self.poly_point0, DOWN)
        self.poly_point2 = MathTex("P(2) = -4", color = PRIMARY_COLOR).next_to(self.poly_point1, DOWN)
        self.poly_point3 = MathTex("P(3) = 15", color = PRIMARY_COLOR).next_to(self.poly_point2, DOWN)
        self.arrow_number_chart = Arrow(RIGHT, LEFT*0.5, tip_shape=StealthTip, 
                               stroke_width=2, max_tip_length_to_length_ratio=0.15).set_color_by_gradient([HIGHLIGHT2_COLOR, SECONDARY_COLOR])
        self.question_mark = Text("?", font = PRIMARY_FONT).set_color_by_gradient([WHITE, HIGHLIGHT2_COLOR]).next_to(self.arrow_number_chart, UP, buff = 0.1)
        self.polynomial_eqn = MathTex(r"P(x) = {{a_3}}\cdot {{x^3}} +{{a_2}} \cdot {{x^2}} + {{a_{1} }}\cdot {{x }} + {{a_0}}", color = PRIMARY_COLOR, font_size = 60).to_edge(DOWN).scale(0.7)
        self.polynomial_eqn_4096 = MathTex(r"P(x) = {{a_{4095}}}\cdot {{x^{4095}}} + {{a_{4094}}} \cdot {{x^{4094}}} + \cdots + {{a_1}}\cdot {{x}} + {{a_0}}", color = PRIMARY_COLOR, font_size = 60).to_edge(DOWN).scale(0.7)
        self.polynomial_eqn_100 = MathTex(r"P(x) = {{a_{100}}}\cdot {{x^{100}}} + {{a_{99}}} \cdot {{x^{99}}} + \cdots + {{a_1}}\cdot {{x}} + {{a_0}}", color = PRIMARY_COLOR, font_size = 60).to_edge(DOWN).scale(0.7)
        self.polynomial = MathTex(r"P({{x}}) = 4 {{x^3}} - 8{{x^2}} - 17 {{x}} + 30 {{}}", color = PRIMARY_COLOR, font_size = 60).to_edge(DOWN).scale(0.7)
        self.lagrange_interpolation = Text("Lagrange interpolation", font = PRIMARY_FONT, font_size = 24, color = PRIMARY_COLOR).next_to(self.chart, RIGHT).shift(DOWN)
        
        self.poly_number0 = MathTex(r"P({{0}}) = {{30}}", color = PINK, font_size = 32).next_to(self.number_sequence_smaller, DOWN).shift(LEFT)
        self.poly_number1 = MathTex(r"P({{1}}) = {{9}}", color = PINK, font_size = 32).next_to(self.poly_number0, RIGHT)
        self.poly_number2 = MathTex(r"P({{2}}) = {{-4}}", color = PINK, font_size = 32).next_to(self.poly_number0, DOWN)
        self.poly_number3 = MathTex(r"P({{3}}) = {{15}}", color = PINK, font_size = 32).next_to(self.poly_number2, RIGHT)
        for i in range(4):
            self.number_sequence_smaller[2*i+1].set_color_by_gradient(MAROON_A)

    def animate_in(self, scene):
        self.new_subsection(scene, "vector commitments - data", "data/sound/e5/slide3-0.mp3")
        scene.play(Write(self.title_label), Write(self.number_sequence), run_time=0.7)
        for i in range(5):
            scene.play(Indicate(self.number_sequence[2*i+1], color = HIGHLIGHT2_COLOR, scale_factor=1.2), run_time=0.25)
        scene.play(Create(self.chart.ax), run_time=0.8)
        scene.play(Create(self.chart.graph), GrowArrow(self.arrow_number_chart), Create(self.question_mark))
        
        
        self.new_subsection(scene, "[30, 9, -4, 15] - points on xy plane", "data/sound/e5/slide3-1.mp3")
        scene.wait(1)
        scene.play(FadeOut(self.number_sequence), FadeIn(self.number_sequence_smaller), FadeOut(self.chart.graph, self.question_mark))
        self.points = [self.p0, self.p1, self.p2, self.p3]
        scene.play(Create(self.number_sequence_smaller_indeces))
        for i in range(11):
            scene.play(Indicate(self.number_sequence_smaller_indeces[i], color = PINK), run_time=0.3)
            point = self.points[i] 
            point.label[1].set_color(PURPLE)
        scene.wait(0.7)
        scene.play(Create(self.p0), run_time=0.5)
        scene.play(Create(self.p1), run_time=0.5)
        scene.play(Create(self.p2), run_time=0.5)
        scene.play(Create(self.p3), run_time=0.5)

        scene.wait(3)
        for i in range(4):
            point = self.points[i] 
            point.label[3].set_color(MAROON_A)
            scene.play(Indicate(self.number_sequence_smaller[2*i+1], color = PINK))
            
        self.new_subsection(scene, "poly of degree 3", "data/sound/e5/slide3-1a.mp3")
        for i in range(4):
            scene.play(FadeOut(self.number_sequence_smaller_indeces[3*i+2], self.number_sequence_smaller_indeces[3*i+1]), run_time=0.2)
        scene.play(Create(self.chart.graph))
        scene.play(FadeIn(self.polynomial))
        scene.wait(1.5)
        scene.play(Indicate(self.polynomial, color = PINK), run_time=0.7)
        scene.wait(0.8)
        
        self.new_subsection(scene, "Lagrange interpolation", "data/sound/e5/slide3-1b.mp3")
        scene.wait(1)
        scene.play(Write(self.lagrange_interpolation))
        scene.wait(3)
        scene.play(Indicate(self.polynomial[3], color = HIGHLIGHT_COLOR, scale_factor=1.6))
        scene.play(Indicate(self.p0, color = SECONDARY_COLOR, scale_factor=1.3), run_time=0.4)
        scene.play(Indicate(self.p1, color = SECONDARY_COLOR, scale_factor=1.3), run_time=0.4)
        scene.play(Indicate(self.p2, color = SECONDARY_COLOR, scale_factor=1.3), run_time=0.4)
        scene.play(Indicate(self.p3, color = SECONDARY_COLOR, scale_factor=1.3), run_time=0.4)
        scene.play(FadeOut(self.lagrange_interpolation))
        
        self.new_subsection(scene, "P(0), P(1)", "data/sound/e5/slide3-1c.mp3")
        scene.wait(4)
        scene.play(TransformMatchingShapes(self.p0.copy(), self.poly_number0))
        scene.wait(0.7)
        scene.play(TransformMatchingShapes(self.p1.copy(), self.poly_number1))
        scene.play(TransformMatchingShapes(self.p2.copy(), self.poly_number2))
        scene.play(TransformMatchingShapes(self.p3.copy(), self.poly_number3))
        scene.wait(1.4)
        
        self.new_subsection(scene, "extend to larger n/o of points", "data/sound/e5/slide3-2.mp3")
        scene.play(FadeOut(self.number_sequence_smaller, self.poly_number3, self.poly_number0, self.poly_number2, self.poly_number1), FadeIn(self.number_sequence))
        scene.wait(0.2)
        scene.play(FadeOut(self.polynomial), FadeIn(self.polynomial_eqn_4096), FadeOut(self.p0, self.p1, self.p2, self.p3))

        self.change_chart_axes(scene, self.chart)
        scene.wait(5.5)

        self.change_chart_axes_to4096(scene, self.chart, True)
        scene.wait(1.5)
        scene.play(Indicate(self.number_sequence[9], color = PURPLE), Indicate(self.polynomial_eqn_4096[1], color = PURPLE), Indicate(self.polynomial_eqn_4096[3], color = PURPLE))
        
        self.new_subsection(scene, "polynomial - not on real numbers, but on prime field", "data/sound/e5/slide3-2a.mp3")
        scene.wait(2.5)
        self.transforming_poly_into_field(scene)
        
        self.new_subsection(scene, "poly - wrapper around blob data", "data/sound/e5/slide3-3.mp3")
        scene.wait(1.8)
        scene.play(Indicate(self.number_sequence))
        scene.wait(2)
        
            
        self.new_subsection(scene, "kzg", "data/sound/e5/slide3-4.mp3")
        scene.wait(5)
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.chart_discrete, self.number_sequence, self.title_label, self.number_sequence, self.polynomial_eqn_4096, self.arrow_number_chart))

        

    def change_chart_axes(self, scene, chart):
        new_axes = Axes(
            x_range=[-4.7, 20, 20],
            y_range=[-45, 6, 20],
            x_length=7,
            axis_config={
                "include_numbers": False,
                "color": PRIMARY_COLOR,
                "decimal_number_config": {
                    "color": PRIMARY_COLOR,
                    "num_decimal_places": 0
                }
            }
        )
        new_axes4096 = Axes(
            x_range=[-4.7, 5000, 4096],
            y_range=[-45, 5000, 4096],
            x_length=7,
            axis_config={
                "include_numbers": False,
                "color": PRIMARY_COLOR,
                "decimal_number_config": {
                    "color": PRIMARY_COLOR,
                    "num_decimal_places": 0
                }
            }
        )

        new_axes.scale(0.7).shift(LEFT*3.5)
        new_axes4096.scale(0.7).shift(LEFT*3.5+UP*0.3)
        new_axes4096[0].shift(UP)
        chart.labels[0].generate_target()
        chart.labels[0].target.next_to(new_axes4096[0], UP+RIGHT, buff = 0.1)
        chart.labels[1].generate_target()
        chart.labels[1].target.next_to(new_axes4096[1], UP+RIGHT, buff = 0.1)
        
        scene.play(
            MoveToTarget(chart.labels[0]),
            MoveToTarget(chart.labels[1]),
            Transform(chart.ax, new_axes4096),  
            Transform(chart.graph, new_axes.plot_implicit_curve(
                lambda x, y: sum((x**k*np.sin(k*np.pi*x/3)-25) / np.math.factorial(k)/k**k/np.math.factorial(k)/k**k/k for k in range(1, 101)) - y,
                color=SECONDARY_COLOR
            )), 
            run_time=2)

    def change_chart_axes_to4096(self, scene, chart, include_numebrs):
        new_axes = Axes(
            x_range=[-4.7, 5000, 4095],
            y_range=[-45, 5000, 4095],
            x_length=7,
            axis_config={
                "include_numbers": include_numebrs,
                "color": PRIMARY_COLOR,
                "decimal_number_config": {
                    "color": PRIMARY_COLOR,
                    "num_decimal_places": 0
                }
            }
        )


        new_axes.scale(0.7).shift(LEFT*3.39+UP*0.21)
        new_axes[0].shift(UP*1.15)
        scene.play(
            Transform(chart.ax, new_axes),  
            run_time=0.2)


    def transforming_poly_into_field(self, scene):
            self.chart_discrete.gen_points()
            scene.play(FadeOut(self.chart.ax, self.chart.graph, self.chart.labels), FadeIn(self.chart_discrete))
