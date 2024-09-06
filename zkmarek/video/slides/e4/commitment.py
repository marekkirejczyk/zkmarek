from manim import Create, DOWN, ImageMobject, RIGHT, LEFT, UP, FadeIn, Polygon, VGroup, Text, Write, Tex, FadeOut, TransformMatchingShapes, RoundedRectangle, MoveToTarget, Transform, MathTex, Circle, Indicate

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, HIGHLIGHT_COLOR, SECONDARY_COLOR, HIGHLIGHT2_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.utils import load
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
        super().__init__("Commitment")

    def construct(self):
        self.title_text = Text("Commitment scheme", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size=40).to_edge(UP)
        self.verifier = ImageMobject("data/images/person.png").shift(RIGHT*5).scale(0.6)
        self.commiter = ImageMobject("data/images/person_blue.png").shift(LEFT*2).scale(0.6)
        self.commiter_label = Text("Committer", color = PRIMARY_COLOR, font=PRIMARY_FONT).scale(0.6).next_to(self.commiter, DOWN, buff = 0.4)
        self.verifier_label = Text("Verifier", color = PRIMARY_COLOR, font=PRIMARY_FONT).scale(0.6).next_to(self.verifier, DOWN, buff = 0.4)
        self.lock = ImageMobject("data/images/Locked@2x.png").scale(0.2)
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
        self.envelope_body.next_to(self.commiter, LEFT+DOWN, buff = 0.4)
        self.envelope_body_closed.next_to(self.commiter, LEFT+DOWN, buff = 0.4)

        self.envelope_flap.next_to(self.envelope_body, UP, buff= 0)
        self.envelope_flap_closed.next_to(self.envelope_body_closed, UP, buff = -0.63)
        self.chart = DiscreetePolynomialChart(41, poly).scale(0.4)
        self.tex = Tex(load("zkmarek/video/slides/e4/stages.tex"), color=SECONDARY_COLOR).scale(0.55).shift(0.9*RIGHT+DOWN*1.5)
        self.opening = MathTex(r"p(x_0) = y", color = SECONDARY_COLOR).shift(2*UP)


    def animate_in(self, scene):
        self.new_subsection(scene, "what is commitment", "data/sound/e4/slide2-0.mp3")
        scene.play(Write(self.title_text))
        scene.play(FadeIn(self.commiter))
        scene.play(Write(self.commiter_label))
        # (1) 0-33 (2) 34-68 (3) 60-99 (4) 100-120 (5) 121-139
        bubble_committer = RoundedRectangle(corner_radius=0.5, width=self.chart.width + 1, height=self.chart.height + 0.5, color = PRIMARY_COLOR).next_to(self.commiter, UP+LEFT, buff = -1).shift(0.4*DOWN+LEFT*0.6)

        self.chart.move_to(bubble_committer.get_center())

        scene.play(Create(bubble_committer))
        self.chart.gen_points()
        scene.play(Create(self.chart))
        self.lock.next_to(self.chart, RIGHT, buff = 0).shift(UP)
        scene.wait(1)
        scene.play(FadeIn(self.lock))

        self.new_subsection(scene, "commitment locked", "data/sound/e4/slide2-1.mp3")


        speech_text_verifier = Tex(r"Hey, can you let me\\ open the commitment?", font_size=32, color = PRIMARY_COLOR)

        bubble_verifier = RoundedRectangle(corner_radius=0.5, width=speech_text_verifier.width + 1, height=speech_text_verifier.height + 0.5, color = PRIMARY_COLOR).next_to(self.verifier, UP+LEFT, buff = -0.7).shift(0.2*DOWN)
        bubble_verifier.shift(UP) 
        speech_text_verifier.move_to(bubble_verifier.get_center())

        self.tau = FieldElement(33, 41)
        self.value_at_tau = poly(self.tau)

        # scene.play(Write(self.tex[0][0:33]))

        scene.play(FadeIn(self.envelope_body_closed, self.envelope_flap_closed))
        scene.play(TransformMatchingShapes(self.envelope_flap_closed, self.envelope_flap))
        self.dots = VGroup(*self.chart.dots).copy()
        self.lock_copy = self.lock.copy()
        self.lock_copy.generate_target()
        self.lock_copy.target.move_to(self.envelope_body_closed.get_center())

        scene.play(TransformMatchingShapes(VGroup(self.envelope_flap, self.dots), self.envelope_flap_closed), MoveToTarget(self.lock_copy), run_time=2)

        self.new_subsection(scene, "cant open it", "data/sound/e4/slide2-2.mp3")

        scene.play(FadeIn(self.verifier))
        scene.play(FadeIn(self.verifier_label))

        commitment_sent = VGroup(self.envelope_body_closed, self.envelope_flap_closed, self.lock_copy)
        commitment_sent.generate_target()
        commitment_sent.target.shift(9.5*RIGHT+DOWN)
        self.envelope_flap.shift(9.5*RIGHT+DOWN)

        scene.play(MoveToTarget(commitment_sent), run_time=1.8)
        # scene.play(Write(self.tex[0][33:68]))
        self.new_subsection(scene, "request to open", "data/sound/e4/slide2-3.mp3")

        scene.play(Create(bubble_verifier))
        scene.play(Create(speech_text_verifier))

        # scene.play(Write(self.tex[0][68:108]))
        self.x0 = FieldElement(13, 41)
        self.y = poly(self.x0)
        self.chart.add_xaxis_label(self.tau.value, r"x_0")
        # scene.play(Write(self.tex[0][108:130]))
        self.circle = Circle(radius = 0.3, color = HIGHLIGHT2_COLOR).next_to(self.chart, DOWN, buff=-1).shift(RIGHT*0.7+UP*0.9)

        scene.play(FadeOut(bubble_verifier, speech_text_verifier))
        scene.play(Create(self.circle))
        scene.play(TransformMatchingShapes(VGroup(self.circle), self.opening))
        self.proof = MathTex(r"\pi", color = SECONDARY_COLOR).next_to(self.opening, DOWN)
        # scene.play(Write(self.tex[0][130:]))
        scene.wait(1.5)
        scene.play(Write(self.proof), run_time=0.5)
        scene.play(Transform(self.envelope_flap_closed, self.envelope_flap), FadeIn(self.envelope_flap), FadeOut(self.envelope_flap_closed))

        self.new_subsection(scene, "once again", "data/sound/e4/slide2-4.mp3")
        scene.play(FadeOut(self.envelope_flap, self.envelope_body_closed, self.opening, self.proof))
        scene.wait(2.7)

        self.new_subsection(scene, "trusted setup", "data/sound/e4/slide2-5.mp3")
        scene.wait(2)
        self.polynomial_enc = MathTex(r"{{}} p({{\tau}})\cdot {{G_1}}", color = PRIMARY_COLOR).next_to(self.chart, DOWN)
        self.commitment = MathTex(r"{{C = }} p({{\tau}})\cdot {{G_1}}", color = PRIMARY_COLOR).next_to(self.chart, DOWN)
        scene.play(Write(self.polynomial_enc), run_time=1)
        scene.wait(2)
        scene.play(Indicate(self.polynomial_enc[1], color = HIGHLIGHT_COLOR), run_time=0.9)

        self.new_subsection(scene, "what is commitment", "data/sound/e4/slide2-6.mp3")
        scene.wait(1)
        scene.play(TransformMatchingShapes(self.polynomial_enc, self.commitment), run_time=1.5)
        scene.wait(1.2)
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
        self.envelope_body.next_to(self.commiter, LEFT+DOWN, buff = 0.4)
        self.envelope_body_closed.next_to(self.commiter, LEFT+DOWN, buff = 0.4)

        self.envelope_flap.next_to(self.envelope_body, UP, buff= 0)
        self.envelope_flap_closed.next_to(self.envelope_body_closed, UP, buff = -0.63)
        scene.play(FadeIn(self.envelope_body_closed, self.envelope_flap_closed))
        
        self.commitment.generate_target()
        self.commitment.target.move_to(self.envelope_body_closed.get_center()).scale(0.7)

        scene.play(TransformMatchingShapes(self.envelope_flap_closed, self.envelope_flap), MoveToTarget(self.commitment))
        scene.wait(1)
        commitment_sent = VGroup(self.envelope_body_closed, self.envelope_flap_closed, self.commitment)
        commitment_sent.generate_target()
        commitment_sent.target.shift(9.5*RIGHT+DOWN)
        self.envelope_flap.shift(9.5*RIGHT+DOWN)

        scene.play(MoveToTarget(commitment_sent), run_time=1.8)

        self.new_subsection(scene, "opening the commitment", "data/sound/e4/slide2-7.mp3")

        scene.play(Create(bubble_verifier))
        scene.play(Create(speech_text_verifier))
        scene.play(FadeOut(bubble_verifier, speech_text_verifier))
        scene.play(Create(self.circle))
        scene.play(TransformMatchingShapes(VGroup(self.circle), self.opening))
        scene.wait(2)
        scene.play(FadeOut(bubble_committer))

    def animate_out(self, scene):
        scene.play(FadeOut(self.commiter, self.title_text, self.commiter_label, self.verifier, self.verifier_label, self.commitment, self.envelope_body_closed, self.envelope_flap, self.envelope_flap_closed, self.chart, self.proof, self.opening))