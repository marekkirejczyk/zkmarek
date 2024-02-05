from manim import (DOWN, LEFT, TAU, UP, CurvedArrow, FadeIn, FadeOut, MathTex,
                   Text, VGroup, Write)

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR
from zkmarek.video.mobjects.tex_array import TexArray
from zkmarek.video.slides.common.slide_base import SlideBase

SETUP_SIMPLE = [
    r"{{ P_0 }}",
    r"{{ P_1 }}",
    r"..." ,
    r"{{ P_{N-1} }}"]

SETUP_COMPLEX = [
    r"{{ \tau_{0..i}^1 }} {{ G_1 }}",
    r"{{ \tau_{0..i}^2 }} {{ G_1 }}",
    r"..." ,
    r"{{ \tau_{0..i}^n }} {{ G_1 }}"]

SETUP_SIMPLE_INDEX = [
    r"{{ P_{0, i} }}",
    r"{{ P_{1, i} }}",
    r"..." ,
    r"{{ P_{N-1, i} }}"]

SETUP_SIMPLE_INDEX_PLUS = [
    r"{{ P_{0, i+1} }}",
    r"{{ P_{1, i+1} }}",
    r"..." ,
    r"{{ P_{N-1, i+1} }}"]


class CeremonyVerification(SlideBase):
    title_label: Text
    main_label: Text
    bullet_1: Text
    bullet_2: Text
    vec_1: TexArray
    pairing_1: MathTex
    pairing_2a: MathTex
    pairing_2b: MathTex
    pairing_2c: MathTex
    curved_arrow: CurvedArrow
    curved_arrow2: CurvedArrow
    curved_arrow3: CurvedArrow
    curved_arrow_v: CurvedArrow

    def __init__(self):
        super().__init__("Ceremony Verification")

    def construct(self):
        self.title_label = Text(self.title, font=PRIMARY_FONT, color=PRIMARY_COLOR)
        self.main_label = Text("Malicious participant can:", font=PRIMARY_FONT, color=SECONDARY_COLOR, font_size=32)
        self.bullet_1 = Text("Provide numbers that are not consecutive powers of tau",
            font=PRIMARY_FONT, color=SECONDARY_COLOR, font_size=24)
        self.bullet_2 = Text("Ignore previous array", font=PRIMARY_FONT, color=SECONDARY_COLOR, font_size=24)
        self.bullet_3 = Text("Keep secret", font=PRIMARY_FONT, color=SECONDARY_COLOR, font_size=24)
        self.vec_1 = TexArray(SETUP_SIMPLE)
        self.pairing_1 = MathTex(
            "e", r"\left(", r"P_0", ",", r"\tau_{0..i} \cdot G_2", r"\right)", "=",
            "e", r"\left(", r"P_1", ",", r"1 \cdot G_2",r"\right)", color=PRIMARY_COLOR).scale(0.8)
        self.curved_arrow = CurvedArrow(self.vec_1[0].get_bottom(), self.vec_1[1].get_bottom(),
            angle=TAU/4, color=PRIMARY_COLOR)
        self.curved_arrow_2 = CurvedArrow(self.vec_1[1].get_bottom(), self.vec_1[2].get_bottom(),
            angle=TAU/4, color=PRIMARY_COLOR)
        self.curved_arrow_3 = CurvedArrow(self.vec_1[2].get_bottom(), self.vec_1[3].get_bottom(),
            angle=TAU/4, color=PRIMARY_COLOR)
        self.vec_2 = TexArray(SETUP_SIMPLE_INDEX)
        self.vec_3 = TexArray(SETUP_SIMPLE_INDEX_PLUS)
        self.title_label.to_edge(UP)
        self.main_label.next_to(self.title_label, DOWN, buff=0.8)
        self.bullet_1.next_to(self.main_label, DOWN, buff=0.3)
        self.vec_1.next_to(self.bullet_1, DOWN, buff=0.3)
        self.pairing_1.next_to(self.curved_arrow, DOWN)
        self.bullet_2.next_to(self.bullet_1, DOWN, buff=0.3)
        self.vec_2.next_to(self.bullet_2, DOWN, buff=0.3)
        self.vec_3.next_to(self.vec_2, DOWN, buff=0.3)
        self.curved_arrow_v = CurvedArrow(self.vec_2[0].get_left(), self.vec_3[0].get_left(),
            angle=TAU/4, color=PRIMARY_COLOR)
        self.pairing_2a = MathTex(
            "e", r"\left(", r"P_{0, i}", r",\ ", r"\tau_i \cdot G_2", r"\right)", color=PRIMARY_COLOR).scale(0.7)
        self.pairing_2b = MathTex("=", color=PRIMARY_COLOR).scale(0.7)
        self.pairing_2c = MathTex(
            "e", r"\left(", r"P_{0, i+1}", r",\ ", r"1 \cdot G_2",r"\right)", color=PRIMARY_COLOR).scale(0.7)
        self.pairing_2 = VGroup(self.pairing_2a, self.pairing_2b, self.pairing_2c)
        self.pairing_2.arrange(DOWN)
        self.pairing_2.next_to(self.curved_arrow_v, LEFT)
        self.bullet_3.next_to(self.bullet_2, DOWN, buff=0.3)

    def animate_in(self, scene):
        scene.play(Write(self.title_label))
        scene.play(Write(self.main_label))
        scene.play(Write(self.bullet_1))
        scene.play(FadeIn(self.vec_1))
        self.vec_1.animate_transform_matching_shapes(scene, SETUP_COMPLEX)
        self.vec_1.animate_transform_matching_shapes(scene, SETUP_SIMPLE)
        scene.play(FadeIn(self.curved_arrow))
        scene.play(FadeIn(self.pairing_1))
        self.vec_1.animate_transform_matching_shapes(scene, SETUP_COMPLEX)
        scene.play(FadeOut(self.pairing_1))
        scene.play(Write(self.curved_arrow_2))
        scene.play(Write(self.curved_arrow_3))

        scene.play(FadeOut(self.pairing_1),
            FadeOut(self.curved_arrow),
            FadeOut(self.curved_arrow_2),
            FadeOut(self.curved_arrow_3),
            FadeOut(self.vec_1))

        scene.play(Write(self.bullet_2))
        scene.play(FadeIn(self.vec_2))
        scene.play(FadeIn(self.vec_3))
        scene.play(FadeIn(self.curved_arrow_v))
        scene.play(FadeIn(self.pairing_2))

        scene.play(FadeOut(self.vec_2),
            FadeOut(self.vec_3),
            FadeOut(self.curved_arrow_v),
            FadeOut(self.pairing_2))

        scene.play(Write(self.bullet_3))

        scene.wait(2)
