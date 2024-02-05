from manim import LEFT, DOWN, UP, MathTex, Tex, Text, Write, Line

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase


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
        self.vector_0 = MathTex(r"[ \tau_0^1 G_1 ,\  \tau_0^2   G_1,\  . . .\ ,\ \tau_0^n   G_1 ]", color=SECONDARY_COLOR)
        self.vector_1 = MathTex(r"[ \tau_0^1 \tau_1^1 G_1, \ \tau_0^2\tau_1^2 G_1,\  . . .\ ,\   \tau_0^n \tau_1^n G_1 ]", color=SECONDARY_COLOR)
        self.vector_k = MathTex(r"[ \tau_0^1 \tau_1^1 ... \tau_k^1 G_1, \  \tau_0^2\tau_1^2 ... \tau_k^2 G_1,\ . . .\ ,\ \tau_0^n \tau_1^n ... \tau_k^n G_1 ]", color=SECONDARY_COLOR)
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
        scene.play(Write(self.title_label))
        scene.play(Write(self.tau_0))
        scene.play(Write(self.vector_0))
        scene.play(Write(self.tau_1))
        scene.play(Write(self.vector_1))
        scene.play(Write(self.three_dot))
        scene.play(Write(self.tau_k))
        scene.play(Write(self.vector_k))
        scene.play(Write(self.tau))
        scene.wait(2)
