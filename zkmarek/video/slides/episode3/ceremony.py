from manim import LEFT, DOWN, UP, RIGHT, MathTex, Tex, Text, Write, Unwrite, Line, ImageMobject, FadeIn, FadeOut, Indicate, Rectangle

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
    r"{{\tau_1^1}} {{G_1}}",
    r"\tau_1^2 G_1",
    ". . .",
    r"\tau_1^n G_1"
]

PARTICIPANT_N = [
    r"{{\tau_i^1}} {{G_1}}",
    r"\tau_i^2 G_1",
    r". . .",
    r"\tau_i^n G_1"
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
        self.group = ImageMobject("data/images/group.png")
        self.person = ImageMobject("data/images/person_blue.png").scale(0.5)
        self.person3 = self.person.copy()
        self.person2 = ImageMobject("data/images/person.png").scale(0.5)
        self.person_tau0 = MathTex(r"\tau_0", color = SECONDARY_COLOR, font_size=70).next_to(self.group, DOWN, buff=0.01)
        self.person_tau1 = MathTex(r"\tau_1", color = SECONDARY_COLOR, font_size=70).next_to(self.group, LEFT, buff=0.1)
        self.person_tau2 = MathTex(r"\tau_2", color = SECONDARY_COLOR, font_size=70).next_to(self.group, RIGHT, buff=0.1)
        self.vector_0 = TexArray(PARTICIPANT_1)
        self.vector_1 = TexArray(PARTICIPANT_2)
        self.vector_k = TexArray(PARTICIPANT_N)
        self.tau_0 = Tex(r"$\tau_0$: ", color=SECONDARY_COLOR)
        self.strike = Line(
            start=self.tau_0.get_critical_point(LEFT),
            end=self.tau_0.get_critical_point(RIGHT), color=SECONDARY_COLOR)

        self.tau_1 = Tex(r"$\tau_1$: ", color=SECONDARY_COLOR)
        self.three_dot = Text(".\n.\n.", font=PRIMARY_FONT, color=SECONDARY_COLOR).scale(0.5)
        self.tau_k = Tex(r"$\tau_i$: ", color=SECONDARY_COLOR)
        self.tau = MathTex(r"\tau = \tau_0 \tau_1 ... \tau_i", color=SECONDARY_COLOR)
        self.secret = Text("secret", font = PRIMARY_FONT, color = SECONDARY_COLOR, font_size=32)

        self.title_label.to_edge(UP)
        self.vector_0.next_to(self.title_label, DOWN, buff=0.8)
        self.tau_0.next_to(self.vector_0, LEFT)
        self.strike.next_to(self.vector_0, LEFT)
        self.secret.next_to(self.vector_0, LEFT)
        self.person.next_to(self.tau_0, LEFT)
        self.vector_1.next_to(self.vector_0, DOWN, buff=0.5)
        self.tau_1.next_to(self.vector_1, LEFT)
        self.person2.next_to(self.tau_1, LEFT)
        self.three_dot.next_to(self.vector_1, DOWN, buff=0.5)
        self.vector_k.next_to(self.three_dot, DOWN, buff=0.5)
        self.tau_k.next_to(self.vector_k, LEFT)
        self.tau.next_to(self.vector_k, DOWN, buff=0.5)
        self.person3.next_to(self.tau_k, LEFT)
        
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
        scene.wait(1)
        scene.play(Indicate(self.tau_0, color = PRIMARY_COLOR), run_time=0.8)
        scene.wait(2.2)
        scene.play(Write(self.strike))
        scene.wait(1.5)
        scene.play(Unwrite(self.strike))
        self.vector_0[0].next_to(self.tau_0, RIGHT)
        scene.play(Write(self.vector_0[0]))
        scene.play(Indicate(self.vector_0.cells[0][1][0], color = HIGHLIGHT_COLOR))

        for i in range(1, len(self.vector_0.cells)):
            self.vector_0.cells[i].next_to(self.vector_0.cells[i-1], RIGHT, buff=0)
            scene.play(Write(self.vector_0.cells[i]), run_time=0.2)
            if i == 3:
                scene.play(Indicate(self.vector_0.cells[i][1][0], color = HIGHLIGHT_COLOR))

        self.new_subsection(scene, "next participant", "data/sound/episode3/slide5-2.mp3")
        scene.play(Write(self.tau_1), FadeIn(self.person2))
        scene.wait(2)
        scene.play(Indicate(self.tau_1, color = PRIMARY_COLOR))
        scene.play(Write(self.vector_1))

        self.new_subsection(scene, "last participant", "data/sound/episode3/slide5-3.mp3")
        scene.play(Write(self.three_dot))
        scene.play(Write(self.tau_k), FadeIn(self.person3))
        scene.play(Write(self.vector_k))
        scene.play(Write(self.tau))
        scene.wait(1.5)
        scene.play(Indicate(self.tau_0, color = PRIMARY_COLOR), run_time=0.5)
        scene.play(Indicate(self.tau_1, color = PRIMARY_COLOR), run_time=0.5)
        scene.play(Indicate(self.tau_k, color = PRIMARY_COLOR), run_time=0.5)
        scene.play(Indicate(self.tau, color = PRIMARY_COLOR), run_time=0.5)
        scene.wait(1.5)

        self.new_subsection(scene, "intro to pairing", "data/sound/episode3_1/slide5-4_new.mp3")
        scene.wait(6)

    def animate_miniature(self, scene):
        rectangle = Rectangle(color=PRIMARY_COLOR, width=15, height=8)
        text = Text("Ceremony of the trusted setup", color=SECONDARY_COLOR,
            font=PRIMARY_FONT, font_size=50).scale(0.65)
        self.add(rectangle, self.title_label, self.tau_0, self.tau_1, self.tau_k)
        self.scale(0.65)
        text.next_to(rectangle, DOWN, buff=0.4)
        self.person.scale(0.65).next_to(self.tau_0, LEFT, buff = 0.6)
        self.person2.scale(0.65).next_to(self.tau_1, LEFT, buff = 0.6)
        self.person3.scale(0.65).next_to(self.tau_k, LEFT, buff = 0.6)
        scene.play(FadeIn(text, rectangle, self.title_label))
        self.add(text)
        scene.play(FadeIn(self.person, self.person2, self.person3))
        scene.play(Write(self.tau_0))
        scene.play(Write(self.tau_1))
        scene.play(Write(self.tau_k))
        self.vector_0.scale(0.65).next_to(self.tau_0, RIGHT, buff = 0.5)
        self.vector_1.scale(0.65).next_to(self.tau_1, RIGHT, buff = 0.5)
        self.vector_k.scale(0.65).next_to(self.tau_k, RIGHT, buff = 0.5)
        self.three_dot.scale(0.65).next_to(self.vector_k, UP, buff = 0.3)

        scene.play(Write(self.vector_0))
        scene.play(Write(self.vector_1))
        scene.play(Write(self.three_dot))
        scene.play(Write(self.vector_k))
        scene.play(Indicate(self.vector_0.cells[0][1][2], color = HIGHLIGHT_COLOR), Indicate(self.vector_1.cells[0][1][2], color = HIGHLIGHT_COLOR), Indicate(self.vector_k.cells[0][1][2], color = HIGHLIGHT_COLOR))

        scene.wait(2)
        scene.play(FadeOut(self.vector_0, self.vector_1, self.vector_k, self.person, self.person2, self.person3, self.tau_0, self.tau_1, self.tau_k, self.three_dot, text, rectangle, self.title_label))
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.person, self.person2, self.person3, self.tau_0, self.tau_1, self.tau_k, self.title_label, self.three_dot, self.vector_0, self.vector_1, self.vector_k, self.tau))