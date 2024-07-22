from manim import DOWN, RIGHT, TAU, UP, CurvedArrow, FadeIn, FadeOut, MathTex, Text, Write

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR
from zkmarek.video.mobjects.tex_array import TexArray
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.episode3.morphin_math_text import MorphinMathText

SETUP_CURRENT = [
    r"{{ P_0 }}",
    r"{{ P_1 }}",
    r"..." ,
    r"{{ P_{N-1} }}"]

SETUP_CURRENT_2 = [
    r"{{ P_0^i }}",
    r"{{ P_1^i} }}",
    r"..." ,
    r"{{ P_{N-1}^i }}"]

SETUP_NEXT = [
    r"{{ P_0^{i+1} }}",
    r"{{ P_1^{i+1} }}",
    r"..." ,
    r"{{ P_{N-1}^{i+1} }}"]


class CeremonyVerification2(SlideBase):
    title_label: Text
    header_label: Text
    subheader_label: Text

    vec_g1_current: TexArray
    vec_next: TexArray
    arrow: CurvedArrow

    pairing: MorphinMathText
    tau_current: MathTex
    tau_next: MathTex


    def __init__(self):
        super().__init__("Ceremony Verification 2")

    def construct(self):
        self.title_label = Text(self.title, font=PRIMARY_FONT, color=PRIMARY_COLOR)
        self.header_label = Text("Malicious participant can:", font=PRIMARY_FONT, color=SECONDARY_COLOR, font_size=32)
        self.subheader_label = Text("Ignore previous array",
            font=PRIMARY_FONT, color=SECONDARY_COLOR, font_size=24)
        self.vec_g1_current = TexArray(SETUP_CURRENT)
        self.vec_next = TexArray(SETUP_NEXT)
        self.tau_current = MathTex(r"\tau_{[i]}", font_size=40, color=SECONDARY_COLOR)
        self.tau_next = MathTex(r"\tau_{[i+1]}", font_size=40, color=SECONDARY_COLOR)

        self.title_label.to_edge(UP)
        self.header_label.next_to(self.title_label, DOWN, buff=0.8)
        self.subheader_label.next_to(self.header_label, DOWN, buff=0.3)
        self.vec_g1_current.next_to(self.subheader_label, DOWN, buff=0.5)
        self.vec_next.next_to(self.vec_g1_current, DOWN, buff=0.5)
        self.tau_current.next_to(self.vec_g1_current, RIGHT, buff=0.5)
        self.tau_next.next_to(self.vec_next, RIGHT, buff=0.5)
        self.arrow = CurvedArrow(self.vec_g1_current[0].get_left(), self.vec_next[0].get_left(),
            angle=TAU/4, color=PRIMARY_COLOR)
        self.pairing = MorphinMathText([
            r"{{e(P_0^i, \tau_{[i+1]} \cdot G_2)}}",
            r"{{e(P_0^i, \tau_{[i+1]} \cdot G_2)}} = e(P_0^{{i}}, {{ \tau_{[i+1]} }} \cdot G_2)}}",
            r"{{e(P_0^i, \tau_{[i+1]} \cdot G_2)}} = e(P_0^{ {{i+1}} }, {{1}} \cdot G_2)",
            r"{{e(P_0^i, Q_0^{[i+1]}) }} = e(P_0^{ {{i+1}} }, G_2)"
        ])
        self.pairing.next_to(self.vec_next, DOWN, buff=0.5)

    def animate_in(self, scene):
        self.new_subsection(scene, "another array", "data/sound/episode3/slide7-0.mp3")
        scene.play(Write(self.title_label))
        scene.play(Write(self.header_label))
        scene.play(Write(self.subheader_label))


        scene.play(FadeIn(self.vec_g1_current))
        scene.play(FadeIn(self.tau_current))
        self.new_subsection(scene, "P i+1", "data/sound/episode3/slide7-1.mp3")
        self.vec_g1_current.animate_transform_matching_shapes(scene, SETUP_CURRENT_2)

        scene.play(FadeIn(self.vec_next))
        scene.play(FadeIn(self.tau_next))
        scene.play(FadeIn(self.arrow))
        self.new_subsection(scene, "verify", "data/sound/episode3/slide7-2.mp3")
        self.pairing.animate_first(scene)
        self.new_subsection(scene, "pairings", "data/sound/episode3/slide7-3.mp3")
        scene.wait(3)
        self.pairing.animate_rest(scene)
        self.new_subsection(scene, "verification", "data/sound/episode3/slide7-4.mp3")
        self.pairing.animate_out(scene)

        scene.wait(4)

    def animate_out(self, scene):
        scene.play(FadeOut(self.vec_g1_current), FadeOut(self.vec_next), FadeOut(self.arrow, self.tau_current, self.tau_next,  self.header_label, self.subheader_label, self.title_label))
