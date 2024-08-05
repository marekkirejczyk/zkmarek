from manim import DOWN, UP, RIGHT, FadeIn, FadeOut, MathTex, ValueTracker, Text, Create, Write, TransformMatchingShapes, VGroup, Indicate, ImageMobject, MoveToTarget, ReplacementTransform

from numpy import linspace
from zkmarek.video.constant import SECONDARY_COLOR, PRIMARY_FONT, PRIMARY_COLOR, HIGHLIGHT_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.mobjects.dot_on_curve import DotOnCurve
from zkmarek.video.slides.e4.chart import Chart
from zkmarek.video.slides.e4.curve import Curve

class Polynomials(SlideBase):

    def __init__(self):
        super().__init__("Polynomials")

    def construct(self):
        self.title_label = Text("Polynomials", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 40).to_edge(UP)
        self.x = MathTex(r"x", color = SECONDARY_COLOR).next_to(self.title_label, DOWN)  
        self.polynomial_eqn1 = MathTex(r"P(x) = x", color = SECONDARY_COLOR)     
        self.polynomial_eqn = MathTex(r"P(x) = {{a_n}} \cdot {{x^n}} + {{a_{n-1} }}\cdot {{x^{n-1} }} + \cdots + {{a_1}} \cdot {{x}} + {{a_0}}", color = SECONDARY_COLOR)
        self.polynomial_eqn2 = MathTex(r"P(x) = {{x}}^n + {{x}}^{n-1} + \cdots + {{x}}", color = SECONDARY_COLOR)
        self.polynomial = MathTex(r"P(x) = 2 x^2 + 3x - 2", color = SECONDARY_COLOR).to_edge(DOWN)
        self.polynomial2 = MathTex(r"P(x) = 2 x^2 + 3x - 2 = (2x-1)(x+2)", color = SECONDARY_COLOR).to_edge(DOWN)

        self.proof = ImageMobject("data/images/Proof.png")
        self.verifying = ImageMobject("data/images/Docs.png")

        self.chart = Chart(include_details=False).scale(0.6).next_to(self.title_label, DOWN).shift(DOWN)
        self.p1_1 = ValueTracker(1)
        a1_1 = Curve.from_x(self.p1_1.get_value())
        self.p1 = DotOnCurve(self.chart.ax, "(1,3)", a1_1)

        self.p2_10 = ValueTracker(2)
        a2_10 = Curve.from_x(self.p2_10.get_value())
        self.p2 = DotOnCurve(self.chart.ax, "(2,12)", a2_10)

        self.p3_23 = ValueTracker(3)
        a3_23 = Curve.from_x(self.p3_23.get_value())
        self.p3 = DotOnCurve(self.chart.ax, "(3,25)", a3_23)

        self.poly_point1 = MathTex("P(1) = 3", color = PRIMARY_COLOR).to_edge(RIGHT)
        self.poly_point2 = MathTex("P(2) = 12", color = PRIMARY_COLOR).next_to(self.poly_point1, DOWN)
        self.poly_point3 = MathTex("P(3) = 25", color = PRIMARY_COLOR).next_to(self.poly_point2, DOWN)

        self.p25 = ValueTracker(-2)
        a25 = Curve.from_x(self.p25.get_value())
        self.root1 = DotOnCurve(self.chart.ax, "(-2,0)", a25)

        self.point = []
        self.N = 30 # n/o of points
        self.values = linspace(-4.5, 3, self.N)
        for i in range(self.N):
            point_value = self.values[i]
            points = ValueTracker(point_value)
            a = Curve.from_x(points.get_value())
            self.point.append(DotOnCurve(self.chart.ax, "", a)) 


    def animate_in(self, scene):
        self.new_subsection(scene, "intro", "data/sound/e4/slide1-0.mp3")
        scene.play(Write(self.title_label))
        scene.wait(3)
        scene.play(FadeIn(self.x))
        scene.wait(2)

        scene.play(FadeIn(self.polynomial_eqn1))
        scene.play(TransformMatchingShapes(VGroup(self.x.copy(), self.polynomial_eqn1), self.polynomial_eqn2), run_time=2)

        scene.play(Indicate(self.polynomial_eqn2[1], color = HIGHLIGHT_COLOR), run_time=0.5)
        scene.play(Indicate(self.polynomial_eqn2[3], color = HIGHLIGHT_COLOR), run_time=0.5)
        scene.play(Indicate(self.polynomial_eqn2[5], color = HIGHLIGHT_COLOR), run_time=0.5)

        scene.play(TransformMatchingShapes(self.polynomial_eqn2, self.polynomial_eqn), run_time=2)

        scene.play(Indicate(self.polynomial_eqn[1], color = HIGHLIGHT_COLOR), run_time=0.5)
        scene.play(Indicate(self.polynomial_eqn[5], color = HIGHLIGHT_COLOR), run_time=0.5)
        scene.play(Indicate(self.polynomial_eqn[9], color = HIGHLIGHT_COLOR), run_time=0.5)
        scene.play(Indicate(self.polynomial_eqn[13], color = HIGHLIGHT_COLOR), run_time=0.5)
        

        self.new_subsection(scene, "crypto", "data/sound/e4/slide1-1.mp3")
        self.polynomial_eqn.generate_target()
        self.polynomial_eqn.target.to_edge(DOWN).scale(0.7)
        scene.play(FadeOut(self.x), MoveToTarget(self.polynomial_eqn), run_time=2)
        scene.play(FadeIn(self.verifying))
        scene.wait(3)
        scene.play(ReplacementTransform(self.verifying, self.proof), run_time=1.5)

        self.new_subsection(scene, "specific eqn", "data/sound/e4/slide1-2.mp3")
        scene.play(FadeOut(self.proof))
        scene.wait(1)
        scene.play(Create(self.chart.ax), run_time=2)
        scene.wait(1.5)
        scene.play(Create(self.p1.dot))
        scene.play(Write(self.p1.label))
        scene.play(Create(self.p2.dot))
        scene.play(Write(self.p2.label))
        scene.play(Create(self.p3.dot))
        scene.play(Write(self.p3.label))
        scene.wait(0.5)
        scene.play(Indicate(self.polynomial_eqn, color = PRIMARY_COLOR))
        scene.wait(1)
        scene.play(TransformMatchingShapes(self.p1.label.copy(), self.poly_point1))
        scene.play(TransformMatchingShapes(self.p2.label.copy(), self.poly_point2))
        scene.play(TransformMatchingShapes(self.p3.label.copy(), self.poly_point3))

        self.new_subsection(scene, "interpolation", "data/sound/e4/slide1-3.mp3")
        scene.play(Write(self.chart.graph))
        scene.wait(3)
        for i in range(self.N):
            point = self.point[i]
            scene.play(Create(point.dot), run_time=0.05)
        scene.wait(2)
        scene.play(TransformMatchingShapes(self.polynomial_eqn, self.polynomial))
        scene.wait(1)
        for i in range(self.N):
            point = self.point[i]
            scene.play(FadeOut(point.dot), run_time=0.05)

        self.new_subsection(scene, "roots", "data/sound/e4/slide1-4.mp3")
        scene.wait(2)
        scene.play(Indicate(self.p1.dot))
        self.root1.shift(UP)
        scene.play(Create(self.root1))
        scene.play(Indicate(self.root1))
        scene.play(TransformMatchingShapes(self.polynomial, self.polynomial2))
        scene.wait(4)

    def animate_out(self, scene):
        scene.play(FadeOut(self.chart.graph, self.title_label, self.p1.dot, self.p1.label, self.p2.dot, self.p2.label, self.p3.dot, self.p3.label, self.root1))
