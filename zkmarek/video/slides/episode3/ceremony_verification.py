from typing import List

from manim import DOWN, TAU, UP, LEFT, RIGHT, CurvedArrow, FadeIn, FadeOut, MathTex, Text, Write, Unwrite, Indicate, MoveToTarget

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR, HIGHLIGHT_COLOR
from zkmarek.video.mobjects.tex_array import TexArray
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.episode3.morphin_math_text import MorphinMathText

SETUP_START_G1 = [
    r"{{ P_0 }}",
    r"{{ P_1 }}",
    r"..." ,
    r"{{ P_{n-1} }}"]

SETUP_START_G2 = [
    r"{{ Q_0 }}",
    r"{{ Q_1 }}",
    r"..." ,
    r"{{ Q_{k-1} }}"]


SETUP_WITH_TAU_G1 = [
    r"{{ \tau^1 }} {{ G_1 }}",
    r"{{ \tau^2 }} {{ G_1 }}",
    r"..." ,
    r"{{ \tau^n }} {{ G_1 }}"]

SETUP_WITH_TAU_G2 = [
    r"{{ \tau^1 }} {{ G_2 }}",
    r"{{ \tau^2 }} {{ G_2 }}",
    r"..." ,
    r"{{ \tau^k }} {{ G_2 }}"]

PARTICIPANT_N = [
    r"\tau_k^1 G_1",
    r"\tau_k^2 G_1",
    r". . .",
    r"\tau_k^n G_1"
]

widths = [2, 2, 1, 2]

class CeremonyVerification(SlideBase):
    title_label: Text
    header_label: Text
    subheader_label: Text
    vec_g1: TexArray
    vec_g2: TexArray
    pairing2: MathTex
    arrows_g1: List[CurvedArrow]
    arrows_g2: List[CurvedArrow]

    def __init__(self):
        super().__init__("Ceremony Verification")

    def generate_arrows(self, vec):
        arrows = []
        for i in range(0, 3):
            arrows.append(CurvedArrow(vec[i].get_bottom(), vec[i+1].get_bottom(),
                angle=TAU/4, color=PRIMARY_COLOR))
        return arrows

    def construct(self):
        self.title_label = Text(self.title, font=PRIMARY_FONT, color=PRIMARY_COLOR)
        self.header_label = Text("Malicious participant can:", font=PRIMARY_FONT, color=SECONDARY_COLOR, font_size=32)
        self.subheader_label = Text("Provide numbers that are not consecutive powers of tau",
            font=PRIMARY_FONT, color=SECONDARY_COLOR, font_size=24)
        self.vec_g1 = TexArray(SETUP_START_G1)
        self.vec_g2 = TexArray(SETUP_START_G2, widths=widths)

        self.pairing = MathTex(r"{{e(P_0, Q_0)}} \quad =", font_size=40, color=SECONDARY_COLOR)
        self.pairing1_1 = MorphinMathText([
            r"e({{P_0}}, {{Q_0}})",
            r"e({{\tau \cdot G_1}}, {{Q_0}})",
            r"e({{\tau \cdot G_1}}, {{\tau \cdot G_2}})",
            r"e({{\tau}} \cdot G_1, {{\tau}} \cdot G_2) {{ }}",
            r"e({{1}} \cdot G_1, {{1}} \cdot G_2)^{ {{ \tau^2}} } ",
            r"e({{\tau^2}} \cdot G_1}}, {{1}} \cdot G_2){{ }}",
            r"e({{P_1}}, {{G_2}})"
        ])
        self.pairing3 = MathTex(r"e({{P _{N-2}}}, {{Q _0}}) {{=}} e({{P_{N-1}}}, {{G_2}})", font_size=40, color=SECONDARY_COLOR)
        self.pairing2 = MathTex(r"e({{P _1}}, {{Q _0}}) {{=}} e({{P_2}}, {{G_2}})", font_size=40, color=SECONDARY_COLOR)
        self.vector_k = TexArray(PARTICIPANT_N)
        self.title_label.to_edge(UP)
        self.header_label.next_to(self.title_label, DOWN, buff=0.6)
        self.subheader_label.next_to(self.header_label, DOWN, buff=0.3)
        self.vec_g1.next_to(self.subheader_label, DOWN, buff=0.3)
        self.vec_g2.next_to(self.vec_g1, DOWN, buff=1.5)
        self.arrows_g1 = self.generate_arrows(self.vec_g1)
        self.arrows_g2 = self.generate_arrows(self.vec_g2)
        self.pairing.next_to(self.vec_g2, DOWN, buff = 0.5)
        self.pairing1_1.next_to(self.vec_g2, DOWN, buff = 0.45).shift(RIGHT)
        self.pairing2.next_to(self.vec_g2, DOWN, buff=0.5)
        self.pairing3.next_to(self.vec_g2, DOWN, buff=0.5)
        self.vector_k.next_to(self.title_label, DOWN, buff=0.8)

    def animate_in(self, scene):
        self.new_subsection(scene, "should have the powers of tau", "data/sound/episode3/slide6-1.mp3")
        scene.play(Write(self.title_label))       
        scene.play(Write(self.vector_k))

        self.new_subsection(scene, "not powers of tau", "data/sound/episode3/slide6-2.mp3")
        scene.play(FadeOut(self.vector_k))
        scene.play(Write(self.header_label))
        scene.play(Write(self.subheader_label))

        self.new_subsection(scene, "setup", "data/sound/episode3/slide6-3.mp3")
        scene.play(FadeIn(self.vec_g1))
        scene.play(FadeIn(self.vec_g2))
        scene.wait(1.6)
        scene.play(Indicate(self.vec_g1.cells[0][1], color = HIGHLIGHT_COLOR), run_time=0.7)
        scene.play(Indicate(self.vec_g1.cells[1][1], color = HIGHLIGHT_COLOR), run_time=0.7)
        scene.play(Indicate(self.vec_g1.cells[3][1], color = HIGHLIGHT_COLOR), run_time=0.7)
        scene.play(Indicate(self.vec_g2.cells[0][1], color = HIGHLIGHT_COLOR), run_time=0.7)
        scene.play(Indicate(self.vec_g2.cells[1][1], color = HIGHLIGHT_COLOR), run_time=0.7)
        scene.play(Indicate(self.vec_g2.cells[3][1], color = HIGHLIGHT_COLOR), run_time=0.7)

        self.new_subsection(scene, "property of pairings", "data/sound/episode3/slide6-4.mp3")
        scene.play(Write(self.pairing[0]))
        self.pairing.generate_target()

        self.pairing.target.next_to(self.vec_g2, DOWN, buff = 0.5).shift(2*LEFT)
        scene.wait(1)
        scene.play(Indicate(self.pairing[0], color = PRIMARY_COLOR))
        scene.play(Write(self.arrows_g1[0]))
        scene.wait(0.2)
        scene.play(MoveToTarget(self.pairing))
        self.pairing1_1.animate_rest(scene)
        scene.play(FadeOut(self.arrows_g1[0]))
        self.new_subsection(scene, "why pairings?", "data/sound/episode3/slide6-5.mp3")
        self.vec_g1.animate_transform_matching_shapes(scene, SETUP_WITH_TAU_G1)
        self.vec_g2.animate_transform_matching_shapes(scene, SETUP_WITH_TAU_G2)
        self.vec_g1.animate_transform_matching_shapes(scene, SETUP_START_G1)
        self.vec_g2.animate_transform_matching_shapes(scene, SETUP_START_G2)

        self.pairing1_1.animate_out(scene)
        scene.play(FadeOut(self.pairing))

        self.new_subsection(scene, "calculations correct", "data/sound/episode3/slide6-6.mp3")
        scene.play(Write(self.arrows_g1[1]), FadeIn(self.pairing2))
        scene.play(Indicate(self.pairing2[5], color = PRIMARY_COLOR))
        scene.play(FadeOut(self.pairing2))
        scene.play(FadeOut(self.arrows_g1[1]))
        
        scene.play(Write(self.arrows_g1[2]), Write(self.pairing3))
        scene.play(FadeOut(self.arrows_g1[2]), Unwrite(self.pairing3))

        for arrow in self.arrows_g2:
            scene.play(Write(arrow))
        for arrow in self.arrows_g2:
            scene.play(FadeOut(arrow))
        scene.wait(2.5)
        
    def animate_out(self, scene):
        scene.play(
            FadeOut(self.vec_g1, self.vec_g2, self.title_label, self.subheader_label, self.header_label))
