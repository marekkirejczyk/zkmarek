from manim import (Create, DOWN, ImageMobject, RIGHT, LEFT, UP, FadeIn, Polygon, VGroup, Text, Write, Tex, FadeOut, TransformMatchingShapes, RoundedRectangle, 
                   MoveToTarget, ReplacementTransform, MathTex, Circle, Group, CurvedArrow)

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, HIGHLIGHT_COLOR, SECONDARY_COLOR, HIGHLIGHT2_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.e4.discreete_polynomial_chart import DiscreetePolynomialChart
from zkmarek.crypto.field_element import FieldElement

def poly(x):
    if isinstance(x, FieldElement):
        output = FieldElement(4, x.order) * x * x * x - FieldElement(8, x.order) * x * x  - FieldElement(17, x.order) * x + FieldElement(30, x.order)
    else:
        output = 4 * x * x * x - 8 * x * x * 2 - 17 * x + 30
    return output

class Commitment(SlideBase):

    def __init__(self):
        super().__init__("Polynomial Commitments")

    def construct(self):
        self.title_text = Text("Polynomial Commitments", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size=40).to_edge(UP)
        self.verifier = ImageMobject("data/images/person.png").shift(RIGHT*5).scale(0.6)
        self.commiter = ImageMobject("data/images/person_blue.png").shift(LEFT*2).scale(0.6)
        self.commiter_label = Text("Committer", color = PRIMARY_COLOR, font=PRIMARY_FONT).scale(0.6).next_to(self.commiter, DOWN, buff = 0.4)
        self.verifier_label = Text("Verifier", color = PRIMARY_COLOR, font=PRIMARY_FONT).scale(0.6).next_to(self.verifier, DOWN, buff = 0.4)
        self.lock = ImageMobject("data/images/Locked@2x.png").scale(0.2)
        self.thumb = ImageMobject("data/images/Thumb_up.png").scale(0.4)
        self.envelope_body_closed = Polygon(
            [-3, -1, 0], [3, -1, 0], [3, 1, 0], [-3, 1, 0],
            fill_color=PRIMARY_COLOR, fill_opacity=0.5
        ).scale(0.4)

        self.envelope_flap_closed = Polygon(
            [-3, 1, 0], [3, 1, 0], [0, -0.6, 0],
            fill_color=HIGHLIGHT_COLOR, fill_opacity=0.5
        ).scale(0.39)

        self.envelope_body = Polygon(
            [-3, -1, 0], [3, -1, 0], [3, 1, 0], [-3, 1, 0],
            fill_color=PRIMARY_COLOR, fill_opacity=0.5
        ).scale(0.4)
        self.envelope_flap = Polygon(
            [-3, 1, 0], [3, 1, 0], [0, 3, 0], 
            fill_color=HIGHLIGHT_COLOR, fill_opacity=0.5
        ).scale(0.395)
        self.envelope_body.next_to(self.commiter, LEFT+DOWN, buff = 0.6)
        self.envelope_body_closed.next_to(self.commiter, LEFT+DOWN, buff = 0.6)

        self.envelope_flap.next_to(self.envelope_body, UP, buff= 0)
        self.envelope_flap_closed.next_to(self.envelope_body_closed, UP, buff = -0.63)
        self.x_zero = FieldElement(13, 41)
        self.value_at_x_zero = poly(self.x_zero)
        self.tau = FieldElement(33, 41)
        self.value_at_tau = poly(self.tau)
        self.chart = DiscreetePolynomialChart(41, poly)
        self.label_x_0 = self.chart.add_xaxis_label(self.x_zero.value, r"x_0")
        self.label_tau = self.chart.add_xaxis_label(self.tau.value, r"\tau")
        self.chart.scale(0.4)
        self.bubble_committer = RoundedRectangle(corner_radius=0.5, width=self.chart.width + 1, height=self.chart.height + 0.5, color = PRIMARY_COLOR).next_to(self.commiter, UP+LEFT, buff = -1).shift(0.4*DOWN+LEFT*0.6)
        self.opening = MathTex(r"{{p}} ({{x_0}}) = {{y_0}}", font_size=32, color = PRIMARY_COLOR)
        self.proof = MathTex(r"\mathrm{proof} \ \pi", font_size=32, color = PRIMARY_COLOR)
        self.bubble_opening = RoundedRectangle(corner_radius=0.5, width=self.opening.width + 1, height=self.opening.height + 1.5, color = PRIMARY_COLOR).next_to(self.commiter, UP+RIGHT, buff = -0.3)
        self.opening.move_to(self.bubble_opening.get_center())
        self.opening.shift(UP*0.3)
        self.proof.next_to(self.opening, DOWN, buff = 0.3)
        self.chart.move_to(self.bubble_committer.get_center())
        self.tail = Polygon(
            [0.06, 0.08, 0], 
            [-0.35, -1.2, 0], 
            [0.93, -0.63, 0], 
            color=PRIMARY_COLOR,
            fill_opacity=0.4
        ).next_to(self.bubble_opening, DOWN+LEFT, buff=-0.8).scale(0.4).shift(LEFT*0.01+DOWN*0.14)


    def animate_in(self, scene):
        self.new_subsection(scene, "what is commitment", "data/sound/e4/slide2-0.mp3")
        scene.play(Write(self.title_text))
        scene.play(FadeIn(self.commiter))
        scene.play(Write(self.commiter_label))


        scene.play(Create(self.bubble_committer))
        self.chart.gen_points()
        scene.play(Create(self.chart))
        self.lock.next_to(self.chart, RIGHT, buff = 0).shift(UP)

        scene.play(FadeIn(self.lock))
        scene.play(FadeIn(self.verifier))
        scene.play(FadeIn(self.verifier_label))
        scene.wait(1.5)

        self.new_subsection(scene, "commitment locked", "data/sound/e4/slide2-1.mp3")
        speech_text_verifier = Tex(r"$p(x_0) = ?$", font_size=32, color = SECONDARY_COLOR)
        bubble_verifier = RoundedRectangle(corner_radius=0.5, width=speech_text_verifier.width + 1, height=speech_text_verifier.height + 1.2, color = SECONDARY_COLOR).next_to(self.verifier, UP+LEFT, buff = -0.7).shift(0.2*DOWN+LEFT*0.3)
        bubble_verifier.shift(UP) 
        speech_text_verifier.move_to(bubble_verifier.get_center())
        tail_verifier = Polygon(
            [0.2, 0.05, 0], 
            [-0.56, -0.67, 0], 
            [0.78, -1.1, 0], 
            color=SECONDARY_COLOR,
            fill_opacity=0.4
        ).next_to(bubble_verifier, DOWN+RIGHT, buff=-0.8).scale(0.4).shift(RIGHT*0.06+DOWN*0.17)
        self.commitment_text = Text("Commitment", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size=25).next_to(self.envelope_body_closed, DOWN+RIGHT).shift(DOWN*0.5+RIGHT*0.7)
        self.arrow_commitment = CurvedArrow(self.commitment_text.get_left(), self.envelope_body_closed.get_right(), color = HIGHLIGHT2_COLOR).shift(UP*0.2)


        scene.play(FadeIn(self.envelope_body_closed, self.envelope_flap_closed))
        scene.play(FadeOut(self.envelope_flap_closed), FadeIn(self.envelope_flap), FadeIn(self.commitment_text, self.arrow_commitment))
        self.dots = VGroup(*self.chart.dots).copy()
        self.lock_copy = self.lock.copy()
        self.lock_copy.generate_target()
        self.lock_copy.target.move_to(self.envelope_body_closed.get_center())

        scene.play(TransformMatchingShapes(VGroup(self.dots), self.envelope_flap_closed), FadeOut(self.envelope_flap), MoveToTarget(self.lock_copy), run_time=2)

        self.new_subsection(scene, "cant open it", "data/sound/e4/slide2-2.mp3")

        commitment_sent = Group(self.envelope_body_closed, self.envelope_flap_closed, self.lock_copy)
        commitment_sent.generate_target()
        commitment_sent.target.shift(9.5*RIGHT+DOWN*0.7)
        self.envelope_flap.shift(9.5*RIGHT+DOWN*0.7)
        scene.play(FadeOut(self.arrow_commitment, self.commitment_text))
        scene.play(MoveToTarget(commitment_sent), run_time=1.8)

        scene.play(Create(bubble_verifier), Create(tail_verifier))
        scene.play(Create(speech_text_verifier))

        self.x0 = FieldElement(13, 41)
        self.y = poly(self.x0)

        self.circle = Circle(radius = 0.12, color = HIGHLIGHT2_COLOR).next_to(self.chart, DOWN, buff=-1).shift(LEFT*0.42+UP*0.28)
        self.circle_full = Circle(radius = 0.1, color = HIGHLIGHT2_COLOR, fill_opacity = 1).next_to(self.chart, DOWN, buff=-1).shift(LEFT*0.42+UP*0.28)
        scene.wait(0.7)
        self.chart.indicate_xaxis_label(scene, self.label_x_0)
        scene.play(Create(self.circle))
        scene.play(TransformMatchingShapes(self.circle, self.circle_full))
        self.circle_full.generate_target()
        self.circle_full.target.next_to(self.opening, LEFT, buff = 0.1)
        self.lock_open = ImageMobject("data/images/Lock_Open.png").scale(0.2).move_to(self.envelope_body_closed.get_center())
        scene.play(FadeIn(self.opening, self.bubble_opening, self.tail), MoveToTarget(self.circle_full), ReplacementTransform(self.lock_copy, self.lock_open))

        self.new_subsection(scene, "request to open", "data/sound/e4/slide2-3.mp3")
        scene.play(FadeOut(bubble_verifier, speech_text_verifier, tail_verifier))
        scene.play(Write(self.proof))
        scene.wait(1)
        self.opening.generate_target()
        self.opening.target.next_to(self.verifier, UP)
        self.proof.generate_target()
        self.proof.target.next_to(self.verifier, UP).shift(UP)
        scene.play(FadeOut(self.bubble_opening, self.tail), FadeOut(self.circle_full))
        scene.play(MoveToTarget(self.proof), MoveToTarget(self.opening), run_time=1.5)
        scene.wait(0.5)
        self.arrow_check_opening = CurvedArrow(self.proof.get_left(), self.opening.get_left(), color = HIGHLIGHT_COLOR)
        self.arrow_check_opening2 = CurvedArrow(self.proof.get_left(), self.envelope_flap_closed.get_left(), color = HIGHLIGHT_COLOR)
        self.thumb.next_to(self.arrow_check_opening2, LEFT, buff=0)
        scene.play(FadeIn(self.thumb), Write(self.arrow_check_opening), Write(self.arrow_check_opening2))
        scene.wait(2.4)
        

    def animate_out(self, scene):
        scene.play(FadeOut(self.bubble_committer, self.envelope_flap_closed, self.lock, self.envelope_body_closed, self.opening, self.proof, self.arrow_check_opening, self.thumb, self.lock_open, self.commiter, self.commiter_label, self.verifier, self.verifier_label, self.title_text, self.chart, self.arrow_check_opening2))


    def animate_miniature(self, scene):
        rectangle = RoundedRectangle(corner_radius=0.5, color=PRIMARY_COLOR, width=15, height=8).scale(0.65).shift(UP).set_color_by_gradient(PRIMARY_COLOR, HIGHLIGHT2_COLOR)
        text = Text("Polynomial commitments", color=SECONDARY_COLOR,
            font=PRIMARY_FONT, font_size=50).scale(0.65).next_to(rectangle, UP, buff = 0.4)

        speech_text_verifier = Tex(r"$p(x_0) = ?$", font_size=32, color = SECONDARY_COLOR).scale(0.65)
        bubble_verifier = RoundedRectangle(corner_radius=0.5, width=speech_text_verifier.width + 1, height=speech_text_verifier.height + 1.2, color = SECONDARY_COLOR).next_to(self.verifier, UP+LEFT, buff = -0.7).shift(0.2*DOWN+LEFT*0.3).scale(0.65)
        bubble_verifier.shift(UP)
        speech_text_verifier.move_to(bubble_verifier.get_center())
        tail_verifier = Polygon(
            [0.2, 0.05, 0], 
            [-0.56, -0.67, 0], 
            [0.78, -1.1, 0], 
            color=SECONDARY_COLOR,
            fill_opacity=0.4
        ).next_to(bubble_verifier, DOWN+RIGHT, buff=-0.8).scale(0.3).shift(RIGHT*0.06+DOWN*0.17)

        self.scale(0.65)
        self.add(text)
        self.all_mobjects = Group(self.commiter, self.commiter_label, self.bubble_opening, self.verifier, self.verifier_label, self.bubble_committer, self.chart, 
                 self.envelope_body_closed, self.envelope_flap_closed, self.opening, tail_verifier, bubble_verifier, speech_text_verifier, self.tail).scale(0.65).shift(UP)
        self.chart.gen_points()
        scene.play(FadeIn(self.commiter, self.commiter_label, self.bubble_opening, self.verifier, self.verifier_label, self.chart, 
                 self.envelope_body_closed, self.envelope_flap_closed, text, rectangle))
        scene.play(FadeIn(tail_verifier, bubble_verifier, speech_text_verifier))
        scene.wait(0.5)
        scene.play(FadeIn(self.bubble_committer, self.tail), Write(self.opening))
        
        