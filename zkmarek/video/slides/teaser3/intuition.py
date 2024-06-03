from manim import FadeIn, FadeOut, Line, MathTex, LEFT, RIGHT, Arrow, DOWN, Text

from zkmarek.video.slides.common.slide_base import SlideBase


class Intuition(SlideBase):
    def __init__(self) -> None:
        super().__init__(title="Intuition")

    def construct(self):
        self.line = Line(LEFT, RIGHT)
        self.u1 = MathTex(r"u_1 = {{-msg \cdot r^{-1} \mod n }}")
        self.u2 = MathTex(r"u_2 = {{s \cdot r^{-1} \mod n }}")
        self.arrow = Arrow(start=self.line.get_end(), end=self.line.get_end() + DOWN)
        self.label = Text(r"\times G").next_to(self.arrow, RIGHT)

    def animate_in(self, scene):
        scene.play(FadeIn(self.line), FadeIn(self.u1), FadeIn(self.u1), run_time=0.7)
        scene.wait(1)
        scene.play(FadeIn(self.arrow), FadeIn(self.label), run_time=0.5)

    def animate_out(self, scene):
        scene.play(FadeOut(self.line))
