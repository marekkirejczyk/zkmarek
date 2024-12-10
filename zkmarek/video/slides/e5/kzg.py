from manim import (FadeIn, FadeOut, MathTex, Text, LEFT, RIGHT, DOWN, UP, Write, PURPLE, BLUE_E, Group, TEAL_E, Brace, MAROON_E, Arrow, 
                   StealthTip, GrowArrow, Indicate, PINK, ImageMobject, MoveToTarget, CurvedArrow, GREEN_E, AddTextLetterByLetter, ApplyWave)
from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR, HIGHLIGHT_COLOR, PRIMARY_FONT, HIGHLIGHT2_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.e5.discrete_polynomial_chart_BLS import PolynomialOnCurve
from zkmarek.video.slides.e4.discreete_polynomial_chart import DiscreetePolynomialChart
from zkmarek.crypto.field_element import FieldElement
from zkmarek.crypto.weierstrass_curve import BLS12381_137

def poly(x):
    output = FieldElement(4, x.order)*x**3 - FieldElement(8, x.order)*x**2 - FieldElement(17, x.order)*x + FieldElement(30, x.order)
    return output


class KZGBlobs(SlideBase):
    def __init__(self) -> None:
        super().__init__(title="KZG as a vector commitment")
        
    def construct(self):
        self.title_text = Text("KZG as a vector commitment", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 40).to_edge(UP)
        self.committer = ImageMobject("data/images/person.png").scale(0.7).shift(LEFT*5)
        self.committer_label = Text("Committer", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size = 30).next_to(self.committer, DOWN)
        self.verifier = ImageMobject("data/images/person_blue.png").scale(0.7).shift(RIGHT*5)
        self.verifier_label = Text("Verifier", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 30).next_to(self.verifier, DOWN)
        self.number_sequence = MathTex(r"\left[ {{y_0}}, {{y_1}}, {{y_2}}, {{\cdots}}, {{y_{4095}}} \right]", color = SECONDARY_COLOR).scale(1.2).shift(UP*2.3)
        self.brace_number = Brace(self.number_sequence, RIGHT).set_color_by_gradient([PURPLE, SECONDARY_COLOR])
        self.number_sequence_kilo_bytes = Text("128 kB", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size=24)
        self.brace_number.put_at_tip(self.number_sequence_kilo_bytes)
        self.sim = MathTex(r"\sim", color = PRIMARY_COLOR).next_to(self.number_sequence_kilo_bytes, LEFT, buff = 0).scale(0.5).shift(RIGHT*0.05)
        
        self.polynomial = MathTex("p(x)", color = PRIMARY_COLOR).next_to(self.committer, RIGHT).shift(RIGHT)
        self.opening = MathTex(r"p(x_0) \stackrel{?}{=} y_0", color = TEAL_E).next_to(self.verifier, UP)

        self.arrow_opening_committer = Arrow(self.committer.get_right(), self.polynomial.get_left(), tip_shape=StealthTip, 
                               stroke_width=2, max_tip_length_to_length_ratio=0.15).set_color_by_gradient([HIGHLIGHT2_COLOR, SECONDARY_COLOR])
        
        self.commitment = MathTex(r"{{C}} = {{p}}({{\tau}}) \cdot {{G_1}}").set_color_by_gradient([BLUE_E, TEAL_E]).next_to(self.polynomial, RIGHT).shift(RIGHT)
        self.proof = MathTex(r"{{\pi}} = {{q}} ({{\tau}}) \cdot {{G_1}}").set_color_by_gradient([MAROON_E, PURPLE]).next_to(self.polynomial, DOWN).shift(DOWN)
        
        self.arrow_number_sequence_poly = Arrow(self.number_sequence.get_bottom(), self.polynomial.get_top(), tip_shape=StealthTip, 
                               stroke_width=2, max_tip_length_to_length_ratio=0.15).set_color_by_gradient([HIGHLIGHT2_COLOR, SECONDARY_COLOR])
        self.arrow_poly_commitment = Arrow(self.polynomial.get_right(), self.commitment.get_left(), tip_shape=StealthTip, 
                               stroke_width=2, max_tip_length_to_length_ratio=0.15).set_color_by_gradient([HIGHLIGHT2_COLOR, SECONDARY_COLOR])
        self.arrow_poly_proof = Arrow(self.polynomial.get_bottom(), self.proof.get_top(), tip_shape=StealthTip, 
                               stroke_width=2, max_tip_length_to_length_ratio=0.15).set_color_by_gradient([HIGHLIGHT2_COLOR, SECONDARY_COLOR])

        self.chart_scalar = DiscreetePolynomialChart(p=41, f=poly, label = "r", include_numbers=False, dot_color=SECONDARY_COLOR).scale(0.6).shift(RIGHT*3+DOWN*0.5)
        self.chart_ec = PolynomialOnCurve(curve=BLS12381_137, dot_color=HIGHLIGHT_COLOR, label = "p", include_numbers=False).scale(0.6).shift(LEFT*3+DOWN*0.5)

        self.p = MathTex(r"{{p}} \approx 2^{381}", color = HIGHLIGHT_COLOR, font_size = 32).next_to(self.chart_ec, LEFT)
        self.r = MathTex(r"{{r}} \approx 2^{256}", color = SECONDARY_COLOR, font_size = 32).next_to(self.chart_scalar, RIGHT)
        self.bytes_p2 = MathTex(r"\sim {{48}} \ \mathrm{B}", color = HIGHLIGHT_COLOR, font_size = 32).next_to(self.p[1], DOWN)
        
        self.bytes_of_el = Text("32 B", font=PRIMARY_FONT, font_size = 24).set_color(HIGHLIGHT_COLOR)
        self.bytes_of_el.next_to(self.number_sequence[3], UP)
        self.curve_ec = Text("BLS12-381", color = HIGHLIGHT_COLOR, font =  PRIMARY_FONT, font_size=34).to_edge(DOWN)
        
        self.base_field = Text("Base field", color = HIGHLIGHT_COLOR, font = PRIMARY_FONT, font_size = 28).next_to(self.chart_ec, LEFT+UP).shift(RIGHT*0.3)
        self.arrow_base_field = CurvedArrow(self.base_field.get_right(), self.chart_ec.get_top()+LEFT+UP*0.6, tip_shape=StealthTip, 
                               stroke_width=2).set_color_by_gradient([GREEN_E, HIGHLIGHT_COLOR]).scale(0.6).rotate(angle=3.14, axis = [1, 0, 0])
        self.scalar_field = Text("Scalar field", color = SECONDARY_COLOR, font = PRIMARY_FONT, font_size = 28).next_to(self.chart_scalar, RIGHT+UP, buff = 0).shift(LEFT*0.8)
        self.arrow_scalar_field = CurvedArrow(self.scalar_field.get_left()+DOWN*0.5, self.chart_scalar.get_top()+RIGHT*0.7, tip_shape=StealthTip, 
                               stroke_width=2).set_color_by_gradient([SECONDARY_COLOR, PURPLE]).scale(0.6)
        self.formula_bls = MathTex(r"{{y^2}} = {{x^3}} + {{4}}", color = HIGHLIGHT_COLOR, font_size=34).next_to(self.chart_ec, DOWN).shift(DOWN*0.3)
        self.formula_polynomial = MathTex(r"{{P(x)}} = \sum_{k=0}^{4095} {{a_k}}  {{x_k}}", color = SECONDARY_COLOR, font_size=32).next_to(self.chart_scalar, DOWN)
        
    def animate_in(self, scene):
        self.new_subsection(scene, "prime fields", "data/sound/e5/slide4-0.mp3")
        scene.play(Write(self.title_text), run_time=0.7)
        self.chart_scalar.gen_points()
        scene.play(FadeIn(self.chart_scalar, self.scalar_field), Write(self.arrow_scalar_field))
        self.chart_ec.gen_points()
        scene.play(FadeIn(self.chart_ec, self.base_field), Write(self.arrow_base_field))
        
        self.new_subsection(scene, "p - base field, r - scalar field", "data/sound/e5/slide4-0a.mp3")
        scene.wait(1)
        scene.play(AddTextLetterByLetter(self.curve_ec), run_time=1)
        scene.play(Write(self.formula_bls), run_time=0.7)
        scene.play(Write(self.formula_polynomial), run_time=0.7)
        scene.wait(0.4)
        scene.play(ApplyWave(self.chart_ec.ax), FadeIn(self.p))
        scene.play(Indicate(self.p, color = PINK))
        scene.wait(2.5)
        scene.play(Indicate(self.chart_scalar, color = PURPLE, scale_factor=1.05), run_time=1)
        scene.wait(1)
        scene.play(FadeIn(self.r), ApplyWave(self.chart_scalar.ax))
        scene.wait(1)
        scene.play(Indicate(self.r, color = PURPLE), run_time=1)
        scene.wait(2)
        
        self.new_subsection(scene, "blob elements", "data/sound/e5/slide4-0b.mp3")
        scene.wait(1.3)
        scene.play(Write(self.number_sequence))
        self.x_k = FieldElement(32, 41)
        self.y_k = poly(self.x_k)
        self.label_x_k = self.chart_scalar.add_xaxis_label(self.x_k.value, r"x_k")
        self.label_y_k = self.chart_scalar.add_yaxis_label(self.y_k.value, r"y_k")
        line_x_k = self.chart_scalar.animate_create_vertical_line(
            scene, self.x_k.value, self.y_k.value
        )
        line_y_k = self.chart_scalar.animate_create_horizontal_line(scene, self.y_k.value, 0, self.x_k.value)
        scene.wait(2.8)
        scene.play(FadeIn(self.bytes_of_el))
        self.number_sequence[3].set_color(GREEN_E)
        
        scene.wait(3)
        scene.play(FadeOut(line_x_k, line_y_k, self.bytes_of_el, self.label_y_k, self.label_x_k))
        self.number_sequence[3].set_color(SECONDARY_COLOR)
        
        self.new_subsection(scene, "kzg setup ec points - BLS", "data/sound/e5/slide4-1.mp3")
        scene.wait(2)
        scene.play(Indicate(self.chart_ec, scale_factor=1.05, color = PURPLE))
        scene.wait(1)
        scene.play(FadeIn(self.bytes_p2))
        scene.wait(3.7)
        scene.play(FadeOut(self.chart_scalar, self.bytes_p2, self.curve_ec, self.chart_ec, self.p, self.r,self.base_field, 
                           self.scalar_field, self.arrow_base_field, self.arrow_scalar_field, self.formula_bls, self.formula_polynomial))
        
        
        self.new_subsection(scene, "put it all together", "data/sound/e5/slide4-2.mp3")
        scene.play(FadeIn(self.verifier, self.committer))
        scene.play(Write(self.verifier_label), Write(self.committer_label))
        scene.play(Write(self.polynomial), GrowArrow(self.arrow_opening_committer), run_time=0.7)
        scene.wait(1.5)
        scene.play(GrowArrow(self.arrow_poly_commitment), Write(self.commitment))
        scene.wait(2.1)
        
        self.new_subsection(scene, "proof", "data/sound/e5/slide4-2a.mp3")
        scene.wait(1.8)
        scene.play(Write(self.opening))
        scene.wait(2.5)
        scene.play(GrowArrow(self.arrow_poly_proof))
        scene.play(Write(self.proof))
        scene.wait(2.5)
        
        scene.play(FadeOut(self.opening, self.arrow_opening_committer))
        self.group_poly = Group(self.polynomial, self.arrow_poly_commitment, self.arrow_poly_proof, self.proof, self.commitment)
        self.group_poly.generate_target()
        self.group_poly.target.next_to(self.number_sequence, DOWN).shift(DOWN)
        scene.play(MoveToTarget(self.group_poly))
        
        self.new_subsection(scene, "compresses 128 kB data", "data/sound/e5/slide4-3.mp3")
        scene.play(Indicate(self.polynomial, color = PINK), Indicate(self.number_sequence, color = PINK))
        scene.wait(2.0)
        scene.play(FadeIn(self.number_sequence_kilo_bytes, self.brace_number, self.sim), run_time=0.7)
        scene.play(Indicate(self.number_sequence_kilo_bytes, color = HIGHLIGHT_COLOR))
        scene.wait(3)
        self.proof_bytes = Text("48 B", font = PRIMARY_FONT, font_size=24).set_color_by_gradient([TEAL_E, HIGHLIGHT_COLOR])
        self.commitment_bytes = Text("48 B", font = PRIMARY_FONT, font_size=24).set_color_by_gradient([HIGHLIGHT_COLOR, TEAL_E])
        self.brace_commitment = Brace(self.commitment, RIGHT).set_color_by_gradient([HIGHLIGHT_COLOR, TEAL_E])
        self.brace_proof = Brace(self.proof, RIGHT).set_color_by_gradient([TEAL_E, HIGHLIGHT_COLOR])
        self.brace_commitment.put_at_tip(self.commitment_bytes)
        self.brace_proof.put_at_tip(self.proof_bytes)
        self.sim_commitment = MathTex(r"\sim").set_color_by_gradient([HIGHLIGHT_COLOR, TEAL_E]).next_to(self.commitment_bytes, LEFT, buff = 0).scale(0.5).shift(RIGHT*0.05)
        self.sim_proof = MathTex(r"\sim").set_color_by_gradient([TEAL_E, HIGHLIGHT_COLOR]).next_to(self.proof_bytes, LEFT, buff = 0).scale(0.5).shift(RIGHT*0.05)
        scene.play(FadeIn(self.brace_commitment, self.commitment_bytes, self.sim_commitment))
        scene.wait(3.2)
        scene.play(FadeIn(self.brace_proof, self.proof_bytes, self.sim_proof))
        scene.wait(3.8) 
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.title_text, self.number_sequence, self.number_sequence_kilo_bytes, self.polynomial, self.arrow_poly_commitment,  
                           self.arrow_poly_proof, self.proof_bytes,self.brace_proof, 
                           self.commitment_bytes, self.brace_commitment, self.sim, 
                           self.brace_number, self.commitment, self.proof, self.verifier, self.committer,
                           self.committer_label, self.verifier_label, self.sim, self.sim_commitment, self.sim_proof))