from typing import List

from manim import (DOWN, TAU, UP, CurvedArrow, FadeIn, FadeOut, MathTex,
                   Text, Unwrite, Write)

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR
from zkmarek.video.mobjects.tex_array import TexArray
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.episode3.morphin_math_text import MorphinMathText

SETUP_START_G1 = [
    r"{{ P_0 }}",
    r"{{ P_1 }}",
    r"..." ,
    r"{{ P_{N-1} }}"]

SETUP_START_G2 = [
    r"{{ Q_0 }}",
    r"{{ Q_1 }}",
    r"..." ,
    r"{{ Q_{N-1} }}"]


SETUP_WITH_TAU_G1 = [
    r"{{ \tau^1 }} {{ G_1 }}",
    r"{{ \tau^2 }} {{ G_1 }}",
    r"..." ,
    r"{{ \tau^n }} {{ G_1 }}"]

SETUP_WITH_TAU_G2 = [
    r"{{ \tau^1 }} {{ G_2 }}",
    r"{{ \tau^2 }} {{ G_2 }}",
    r"..." ,
    r"{{ \tau^n }} {{ G_2 }}"]



class CeremonyVerification(SlideBase):
    title_label: Text
    header_label: Text
    subheader_label: Text
    vec_g1: TexArray
    vec_g2: TexArray
    pairing1: MorphinMathText
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
        self.vec_g2 = TexArray(SETUP_START_G2)

        self.pairing1 = MorphinMathText([
            r"e({{P_0}}, {{Q_0}})",
            r"e({{P_0}}, {{Q_0}}) = e({{P_0}}, {{Q_0}})",
            r"e({{P_0}}, {{Q_0}}) = e({{\tau \cdot G_1}}, {{Q_0}})",
            r"e({{P_0}}, {{Q_0}}) = e({{\tau \cdot G_1}}, {{\tau \cdot G_2}})",
            r"e({{P_0}}, {{Q_0}}) = e({{\tau}} \cdot G_1, {{\tau}} \cdot G_2) {{ }}",
            r"e({{P_0}}, {{Q_0}}) = e({{1}} \cdot G_1, {{1}} \cdot G_2)^{ {{ \tau^2}} } ",
            r"e({{P_0}}, {{Q_0}}) = e({{\tau^2}} \cdot G_1}}, {{1}} \cdot G_2){{ }}",
            r"e({{P_0}}, {{Q_0}}) = e({{P_1}}, {{G_2}})"
        ])
        self.pairing2 = MathTex(r"e({{P_1}}, {{Q_0}}) = e({{P_2}}, {{G_2}})", font_size=40, color=SECONDARY_COLOR)
        self.title_label.to_edge(UP)
        self.header_label.next_to(self.title_label, DOWN, buff=0.6)
        self.subheader_label.next_to(self.header_label, DOWN, buff=0.3)
        self.vec_g1.next_to(self.subheader_label, DOWN, buff=0.3)
        self.vec_g2.next_to(self.vec_g1, DOWN, buff=1.5)
        self.arrows_g1 = self.generate_arrows(self.vec_g1)
        self.arrows_g2 = self.generate_arrows(self.vec_g2)
        self.pairing1.next_to(self.vec_g2, DOWN, buff=0.5)
        self.pairing2.next_to(self.vec_g2, DOWN, buff=0.5)

    def animate_in(self, scene):
        scene.play(Write(self.title_label))
        scene.play(Write(self.header_label))
        scene.play(Write(self.subheader_label))
        scene.play(FadeIn(self.vec_g1))
        scene.play(FadeIn(self.vec_g2))
        scene.play(FadeIn(self.arrows_g1[0]))
        self.pairing1.animate_first(scene)
        self.vec_g1.animate_transform_matching_shapes(scene, SETUP_WITH_TAU_G1)
        self.vec_g2.animate_transform_matching_shapes(scene, SETUP_WITH_TAU_G2)
        self.pairing1.animate_rest(scene)

        self.vec_g1.animate_transform_matching_shapes(scene, SETUP_START_G1)
        self.vec_g2.animate_transform_matching_shapes(scene, SETUP_START_G2)

        scene.play(FadeOut(self.arrows_g1[0]))
        self.pairing1.animate_out(scene)

        scene.play(Write(self.arrows_g1[1]))
        scene.play(Write(self.pairing2))
        scene.play(Unwrite(self.pairing2))
        scene.play(FadeOut(self.arrows_g1[1]))

        scene.play(Write(self.arrows_g1[2]))
        scene.play(FadeOut(self.arrows_g1[2]))

        for arrow in self.arrows_g2:
            scene.play(Write(arrow))
        for arrow in self.arrows_g2:
            scene.play(FadeOut(arrow))

        scene.wait(2)

        scene.play(
            FadeOut(self.vec_g1),
            FadeOut(self.vec_g2))
