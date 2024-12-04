from manim import (FadeIn, FadeOut, MathTex, Text, LEFT, RIGHT, DOWN, UP, Write, PURPLE, BLUE_E, Group, TEAL_E, Brace, MAROON_E, Arrow, 
                   StealthTip, GrowArrow, Indicate, PINK, ImageMobject, MoveToTarget)
from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR, HIGHLIGHT_COLOR, PRIMARY_FONT, HIGHLIGHT2_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase

class KZGBlobs(SlideBase):
    def __init__(self) -> None:
        super().__init__(title="KZG as a vector commitment")
        
    def construct(self):
        self.title_text = Text("KZG as a vector commitment", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 40).to_edge(UP)
        self.committer = ImageMobject("data/images/person.png").scale(0.7).shift(LEFT*5)
        self.committer_label = Text("Committer", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size = 30).next_to(self.committer, DOWN)
        self.verifier = ImageMobject("data/images/person_blue.png").scale(0.7).shift(RIGHT*5)
        self.verifier_label = Text("Verifier", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 30).next_to(self.verifier, DOWN)
        self.number_sequence = MathTex(r"\left[ {{y_0}}, {{y_1}}, {{y_2}}, {{\cdots}}, {{y_{4095}}} \right]", color = SECONDARY_COLOR).scale(1.2).shift(UP*2)
        self.brace_number = Brace(self.number_sequence, RIGHT).set_color_by_gradient([PURPLE, SECONDARY_COLOR])
        self.number_sequence_kilo_bytes = Text("128 kB", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size=24)
        self.brace_number.put_at_tip(self.number_sequence_kilo_bytes)
        
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

        
        
    def animate_in(self, scene):
        self.new_subsection(scene, "two prime fields", "data/sound/e5/slide4-0.mp3")
        scene.play(Write(self.title_text), run_time=0.7)
        
        
        self.new_subsection(scene, "y_k belong to p1", "data/sound/e5/slide4-0a.mp3")
        scene.play(Write(self.number_sequence))
        scene.play(FadeIn(self.brace_number, self.number_sequence_kilo_bytes))

        self.new_subsection(scene, "kzg setup ec points - BLS", "data/sound/e5/slide4-1.mp3")
        
        
        self.new_subsection(scene, "rput it all together", "data/sound/e5/slide4-2.mp3")
        scene.play(Write(self.verifier_label), Write(self.committer_label))
        scene.play(FadeIn(self.verifier, self.committer))
        scene.play(Write(self.polynomial), GrowArrow(self.arrow_opening_committer), run_time=0.7)
        scene.wait(1.5)
        scene.play(GrowArrow(self.arrow_poly_commitment), Write(self.commitment))
        scene.wait(2.5)
        
        self.new_subsection(scene, "put it all together", "data/sound/e5/slide4-2a.mp3")
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
        scene.wait(2)
        scene.play(Indicate(self.number_sequence_kilo_bytes, color = HIGHLIGHT_COLOR))
        scene.wait(1)
        self.proof_bytes = Text("48 B", font = PRIMARY_FONT, font_size=24).set_color_by_gradient([TEAL_E, HIGHLIGHT_COLOR])
        self.commitment_bytes = Text("48 B", font = PRIMARY_FONT, font_size=24).set_color_by_gradient([HIGHLIGHT_COLOR, TEAL_E])
        self.brace_commitment = Brace(self.commitment, RIGHT).set_color_by_gradient([HIGHLIGHT_COLOR, TEAL_E])
        self.brace_proof = Brace(self.proof, RIGHT).set_color_by_gradient([TEAL_E, HIGHLIGHT_COLOR])
        self.brace_commitment.put_at_tip(self.commitment_bytes)
        self.brace_proof.put_at_tip(self.proof_bytes)
        scene.play(FadeIn(self.brace_commitment, self.commitment_bytes))
        scene.wait(2)
        scene.play(FadeIn(self.brace_proof, self.proof_bytes))
        scene.wait(3.5)
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.title_text, self.number_sequence, self.number_sequence_kilo_bytes, self.polynomial, self.arrow_poly_commitment,  
                           self.arrow_poly_proof, self.proof_bytes,self.brace_proof, 
                           self.commitment_bytes, self.brace_commitment, 
                           self.brace_number, self.commitment, self.proof, self.verifier, self.committer,
                           self.committer_label, self.verifier_label))