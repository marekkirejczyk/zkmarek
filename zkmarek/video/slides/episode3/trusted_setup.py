from manim import LEFT, RIGHT, DOWN, UP, MathTex, Tex, Text, Write, Line

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR
from zkmarek.video.mobjects.tex_array import TexArray
from zkmarek.video.slides.common.slide_base import SlideBase


SETUP_G1_1 = [
    r"{{ \tau^1 }} \cdot {{ G_1 }}",
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
    r"\tau^1 G_2",
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
        self.vector_g2 = TexArray(SETUP_G2_1)
        self.title_label.to_edge(UP)
        self.tau.next_to(self.title_label, DOWN, buff=0.8)
        self.vector_g1.next_to(self.tau, DOWN, buff=0.6)
        self.vector_g2.next_to(self.vector_g1, DOWN)
        self.strike = Line(
            start=self.tau.get_critical_point(LEFT),
            end=self.tau.get_critical_point(RIGHT), color=SECONDARY_COLOR)

    def animate_in(self, scene):
        self.new_subsection(scene, "intro to trusted setup", "data/sound/episode3/slide4-0.mp3")
        scene.play(Write(self.title_label))
        scene.wait(1.5)
        scene.play(Write(self.tau))
        
        self.new_subsection(scene, "multiplying by G1", "data/sound/episode3/slide4-2.mp3")
        scene.play(Write(self.vector_g1))
        self.vector_g1.animate_transform_matching_shapes(scene, SETUP_G1_2)

        self.new_subsection(scene, "multiplying by G2", "data/sound/episode3/slide4-3.mp3")
        scene.play(Write(self.vector_g2))
        scene.play(Write(self.strike))
        self.vector_g1.animate_transform_matching_shapes(scene, SETUP_G1_3)
        
        self.new_subsection(scene, "there are ec points", "data/sound/episode3/slide4-4.mp3")
        self.vector_g2.animate_transform_matching_shapes(scene, SETUP_G2_2)
        
        scene.wait(5)


