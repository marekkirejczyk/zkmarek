from manim import LEFT, DOWN, UP, RIGHT, MathTex, Tex, Text, Write, Line, ImageMobject, FadeIn, FadeOut, Indicate

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR, HIGHLIGHT_COLOR
from zkmarek.video.mobjects.tex_array import TexArray
from zkmarek.video.slides.common.slide_base import SlideBase

PARTICIPANT_1 = [
    r"{{\tau_0^1}}  {{G_1}}",
    r"{{\tau_0^2}} {{G_1}}",
    r". . .",
    r"{{\tau_0^n}}  {{G_1}}"
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
        self.person = ImageMobject("zkmarek/video/slides/episode3/person_blue.png").scale(0.5)
        self.person2 = ImageMobject("zkmarek/video/slides/teaser3/person.png").scale(0.5)
        self.person_tau0 = MathTex(r"\tau_0", color = SECONDARY_COLOR, font_size=70).next_to(self.group, DOWN, buff=0.01)
        self.person_tau1 = MathTex(r"\tau_1", color = SECONDARY_COLOR, font_size=70).next_to(self.group, LEFT, buff=0.1)
        self.person_tau2 = MathTex(r"\tau_2", color = SECONDARY_COLOR, font_size=70).next_to(self.group, RIGHT, buff=0.1)
        self.vector_0 = TexArray(PARTICIPANT_1)
        self.vector_1 = TexArray(PARTICIPANT_2)
        self.vector_k = TexArray(PARTICIPANT_N, 3)
        self.tau_0 = Tex(r"$\tau_0$: ", color=SECONDARY_COLOR)
        self.tau_1 = Tex(r"$\tau_1$: ", color=SECONDARY_COLOR)
        self.three_dot = Text(".\n.\n.", font=PRIMARY_FONT, color=SECONDARY_COLOR).scale(0.5)
        self.tau_k = Tex(r"$\tau_k$: ", color=SECONDARY_COLOR)
        self.tau = MathTex(r"\tau = \tau_0 \tau_1 ... \tau_k", color=SECONDARY_COLOR)

        self.title_label.to_edge(UP)
        self.vector_0.next_to(self.title_label, DOWN, buff=0.8)
        self.tau_0.next_to(self.vector_0, LEFT)
        self.person.next_to(self.tau_0, LEFT)
        self.vector_1.next_to(self.vector_0, DOWN, buff=0.5)
        self.tau_1.next_to(self.vector_1, LEFT)
        self.person2.next_to(self.tau_1, LEFT)
        self.three_dot.next_to(self.vector_1, DOWN, buff=0.5)
        self.vector_k.next_to(self.three_dot, DOWN, buff=0.5)
        self.tau_k.next_to(self.vector_k, LEFT)
        self.tau.next_to(self.vector_k, DOWN, buff=0.5)

    def animate_in(self, scene):
        self.new_subsection(scene, "ceremony intro", "data/sound/episode3/slide5-0.mp3")
        scene.play(Write(self.title_label))
        scene.wait(1.5)
        scene.play(FadeIn(self.group))
        scene.play(FadeIn(self.person_tau0))
        scene.play(FadeIn(self.person_tau1))
        scene.play(FadeIn(self.person_tau2))

        self.new_subsection(scene, "first participant", "data/sound/episode3/slide5-1.mp3")
        scene.play(FadeIn(self.person), Write(self.tau_0), FadeOut(self.person_tau0, self.person_tau1, self.person_tau2, self.group))
        scene.wait(1.2)
        scene.play(Indicate(self.tau_0, color = PRIMARY_COLOR), run_time=0.8)
        scene.wait(2.5)
        self.vector_0[0].next_to(self.tau_0, RIGHT)
        scene.play(Write(self.vector_0[0]))
        scene.play(Indicate(self.vector_0.cells[0][1][0], color = HIGHLIGHT_COLOR))

        for i in range(1, len(self.vector_0.cells)):
            self.vector_0.cells[i].next_to(self.vector_0.cells[i-1], RIGHT, buff=0)
            scene.play(Write(self.vector_0.cells[i]), run_time=0.5)
            if i != 2:
                scene.play(Indicate(self.vector_0.cells[i][1][0], color = HIGHLIGHT_COLOR))
            scene.wait(0.4) 

        self.new_subsection(scene, "next participant", "data/sound/episode3/slide5-2.mp3")
        scene.play(Write(self.tau_1), FadeIn(self.person2))
        scene.play(Write(self.vector_1))
        scene.wait(2)
        scene.play(Indicate(self.vector_0.cells[0][1], color = HIGHLIGHT_COLOR))
        scene.play(Indicate(self.vector_0.cells[1][1], color = HIGHLIGHT_COLOR))
        scene.play(Indicate(self.vector_0.cells[3][1], color = HIGHLIGHT_COLOR))

        self.new_subsection(scene, "last participant", "data/sound/episode3/slide5-3.mp3")
        scene.play(Write(self.three_dot))
        scene.play(Write(self.tau_k))
        scene.play(Write(self.vector_k))
        scene.play(Write(self.tau))
        scene.wait(1.5)
        scene.play(Indicate(self.tau_0, color = PRIMARY_COLOR))
        scene.play(Indicate(self.tau_1, color = PRIMARY_COLOR))
        scene.play(Indicate(self.tau_k, color = PRIMARY_COLOR))
        scene.play(Indicate(self.tau, color = PRIMARY_COLOR))