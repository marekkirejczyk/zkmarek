from manim import LEFT, RIGHT, DOWN, UP, MathTex, Tex, Text, Write, Line, ImageMobject, FadeIn, FadeOut, Indicate, TransformMatchingShapes

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR, HIGHLIGHT_COLOR
from zkmarek.video.mobjects.tex_array import TexArray
from zkmarek.video.slides.common.slide_base import SlideBase


SETUP_G1_1 = [
    r"{{ \tau }} \cdot {{ G_1 }}",
    r"{{ \tau^2 }} \cdot {{ G_1 }}",
    r"..." ,
    r"{{ \tau^n }} \cdot {{ G_1 }}"]

SETUP_G1_2 = [
    r"{{ \tau^1 }} {{ G_1 }}",
    r"{{ \tau^2 }} {{ G_1 }}",
    r"...",
    r"{{ \tau^n }} {{ G_1 }}"
]

SETUP_G1_3 = [
    r"P_0",
    r"P_1",
    r"...",
    r"P_{N-1}"
]

SETUP_G2_1 = [
    r"{{\tau}} {{G_2}}",
    r"\tau^2 G_2",
    r"...",
    r"\tau^n G_2"
]

SETUP_G2_2 = [
    r"Q_0",
    r"Q_1",
    r"...",
    r"Q_{N-1}"
]

class TrustedSetup(SlideBase):
    title_label: Text
    tau: Tex
    vector_g1: MathTex
    vector_g2: MathTex
    strike: Line

    def __init__(self):
        super().__init__("Trusted setup")

    def construct(self):
        self.title_label = Text("Trusted setup", font=PRIMARY_FONT, color=PRIMARY_COLOR)
        self.tau = Tex(r"$\tau$ - random secret shared number in $\mathbb{F}_p$", color=SECONDARY_COLOR)

        self.vector_g1 = TexArray(SETUP_G1_1)
        self.new_vector_g1 = TexArray(SETUP_G1_2)
        self.vector_g2 = TexArray(SETUP_G2_1)
        self.new_vector_g2 = TexArray(SETUP_G2_1)
        self.title_label.to_edge(UP)
        self.tau.next_to(self.title_label, DOWN, buff=0.8)
        self.vector_g1.next_to(self.tau, DOWN, buff=0.6)
        self.new_vector_g1.next_to(self.tau, DOWN, buff=0.6)
        self.vector_g2.next_to(self.vector_g1, DOWN)
        self.new_vector_g2.next_to(self.vector_g1, DOWN)
        self.strike = Line(
            start=self.tau.get_critical_point(LEFT),
            end=self.tau.get_critical_point(RIGHT), color=SECONDARY_COLOR)

        person = ImageMobject("data/images/person.png").scale(0.45).shift(DOWN)

        self.person1 = person.copy().shift(2*LEFT)
        self.person2 = person.copy().shift(2*RIGHT)
        self.person3 = person.copy().shift(1.5*UP)
        self.person4 = person.copy().shift(1.5*DOWN)

        self.tau_number = MathTex(r"\tau", font_size=80, color = SECONDARY_COLOR).shift(DOWN)

        question = Text("?", font_size=35, color = PRIMARY_COLOR, font = PRIMARY_FONT)

        self.question1 = question.copy().next_to(self.person1, UP+RIGHT).shift(DOWN*0.7+LEFT*0.5)
        self.question2 = question.copy().next_to(self.person2, UP+RIGHT).shift(DOWN*0.7+LEFT*0.5)
        self.question3 = question.copy().next_to(self.person3, UP+RIGHT).shift(DOWN*0.7+LEFT*0.5)
        self.question4 = question.copy().next_to(self.person4, UP+RIGHT).shift(DOWN*0.7+LEFT*0.5)

    def animate_in(self, scene):
        self.new_subsection(scene, "intro to trusted setup", "data/sound/episode3/slide4-0.mp3")
        scene.play(Write(self.title_label))
        scene.wait(2)
        scene.play(Write(self.tau))
        scene.play(FadeIn(self.person1))
        scene.play(FadeIn(self.person3))
        scene.play(FadeIn(self.person2))
        scene.play(FadeIn(self.person4))
        scene.play(FadeIn(self.tau_number))
        scene.play(FadeIn(self.question4, self.question1, self.question3, self.question2))
        scene.wait(3.5)

        self.new_subsection(scene, "multiplying by G1", "data/sound/episode3/slide4-1.mp3")
        scene.play(FadeOut(self.question4, self.question1, self.question3, self.question2, self.person1, self.person2, self.person3, self.person4, self.tau_number))
        scene.play(Write(self.vector_g1.cells[0])) 
        scene.wait(6)

        scene.play(Indicate(self.vector_g1.cells[0][1][2], color = HIGHLIGHT_COLOR)) # indicate on G1
        scene.wait(3)
        scene.play(Indicate(self.vector_g1.cells[0][1][0], color = HIGHLIGHT_COLOR)) # indicate on tau
        scene.wait(3)
        scene.play(Indicate(self.vector_g1.cells[0][1][0], color = HIGHLIGHT_COLOR))
        for i in range(1, len(self.vector_g1.cells)):
            self.vector_g1.cells[i].next_to(self.vector_g1.cells[i-1], RIGHT, buff=0)
            scene.play(FadeIn(self.vector_g1.cells[i]), run_time=0.4)
            if i != 2:
                scene.play(Indicate(self.vector_g1.cells[i][1][0], color = HIGHLIGHT_COLOR))
            # scene.wait(0.4) 

        for old_cell, new_cell in zip(self.vector_g1.cells, self.new_vector_g1.cells):
            scene.play(TransformMatchingShapes(old_cell[1], new_cell[1]), run_time=0.4)

        self.new_subsection(scene, "multiplying by G2", "data/sound/episode3/slide4-2.mp3")
        scene.wait(1.5)
        scene.play(Write(self.vector_g2))
        scene.play(Indicate(self.new_vector_g1.cells[0][1][2], color = HIGHLIGHT_COLOR), Indicate(self.vector_g2.cells[0][1][2], color = HIGHLIGHT_COLOR))

        self.new_subsection(scene, "there are ec points", "data/sound/episode3/slide4-3.mp3")
        self.new_vector_g1.animate_transform_matching_shapes(scene, SETUP_G1_3)
        self.vector_g2.animate_transform_matching_shapes(scene, SETUP_G2_2)
        scene.wait(3.5)

