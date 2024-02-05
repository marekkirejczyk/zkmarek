from manim import UP, DOWN, Text, Write, FadeIn, FadeOut, CurvedArrow, MathTex, TAU

from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR, PRIMARY_FONT
from zkmarek.video.mobjects.tex_array import TexArray
from zkmarek.video.slides.common.slide_base import SlideBase

SETUP = [
    r"{{ P_0 }}",
    r"{{ P_1 }}",
    r"..." ,
    r"{{ P_{N-1} }}"]

SETUP_1 = [
    r"{{ \tau_{0..i}^1 }} {{ G_1 }}",
    r"{{ \tau_{0..i}^2 }} {{ G_1 }}",
    r"..." ,
    r"{{ \tau_{0..i}^n }} {{ G_1 }}"]


class CeremonyVerification(SlideBase):
    title_label: Text
    main_label: Text
    bullet_1: Text
    bullet_2: Text
    vec_1: TexArray
    pairing_1: MathTex
    curved_arrow: CurvedArrow
    curved_arrow2: CurvedArrow
    curved_arrow3: CurvedArrow

    def __init__(self):
        super().__init__("Ceremony Verification")

    def construct(self):
        self.title_label = Text(self.title, font=PRIMARY_FONT, color=PRIMARY_COLOR)
        self.main_label = Text("Malicious participant can:", font=PRIMARY_FONT, color=SECONDARY_COLOR, font_size=32)
        self.bullet_1 = Text("Provide numbers that are not consecutive powers of tau",
            font=PRIMARY_FONT, color=SECONDARY_COLOR, font_size=24)
        self.bullet_2 = Text("Ignore previous array", font=PRIMARY_FONT, color=SECONDARY_COLOR, font_size=24)
        self.bullet_3 = MathTex("Keep \tau", font=PRIMARY_FONT, color=SECONDARY_COLOR, font_size=24)
        self.vec_1 = TexArray(SETUP)
        self.pairing_1 = MathTex(
            "e", r"\left(", r"P_0", ",", r"\tau_{0..i} \cdot G_2", r"\right)", "=",
            "e", r"\left(", r"P_1", ",", r"1 \cdot G_2",r"\right)", color=PRIMARY_COLOR).scale(0.8)
        self.curved_arrow = CurvedArrow(self.vec_1[0].get_bottom(), self.vec_1[1].get_bottom(),
            angle=TAU/4, color=PRIMARY_COLOR)
        self.curved_arrow_2 = CurvedArrow(self.vec_1[1].get_bottom(), self.vec_1[2].get_bottom(),
            angle=TAU/4, color=PRIMARY_COLOR)
        self.curved_arrow_3 = CurvedArrow(self.vec_1[2].get_bottom(), self.vec_1[3].get_bottom(),
            angle=TAU/4, color=PRIMARY_COLOR)
        self.title_label.to_edge(UP)
        self.main_label.next_to(self.title_label, DOWN, buff=0.8)
        self.bullet_1.next_to(self.main_label, DOWN, buff=0.3)
        self.vec_1.next_to(self.bullet_1, DOWN, buff=0.3)
        self.pairing_1.next_to(self.curved_arrow, DOWN)

    def animate_in(self, scene):
        scene.play(Write(self.title_label))
        scene.play(Write(self.main_label))
        scene.play(Write(self.bullet_1))
        scene.play(FadeIn(self.vec_1))
        self.vec_1.animate_transform_matching_shapes(scene, SETUP_1)
        self.vec_1.animate_transform_matching_shapes(scene, SETUP)
        scene.play(FadeIn(self.curved_arrow))
        scene.play(FadeIn(self.pairing_1))
        self.vec_1.animate_transform_matching_shapes(scene, SETUP_1)
        scene.play(FadeOut(self.pairing_1))
        scene.play(FadeIn(self.curved_arrow_2))
        scene.play(FadeIn(self.curved_arrow_3))
        scene.wait(2)
