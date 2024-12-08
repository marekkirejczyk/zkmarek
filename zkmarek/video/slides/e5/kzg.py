from manim import (FadeIn, FadeOut, MathTex, Text, LEFT, RIGHT, DOWN, UP, Write, PURPLE, BLUE_E, Group, TEAL_E, Brace, MAROON_E, Arrow, 
                   StealthTip, GrowArrow, Indicate, PINK, ImageMobject, MoveToTarget, CurvedArrow, PI, GREEN_E)
from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR, HIGHLIGHT_COLOR, PRIMARY_FONT, HIGHLIGHT2_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.e5.discrete_polynomial_chart_BLS import PolynomialOnCurve
from zkmarek.crypto.field_element import FieldElement
from zkmarek.crypto.weierstrass_curve import BN254

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

        self.chart_ec = PolynomialOnCurve(polynomial=poly, dot_color=HIGHLIGHT_COLOR).scale(0.6).shift(LEFT*2.5+DOWN)
        self.chart_field = PolynomialOnCurve(polynomial=poly, curve=BN254, dot_color = SECONDARY_COLOR).scale(0.6).shift(RIGHT*2.5+DOWN)
        
        self.p1 = MathTex(r"{{p_1}} \approx 2^{254}", color = SECONDARY_COLOR, font_size = 32).next_to(self.chart_field, RIGHT)
        self.p2 = MathTex(r"{{p_2}} \approx 2^{381}", color = HIGHLIGHT_COLOR, font_size = 32).next_to(self.chart_ec, LEFT)
        self.bytes_p1 = MathTex(r"\sim {{32}} \ \mathrm{B}", color = SECONDARY_COLOR, font_size = 32).next_to(self.p1[1], DOWN)
        self.bytes_p2 = MathTex(r"\sim {{48}} \ \mathrm{B}", color = HIGHLIGHT_COLOR, font_size = 32).next_to(self.p2[1], DOWN)
        
        self.curve_field = Text("BN-254", color = SECONDARY_COLOR, font =  PRIMARY_FONT, font_size=24).next_to(self.chart_field, RIGHT+UP)
        self.curve_ec = Text("BLS12-381", color = HIGHLIGHT_COLOR, font =  PRIMARY_FONT, font_size=24).next_to(self.chart_ec, LEFT+UP)
        self.arrow_curve_to_chart_ec = CurvedArrow(self.curve_ec.get_right(), self.chart_ec.get_top()+UP*0.7+LEFT, tip_shape=StealthTip, 
                               stroke_width=2).rotate(axis=[1,0,0], angle=PI).set_color_by_gradient([GREEN_E, HIGHLIGHT_COLOR]).scale(0.6)
        self.arrow_curve_to_chart_field = CurvedArrow(self.curve_field.get_left()+RIGHT*0.2, self.chart_field.get_top()+RIGHT*0.75, tip_shape=StealthTip, 
                               stroke_width=2).set_color_by_gradient([PINK, SECONDARY_COLOR, MAROON_E, PURPLE]).scale(0.6)
        
    def animate_in(self, scene):
        self.new_subsection(scene, "two prime fields", "data/sound/e5/slide4-0.mp3")
        scene.play(Write(self.title_text), run_time=0.7)
        
        
        self.new_subsection(scene, "y_k belong to p1", "data/sound/e5/slide4-0a.mp3")
        scene.play(Write(self.number_sequence))
        scene.play(FadeIn(self.brace_number, self.number_sequence_kilo_bytes, self.sim))
        scene.wait(1)
        self.chart_field.gen_points()
        scene.play(FadeIn(self.chart_field, self.p1))
        scene.play(Indicate(self.p1, color = PINK))
        scene.play(FadeIn(self.curve_field), Write(self.arrow_curve_to_chart_field))
        scene.wait(1)
        scene.play(FadeIn(self.bytes_p1))
        scene.wait(1)
        scene.play(Indicate(self.number_sequence_kilo_bytes, color = PINK))

        self.new_subsection(scene, "kzg setup ec points - BLS", "data/sound/e5/slide4-1.mp3")
        self.chart_ec.gen_points()
        scene.play(FadeIn(self.chart_ec, self.p2))
        scene.wait(3)
        scene.play(FadeIn(self.curve_ec), Write(self.arrow_curve_to_chart_ec))
        scene.wait(3)
        scene.play(Indicate(self.p2, color = PINK))
        scene.play(FadeIn(self.bytes_p2))
        scene.wait(3.5)
        scene.play(FadeOut(self.chart_field, self.chart_ec, self.p1, self.p2, self.arrow_curve_to_chart_ec, self.arrow_curve_to_chart_field,
                           self.curve_ec, self.curve_field, self.bytes_p1, self.bytes_p2))
        
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
        scene.wait(2.7)
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
                           self.commitment_bytes, self.brace_commitment, 
                           self.brace_number, self.commitment, self.proof, self.verifier, self.committer,
                           self.committer_label, self.verifier_label, self.sim, self.sim_commitment, self.sim_proof))