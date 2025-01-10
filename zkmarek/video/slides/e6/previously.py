from manim import FadeIn, FadeOut, Text, MathTex, Brace, Create, LEFT, RIGHT, UP, DOWN, Write, TransformMatchingShapes, MoveToTarget, Indicate, VGroup, ValueTracker, ImageMobject, Axes, Arrow, StealthTip, GrowArrow, Transform
from zkmarek.video.slides.e4.discreete_polynomial_chart import DiscreetePolynomialChart
from zkmarek.video.constant import SECONDARY_COLOR, PRIMARY_COLOR, PRIMARY_FONT
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.crypto.field_element import FieldElement
from zkmarek.video.mobjects.dot_on_curve import DotOnCurve
from zkmarek.video.slides.e4.chart import Chart
from zkmarek.video.slides.e6.curve import Curve
from zkmarek.video.slides.e5.layer2 import Layer2
from zkmarek.video.mobjects.verkle_tree import VerkleTree
import numpy as np

def poly(x):
    output = FieldElement(4, x.order)*x**3 - FieldElement(8, x.order)*x**2 - FieldElement(17, x.order)*x + FieldElement(30, x.order)
    return output
class Previously(SlideBase):
    def __init__(self) -> None:
        super().__init__("Previously on zkmarek")
        
    def construct(self):
        self.title_label = Text("Previously on zkmarek", font = PRIMARY_FONT, color = PRIMARY_COLOR).to_edge(UP)
        self.polynomial_chart = DiscreetePolynomialChart(p = 41, f = poly, label = "r", include_numbers=False, dot_color=SECONDARY_COLOR).scale(0.6).shift(3.7*LEFT+DOWN*0.2)
        self.polynomial_label = MathTex(r"p(x)", color = PRIMARY_COLOR).next_to(self.polynomial_chart, direction = RIGHT+UP, buff = 0).shift(DOWN*0.3+LEFT*2)

        self.polynomial_opening_label = MathTex(r"p(x) - y_0", color = PRIMARY_COLOR).next_to(self.polynomial_chart, RIGHT+UP, buff = 0).shift(DOWN*0.3+LEFT*2)
        self.quotient_deriviation_0 = MathTex(r"{{a}}{{(x_0-x_1)}}{{(x_0-x_2)}}{{(x_0 - x_0)}} = {{p(x_0)}} - {{y_0}}", color = PRIMARY_COLOR, font_size = 30).shift(UP*1.5+RIGHT*2.5)
        self.brace_0 = Brace(self.quotient_deriviation_0[3], direction = UP, color = PRIMARY_COLOR)
        self.brace_0.shift(DOWN*0.1)
        self.brace_text = Text("0", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 20)
        self.brace_0.put_at_tip(self.brace_text)
        self.brace_text.shift(DOWN*0.1)
        
        self.quotient_deriviation_1 = MathTex(r"{{a}}{{(x-x_1)}}{{(x-x_2)}}{{(x - x_0)}} = {{p(x)}} - {{y_0}}", font_size = 30, color = PRIMARY_COLOR).next_to(self.quotient_deriviation_0, DOWN, buff = 0.5)
        self.quotient_deriviation_1[0:4].set_color(SECONDARY_COLOR)
        
        self.quotient_deriviation_2 = MathTex(r"{{q(x)}}{{\cdot}}{{}}{{(x - x_0)}} = {{p(x)}} - {{y_0}}", font_size = 35, color = PRIMARY_COLOR).next_to(self.quotient_deriviation_1, DOWN, buff = 0.5)
        self.quotient_deriviation_2[0].set_color(SECONDARY_COLOR)
        
        self.commitment = MathTex(r"{{C}} = {{p(\tau)}} {{\cdot G_1}}", font_size = 35, color = PRIMARY_COLOR).shift(UP*1.5+RIGHT*1.5)
        self.proof = MathTex(r"{{\pi}} = {{q(\tau)}} {{\cdot G_1}}", font_size = 35, color = PRIMARY_COLOR).next_to(self.commitment, DOWN, buff = 0.5)
        
        self.pairing_verifiaction_0 = MathTex(r"e( {{\pi}}, ({{\tau}} -{{x_0}}) {{\cdot G_2}} ) = e({{C}} - {{y_0}} {{\cdot G_1}}, {{G_2}})", color = SECONDARY_COLOR).to_edge(DOWN).shift(RIGHT+UP*0.5)
        self.pairing_verifiaction_1 = MathTex(r"e( {{\pi}}{{}}, {{(\tau-x_0)}} {{\cdot G_2}} ) = e({{p(\tau)}} \cdot {{G_1}} - {{y_0}} {{\cdot G_1}}, {{G_2}})", color = SECONDARY_COLOR).to_edge(DOWN).shift(RIGHT+UP*0.5)        
        self.pairing_verifiaction_2 = MathTex(r"e( {{q(\tau)}}\cdot {{~G_1}}, {{(\tau-x_0)}} {{\cdot G_2}} ) = e({{p(\tau)}} \cdot {{G_1}} - {{y_0}} {{\cdot G_1}}, {{G_2}})", color = SECONDARY_COLOR).to_edge(DOWN).shift(RIGHT+UP*0.5)       
        self.pairing_verifiaction_3 = MathTex(
            r"q({{\tau}}) {{\cdot}} ({{\tau}}-x_0) = p({{\tau}}) - {{y_0}}",
            color=SECONDARY_COLOR,
        ).to_edge(DOWN).shift(RIGHT+UP*0.5)    


        self.tau = FieldElement(33, 41)
        self.value_at_tau = poly(self.tau)
        self.z = FieldElement(13, 41)
        self.y = poly(self.z)
        
        self.chart_interpolation = Chart(include_details=True)
        self.chart_interpolation.ax = Axes(
            x_range=[0, 11, 1],
            y_range=[-13, 10, 5],
            x_length=7,
            axis_config={
                "include_numbers": True,
                "color": PRIMARY_COLOR,
                "decimal_number_config": {
                    "color": PRIMARY_COLOR,
                    "num_decimal_places": 0
                }
            }
        )
        self.chart_interpolation.scale(0.7).shift(LEFT*3.5)
        self.chart_interpolation.ax.scale(0.7).shift(LEFT*3.5)
        self.chart_interpolation.labels[0].next_to(self.chart_interpolation.ax[0], RIGHT+UP, buff = 0.0)
        self.chart_interpolation.labels[1].next_to(self.chart_interpolation.ax[1], RIGHT+UP, buff = 0.0)
        self.chart_interpolation.graph4 = self.chart_interpolation.ax.plot_implicit_curve(
                lambda x, y: sum(((x+1)**k*np.sin(k*np.pi*(x+1)/3)+0.3) / np.math.factorial(k)/k**k/np.math.factorial(k)/k**k/k for k in range(1, 101)) - y,
                color=SECONDARY_COLOR)
        self.vector_values = MathTex(r"\left[{{3, }}{{4, }}{{2, }}{{-1, }}{{-2, }}{{\cdots}} \right]", color = SECONDARY_COLOR).next_to(self.chart_interpolation.ax, DOWN, buff = 0.5)
        
        self.data_points = Text("data points", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size = 30).shift(UP*1.5+RIGHT*2)
        self.interpolation = Text("interplolation", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size = 30).next_to(self.data_points, DOWN, buff = 1.5)
        self.vector_commitment = Text("vector commitment", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size = 30).next_to(self.interpolation, DOWN, buff = 1.5)
        
        self.arrow_data_interpolation = Arrow(self.data_points.get_bottom(), self.interpolation.get_top(), color = PRIMARY_COLOR, tip_shape = StealthTip)
        self.arrow_interpolation_vector = Arrow(self.interpolation.get_bottom(), self.vector_commitment.get_top(), color = PRIMARY_COLOR, tip_shape = StealthTip)

        self.blob = ImageMobject("data/images/blob.png").scale(0.7).shift(LEFT*2.5)
        self.blob_1 = self.blob.copy().scale(0.5).next_to(self.blob, LEFT, buff = 0.0)
        self.blob_2 = self.blob.copy().scale(0.5).next_to(self.blob, RIGHT, buff = 0.0)
        
        self.layer2 = Layer2()
        
        self.tree = VerkleTree().scale(0.5).shift(RIGHT*2.5+UP*1.5)
        
        
    def animate_in(self, scene):
        self.new_subsection(scene, "last time...", "data/sound/e6/slide1-0.mp3")
        scene.play(Write(self.title_label))
        self.polynomial_chart.gen_points()
        scene.play(FadeIn(self.polynomial_chart), Write(self.polynomial_label))
        
        self.new_subsection(scene, "kzg commitment scheme", "data/sound/e6/slide1-0a.mp3")
        scene.wait(3)
        self.bullet_list(scene)
        
        self.new_subsection(scene, "proof", "data/sound/e6/slide1-0b.mp3")
        scene.play(FadeOut(self.item1, self.item2, self.item3))
        line_z = self.polynomial_chart.animate_create_vertical_line(
            scene, self.z.value, self.y.value
        )
        self.polynomial_chart.animate_shift_dots_with_fade(scene, self.y.value)
        scene.play(TransformMatchingShapes(self.polynomial_label, self.polynomial_opening_label))
        scene.play(FadeOut(line_z))
        self.polynomial_chart.remove(line_z)
        self.polynomial_chart.animate_shift_dots_wrap_fix(scene, self.y.value)
        scene.play(FadeIn(self.quotient_deriviation_0))
        scene.play(FadeIn(self.brace_0, self.brace_text))
        scene.wait(1)
        scene.play(TransformMatchingShapes(self.quotient_deriviation_0.copy(), self.quotient_deriviation_1), FadeOut(self.brace_0, self.brace_text))
        scene.wait(1.5)
        scene.play(TransformMatchingShapes(self.quotient_deriviation_1.copy(), self.quotient_deriviation_2))
        
        
        self.new_subsection(scene, "comparing two pairings", "data/sound/e6/slide1-1.mp3")
        scene.play(FadeOut(self.quotient_deriviation_0, self.quotient_deriviation_1))
        self.quotient_deriviation_2.generate_target()
        self.quotient_deriviation_2.target.next_to(self.proof, DOWN, buff = 0.5).set_color(PRIMARY_COLOR)
        scene.play(MoveToTarget(self.quotient_deriviation_2))
        scene.play(Write(self.commitment), Write(self.proof))
        scene.play(Write(self.pairing_verifiaction_0))
        scene.wait(1)
        scene.play(Indicate(self.commitment, color = SECONDARY_COLOR))
        scene.play(Indicate(self.proof, color = SECONDARY_COLOR))
        scene.play(TransformMatchingShapes(self.pairing_verifiaction_0, self.pairing_verifiaction_1), Indicate(self.commitment, color = SECONDARY_COLOR))
        scene.wait(0.5)
        scene.play(TransformMatchingShapes(self.pairing_verifiaction_1, self.pairing_verifiaction_2), Indicate(self.proof, color = SECONDARY_COLOR))
        scene.wait(1.5)
        scene.play(TransformMatchingShapes(self.pairing_verifiaction_2, self.pairing_verifiaction_3))
        
        self.new_subsection(scene, "real data", "data/sound/e6/slide1-2.mp3")
        scene.wait(1.5)
        scene.play(FadeOut(self.quotient_deriviation_2, self.pairing_verifiaction_3, self.proof, self.commitment, self.polynomial_chart, self.polynomial_opening_label))
        scene.play(FadeIn(self.chart_interpolation.ax, self.chart_interpolation.labels))
        
        self.new_subsection(scene, "interpolation", "data/sound/e6/slide1-2a.mp3")
    
        scene.wait(1.5)
        self.dots_defining(scene)
        scene.play(Create(self.chart_interpolation.graph4))
        
        self.new_subsection(scene, "vector commitment", "data/sound/e6/slide1-2b.mp3")
        scene.wait(1)
        scene.play(Write(self.data_points))
        scene.play(GrowArrow(self.arrow_data_interpolation))
        scene.play(Write(self.interpolation))
        scene.play(GrowArrow(self.arrow_interpolation_vector))
        scene.play(Write(self.vector_commitment))
        
        self.new_subsection(scene, "blobs", "data/sound/e6/slide1-3.mp3")
        scene.play(FadeOut(self.point), FadeOut(self.chart_interpolation.ax, self.chart_interpolation.labels, self.chart_interpolation.graph4, self.vector_values, self.interpolation, self.vector_commitment, self.data_points, self.arrow_data_interpolation, self.arrow_interpolation_vector))

        scene.play(FadeIn(self.blob), run_time=0.5)
        scene.play(FadeIn(self.blob_1), run_time=0.5)
        scene.play(FadeIn(self.blob_2), run_time=0.5)
        # self.layer2.mini_blockchain_e6(scene)
        
        self.new_subsection(scene, "verkle trees", "data/sound/e6/slide1-3a.mp3")
        scene.play(FadeOut(self.blob, self.blob_1, self.blob_2), run_time=0.5)
        self.vast_data(scene)
        scene.play(Create(self.tree), run_time=1.5)
        scene.wait(1)
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.title_label, self.tree, self.binary_matrix))
        
        
        
    def bullet_list(self, scene):
        bullet1 = Text("(1)", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size = 30).shift(RIGHT+UP*1.5)
        bullet2 = Text("(2)", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size = 30).next_to(bullet1, DOWN)
        bullet3 = Text("(3)", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size = 30).next_to(bullet2, DOWN)
        item1 = Text("Polynomial", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size = 30).next_to(bullet1, RIGHT)
        item2 = Text("Quotient", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size = 30).next_to(bullet2, RIGHT)
        item3 = Text("Trusted setup", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size = 30).next_to(bullet3, RIGHT)
        
        polynomial_label = MathTex(r"p(x)", color = PRIMARY_COLOR, font_size = 40).next_to(item1, RIGHT)
        quotient_label = MathTex(r"q(x)", color = PRIMARY_COLOR, font_size = 40).next_to(item2, RIGHT)
        trusted_setup_label = MathTex(r"p(\tau) \cdot G_1, \quad q(\tau) \cdot G_1", font_size = 35, color = PRIMARY_COLOR).next_to(item3, DOWN)
        
        self.item1 = VGroup(bullet1, item1, polynomial_label)
        self.item2 = VGroup(bullet2, item2, quotient_label)
        self.item3 = VGroup(bullet3, item3, trusted_setup_label)
        
        scene.play(Write(self.item1))
        scene.wait(1.5)
        scene.play(Write(self.item2))
        scene.wait(1.5)
        scene.play(Write(self.item3))
        
    def dots_defining(self, scene):
        point0 = ValueTracker(0)  
        a0 = Curve.from_x(point0.get_value())   
        self.p0 = DotOnCurve(self.chart_interpolation.ax, "", a0) 
        point1 = ValueTracker(1)
        a1 = Curve.from_x(point1.get_value())
        self.p1 = DotOnCurve(self.chart_interpolation.ax, "", a1)   
        point2 = ValueTracker(2)
        a2 = Curve.from_x(point2.get_value())
        self.p2 = DotOnCurve(self.chart_interpolation.ax, "", a2)
        point3 = ValueTracker(3)
        a3 = Curve.from_x(point3.get_value())
        self.p3 = DotOnCurve(self.chart_interpolation.ax, "", a3)
        point4 = ValueTracker(4)
        a4 = Curve.from_x(point4.get_value())
        self.p4 = DotOnCurve(self.chart_interpolation.ax, "", a4)
        point5 = ValueTracker(5)
        a5 = Curve.from_x(point5.get_value())
        self.p5 = DotOnCurve(self.chart_interpolation.ax, "", a5)
        point6 = ValueTracker(6)
        a6 = Curve.from_x(point6.get_value())
        self.p6 = DotOnCurve(self.chart_interpolation.ax, "", a6)
        point7 = ValueTracker(7)
        a7 = Curve.from_x(point7.get_value())
        self.p7 = DotOnCurve(self.chart_interpolation.ax, "", a7)
        point8 = ValueTracker(8)
        a8 = Curve.from_x(point8.get_value())
        self.p8 = DotOnCurve(self.chart_interpolation.ax, "", a8)
        point9 = ValueTracker(9)
        a9 = Curve.from_x(point9.get_value())
        self.p9 = DotOnCurve(self.chart_interpolation.ax, "", a9)

        scene.play(Create(self.p0), FadeIn(self.vector_values[1], self.vector_values[0]), run_time=0.2)
        scene.play(Create(self.p1), FadeIn(self.vector_values[2]), run_time=0.2)
        scene.play(Create(self.p2), FadeIn(self.vector_values[3]), run_time=0.2)
        scene.play(Create(self.p3), FadeIn(self.vector_values[4]), run_time=0.2)
        scene.play(Create(self.p4), FadeIn(self.vector_values[5]), run_time=0.2)
        scene.play(Create(self.p5), FadeIn(self.vector_values[6], self.vector_values[7]), run_time=0.2)
        scene.play(Create(self.p6), run_time=0.2)
        scene.play(Create(self.p7), run_time=0.2)
        scene.play(Create(self.p8), run_time=0.2)
        scene.play(Create(self.p9), run_time=0.2)
        self.point = VGroup(self.p0, self.p1, self.p2, self.p3, self.p4, self.p5, self.p6, self.p7, self.p8, self.p9)

        scene.wait(1)
        
    def vast_data(self, scene):
        import random
        rows, cols = 10, 16 
        self.binary_matrix = VGroup(*[
            VGroup(*[
                Text(str(random.choice([0, 1])), font_size=24)
                for _ in range(cols)
            ]).arrange(RIGHT, buff=0.1)
            for _ in range(rows)
        ]).arrange(DOWN, buff=0.2)

        self.binary_matrix.move_to(LEFT*2)
        scene.add(self.binary_matrix)

        for _ in range(20):  
            new_rows = VGroup(*[
                VGroup(*[
                    Text(str(random.choice([0, 1])), font_size=24)
                    for _ in range(cols)
                ]).arrange(RIGHT, buff=0.1)
                for _ in range(rows)
            ]).arrange(DOWN, buff=0.2).move_to(LEFT*2)

            scene.play(*[
                Transform(self.binary_matrix[i], new_rows[i])
                for i in range(rows)
            ], run_time=0.1)
            