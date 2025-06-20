from manim import (FadeIn, Text, UP, FadeOut, Create, RIGHT, LEFT, DOWN, Brace, Indicate, 
                   MathTex, Write, TransformMatchingShapes)
from zkmarek.video.constant import PRIMARY_FONT, PRIMARY_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase

from zkmarek.video.slides.e7.tree import MerkleTree as MT16
from zkmarek.video.slides.e7.proofs import Proofs
from zkmarek.video.slides.e7.table_proofs import MerkleVerkleTable

class MerkleVerkle(SlideBase):
    def __init__(self) -> None:
        super().__init__("Merkle Verkle Trees")

    def construct(self):
        self.title_label = (
            Text(
                "Merkle vs Verkle Trees",
                font=PRIMARY_FONT,
                color=PRIMARY_COLOR,
                font_size=40,
            )
            .to_edge(UP)
        )
        
        self.tree_MT = (
            MT16(include_labels=False)
            .scale(0.4)
            .shift(UP * 4 + LEFT * 3,)
        )
        
        self.brace_levels = Brace(self.tree_MT, RIGHT, buff=0.1).set_color(PRIMARY_COLOR)
        self.label_levels = Text("9 levels", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=30).next_to(self.brace_levels, RIGHT, buff=0.1)
        
        self.slide_VT = Proofs()
        self.slide_VT.construct()
        self.tree_VT = self.slide_VT.tree.shift(RIGHT * 6).scale(0.8)
        
        self.brace_MT = Brace(self.tree_MT.copy().scale(0.118), DOWN, buff = 0.1).set_color(PRIMARY_COLOR).shift(LEFT*1.45).move_to(self.tree_MT.get_bottom() + DOWN * 0.04)
        self.brace_VT = Brace(self.tree_VT.copy().scale(0.2), DOWN, buff = 0.1).set_color(PRIMARY_COLOR).shift(LEFT*0.73+DOWN*2.)
        
        self.VT_children= Text("256 children", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=30).next_to(self.brace_VT, DOWN, buff=0.1)
        self.MT_children = Text("16 children", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=30).next_to(self.brace_MT, DOWN, buff=0.1)
        self.table = MerkleVerkleTable().scale(0.7)
        
        self.merkle_proof_constr1 = MathTex(r"16 \texttt{hashes} \times \texttt{level}", color = PRIMARY_COLOR, font = 35).next_to(self.table, DOWN, buff = 0.5)
        self.merkle_proof_constr2= MathTex(r"16 \times \texttt{32 B} \times \texttt{level}", color = PRIMARY_COLOR, font = 35).next_to(self.table, DOWN, buff = 0.5)
        self.merkle_proof_constr3 = MathTex(r"16 \times \texttt{32 B} \times \texttt{9}", color = PRIMARY_COLOR, font = 35).next_to(self.table, DOWN, buff = 0.5)
        
        
    
    def animate_in(self, scene):
        self.new_subsection(scene, "depth -MT", "data/sound/e7/slide8-1.mp3")
        scene.play(FadeIn(self.title_label))
        scene.play(
            Create(self.tree_MT),
            run_time=2,
        )
        scene.play(FadeIn(self.brace_levels, self.label_levels), run_time=1.5)
        
        self.new_subsection(scene, "depth VT", "data/sound/e7/slide8-2.mp3")
        scene.play(self.tree_MT.animate.shift(LEFT * 0.3).scale(0.9),
                   FadeOut(self.brace_levels, self.label_levels), run_time=1.5)
        scene.play(Create(self.tree_VT), run_time=2)
        scene.wait(3)
        scene.play(FadeIn(self.brace_MT, self.brace_VT), run_time=1.5)
        scene.play(FadeIn(self.VT_children, self.MT_children), run_time=1.5)
        
        self.new_subsection(scene, "proof sizes", "data/sound/e7/slide8-3.mp3")
        scene.play(FadeOut(self.brace_MT, self.brace_VT, self.VT_children, self.MT_children), run_time=1.5)
        
        self.new_subsection(scene, "MT proof size", "data/sound/e7/slide8-4.mp3")
        scene.play(FadeOut(self.tree_VT, self.tree_MT), run_time=1)
        self.table.reveal_header(scene)
        scene.wait(2)
        scene.play(Create(self.table.merkle_col[3]), run_time=1)
        scene.wait(0.5)
        scene.play(Write(self.merkle_proof_constr1), run_time=0.8)
        scene.wait(2)
        scene.play(TransformMatchingShapes(self.merkle_proof_constr1, self.merkle_proof_constr2), run_time=0.8)
        
        self.new_subsection(scene, "MT: 4 kB", "data/sound/e7/slide8-5.mp3")
        scene.play(TransformMatchingShapes(self.merkle_proof_constr2, self.merkle_proof_constr3), run_time=0.8)
        scene.play(Create(self.table.merkle_col[0]), run_time=1)
        scene.wait(1)
        scene.play(Create(self.table.merkle_col[1]), run_time=1)
        scene.wait(1)
        
        self.new_subsection(scene, "MT: 4 MB", "data/sound/e7/slide8-6.mp3")
        scene.play(Indicate(self.table.vec[2]), run_time=1)
        scene.wait(1)
        scene.play(Create(self.table.merkle_col[2]), run_time=1)
        
        self.new_subsection(scene, "VT: efficient", "data/sound/e7/slide8-7.mp3")
        scene.play(Create(self.table.headers[1:]), run_time=2)
        
        self.new_subsection(scene, "IPA VT: 1.3 kB, KZG VP: 600 B ", "data/sound/e7/slide8-8.mp3")
        scene.play(Create(self.table.ipa_col[0:2]), Create(self.table.ipa_col[3]), run_time=1)
        scene.play(Create(self.table.kzg_col[0:2]),Create(self.table.kzg_col[3]), run_time=1)
        scene.wait(2.5)
        scene.play(Indicate(self.table.ipa_col[1]), run_time=1)
        scene.wait(2.5)
        scene.play(Indicate(self.table.kzg_col[1]), run_time=1  )
        
        self.new_subsection(scene, "1000 VP: 45 kB, 1000 VP: 15 kB", "data/sound/e7/slide8-9.mp3")
        scene.wait(4)
        scene.play(Create(self.table.ipa_col[2]), run_time=1)
        scene.play(Create(self.table.kzg_col[2]), run_time=1)
        scene.wait(7)
        scene.play(Indicate(self.table.ipa_col[2]), run_time=1)
        scene.wait(2.5)
        scene.play(Indicate(self.table.kzg_col[2]), run_time=1)
        
        self.new_subsection(scene, "can be the future", "data/sound/e7/slide8-11.mp3")
        scene.wait(7)
    def animate_out(self, scene):
        scene.play(FadeOut(self.title_label))