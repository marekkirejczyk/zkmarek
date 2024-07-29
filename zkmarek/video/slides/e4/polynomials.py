from manim import DOWN, UP, FadeIn, FadeOut, MathTex, ValueTracker, Text, Create, Write, TransformMatchingShapes, VGroup

from zkmarek.video.constant import SECONDARY_COLOR, PRIMARY_FONT, PRIMARY_COLOR
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
        self.polynomial_eqn = MathTex(r"P(x) = a_n \cdot x^n + a_{n-1}\cdot x^{n-1} + \cdots + a_1 \cdot x + a_0", color = SECONDARY_COLOR)
        self.polynomial_eqn1 = MathTex(r"P(x) = a_n \cdot x^n ", color = SECONDARY_COLOR)
        self.polynomial_eqn2 = MathTex(r"P(x) = a_n \cdot x^n + a_{n-1}\cdot x^{n-1} ", color = SECONDARY_COLOR)
        
        self.chart = Chart(include_details=True).scale(0.6).next_to(self.title_label, DOWN)
        self.p1_1 = ValueTracker(1)
        a1_1 = Curve.from_x(self.p1_1.get_value())
        self.p1 = DotOnCurve(self.chart.ax, "(1,1)", a1_1)

        self.p2_10 = ValueTracker(2)
        a2_10 = Curve.from_x(self.p2_10.get_value())
        self.p2 = DotOnCurve(self.chart.ax, "(2,10)", a2_10)

        self.p3_23 = ValueTracker(3)
        a3_23 = Curve.from_x(self.p3_23.get_value())
        self.p3 = DotOnCurve(self.chart.ax, "(3,23)", a3_23)

    def animate_in(self, scene):
        self.new_subsection(scene, "intro", "data/sound/e4/slide1-0.mp3")
        scene.play(Write(self.title_label))
        scene.play(FadeIn(self.x))
        scene.play(FadeIn(self.polynomial_eqn1))
        scene.play(TransformMatchingShapes(VGroup(self.x.copy(), self.polynomial_eqn1), self.polynomial_eqn2))
        scene.play(TransformMatchingShapes(VGroup(self.x.copy(), self.polynomial_eqn2), self.polynomial_eqn))

        self.new_subsection(scene, "crypto", "data/sound/e4/slide1-1.mp3")
        scene.play(FadeOut(self.polynomial_eqn, self.x))

        self.new_subsection(scene, "specific eqn", "data/sound/e4/slide1-2.mp3")
        scene.play(Create(self.p1.dot))
        scene.play(Create(self.p2.dot))
        scene.play(Create(self.p3.dot))
        scene.play(Write(self.p1.label))
        scene.play(Write(self.p2.label))
        scene.play(Write(self.p3.label))

        self.new_subsection(scene, "interpolation", "data/sound/e4/slide1-3.mp3")

        self.chart.animate_in(scene)

        self.new_subsection(scene, "roots", "data/sound/e4/slide1-4.mp3")
