from manim import LEFT, RIGHT, DOWN, UP, MathTex, Tex, Text, Write, Line

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR
from zkmarek.video.mobjects.tex_array import TexArray
from zkmarek.video.slides.common.slide_base import SlideBase


SETUP_1 = [
    r"{{ \tau^1 }} \cdot {{ G_1 }}",
    r"{{ \tau^2 }} \cdot {{ G_1 }}",
    r"..." ,
    r"{{ \tau^n }} \cdot {{ G_1 }}"]

SETUP_1_SIMPLER = [
    r"{{ \tau^1 }} {{ G_1 }}",
    r"{{ \tau^2 }} {{ G_1 }}",
    r"...",
    r"{{ \tau^n }} {{ G_1 }}"
]

SETUP_2 = [
    r"\tau^1 G_2",
    r"\tau^2 G_2",
    r"...",
    r"\tau^n G_2"
]

class TrustedSetup(SlideBase):
    title_label: Text
    tau: Tex
    vector: MathTex
    vector_simpler: MathTex
    vector2: MathTex
    strike: Line

    def __init__(self):
        super().__init__("Trusted setup")

    def construct(self):
        self.title_label = Text("Trusted setup", font=PRIMARY_FONT, color=PRIMARY_COLOR)
        self.tau = Tex(r"$\tau$ - random secret shared number in $\mathbb{F}_p$", color=SECONDARY_COLOR)

        self.vector = TexArray(SETUP_1)
        self.vector2 = TexArray(SETUP_2)
        self.title_label.to_edge(UP)
        self.tau.next_to(self.title_label, DOWN, buff=0.8)
        self.vector.next_to(self.tau, DOWN, buff=0.6)
        self.vector2.next_to(self.vector, DOWN)
        self.strike = Line(
            start=self.tau.get_critical_point(LEFT),
            end=self.tau.get_critical_point(RIGHT), color=SECONDARY_COLOR)

    def animate_in(self, scene):
        scene.play(Write(self.title_label))
        scene.play(Write(self.tau))
        scene.play(Write(self.vector))
        self.vector.animate_transform_matching_shapes(scene, SETUP_1_SIMPLER)
        scene.play(Write(self.vector2))
        scene.play(Write(self.strike))

