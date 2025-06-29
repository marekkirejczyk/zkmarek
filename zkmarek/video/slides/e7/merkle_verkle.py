from manim import (FadeIn, Text, UP, FadeOut, Create, RIGHT, LEFT, DOWN, Brace, Indicate, 
                   MathTex, Write, TransformMatchingShapes, Tex)
from zkmarek.video.constant import PRIMARY_FONT, PRIMARY_COLOR, SECONDARY_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase

from zkmarek.video.slides.e6.proof_sizes import ProofSize
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
        self.proof_slide = ProofSize()
        self.proof_slide.construct()
        self.tree_MT = (
            self.proof_slide.merkle_tree 
        ).shift(LEFT)
        
        self.brace_levels = Brace(self.tree_MT, RIGHT, buff=0.1).set_color(PRIMARY_COLOR)
        self.label_levels = Text("9 levels", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=30).next_to(self.brace_levels, RIGHT, buff=0.1)
        
        self.slide_VT = Proofs()
        self.slide_VT.construct()
        self.tree_VT = self.slide_VT.tree.shift(RIGHT * 6).scale(0.8)
        
        self.brace_MT = Brace(self.tree_MT.branch2.copy().scale(0.9), DOWN, buff = 0.7).set_color(PRIMARY_COLOR).move_to(self.tree_MT.get_bottom() + DOWN * 0.04).shift(LEFT*0.45)
        self.brace_VT = Brace(self.tree_VT.copy().scale(0.2), DOWN, buff = 0.1).set_color(PRIMARY_COLOR).shift(LEFT*0.73+DOWN*2.)
        
        self.VT_children= Text("256 children", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=30).next_to(self.brace_VT, DOWN, buff=0.1)
        self.MT_children = Text("16 children", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=30).next_to(self.brace_MT, DOWN, buff=0.1)
        self.table = MerkleVerkleTable().scale(0.7)
        
        self.merkle_proof_constr1 = MathTex(r"\texttt{16}\ \texttt{hashes} \times \texttt{level}", color = PRIMARY_COLOR, font_size = 35).next_to(self.table, DOWN, buff = 0.5)
        self.merkle_proof_constr2= MathTex(r"\texttt{16} \times \texttt{32 B} \times \texttt{level}", color = PRIMARY_COLOR, font_size = 35).next_to(self.table, DOWN, buff = 0.5)
        self.merkle_proof_constr3 = MathTex(r"\texttt{16} \times \texttt{32 B} \times \texttt{9}", color = PRIMARY_COLOR, font_size = 35).next_to(self.table, DOWN, buff = 0.5)
        
        self.horizontals = Tex(r"\texttt{verify({{opening: scalar}}, root: EC\_point, \\ VerklePath(commitment, proof))}", color = PRIMARY_COLOR, font_size = 30).next_to(self.table, DOWN, buff = 0.8)
        self.horizontals2 = Tex(r"\texttt{verify({{opening: List[scalar]}}, root: EC\_point, \\ VerklePath(commitment, proof))}", color = PRIMARY_COLOR, font_size = 30).next_to(self.table, DOWN, buff = 0.8)
        
        self.multiproof_ipa = MathTex(r"\texttt{IPA: } 2256\times \texttt{32 B}", color = PRIMARY_COLOR, font_size = 35).next_to(self.table, DOWN).shift(RIGHT* 2)
        self.multiproof_kzg = MathTex(r"\texttt{KZG: } 2256\times \texttt{48 B}", color = PRIMARY_COLOR, font_size = 35).next_to(self.table, DOWN).shift(LEFT* 2)
    
        self.multiproof_vs_commitments_IPA = MathTex(r"\texttt{512 B}<<\texttt{2256 * 48 B}", color = PRIMARY_COLOR, font_size = 35).next_to(self.multiproof_ipa, DOWN, buff=0.0)
        self.multiproof_vs_commitments_KZG = MathTex(r"\texttt{48 B}<<\texttt{2256 * 32 B}", color = PRIMARY_COLOR, font_size = 35).next_to(self.multiproof_kzg, DOWN, buff=0.0)
        
        self.thousand_values = MathTex(r"\texttt{1000 values}\rightarrow \texttt{1000 parent commitments}", color = PRIMARY_COLOR, font_size = 35).next_to(self.table, DOWN, buff=0.5)
        self.verkle_path = MathTex(r"\texttt{VerkleProof}({{C_0}}, {{C_1}}, {{C_2}}, {{C_3}}, {{...}}, {{\pi}})", color = PRIMARY_COLOR, font_size = 35).next_to(self.table, DOWN, buff=0.5)
        self.verkle_path_2256 = MathTex(r"\texttt{VerkleProof}({{C_0}}, {{C_1}}, {{C_2}}, {{C_3}}, {{...}}, {{C_{2255}}}, {{\pi}})", color = PRIMARY_COLOR, font_size = 35).next_to(self.table, DOWN, buff=0.5)
        self.kzg_size_brace = Brace(self.verkle_path_2256[3], DOWN, buff=0.1).set_color(PRIMARY_COLOR)
        self.kzg_size_label = MathTex(r"\texttt{KZG: 48 B}", color=PRIMARY_COLOR, font_size=35).next_to(self.kzg_size_brace, DOWN, buff=0.1)
        self.ipa_size_label = MathTex(r"\texttt{IPA: 32 B}", color=PRIMARY_COLOR, font_size=35).next_to(self.kzg_size_brace, DOWN, buff=0.1)
        
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
        scene.play(Create(self.table.merkle_col[0]), run_time=1)
        scene.wait(0.5)
        scene.play(Write(self.merkle_proof_constr1), run_time=0.8)
        scene.wait(1)
        scene.play(TransformMatchingShapes(self.merkle_proof_constr1, self.merkle_proof_constr2), run_time=0.8)
        
        self.new_subsection(scene, "MT: 4 kB", "data/sound/e7/slide8-5.mp3")
        scene.wait(0.8)
        scene.play(TransformMatchingShapes(self.merkle_proof_constr2, self.merkle_proof_constr3), run_time=0.8)
        scene.play(Create(self.table.merkle_col[1]), run_time=1)
        scene.wait(1)
        scene.play(Create(self.table.merkle_col[2]), FadeOut(self.merkle_proof_constr3), run_time=1)
        scene.wait(1)
        
        self.new_subsection(scene, "MT: 4 MB", "data/sound/e7/slide8-6.mp3")
        scene.play(Indicate(self.table.vec[3]), run_time=1)
        scene.wait(1)
        scene.play(Create(self.table.merkle_col[3]), run_time=1)
        
        self.new_subsection(scene, "VT: efficient", "data/sound/e7/slide8-7.mp3")
        scene.play(Create(self.table.headers[1:]), run_time=2)
        scene.wait(4)
        scene.play(Create(self.table.ipa_col[0]), run_time=1)
        scene.play(Create(self.table.kzg_col[0]), run_time=1)
        
        self.new_subsection(scene, "IPA VT: 600 B, KZG VP: 200 B ", "data/sound/e7/slide8-8.mp3")
        scene.play(Create(self.table.ipa_col[1:3]), run_time=1)
        scene.play(Create(self.table.kzg_col[1:3]), run_time=1)
        scene.wait(1.8)
        scene.play(Indicate(self.table.ipa_col[2]), run_time=1)
        scene.wait(2.3)
        scene.play(Indicate(self.table.kzg_col[2]), run_time=1  )
        
        self.new_subsection(scene, "4 level VT", "data/sound/e7/slide8-9.mp3")
        scene.wait(3)
        scene.play(Write(self.thousand_values), run_time=1)
        scene.wait(3)
        scene.play(FadeOut(self.thousand_values), FadeIn(self.verkle_path), run_time=1)
        scene.play(self.verkle_path[11].animate.set_color(SECONDARY_COLOR))
        scene.play(TransformMatchingShapes(self.verkle_path, self.verkle_path_2256), run_time=1)
        
        self.new_subsection(scene, "1000 VP: 72 kB, 1000 VP: 109 kB", "data/sound/e7/slide8-9a.mp3")
        scene.wait(2)
        scene.play(Write(self.kzg_size_brace), Write(self.ipa_size_label), run_time=1)
        scene.wait(1)
        scene.play(FadeOut(self.ipa_size_label), Write(self.kzg_size_label), run_time=1)
        scene.wait(1)
        scene.play(FadeOut(self.kzg_size_label), FadeIn(self.ipa_size_label), run_time=1)
        scene.wait(1)
        scene.play(Create(self.table.ipa_col[3]), run_time=1)
        scene.play(Create(self.table.kzg_col[3]), run_time=1)
        scene.wait(1.5)
        self.new_subsection(scene, "horizontals", "data/sound/e7/slide8-10.mp3")
        scene.wait(1)
        scene.play(FadeOut(self.verkle_path_2256, self.ipa_size_label, self.kzg_size_brace), run_time=1)
        scene.play(Write(self.multiproof_vs_commitments_KZG), run_time=1)
        scene.play(Write(self.multiproof_vs_commitments_IPA), run_time=1)
        scene.wait(5)
        scene.play(FadeOut(self.multiproof_vs_commitments_KZG, self.multiproof_vs_commitments_IPA), run_time=1)
        
        self.new_subsection(scene, "can be the future", "data/sound/e7/slide8-11.mp3")
        scene.wait(10)
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.title_label, self.table))