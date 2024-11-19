from manim import (FadeIn, FadeOut, MathTex, Text, LEFT, RIGHT, DOWN, UP, Write, PURPLE, BLUE_E, Group, TEAL_E, Brace, MAROON_E, Arrow, StealthTip, GrowArrow, Indicate, PURPLE_A, ImageMobject, MoveToTarget)
from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR, HIGHLIGHT_COLOR, PRIMARY_FONT, HIGHLIGHT2_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase

class KZGBlobs(SlideBase):
    def __init__(self) -> None:
        super().__init__(title="KZG")
        
    def construct(self):
        self.title_text = Text("KZG in practice", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 40).to_edge(UP)
        self.verifier = ImageMobject("data/images/person.png").scale(0.7).shift(LEFT*5)
        self.number_sequence = MathTex(r"\left[ {{a_0}}, {{a_1}}, {{a_2}}, {{\cdots}}, {{a_{4095}}} \right]", color = SECONDARY_COLOR).scale(1.2).shift(UP*2)
        self.brace_number = Brace(self.number_sequence, RIGHT).set_color_by_gradient([PURPLE, SECONDARY_COLOR])
        self.number_sequence_kilo_bytes = Text("128 kB", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size=24)
        self.brace_number.put_at_tip(self.number_sequence_kilo_bytes)
        
        self.opening = MathTex(r"p(x_0) = y_0", color = TEAL_E).next_to(self.verifier, RIGHT).shift(RIGHT)
        self.polynomial = MathTex("p(x)", color = PRIMARY_COLOR).next_to(self.opening, RIGHT).shift(RIGHT)
        self.arrow_opening_poly = Arrow(self.opening.get_right(), self.polynomial.get_left(), tip_shape=StealthTip, 
                               stroke_width=2, max_tip_length_to_length_ratio=0.15).set_color_by_gradient([HIGHLIGHT2_COLOR, SECONDARY_COLOR])
        
        self.arrow_opening_verifier = Arrow(self.verifier.get_right(), self.opening.get_left(), tip_shape=StealthTip, 
                               stroke_width=2, max_tip_length_to_length_ratio=0.15).set_color_by_gradient([HIGHLIGHT2_COLOR, SECONDARY_COLOR])
        
        self.commitment = MathTex(r"{{C}} = {{p}}({{\tau}}) \cdot {{G_1}}").set_color_by_gradient([BLUE_E, TEAL_E]).next_to(self.polynomial, RIGHT).shift(RIGHT)
        self.proof = MathTex(r"{{\pi}} = {{q}} ({{\tau}}) \cdot {{G_1}}").set_color_by_gradient([MAROON_E, PURPLE]).next_to(self.polynomial, DOWN).shift(DOWN)
        
        self.arrow_number_sequence_poly = Arrow(self.number_sequence.get_bottom(), self.polynomial.get_top(), tip_shape=StealthTip, 
                               stroke_width=2, max_tip_length_to_length_ratio=0.15).set_color_by_gradient([HIGHLIGHT2_COLOR, SECONDARY_COLOR])
        self.arrow_poly_commitment = Arrow(self.polynomial.get_right(), self.commitment.get_left(), tip_shape=StealthTip, 
                               stroke_width=2, max_tip_length_to_length_ratio=0.15).set_color_by_gradient([HIGHLIGHT2_COLOR, SECONDARY_COLOR])
        self.arrow_poly_proof = Arrow(self.polynomial.get_bottom(), self.proof.get_top(), tip_shape=StealthTip, 
                               stroke_width=2, max_tip_length_to_length_ratio=0.15).set_color_by_gradient([HIGHLIGHT2_COLOR, SECONDARY_COLOR])


        
        
    def animate_in(self, scene):
        # self.new_subsection(scene, "using kzg", "data/sound/e5/slide4-0.mp3")

        self.new_subsection(scene, "remember, kzg", "data/sound/e5/slide4-1.mp3")
        scene.play(Write(self.title_text))
        scene.play(FadeIn(self.verifier), Write(self.opening))
        scene.play(Write(self.polynomial), GrowArrow(self.arrow_opening_poly), GrowArrow(self.arrow_opening_verifier))
        scene.wait(1.5)
        scene.play(Indicate(self.opening, color = [PURPLE, TEAL_E]))
        scene.wait(2)
        scene.play(GrowArrow(self.arrow_poly_commitment))
        scene.play(Write(self.commitment))
        scene.play(GrowArrow(self.arrow_poly_proof))
        scene.play(Write(self.proof))
        
        
        self.new_subsection(scene, "compresses 128 kB data", "data/sound/e5/slide4-2.mp3")
        scene.play(FadeOut(self.opening, self.arrow_opening_poly, self.arrow_opening_verifier))
        self.group_poly = Group(self.polynomial, self.arrow_poly_commitment, self.arrow_poly_proof, self.proof, self.commitment)
        self.group_poly.generate_target()
        self.group_poly.target.next_to(self.number_sequence, DOWN).shift(DOWN)
        scene.play(MoveToTarget(self.group_poly))

        scene.play(Indicate(self.commitment, color = SECONDARY_COLOR))
        scene.play(Indicate(self.proof, color = SECONDARY_COLOR))
        scene.play(Write(self.number_sequence))
        # scene.play(GrowArrow(self.arrow_number_sequence_poly))
        scene.wait(1)
        for i in range(5):
            scene.play(Indicate(self.number_sequence[2*i+1], color = [HIGHLIGHT2_COLOR, PURPLE_A], scale_factor=1.2), run_time=0.25)
        scene.play(FadeIn(self.brace_number, self.number_sequence_kilo_bytes))
        scene.play(Indicate(self.number_sequence_kilo_bytes, color = HIGHLIGHT_COLOR))
        scene.wait(1)
        self.proof_bytes = Text("32 B", font = PRIMARY_FONT, font_size=24).set_color_by_gradient([TEAL_E, HIGHLIGHT_COLOR])
        self.commitment_bytes = Text("32 B", font = PRIMARY_FONT, font_size=24).set_color_by_gradient([HIGHLIGHT_COLOR, TEAL_E])
        self.brace_commitment = Brace(self.commitment, RIGHT).set_color_by_gradient([HIGHLIGHT_COLOR, TEAL_E])
        self.brace_proof = Brace(self.proof, LEFT).set_color_by_gradient([TEAL_E, HIGHLIGHT_COLOR])
        self.brace_commitment.put_at_tip(self.commitment_bytes)
        self.brace_proof.put_at_tip(self.proof_bytes)
        scene.play(FadeIn(self.brace_commitment, self.commitment_bytes))
        scene.play(FadeIn(self.brace_proof, self.proof_bytes))
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.title_text, self.number_sequence, self.number_sequence_kilo_bytes, self.polynomial, self.arrow_poly_commitment,  
                           self.arrow_poly_proof, self.proof_bytes,self.brace_proof, 
                           self.commitment_bytes, self.brace_commitment, 
                           self.brace_number, self.commitment, self.proof, self.verifier))