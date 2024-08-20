from manim import DOWN, UP, RIGHT, LEFT, FadeIn, FadeOut, MathTex, ValueTracker, Text, Create, Write, TransformMatchingShapes, Indicate, ApplyWave, MoveToTarget, Transform, Line, VGroup, Unwrite

from numpy import linspace
import random
from zkmarek.video.constant import SECONDARY_COLOR, PRIMARY_FONT, PRIMARY_COLOR, HIGHLIGHT_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.mobjects.dot_on_curve import DotOnCurve
from zkmarek.video.slides.e4.chart import Chart
from zkmarek.video.slides.e4.curve import Curve
from zkmarek.video.slides.episode4.discreete_polynomial_chart import DiscreetePolynomialChart
from zkmarek.crypto.field_element import FieldElement

def poly(x):
    if isinstance(x, FieldElement):
        output = FieldElement(4, x.order) * x * x * x - FieldElement(8, x.order) * x * x  - FieldElement(17, x.order) * x + FieldElement(30, x.order)
    else:
        output = 4 * x * x * x - 8 * x * x * 2 - 17 * x + 30
    return output


class Polynomials(SlideBase):

    def __init__(self):
        super().__init__("Polynomials")

    def construct(self):
        self.chart1 = DiscreetePolynomialChart(5, poly)
        self.chart1.to_edge(RIGHT).scale(0.8).shift(UP*0.2)
        self.chart2 = DiscreetePolynomialChart(23, poly)
        self.chart2.to_edge(RIGHT).scale(0.8).shift(UP*0.2)
        self.chart3 = DiscreetePolynomialChart(41, poly)
        self.chart3.to_edge(RIGHT).scale(0.8).shift(UP*0.2)
        self.title_label = Text("Polynomials", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 40).to_edge(UP)
        self.x = MathTex(r"x", color = PRIMARY_COLOR, font_size=70)  

        self.polynomial_eqn = MathTex(r"P(x) = {{a_n}} \cdot {{x^n}} + {{a_{n-1} }}\cdot {{x^{n-1} }} + \cdots + {{a_1}} \cdot {{x}} + {{a_0}}", color = PRIMARY_COLOR, font_size = 60)
        self.polynomial_eqn1 = MathTex(r"{{a_n}} \cdot {{x^n}} + {{a_{n-1} }}\cdot {{x^{n-1} }} + \cdots + {{a_1}} \cdot {{x}} + {{a_0}}", color = PRIMARY_COLOR, font_size = 60)
        self.polynomial_eqn3 = MathTex(r"P(x) = {{a_3}}\cdot {{x^3}} +{{a_2}} \cdot {{x^2}} + {{a_{1} }}\cdot {{x }} + {{a_0}}", color = PRIMARY_COLOR, font_size = 60).to_edge(DOWN).scale(0.7)

        self.polynomial_eqn2 = MathTex(r"{{x}}^n + {{x}}^{n-1} + \cdots + {{x}}", color = PRIMARY_COLOR, font_size = 60)
        self.polynomial = MathTex(r"P({{x}}) = 4 {{x^3}} - 8{{x^2}} - 17 {{x}} + 30 {{}}", color = PRIMARY_COLOR).to_edge(DOWN)
        self.polynomial_z = MathTex(r"P({{z}}) = 4 {{z^3}} - 8{{z^2}} - 17 {{z}} + 30 {{=y}}", color = PRIMARY_COLOR).to_edge(RIGHT).shift(LEFT*0.1+UP*0.4)
        self.polynomial_roots = MathTex(r"P({{x_0}}) = 4 {{x_0^3}} - 8{{x_0^2}} - 17 {{x_0}} + 30 = {{0}}", color = PRIMARY_COLOR).to_edge(DOWN)
        self.quotient = MathTex(r"Q({{x}}) = {{x^3}} + {{x^2}} - 2{{x}} + 8 {{}}", color = PRIMARY_COLOR).to_edge(DOWN)

        self.quotient_z = MathTex(r"Q({{z}}) = {{z}}^3 + {{z}}^2 - 2{{z}} + 8 {{=y}}", color = PRIMARY_COLOR).next_to(self.polynomial_z, DOWN, buff = 0.3)
        self.line_subtract = Line(start = self.quotient_z.get_left(), end = self.quotient_z.get_right(), color = HIGHLIGHT_COLOR).next_to(self.quotient_z, DOWN, buff = 0.2)
        self.subtract = MathTex("R(x)", "=", "3x^3", "-", "9x^2", "-", "15x", "+", "22", color = PRIMARY_COLOR).next_to(self.line_subtract, DOWN, aligned_edge=LEFT)
        self.subtract_z = MathTex("R(z)", "=", "3z^3", "-", "9z^2", "-", "15z", "+", "22", "=0", color = PRIMARY_COLOR).next_to(self.line_subtract, DOWN, aligned_edge=LEFT)
        self.polynomial2 = MathTex(r"P({{x}}) = 4 {{x^3}} - 8{{x^2}} - 17 {{x}} + {{30}} = {{(2x-3)}}{{(2x-5)}}{{(x+2)}}", color = PRIMARY_COLOR).to_edge(DOWN)

        self.chart = Chart(include_details=True).scale(0.8).next_to(self.title_label, DOWN)
        self.p1_1 = ValueTracker(1)
        a1_1 = Curve.from_x(self.p1_1.get_value())
        self.p1 = DotOnCurve(self.chart.ax, "(1,9)", a1_1)

        self.p2_10 = ValueTracker(2)
        a2_10 = Curve.from_x(self.p2_10.get_value())
        self.p2 = DotOnCurve(self.chart.ax, "(2,-4)", a2_10)

        self.p3_23 = ValueTracker(3)
        a3_23 = Curve.from_x(self.p3_23.get_value())
        self.p3 = DotOnCurve(self.chart.ax, "(3, 15)", a3_23)

        self.poly_point1 = MathTex("P(1) = 9", color = PRIMARY_COLOR).to_edge(RIGHT)
        self.poly_point2 = MathTex("P(2) = -4", color = PRIMARY_COLOR).next_to(self.poly_point1, DOWN)
        self.poly_point3 = MathTex("P(3) = 15", color = PRIMARY_COLOR).next_to(self.poly_point2, DOWN)

        self.p_2 = ValueTracker(-2)
        a2 = Curve.from_x(self.p_2.get_value())
        self.root1 = DotOnCurve(self.chart.ax, "({{-2}},{{0}})", a2)
        self.p05 = ValueTracker(1.5)
        a05 = Curve.from_x(self.p05.get_value())
        self.root2 = DotOnCurve(self.chart.ax, "({{1.5}},{{0}})", a05)
        self.p52 = ValueTracker(2.5)
        a25 = Curve.from_x(self.p52.get_value())
        self.root3 = DotOnCurve(self.chart.ax, "({{2.5}},{{0}})", a25)

        self.p_intersect = ValueTracker(-1.849)
        a_i = Curve.from_x(self.p_intersect.get_value())
        self.intersect = DotOnCurve(self.chart.ax, r"({{z}}, {{y}})", a_i)
        self.intersect.set_color(PRIMARY_COLOR)

        self.point = []
        self.N = 30 # n/o of points
        self.values = linspace(-4.5, 3, self.N)
        for i in range(self.N):
            point_value = self.values[i]
            points = ValueTracker(point_value)
            a = Curve.from_x(points.get_value())
            self.point.append(DotOnCurve(self.chart.ax, "", a)) 
        self.polynomial_modulo = MathTex(r"P({{x}}) \mod \ p = 4 {{x^3}} - 8{{x^2}} - 17 {{x}} + 30 {{\mod \ p}}", color = PRIMARY_COLOR).scale(0.7).to_edge(DOWN)
        self.polynomial_modulo5 = MathTex(r"P({{x}}) \mod \ 5 = 4 {{x^3}} - 8{{x^2}} - 17 {{x}} + 30 {{\mod \ 5}} {{}} {{}}", color = PRIMARY_COLOR).scale(0.7).to_edge(DOWN)
        self.polynomial0_modulo5 = MathTex(r"P({{0}}) \rightarrow 4\cdot {{0^3}} - 8\cdot{{0^2}} - 17\cdot {{0}} + 30 {{\mod \ 5}} {{= 30 \mod 5}} {{= 0}}", color = PRIMARY_COLOR).scale(0.7).to_edge(DOWN)
        self.polynomial1_modulo5 = MathTex(r"P({{1}}) \rightarrow 4\cdot {{1^3}} - 8\cdot{{1^2}} - 17\cdot {{1}} + 30 {{\mod \ 5}} {{= 9 \mod 5}} {{= 4}}", color = PRIMARY_COLOR).scale(0.7).to_edge(DOWN)

        self.polynomial_modulo23 = MathTex(r"P({{x}}) \mod \ 23 = 4 {{x^3}} - 8{{x^2}} - 17 {{x}} + 30 {{\mod \ 23}}", color = PRIMARY_COLOR).scale(0.7).to_edge(DOWN)
        self.polynomial_modulo41 = MathTex(r"P({{x}}) \mod \ 41 = 4 {{x^3}} - 8{{x^2}} - 17 {{x}} + 30 {{\mod \ 41}}", color = PRIMARY_COLOR).scale(0.7).to_edge(DOWN)

    def animate_in(self, scene):
        self.new_subsection(scene, "intro", "data/sound/e4/slide1-0.mp3")
        scene.play(Write(self.title_label), run_time=2)
        scene.wait(2)
        self.animate_random_number(scene)

        scene.play(TransformMatchingShapes(self.x, self.polynomial_eqn2))

        scene.play(Indicate(self.polynomial_eqn2[0], color = HIGHLIGHT_COLOR), run_time=0.3)
        scene.play(Indicate(self.polynomial_eqn2[2], color = HIGHLIGHT_COLOR), run_time=0.3)
        scene.play(Indicate(self.polynomial_eqn2[4], color = HIGHLIGHT_COLOR), run_time=0.3)

        scene.play(TransformMatchingShapes(self.polynomial_eqn2, self.polynomial_eqn1), run_time=1)

        scene.play(Indicate(self.polynomial_eqn1[0], color = HIGHLIGHT_COLOR), run_time=0.3)
        scene.play(Indicate(self.polynomial_eqn1[4], color = HIGHLIGHT_COLOR), run_time=0.3)
        scene.play(Indicate(self.polynomial_eqn1[8], color = HIGHLIGHT_COLOR), run_time=0.3)
        scene.play(Indicate(self.polynomial_eqn1[12], color = HIGHLIGHT_COLOR), run_time=0.3)

        scene.play(TransformMatchingShapes(self.polynomial_eqn1, self.polynomial_eqn), run_time=1)

        self.new_subsection(scene, "specific eqn", "data/sound/e4/slide1-1.mp3")
        self.polynomial_eqn.generate_target()
        self.polynomial_eqn.target.to_edge(DOWN).scale(0.7)
        scene.play(MoveToTarget(self.polynomial_eqn))
        scene.play(Create(self.chart.ax), Create(self.chart.labels), run_time=2)
        scene.wait(2.5)
        scene.play(Create(self.p1.dot), run_time=0.7)
        scene.play(Write(self.p1.label), run_time=0.7)
        scene.play(Create(self.p2.dot), run_time=0.7)
        scene.play(Write(self.p2.label), run_time=0.7)
        scene.play(Create(self.p3.dot), run_time=0.7)
        scene.play(Write(self.p3.label), run_time=0.7)
        scene.wait(2.7)
        scene.play(Indicate(self.polynomial_eqn, color = PRIMARY_COLOR))
        scene.wait(2)
        scene.play(TransformMatchingShapes(self.p1.label.copy(), self.poly_point1))
        scene.play(TransformMatchingShapes(self.p2.label.copy(), self.poly_point2))
        scene.play(TransformMatchingShapes(self.p3.label.copy(), self.poly_point3))

        self.new_subsection(scene, "interpolation", "data/sound/e4/slide1-2.mp3")
        scene.play(Indicate(self.p1, color = HIGHLIGHT_COLOR), run_time=0.7)
        scene.play(Indicate(self.p2, color = HIGHLIGHT_COLOR), run_time=0.7)
        scene.play(Indicate(self.p3, color = HIGHLIGHT_COLOR), run_time=0.7)
        scene.play(Write(self.chart.graph))
        # for i in range(self.N):
        #     point = self.point[i]
        #     scene.play(Create(point.dot), run_time=0.05)

        scene.play(Indicate(self.polynomial_eqn, color = HIGHLIGHT_COLOR))
        scene.wait(2)
        scene.play(TransformMatchingShapes(self.polynomial_eqn, self.polynomial_eqn3))
        scene.wait(1.5)
        scene.play(TransformMatchingShapes(self.polynomial_eqn3, self.polynomial))

        # for i in range(self.N):
        #     point = self.point[i]
        #     scene.play(FadeOut(point.dot), run_time=0.05)

        self.new_subsection(scene, "roots", "data/sound/e4/slide1-3.mp3")
        scene.play(FadeOut(self.p1.dot, self.p1.label, self.p2.dot, self.p2.label, self.p3.dot, self.p3.label, self.poly_point1, self.poly_point2, self.poly_point3), run_time=1)
        scene.play(Indicate(self.polynomial, color = SECONDARY_COLOR))

        self.root1.label.shift(UP*0.2+LEFT*1.3)
        self.root2.label.shift(DOWN*0.2+LEFT*1.2)
        self.root3.label.shift(UP*0.2+LEFT*0.2)

        scene.play(Create(self.root1), run_time=0.4)
        scene.play(Create(self.root2), run_time=0.4)
        scene.play(Create(self.root3), run_time=0.4)
        scene.play(Indicate(self.root1, color = SECONDARY_COLOR), Indicate(self.root2, color = SECONDARY_COLOR), Indicate(self.root3, color = SECONDARY_COLOR))
        scene.play(TransformMatchingShapes(self.polynomial, self.polynomial_roots))
        scene.play(Indicate(self.root1.label[1], color = HIGHLIGHT_COLOR, scale_factor=2), Indicate(self.root2.label[1], color = HIGHLIGHT_COLOR, scale_factor=2), Indicate(self.root3.label[1], color = HIGHLIGHT_COLOR, scale_factor=2), Indicate(self.polynomial_roots[1], color = HIGHLIGHT_COLOR), Indicate(self.polynomial_roots[3], color = HIGHLIGHT_COLOR), Indicate(self.polynomial_roots[5], color = HIGHLIGHT_COLOR))
        scene.wait(1.1)
        scene.play(Indicate(self.root1.label[3], color = HIGHLIGHT_COLOR, scale_factor=2), Indicate(self.root2.label[3], color = HIGHLIGHT_COLOR, scale_factor=2), Indicate(self.root3.label[3], color = HIGHLIGHT_COLOR, scale_factor=2), Indicate(self.polynomial_roots[9], color = HIGHLIGHT_COLOR, scale_factor=2))
        scene.play(TransformMatchingShapes(self.polynomial_roots, self.polynomial2))
        scene.wait(1)
        scene.play(Indicate(self.polynomial2[11], color = HIGHLIGHT_COLOR), Indicate(self.root2, color = HIGHLIGHT_COLOR))
        scene.wait(0.2)
        scene.play(Indicate(self.polynomial2[12], color = HIGHLIGHT_COLOR), Indicate(self.root3, color = HIGHLIGHT_COLOR))
        scene.wait(0.2)
        scene.play(Indicate(self.polynomial2[13], color = HIGHLIGHT_COLOR), Indicate(self.root1, color = HIGHLIGHT_COLOR))

        self.new_subsection(scene, "operations", "data/sound/e4/slide1-4.mp3")
        scene.play(FadeOut(self.root1, self.polynomial2, self.root2, self.root3))
        scene.wait(1.5)
        self.chart_group = VGroup(self.chart.ax, self.chart.labels, self.chart.graph)
        self.chart_group.generate_target()
        self.chart_group.target.shift(LEFT*4+UP*0.15)
        self.polynomial.to_edge(RIGHT).shift(LEFT*0.8+UP*3.7)
        self.label_poly_p = MathTex(r"P(x)", color = SECONDARY_COLOR).next_to(self.chart.graph, RIGHT, buff = 0.1).shift(4*LEFT+UP)
        self.label_poly_q = MathTex(r"Q(x)", color = HIGHLIGHT_COLOR).next_to(self.chart.graph2, LEFT, buff = 0.1).shift(LEFT*0.8+UP)
        self.label_poly_r = MathTex(r"R(x)", color = PRIMARY_COLOR).next_to(self.chart.graph3, RIGHT, buff = 0.1).shift(LEFT*4+UP)
        scene.play(MoveToTarget(self.chart_group), Write(self.polynomial), Write(self.label_poly_p), run_time=1.5)
        self.chart.graph2.shift(LEFT*4+UP*0.15)
        self.chart.graph3.shift(LEFT*4+UP*0.15)
        self.intersect.shift(LEFT*4+UP*0.15)
        self.intersect.label.shift(0.2*DOWN+LEFT*0.1)
        scene.play(Write(self.chart.graph2), Write(self.label_poly_q))
        scene.play(Create(self.intersect.dot))
        self.quotient.next_to(self.polynomial, DOWN, buff = 0.3)
        scene.wait(1)
        scene.play(Indicate(self.intersect.dot, color = HIGHLIGHT_COLOR))
        scene.play(Write(self.quotient))
        scene.wait(2)
        scene.play(Write(self.intersect.label))
        scene.play(Indicate(self.intersect.label[1], color = HIGHLIGHT_COLOR))
        scene.wait(0.5)
        scene.play(TransformMatchingShapes(self.polynomial, self.polynomial_z), TransformMatchingShapes(self.quotient, self.quotient_z), run_time=1.5)
        scene.play(Indicate(self.intersect.label, color = SECONDARY_COLOR))
        scene.play(Indicate(self.polynomial_z[9], color = SECONDARY_COLOR))
        scene.play(Indicate(self.quotient_z[9], color = SECONDARY_COLOR))

        self.new_subsection(scene, "equality", "data/sound/e4/slide1-5.mp3")
        scene.play(TransformMatchingShapes(self.polynomial_z, self.polynomial), TransformMatchingShapes(self.quotient_z, self.quotient), run_time=1)
        self.minus = MathTex("-", color = PRIMARY_COLOR).next_to(self.quotient_z, LEFT, buff = 0.3)
        scene.play(Write(self.minus), run_time=1)
        scene.play(Create(self.line_subtract), run_time=1)
        scene.wait(1)
        a_i = Curve.from_x(self.p_intersect.get_value())
        self.intersect_sub = DotOnCurve(self.chart.ax, r"(z,0)", a_i)
        self.intersect_sub.set_color(PRIMARY_COLOR).shift(DOWN*0.9)
        self.intersect_sub.label.shift(LEFT*0.2+UP*0.35)

        scene.play(Write(self.subtract), run_time=1)
        scene.play(TransformMatchingShapes(VGroup(self.chart.graph2, self.chart.graph), self.chart.graph3), TransformMatchingShapes(self.intersect, self.intersect_sub), Write(self.label_poly_r), Unwrite(self.label_poly_p), Unwrite(self.label_poly_q))
        scene.wait(2)
        scene.play(TransformMatchingShapes(self.subtract, self.subtract_z), TransformMatchingShapes(self.polynomial, self.polynomial_z), TransformMatchingShapes(self.quotient, self.quotient_z))
        scene.wait(2)
        scene.play(FadeOut(self.intersect_sub))
        scene.wait(2)
        scene.play(Indicate(self.intersect_sub, color = HIGHLIGHT_COLOR, scale_factor=1.7))
        self.polynomial.to_edge(DOWN).shift(LEFT*3).scale(0.7)
        scene.play(FadeOut(self.line_subtract, self.minus, self.subtract_z, self.quotient_z, self.intersect_sub), TransformMatchingShapes(self.polynomial_z, self.polynomial))

        self.new_subsection(scene, "finite fields", "data/sound/e4/slide1-6.mp3")
        self.chart1.gen_points()
        scene.play(Create(self.chart1), TransformMatchingShapes(self.chart.graph3, self.chart.graph), Unwrite(self.label_poly_r), run_time=2)
        scene.wait(4)
        scene.play(ApplyWave(self.chart1.ax[0]), ApplyWave(self.chart1.ax[1]), DIRECTION=UP)
        scene.wait(4)
        scene.play(TransformMatchingShapes(self.polynomial, self.polynomial_modulo), run_time=1)

        self.new_subsection(scene, "example of finite field", "data/sound/e4/slide1-7.mp3")
        # self.chart.shift(LEFT*4+UP*0.3)
        self.p0_30 = ValueTracker(0)
        a0_30 = Curve.from_x(self.p0_30.get_value())
        self.p0 = DotOnCurve(self.chart.ax, "(0,30)", a0_30)

        self.p1_1 = ValueTracker(1)
        a1_1 = Curve.from_x(self.p1_1.get_value())
        self.p1 = DotOnCurve(self.chart.ax, "(1,9)", a1_1)

        self.p2_10 = ValueTracker(2)
        a2_10 = Curve.from_x(self.p2_10.get_value())
        self.p2 = DotOnCurve(self.chart.ax, "(2,-4)", a2_10)

        self.p3_23 = ValueTracker(3)
        a3_23 = Curve.from_x(self.p3_23.get_value())
        self.p3 = DotOnCurve(self.chart.ax, "(3, 15)", a3_23)
    
        scene.wait(2)
        scene.play(Create(self.p0), Create(self.p1), Create(self.p2), Create(self.p3))
        scene.wait(0.5)
        scene.play(ApplyWave(self.chart1.ax[0]), ApplyWave(self.chart1.ax[1]), TransformMatchingShapes(self.polynomial_modulo, self.polynomial_modulo5))

        self.new_subsection(scene, "P(0)", "data/sound/e4/slide1-8.mp3")
        scene.play(Indicate(self.p0, color = HIGHLIGHT_COLOR))
        scene.play(TransformMatchingShapes(self.polynomial_modulo5, self.polynomial0_modulo5), run_time=1.3)
        scene.wait(0.6)
        scene.play(Indicate(self.polynomial0_modulo5[11], color = HIGHLIGHT_COLOR))
        scene.wait(0.5)
        scene.play(Indicate(self.polynomial0_modulo5[13], color = HIGHLIGHT_COLOR))

        self.new_subsection(scene, "P(1)", "data/sound/e4/slide1-9.mp3")
        scene.play(Indicate(self.p1, color = HIGHLIGHT_COLOR), TransformMatchingShapes(self.polynomial0_modulo5, self.polynomial1_modulo5), run_time=1.2)

        scene.play(Indicate(self.polynomial1_modulo5[11], color = HIGHLIGHT_COLOR))
        scene.wait(0.5)
        scene.play(Indicate(self.polynomial1_modulo5[13], color = HIGHLIGHT_COLOR))
        scene.wait(4)
        scene.play(ApplyWave(self.chart1.ax[1], DIRECTION=UP))

        top_val = MathTex(r"p-1", color = SECONDARY_COLOR).to_edge(UP+RIGHT).shift(DOWN*1.2+LEFT*3).scale(0.8)
        scene.play(FadeIn(top_val))
        self.chart1.animate_create_horizontal_line(
            scene, 4, 0, 4
        )
        scene.play(FadeOut(top_val))

        self.new_subsection(scene, "p=23", "data/sound/e4/slide1-10.mp3")
        scene.wait(2.3)
        scene.play(TransformMatchingShapes(self.polynomial1_modulo5, self.polynomial_modulo23))
        self.chart2.gen_points()
        scene.play(FadeOut(self.chart1), FadeIn(self.chart2))
        scene.wait(1)

        self.new_subsection(scene, "p=41", "data/sound/e4/slide1-11.mp3")
        self.chart3.gen_points()
        scene.play(FadeOut(self.chart2), FadeIn(self.chart3), TransformMatchingShapes(self.polynomial_modulo23, self.polynomial_modulo41))

        scene.wait(1)
    
    def animate_out(self, scene):
        scene.play(FadeOut(self.chart3, self.chart.ax, self.chart.graph, self.chart.labels, self.title_label, self.polynomial_modulo41, self.p0, self.p1, self.p2, self.p3))

    def animate_random_number(self, scene):
        first_number = random.randint(1, 20)
        number_text = Text(str(first_number), color = PRIMARY_COLOR, font = PRIMARY_FONT)
        scene.play(FadeIn(number_text), run_time=0.2)
        for _ in range(16):  
            new_number = random.randint(1, 20)
            new_number_text = Text(str(new_number), color = PRIMARY_COLOR, font = PRIMARY_FONT)
            scene.play(Transform(number_text, new_number_text), run_time=0.01)
            scene.wait(0.035)
            if _==15:
                scene.play(FadeOut(number_text))

        scene.play(FadeIn(self.x))