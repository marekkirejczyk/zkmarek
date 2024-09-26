from manim import FadeIn, FadeOut, MathTex, Arrow, Text, LEFT, DOWN, UP, RIGHT, Write, Create, MoveToTarget

from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.e4.discreete_polynomial_chart import (
    DiscreetePolynomialChart,
)
from zkmarek.crypto.field_element import FieldElement
from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR, HIGHLIGHT_COLOR, HIGHLIGHT2_COLOR, PRIMARY_FONT
def poly(x):
    return x * x * x - x * x * 2 + x * 3 + 7

class Security(SlideBase):

    def __init__(self):
        super().__init__("Security")

    def construct(self):
        self.title_text = Text("Security", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 40).to_edge(UP)
        self.chart = DiscreetePolynomialChart(41, poly).to_edge(LEFT).shift(DOWN+LEFT*0.7).scale(0.7)
        self.correct_opening = MathTex(r"{{p(x_0)}} = {{y_0}}", color = PRIMARY_COLOR).scale(0.8).shift(RIGHT*1.5+UP*1.5)
        self.fake_opening = MathTex(r"{{p(x_0)}} = {{y_1}}", color = PRIMARY_COLOR).scale(0.8).shift(RIGHT*1.5)
        self.correct_text = Text("Correct opening", color = PRIMARY_COLOR, font = PRIMARY_FONT).scale(0.7).shift(RIGHT*5+UP*1.5)
        self.fake_text = Text("Fake opening", color = PRIMARY_COLOR, font = PRIMARY_FONT).scale(0.7).shift(RIGHT*5)
        self.arrow_fake = Arrow(self.fake_text.get_left(), self.fake_opening.get_right())
        self.arrow_correct = Arrow(self.correct_text.get_left(), self.correct_opening.get_right())

        self.division_fake = MathTex(r"{{p(x)}} - {{y_0}} = {{(x-x_0)}} {{\cdot q_1(x)}} + \frac{a}{x-x_0}", color = HIGHLIGHT_COLOR).scale(0.7)
        self.division_correct = MathTex(r"{{p(x)}} - {{y_0}} = {{(x-x_0)}} {{\cdot q(x)}}", color = HIGHLIGHT_COLOR).scale(0.7)

        self.tau = FieldElement(33, 41)
        self.value_at_tau = poly(self.tau)
        self.z = FieldElement(14, 41)
        self.y = poly(self.z)
        self.fake_z = FieldElement(32, 41)
        self.fake_y = poly(self.fake_z)
        self.sdh = Text("q-strong SDH assumption", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size=25).next_to(self.chart, RIGHT).shift(UP*1.5+RIGHT)

    def animate_in(self, scene):
        self.new_subsection(scene, "fake proof", "data/sound/e4/slide5-1.mp3")
        scene.play(Write(self.title_text))
        self.chart.gen_points()
        scene.play(Create(self.chart))
        line_z = self.chart.animate_create_vertical_line(
            scene, self.z.value, self.y.value
        )

        scene.play(FadeIn(line_z))
        self.chart.add_xaxis_label(self.z.value, r"x_0")
        scene.wait(2)
        scene.play(Write(self.fake_opening), Write(self.correct_opening))
        scene.wait()
        scene.play(Create(self.arrow_fake), FadeIn(self.fake_text))
        scene.play(Create(self.arrow_correct), FadeIn(self.correct_text))
        scene.wait()
        self.chart.add_yaxis_label(self.y.value, r"y_0")
        self.chart.add_yaxis_label(self.fake_y.value, r"y_1")
        line_fake_y = self.chart.animate_create_horizontal_line(
            scene, self.fake_y.value, 0, self.fake_z.value
        )
        line_correct_y = self.chart.animate_create_horizontal_line(
            scene, self.y.value, 0, self.z.value
        )
        scene.play(FadeIn(line_correct_y))
        scene.play(FadeIn(line_fake_y))
        self.fake_opening.generate_target()
        self.fake_opening.target.shift(1.5*RIGHT+DOWN*1.7)
        self.correct_opening.generate_target()
        self.correct_opening.target.shift(UP*0.1+1.5*RIGHT)
        scene.play(FadeOut(self.fake_text, self.correct_text, self.arrow_correct, self.arrow_fake))

        self.new_subsection(scene, "this only works for correct opening", "data/sound/e4/slide5-2.mp3")
        scene.play(MoveToTarget(self.correct_opening), MoveToTarget(self.fake_opening))
        scene.wait()
        self.division_correct.next_to(self.correct_opening, DOWN)
        self.division_fake.next_to(self.fake_opening, DOWN)
        scene.play(Write(self.division_correct), Write(self.division_fake))

        scene.play(FadeOut(line_z))

        self.new_subsection(scene, "SDH assumption", "data/sound/e4/slide5-3.mp3")
        scene.play(FadeOut(self.fake_opening, self.division_correct, self.division_fake, self.correct_opening))
        scene.wait(1)
        scene.play(Write(self.sdh))
        scene.wait(6)


    def animate_out(self, scene):
        scene.play(FadeOut(self.title_text, self.chart))