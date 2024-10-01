from manim import Create, DOWN, ImageMobject, RIGHT, LEFT, UP, FadeIn, Polygon, VGroup, Text, Write, Tex, FadeOut, TransformMatchingShapes, RoundedRectangle, MoveToTarget, MathTex, Circle, Indicate

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

class KZG(SlideBase):

    def __init__(self):
        super().__init__("KZG")

    def construct(self):
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
        self.x_zero = FieldElement(33, 41)
        self.value_at_x_zero = poly(self.x_zero)
        self.tau = FieldElement(18, 41)
        self.value_at_tau = poly(self.tau)
        self.chart = DiscreetePolynomialChart(41, poly)
        self.chart.add_xaxis_label(self.x_zero.value, r"x_0")
        self.chart.add_xaxis_label(self.tau.value, r"\tau")
        self.chart.scale(0.4)
        self.trusted_setup = MathTex(r"{{\tau^1}} {{\cdot G_1}} + {{\tau^2}} {{\cdot G_1}} + \cdots + {{\tau^n}} {{\cdot G_1}}", color = SECONDARY_COLOR).shift(DOWN*2.5)
        self.trusted_setup1 = MathTex(r"{{}} \left[ {{\tau^1}} + {{\tau^2}}  + \cdots + {{\tau^n}} \right] {{\cdot G_1}}", color = SECONDARY_COLOR).shift(DOWN*2.5)
        self.trusted_setup2 = MathTex(r"{{p(\tau)}} {{\cdot G_1}}= \left[ {{a_1\cdot}} {{\tau^1}} + {{a_2\cdot}} {{\tau^2}}  + \cdots + {{a_n \cdot}} {{\tau^n}} \right] {{\cdot G_1}}", color = SECONDARY_COLOR).shift(DOWN*2.5)

    def animate_in(self, scene):
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
        bubble_committer = RoundedRectangle(corner_radius=0.5, width=self.chart.width + 1, height=self.chart.height + 0.5, color = PRIMARY_COLOR).next_to(self.commiter, UP+LEFT, buff = -1).shift(0.4*DOWN+LEFT*0.6)
        self.opening = MathTex(r"{{p}} ({{x_0}}) = {{y_0}}", font_size=32, color = PRIMARY_COLOR)
        self.proof = MathTex(r"\pi = \mathrm{proof}", font_size=32, color = PRIMARY_COLOR)
        bubble_opening = RoundedRectangle(corner_radius=0.5, width=self.opening.width + 1, height=self.opening.height + 1.5, color = PRIMARY_COLOR).next_to(self.commiter, UP+RIGHT, buff = -0.3)
        tail = Polygon(
            [0.08, 0.08, 0], 
            [-0.35, -1.2, 0], 
            [0.93, -0.63, 0], 
            color=PRIMARY_COLOR,
            fill_opacity=0.4
        ).next_to(bubble_opening, DOWN+LEFT, buff=-0.8).scale(0.4).shift(LEFT*0.03+DOWN*0.15)
        self.opening.move_to(bubble_opening.get_center())
        self.opening.shift(UP*0.3)
        self.proof.next_to(self.opening, DOWN, buff = 0.3)
        self.chart.move_to(bubble_committer.get_center())

        self.new_subsection(scene, "trusted setup", "data/sound/e4/slide2-5.mp3")
        self.title_text_kzg = Text("KZG", font_size=40, color = PRIMARY_COLOR, font = PRIMARY_FONT).to_edge(UP)
        scene.play(FadeIn(self.verifier, self.verifier_label, self.commiter, self.commiter_label, self.title_text_kzg), run_time=0.7)
        self.chart.gen_points()
        scene.play(Create(bubble_committer), Create(self.chart), FadeIn(self.lock), run_time=0.7)
        self.lock.next_to(self.chart, RIGHT, buff = 0).shift(UP)
        self.opening.move_to(bubble_opening.get_center())
        self.opening.shift(UP*0.3)
        scene.play(Write(self.trusted_setup), run_time=0.5)
        scene.wait(1)
        scene.play(TransformMatchingShapes(self.trusted_setup, self.trusted_setup1), run_time=1)
        scene.wait(1.2)
        scene.play(TransformMatchingShapes(self.trusted_setup1, self.trusted_setup2), run_time=1.2)
        scene.wait(1.5)
        self.polynomial_enc = MathTex(r"{{}} p({{\tau}})\cdot {{G_1}}", color = PRIMARY_COLOR).next_to(self.chart, DOWN).shift(DOWN*0.2)
        self.commitment = MathTex(r"{{C = }} p({{\tau}})\cdot {{G_1}}", color = PRIMARY_COLOR).next_to(self.chart, DOWN).shift(DOWN*0.2)
        scene.play(TransformMatchingShapes(self.trusted_setup2, self.polynomial_enc), run_time=0.8)
        scene.wait(0.5)

        self.new_subsection(scene, "what is commitment", "data/sound/e4/slide2-6.mp3")
        scene.wait(1)
        scene.play(TransformMatchingShapes(self.polynomial_enc, self.commitment), run_time=1.5)
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
        scene.play(FadeIn(self.envelope_body_closed, self.envelope_flap_closed))
        
        self.commitment.generate_target()
        self.commitment.target.move_to(self.envelope_body_closed.get_center()).scale(0.7)

        scene.play(FadeOut(self.envelope_flap_closed), FadeIn(self.envelope_flap), MoveToTarget(self.commitment))
        scene.wait(1)
        scene.play(FadeOut(self.envelope_flap), FadeIn(self.envelope_flap_closed))
        commitment_sent = VGroup(self.envelope_body_closed, self.envelope_flap_closed, self.commitment)
        commitment_sent.generate_target()
        commitment_sent.target.shift(9.5*RIGHT+DOWN)
        self.envelope_flap.shift(9.5*RIGHT+DOWN)

        scene.play(MoveToTarget(commitment_sent), run_time=1.8)

        self.new_subsection(scene, "opening the commitment", "data/sound/e4/slide2-7.mp3")

        scene.play(Create(bubble_verifier), Create(tail_verifier))
        scene.play(Create(speech_text_verifier))
        self.circle = Circle(radius = 0.1, color = HIGHLIGHT2_COLOR).next_to(self.chart, DOWN, buff=-1).shift(RIGHT*0.95+UP*0.8)
        self.circle_full = Circle(radius = 0.1, color = HIGHLIGHT2_COLOR, fill_opacity = 1).next_to(self.chart, DOWN, buff=-1).shift(RIGHT*0.95+UP*0.8)
        scene.wait(1)
        scene.play(FadeOut(bubble_verifier, speech_text_verifier, tail_verifier))
        scene.play(Create(self.circle))
        scene.play(TransformMatchingShapes(self.circle, self.circle_full))
        self.circle_full.generate_target()
        self.circle_full.target.next_to(self.opening, LEFT, buff = 0.1)
        scene.play(FadeIn(self.opening, bubble_opening, tail), MoveToTarget(self.circle_full))
        scene.wait(0.5)
        scene.play(Indicate(self.opening[4], color = HIGHLIGHT2_COLOR), run_time=1)

        scene.wait(1)
        scene.play(Indicate(self.opening[2], color = HIGHLIGHT2_COLOR), run_time=1)
        scene.wait(2)
        self.proof = MathTex(r"{{\pi}} = {{q(\tau)}} \cdot {{G_1}}", color = PRIMARY_COLOR, font_size=32)
        self.proof.next_to(self.opening, DOWN, buff = 0.3)
        scene.play(Write(self.proof), run_time=0.5)
        scene.wait(1.5)
        scene.play(Indicate(self.proof[0], color = HIGHLIGHT_COLOR))
        scene.play(Indicate(self.proof[2], color = HIGHLIGHT_COLOR))
        scene.play(FadeOut(bubble_committer, bubble_opening, tail))

    def animate_out(self, scene):
        scene.play(FadeOut(self.commiter, self.circle_full, self.title_text_kzg, self.commiter_label, self.verifier, self.verifier_label, self.commitment, self.envelope_body_closed, self.envelope_flap_closed, self.chart, self.opening, self.lock, self.proof))