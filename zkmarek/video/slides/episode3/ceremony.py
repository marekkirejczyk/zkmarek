from manim import LEFT, DOWN, UP, MathTex, Tex, Text, Write, Line, ImageMobject, FadeIn, FadeOut, Indicate

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR
from zkmarek.video.mobjects.tex_array import TexArray
from zkmarek.video.slides.common.slide_base import SlideBase

PARTICIPANT_1 = [
    r"\tau_0^1 G_1",
    r"\tau_0^2 G_1",
    r". . .",
    r"\tau_0^n  G_1"
]

PARTICIPANT_2 = [
    r"\tau_0^1 \tau_1^1 G_1",
    r"\tau_0^2\tau_1^2 G_1",
    ". . .",
    r"\tau_0^n \tau_1^n G_1"
]

PARTICIPANT_N = [
    r"\tau_0^1 \tau_1^1 ... \tau_k^1 G_1",
    r"\tau_0^2\tau_1^2 ... \tau_k^2 G_1",
    r". . .",
    r"\tau_0^n \tau_1^n ... \tau_k^n G_1"
]


class Ceremony(SlideBase):
    title_label: Text
    three_dot: Text
    tau_0: Tex
    tau_1: Tex
    tau_k: Tex
    tau: Tex
    vector_0: MathTex
    vector_1: MathTex
    vector_k: MathTex
    strike: Line

    def __init__(self):
        super().__init__("Ceremony")

    def construct(self):
        self.title_label = Text("Ceremony", font=PRIMARY_FONT, color=PRIMARY_COLOR)
        self.group = ImageMobject("zkmarek/video/slides/episode3/group.png")
        self.vector_0 = TexArray(PARTICIPANT_1)
        self.vector_1 = TexArray(PARTICIPANT_2)
        self.vector_k = TexArray(PARTICIPANT_N, 3)
        self.tau_0 = Tex(r"$\tau_0$: ", color=SECONDARY_COLOR)
        self.tau_1 = Tex(r"$\tau_1$: ", color=SECONDARY_COLOR)
        self.three_dot = Text(".\n.\n.", font=PRIMARY_FONT, color=SECONDARY_COLOR)
        self.tau_k = Tex(r"$\tau_k$: ", color=SECONDARY_COLOR)
        self.tau = MathTex(r"\tau = \tau_0 \tau_1 ... \tau_k", color=SECONDARY_COLOR)

        self.title_label.to_edge(UP)
        self.vector_0.next_to(self.title_label, DOWN, buff=0.8)
        self.tau_0.next_to(self.vector_0, LEFT)
        self.vector_1.next_to(self.vector_0, DOWN, buff=0.5)
        self.tau_1.next_to(self.vector_1, LEFT)
        self.three_dot.next_to(self.vector_1, DOWN, buff=0.5)
        self.vector_k.next_to(self.three_dot, DOWN, buff=0.5)
        self.tau_k.next_to(self.vector_k, LEFT)
        self.tau.next_to(self.vector_k, DOWN, buff=0.5)

    def animate_in(self, scene):
        self.new_subsection(scene, "ceremony intro", "data/sound/episode3/slide5-0.mp3")
        scene.play(Write(self.title_label))
        scene.wait(1.5)
        scene.play(FadeIn(self.group))

        self.new_subsection(scene, "first participant", "data/sound/episode3/slide5-1.mp3")
        scene.play(Write(self.tau_0), FadeOut(self.group))
        scene.play(Write(self.vector_0))
        scene.play(Indicate(self.tau_0, color = SECONDARY_COLOR))
        self.new_subsection(scene, "beginning of ceremony", "data/sound/episode3/slide5-2.mp3")
        scene.play(Write(self.tau_1))
        scene.play(Write(self.vector_1))
        scene.play(Write(self.three_dot))
        scene.wait(3)
        scene.play(Indicate(self.tau_0))
        scene.play(Indicate(self.tau_1))
        self.new_subsection(scene, "next participant", "data/sound/episode3/slide5-3.mp3")
        scene.play(Write(self.tau_k))
        scene.play(Write(self.vector_k))
        scene.play(Write(self.tau))
        scene.wait(2)
