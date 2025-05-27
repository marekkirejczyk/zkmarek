from manim import (Text, Write, UP, RIGHT, DOWN, LEFT, VGroup, FadeOut, RoundedRectangle, Arrow, StealthTip, Create, 
                   MoveToTarget, ORIGIN, ImageMobject, Polygon, FadeIn, MathTex, Group)
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR, HIGHLIGHT_COLOR

class Proofs(SlideBase):
    def __init__(self)-> None:
        super().__init__("Proofs")
        
    def construct(self):
        self.title_label = Text("Proofs", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size = 40).to_edge(UP)
        
        ## values (1 level)
        values_rectangles = RoundedRectangle(corner_radius=0.1, width = 0.5, height = 0.3, fill_opacity = 0.25,  stroke_width = 0.0).set_color(SECONDARY_COLOR)
        
        self.values = VGroup(*[values_rectangles.copy() for _ in range(2)]).arrange(RIGHT, buff = 0.65)
        self.cdots = Text("...", color = PRIMARY_COLOR, font= PRIMARY_FONT, font_size = 30).next_to(self.values[0], RIGHT, buff = 0.21)
        self.values.add(self.cdots)
        
        self.values2 = self.values.copy()
        self.values3 = self.values.copy()
        self.values4 = self.values.copy()
        
        texts_values = [Text("4", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 16),
                        Text("85", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 16)]
        
        for i, text in enumerate(texts_values):
            text.move_to(self.values[i].get_center())
            self.values[i].add(text)
            
        self.values_all = VGroup(self.values, self.values2, self.values3, self.values4).arrange(RIGHT, buff = 0.6).shift(DOWN * 3)
            
        ## commitments (2 level)
        commitments_rectangles = RoundedRectangle(corner_radius=0.1, width = 0.8, height = 0.6, fill_opacity = 0.25, stroke_width = 0.0).set_color(PRIMARY_COLOR)
        self.hashes_commitments_level2 = VGroup(*[commitments_rectangles.copy() for _ in range(4)]).arrange(RIGHT, buff = 1.43).next_to(self.values_all, UP, buff = 1.3)
        text_commitment_C255 = Text("C255", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 20).move_to(self.hashes_commitments_level2[1].get_center())
        self.cdots_level2 = self.cdots.copy().next_to(self.hashes_commitments_level2[0], RIGHT, buff = 0.6)
        self.cdots_level2_2 = self.cdots.copy().next_to(self.hashes_commitments_level2[2], RIGHT, buff = 0.6)
        self.hashes_commitments_level2.add(text_commitment_C255, self.cdots_level2, self.cdots_level2_2)
        
        ## commitments (3 level)
        self.hashes_commitments_level3 = VGroup(*[commitments_rectangles.copy() for _ in range(2)]).arrange(RIGHT, buff = 3.5).next_to(self.hashes_commitments_level2, UP, buff = 1.3)
        text_hash_commitmentH0= Text("H(C0)", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 20).move_to(self.hashes_commitments_level3[0].get_center())
        tilde = Text("~", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 30).move_to(text_hash_commitmentH0.get_top()+UP*0.05)
        self.cdots_level3 = self.cdots.copy().next_to(self.hashes_commitments_level3[0], RIGHT, buff = 1.65)
        self.hashes_commitments_level3.add(text_hash_commitmentH0, tilde, self.cdots_level3)
        
        ## root commitment
        self.hashes_commitments_root = commitments_rectangles.copy().next_to(self.hashes_commitments_level3, UP, buff = 1.3)
        text_hash_commitmentH = Text("C", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 20).move_to(self.hashes_commitments_root.get_center())
        self.hashes_commitments_root.add(text_hash_commitmentH)
        
        
        ## arrows
        self.arrows = VGroup()
        for i in range(2):
            self.create_arrow(self.hashes_commitments_level2[0], self.values[i], self.arrows)
            self.create_arrow(self.hashes_commitments_level2[1], self.values2[i], self.arrows)
            self.create_arrow(self.hashes_commitments_level2[2], self.values3[i], self.arrows)
            self.create_arrow(self.hashes_commitments_level2[3], self.values4[i], self.arrows)
            
            self.create_arrow(self.hashes_commitments_level3[0], self.hashes_commitments_level2[i], self.arrows)
            self.create_arrow(self.hashes_commitments_level3[1], self.hashes_commitments_level2[i+2], self.arrows)
            self.create_arrow(self.hashes_commitments_root, self.hashes_commitments_level3[i], self.arrows)
            
        ## node rectangles
        
        ## other elements
        self.prover = ImageMobject("data/images/person.png").scale(0.5).to_edge(LEFT, buff=1.0).shift(RIGHT+UP*1.5)
        self.prover_label = Text("insert function", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size = 30).next_to(self.prover, DOWN, buff = 0.2)
        self.prover_whole = Group(self.prover, self.prover_label)
        
        self.verifier = ImageMobject("data/images/person_blue.png").scale(0.5).to_edge(RIGHT, buff=1.0).shift(LEFT+UP*1.5)
        self.verifier_label = Text("verification function", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size = 30).next_to(self.prover, DOWN, buff = 0.2)
        self.verifier_whole = Group(self.verifier, self.verifier_label)
        
        self.commitment = Text("C", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size = 30).next_to(self.prover_whole, RIGHT, buff = 1.)
        self.envelope = RoundedRectangle(width = 8 * 0.3, height = 4 * 0.3, fill_opacity = 0.3, stroke_width = 0.0, corner_radius=0.1).set_color(PRIMARY_COLOR).move_to(self.commitment.get_center())
        self.envelope_flap_closed = Polygon(
            [-4.3, 1, 0],
            [4.3, 1, 0],
            [0, -1.6, 0],
            fill_color=HIGHLIGHT_COLOR,
            fill_opacity=0.2,
            stroke_width = 0.0
        ).scale(0.27).shift(UP*0.55)
        
        self.proof_text = Text("proof", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size = 30).next_to(self.commitment, DOWN, buff = 0.7)
        self.pi = MathTex(r"\pi", color = PRIMARY_COLOR, font_size = 40).next_to(self.proof_text, RIGHT, buff = 0.05)
        self.proof = VGroup(self.proof_text, self.pi)
        
    def animate_in(self, scene):
        self.new_subsection(scene, "85: proof C, opening", "data/sound/e7/slide5-1.mp3")
        scene.play(Write(self.title_label), run_time=0.7)
        scene.wait(1)
        self.values.scale(2).move_to(ORIGIN)
        scene.play(Write(self.values), run_time=0.7)
        scene.wait(1)
        scene.play(FadeIn(self.verifier_whole, self.prover_whole), run_time=0.5)
        scene.play(Write(self.commitment),
                   Create(self.envelope), Create(self.envelope_flap_closed), run_time=0.5)
        scene.play(Write(self.proof), run_time=0.5)
        
        
        self.new_subsection(scene, "multi-level", "data/sound/e7/slide5-2.mp3")
        self.values.generate_target()
        self.values.target.scale(1/2).next_to(self.values2, LEFT, buff = 0.6)
        scene.play(MoveToTarget(self.values), run_time=1.3)
        scene.play(Create(self.values_all), run_time=0.7)
        scene.play(Create(self.hashes_commitments_level2), run_time=0.7)
        scene.play(Create(self.hashes_commitments_level3), run_time=0.7)
        scene.play(Create(self.hashes_commitments_root), run_time=0.7)
        scene.play(Create(self.arrows), run_time=0.7)
        
        self.new_subsection(scene, "C0, opening, proof pi", "data/sound/e7/slide5-3.mp3")
        
        self.new_subsection(scene, "parent commitment, opening", "data/sound/e7/slide5-4.mp3")
        
        self.new_subsection(scene, "root, proof, opening", "data/sound/e7/slide5-5.mp3")
        
        self.new_subsection(scene, "3 commitments, 3 openings, 3 proofs", "data/sound/e7/slide5-6.mp3")
        
        self.new_subsection(scene, "different weight", "data/sound/e7/slide5-6a.mp3")
        
        self.new_subsection(scene, "IPA", "data/sound/e7/slide5-6b.mp3")
        
        self.new_subsection(scene, "total 1728", "data/sound/e7/slide5-6c.mp3")
        
        self.new_subsection(scene, "KZG", "data/sound/e7/slide5-6d.mp3")
        
        self.new_subsection(scene, "total 384 b", "data/sound/e7/slide5-6e.mp3")
        
        self.new_subsection(scene, "much smaller but pairings", "data/sound/e7/slide5-6f.mp3")
        
        self.new_subsection(scene, "3 proofs - to verify", "data/sound/e7/slide5-6g.mp3")
        
        self.new_subsection(scene, "simplified to sinlge proof", "data/sound/e7/slide5-7.mp3")
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.title_label), run_time=0.7)
        
    def create_arrow(self, start, end, arrow_array):
        arrow = Arrow(start.get_bottom(), end.get_top(), 
                      buff = 0.0, color=PRIMARY_COLOR,
                      stroke_width=0.8, max_tip_length_to_length_ratio=0.05,
                      tip_length = 0.1, 
                      tip_shape = StealthTip)
        arrow_array.add(arrow)