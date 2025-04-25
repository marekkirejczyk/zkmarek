from manim import (FadeIn, CurvedArrow, Write, Text, Create, RIGHT, UP, DOWN, LEFT, MathTex, ImageMobject, StealthTip, FadeOut,
                   Circle, MoveToTarget, Indicate)
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR, HIGHLIGHT_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.episode5.discrete_polynomial_chart_BLS import PolynomialOnCurve
from zkmarek.video.slides.episode4.discreete_polynomial_chart import DiscreetePolynomialChart
from zkmarek.crypto.field_element import FieldElement
from zkmarek.crypto.weierstrass_curve import BLS12381_137
from zkmarek.crypto.weierstrass_curve import BanderSnatch
from zkmarek.video.mobjects.continuous_elliptic_chart import ContinuousEllipticChart
from zkmarek.video.slides.episode4.chart import Chart

def poly(x):
    output = FieldElement(4, x.order)*x**3 - FieldElement(8, x.order)*x**2 - FieldElement(17, x.order)*x + FieldElement(30, x.order)
    return output

class EllipticCurves(SlideBase):
    def __init__(self) -> None:
        super().__init__("Elliptic curves")
        
    def construct(self):
        self.title_label = Text("Elliptic curves", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 40).to_edge(UP)
        
        self.chart_ec_continuous = ContinuousEllipticChart(include_details=False, curve_color=HIGHLIGHT_COLOR, b = 4).scale(0.8)
        self.formula_bls = MathTex(r"{{y^2}} = {{x^3}} + {{4}}", color = HIGHLIGHT_COLOR, font_size=34).next_to(self.chart_ec_continuous, DOWN)
        self.blob = ImageMobject("data/images/blob.png").scale(0.3).next_to(self.chart_ec_continuous, LEFT+UP*0.2, buff = 0.1).shift(LEFT*0.8+DOWN)
        self.blob2 = self.blob.copy().scale(0.75).next_to(self.blob, RIGHT, buff = 0.0)
        self.blob3 = self.blob.copy().scale(0.75).next_to(self.blob, LEFT, buff = 0.0)
        self.chart_scalar = DiscreetePolynomialChart(p=41, f=poly, label = "r", include_numbers=False, dot_color=SECONDARY_COLOR).scale(0.6).shift(RIGHT*3+DOWN*0.5)
        self.chart_ec = PolynomialOnCurve(curve=BLS12381_137, dot_color=HIGHLIGHT_COLOR, label = "p", include_numbers=False).scale(0.7).shift(DOWN*0.1)
        self.chart_bander = PolynomialOnCurve(curve=BanderSnatch, dot_color=HIGHLIGHT_COLOR, label = "p", include_numbers=False).scale(0.6).shift(LEFT*3+DOWN*0.5)

        self.p = MathTex(r"{{p}} \approx 2^{381}", color = HIGHLIGHT_COLOR, font_size = 32).next_to(self.chart_ec, LEFT).shift(UP * 0.2)
        self.r = MathTex(r"{{r}} \approx 2^{256}", color = SECONDARY_COLOR, font_size = 32).next_to(self.chart_scalar, RIGHT)
        self.bytes_p2 = MathTex(r"\sim {{48}} \ \mathrm{B}", color = HIGHLIGHT_COLOR, font_size = 32).next_to(self.p[1], DOWN)
        
        self.bytes_of_el = Text("32 B", font=PRIMARY_FONT, font_size = 24).set_color(HIGHLIGHT_COLOR)
        self.bytes_of_el.next_to(self.r, UP)
        self.sim_32 = MathTex(r"\sim", color = HIGHLIGHT_COLOR, font_size = 32).next_to(self.bytes_of_el, LEFT, buff = 0.1)
        self.curve_ec = Text("BLS12-381", color = HIGHLIGHT_COLOR, font =  PRIMARY_FONT, font_size=34).next_to(self.chart_ec, UP, buff = 0.05)
        self.curve_ec_bander = Text("BanderSnatch", color = HIGHLIGHT_COLOR, font =  PRIMARY_FONT, font_size=34).to_edge(DOWN)
        
        self.base_field = Text("Base field", color = HIGHLIGHT_COLOR, font = PRIMARY_FONT, font_size = 28).next_to(self.chart_ec, LEFT+UP).shift(RIGHT*0.3)
        self.arrow_base_field = CurvedArrow(self.base_field.get_right(), self.chart_ec.get_top()+LEFT+UP*0.6, tip_shape=StealthTip, 
                               stroke_width=2).set_color_by_gradient([HIGHLIGHT_COLOR, HIGHLIGHT_COLOR]).scale(0.6).rotate(angle=3.14, axis = [1, 0, 0])
        self.scalar_field = Text("Scalar field", color = SECONDARY_COLOR, font = PRIMARY_FONT, font_size = 28).next_to(self.chart_scalar, RIGHT+UP, buff = 0).shift(LEFT*0.8)
        self.arrow_scalar_field = CurvedArrow(self.scalar_field.get_left()+DOWN*0.05, self.chart_scalar.get_top()+RIGHT*0.3, tip_shape=StealthTip, 
                               stroke_width=2).set_color(SECONDARY_COLOR).scale(0.6)
        self.formula_bls = MathTex(r"{{y^2}} = {{x^3}} + {{4}}", color = HIGHLIGHT_COLOR, font_size=34).next_to(self.chart_ec, DOWN).shift(DOWN*0.3)
        self.formula_polynomial = MathTex(r"{{P(x)}} = \sum_{k=0}^{4095} {{a_k}}  {{x^k}}", color = SECONDARY_COLOR, font_size=32).next_to(self.chart_scalar, DOWN)
        
        self.chart_polynomial_continuous = Chart(include_details=False).scale(0.6).shift(DOWN*0.2)
        
        self.point_to_generator = self.chart_ec.get_point(FieldElement(4, 137))
        self.circle_gen = Circle(radius = 0.3, color = HIGHLIGHT_COLOR).move_to(self.point_to_generator.get_center())
        self.point_to_generator_label = MathTex(r"{{G \cdot 1}}", color = HIGHLIGHT_COLOR, font_size = 32).next_to(self.point_to_generator, UP+RIGHT*0.2)
        
        
    def animate_in(self, scene):
        self.new_subsection(scene, "kzg->elliptic curves", "data/sound/e7/slide2-1.mp3")
        scene.play(Write(self.title_label), run_time=0.7)
        scene.wait(0.5)
        scene.play(Create(self.chart_ec_continuous), run_time=1.5)
        
        self.new_subsection(scene, "BLS12-381", "data/sound/e7/slide2-1a.mp3")
        scene.wait(2)
        scene.play(Write(self.curve_ec), run_time=0.7)
        scene.play(Write(self.formula_bls), run_time=0.7)
        scene.wait(2)
        scene.play(FadeIn(self.blob), run_time=1)
        scene.play(FadeIn(self.blob2), run_time=0.3)
        scene.play(FadeIn(self.blob3), run_time=0.3)
        
        self.new_subsection(scene, "over finite field", "data/sound/e7/slide2-2.mp3")
        scene.play(FadeOut(self.blob, self.blob2, self.blob3), run_time=0.5)
        scene.wait(1.5)
        scene.play(FadeOut(self.chart_ec_continuous), FadeIn(self.chart_ec), run_time=0.5)
        
        self.new_subsection(scene, "2^381", "data/sound/e7/slide2-3.mp3")
        scene.wait(2)
        scene.play(Write(self.p), run_time=0.7)
        
        self.new_subsection(scene, "48 bytes", "data/sound/e7/slide2-4.mp3")
        scene.play(FadeIn(self.bytes_p2))
        
        self.new_subsection(scene, "generator", "data/sound/e7/slide2-5.mp3")
        scene.wait(1)
        scene.play(Create(self.circle_gen), run_time=1)
        scene.play(Create(self.point_to_generator), run_time=0.5)
        scene.play(Write(self.point_to_generator_label), run_time=0.5)
        
        self.new_subsection(scene, "scalar field", "data/sound/e7/slide2-6.mp3")
        self.chart_ec.generate_target()
        self.chart_ec.target.shift(LEFT*3)
        self.curve_ec.generate_target()
        self.curve_ec.target.shift(LEFT*3)
        
        self.p.generate_target()
        self.p.target.shift(LEFT*3)
        self.bytes_p2.generate_target()
        self.bytes_p2.target.shift(LEFT*3)
        scene.play(MoveToTarget(self.chart_ec), MoveToTarget(self.curve_ec), MoveToTarget(self.p), MoveToTarget(self.bytes_p2), FadeOut(self.point_to_generator_label, self.circle_gen), run_time=1)
        self.chart_scalar.gen_points()
        scene.play(Create(self.chart_scalar), run_time=1)
        scene.wait(1)
        scene.play(Write(self.scalar_field), Write(self.arrow_scalar_field), run_time=0.5)
        scene.wait(2)
        scene.play(Write(self.r), run_time=0.7)
        scene.wait(1)
        scene.play(Write(self.bytes_of_el), Write(self.sim_32), run_time=0.7)
        
        self.new_subsection(scene, "kzg: eval scalars, proof ec", "data/sound/e7/slide2-7.mp3")
        scene.wait(1)
        scene.play(Write(self.formula_polynomial), run_time=0.7)
        scene.wait(1)
        scene.play(Indicate(self.bytes_of_el), run_time=0.9)
        scene.wait(2)
        scene.play(Indicate(self.bytes_p2), run_time=0.9)
        
        self.new_subsection(scene, "BanderSnatch", "data/sound/e7/slide2-8.mp3")
        scene.wait(1)
        scene.play(FadeOut(self.chart_ec), FadeIn(self.chart_bander), run_time=1)
        scene.play(FadeOut(self.curve_ec), FadeIn(self.curve_ec_bander), FadeOut(self.formula_bls), run_time=1)
        
        self.new_subsection(scene, "pairings", "data/sound/e7/slide2-9.mp3")
        

        
        