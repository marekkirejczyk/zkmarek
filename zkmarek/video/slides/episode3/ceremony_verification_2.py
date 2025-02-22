from manim import DOWN, RIGHT, TAU, UP, LEFT, CurvedArrow, FadeIn, FadeOut, MathTex, Text, Write, Indicate, MoveToTarget, TransformMatchingTex, ImageMobject

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR, HIGHLIGHT_COLOR
from zkmarek.video.mobjects.tex_array import TexArray
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.episode3.morphin_math_text import MorphinMathText

SETUP_CURRENT = [
    r"{{ P_0 }}",
    r"{{ P_1 }}",
    r"..." ,
    r"{{ P_{n-1} }}"]


SETUP_NEXT = [
    r"{{ \Tilde{P_0}}}",
    r"{{ \Tilde{P_1} }}",
    r"..." ,
    r"{{ \Tilde{P}_{n-1} }}"]

SETUP_CURRENT_Q = [
    r"{{ Q_0 }}",
    r"{{ Q_1} }}",
    r"..." ,
    r"{{ Q_{k-1} }}"]

SETUP_NEXT_Q = [
    r"{{ \Tilde{Q_0}}}",
    r"{{ \Tilde{Q_1} }}",
    r"..." ,
    r"{{ \Tilde{Q}_{k-1} }}"]

widths = [2, 2, 1, 2]

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
        self.vec_next_Q = TexArray(SETUP_NEXT_Q, widths=widths)
        self.vec_current_Q = TexArray(SETUP_CURRENT_Q, widths=widths)
        self.tau_current = MathTex(r"\tau", font_size=40, color=SECONDARY_COLOR)
        self.tau_next = MathTex(r"\Tilde{\tau}", font_size=40, color=SECONDARY_COLOR)

        self.person_current = ImageMobject("data/images/person_blue.png").scale(0.5)
        self.person_next = ImageMobject("data/images/person.png").scale(0.5)

        self.title_label.to_edge(UP)
        self.header_label.next_to(self.title_label, DOWN, buff=0.8)
        self.subheader_label.next_to(self.header_label, DOWN, buff=0.3)
        self.vec_g1_current.next_to(self.subheader_label, DOWN, buff=0.3)
        self.vec_next.next_to(self.vec_g1_current, DOWN, buff=0.5)
        self.tau_current.next_to(self.vec_g1_current, RIGHT, buff=0.5)
        self.tau_next.next_to(self.vec_next, RIGHT, buff=0.5)

        self.vec_current_Q.next_to(self.vec_g1_current, DOWN, buff=0.03)
        self.arrow = CurvedArrow(self.vec_g1_current[0].get_left(), self.vec_next[0].get_left(),
            angle=TAU/4, color=PRIMARY_COLOR)
        self.pairing_ex = MathTex(r"e({{G_1}}, {{G_2}})", color = SECONDARY_COLOR)
        self.pairing_ex2 = MathTex(r"e({{P}}, {{Q}})", color = SECONDARY_COLOR)
        self.pairing = MorphinMathText([
            r"{{e(P_0, \Tilde{Q}_0)}}",
            r"{{e(P_0, \Tilde{Q}_0)}} = e(P_0, {{ \Tilde{\tau} }} \cdot G_2)}}",
            r"{{e(P_0, \Tilde{Q}_0)}} = e(P_0 {{ \Tilde{\tau} }}, G_2)}}",
            r"{{e(P_0, \Tilde{Q}_0)}} = e(\Tilde{P}_0, G_2)",
        ], wait_time=2)
        self.pairing.next_to(self.vec_next, DOWN, buff=0.5)
        self.pairing_ex.next_to(self.vec_next, DOWN, buff=0.5)
        self.pairing_ex2.next_to(self.vec_next, DOWN, buff=0.5)
        self.person_current.next_to(self.vec_g1_current, LEFT)
        self.person_next.next_to(self.vec_next, LEFT)

    def animate_in(self, scene):
        self.new_subsection(scene, "another array", "data/sound/episode3/slide7-0.mp3")
        scene.play(Write(self.title_label))
        scene.play(Write(self.header_label))
        scene.play(Write(self.subheader_label))


        scene.play(FadeIn(self.vec_g1_current, self.person_current))
        scene.play(FadeIn(self.tau_current))

        self.new_subsection(scene, "P and P tilde", "data/sound/episode3/slide7-1.mp3")
        scene.wait(1.5)

        scene.play(FadeIn(self.vec_next, self.person_next))
        scene.play(FadeIn(self.tau_next))

        scene.wait(4)
        self.vec_next.generate_target()
        self.vec_next.target.next_to(self.vec_current_Q, DOWN, buff=0.2)    
        self.vec_next_Q.to_edge(DOWN)

        self.tau_next.generate_target()
        self.tau_next.target.shift(DOWN*1.2)
        self.tau_current.generate_target()
        self.tau_current.target.shift(DOWN*0.4)

        self.person_next.generate_target()
        self.person_next.target.shift(DOWN*1.2)
        self.person_current.generate_target()
        self.person_current.target.shift(DOWN*0.4)
        scene.play(MoveToTarget(self.vec_next), MoveToTarget(self.tau_next), MoveToTarget(self.person_current), MoveToTarget(self.tau_current), MoveToTarget(self.person_next), FadeIn(self.vec_current_Q, self.vec_next_Q))

        self.new_subsection(scene, "verify", "data/sound/episode3/slide7-2.mp3")
        self.vec_next.generate_target()
        self.vec_next.target.next_to(self.vec_g1_current, DOWN, buff=0.5)
        self.tau_next.generate_target()
        self.tau_next.target.shift(UP*1.2)
        self.tau_current.generate_target()
        self.tau_current.target.shift(UP*0.4)

        self.person_next.generate_target()
        self.person_next.target.shift(UP*1.2)
        self.person_current.generate_target()
        self.person_current.target.shift(UP*0.4)
        scene.play(MoveToTarget(self.vec_next), MoveToTarget(self.tau_next), MoveToTarget(self.person_current), MoveToTarget(self.person_next), FadeOut(self.vec_current_Q, self.vec_next_Q))
        scene.play(FadeIn(self.arrow))

        self.new_subsection(scene, "pairings", "data/sound/episode3/slide7-3.mp3")
        scene.wait(1)
        scene.play(Write(self.pairing_ex))
        scene.wait(4.5)
        scene.play(Indicate(self.pairing_ex[1], color = HIGHLIGHT_COLOR))
        scene.wait(1)
        scene.play(Indicate(self.pairing_ex[3], color = HIGHLIGHT_COLOR))
        scene.wait(2)
        scene.play(TransformMatchingTex(self.pairing_ex, self.pairing_ex2))
        scene.wait(1.5)
        scene.play(FadeOut(self.pairing_ex2))
        self.new_subsection(scene, "we take P and Q tilde", "data/sound/episode3_1/slide7-3_2.mp3")
        self.pairing.animate_first(scene)

        self.new_subsection(scene, "evaluating Pi", "data/sound/episode3/slide7-4.mp3")
        self.pairing.animate_rest(scene)

        self.new_subsection(scene, "verification", "data/sound/episode3_1/slide7-5.mp3")
        self.pairing.animate_out(scene)
        scene.wait(1)
        scene.play(Indicate(self.vec_next.cells[0][1], color = HIGHLIGHT_COLOR), run_time=0.5) 
        scene.play(Indicate(self.vec_next.cells[1][1], color = HIGHLIGHT_COLOR), run_time=0.5) 
        scene.play(Indicate(self.vec_next.cells[3][1], color = HIGHLIGHT_COLOR), run_time=0.5) 
        scene.wait(2.7)

    def animate_out(self, scene):
        scene.play(FadeOut(self.vec_g1_current), FadeOut(self.vec_next), FadeOut(self.arrow, self.tau_current, self.tau_next,  self.header_label, self.subheader_label, self.title_label, self.person_current, self.person_next))
