from manim import LEFT, RIGHT, FadeIn, ImageMobject, Text, DOWN, UP, Write, MathTex, FadeOut, Indicate, ValueTracker, Create, TransformMatchingShapes, MoveToTarget, Group, Tex, Polygon, VGroup, Transform, Circle, RoundedRectangle

from zkmarek.video.utils import load
from zkmarek.video.constant import SECONDARY_COLOR, PRIMARY_FONT, PRIMARY_COLOR, HIGHLIGHT_COLOR, HIGHLIGHT2_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.mobjects.dot_on_curve import DotOnCurve
from zkmarek.video.slides.e4.chart import Chart
from zkmarek.video.slides.e4.curve import Curve

class PolynomialCommitment(SlideBase):
    chart: Chart

    def __init__(self):
        super().__init__("Polynomial Commitment")

    def construct(self):
        self.title = Text("Polynomial Commitment", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size=40).to_edge(UP)
        self.verifier = ImageMobject("data/images/person.png").shift(RIGHT*1.5)
        self.commiter = ImageMobject("data/images/person_blue.png").shift(LEFT*1.5)

        self.commiter_label = Text("Committer", color = PRIMARY_COLOR, font=PRIMARY_FONT).next_to(self.commiter, DOWN, buff = 0.4)
        self.verifier_label = Text("Verifier", color = PRIMARY_COLOR, font=PRIMARY_FONT).next_to(self.verifier, DOWN, buff = 0.4)

        self.message = Text("message", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size=50)

        self.chart = Chart(include_details=True).scale(0.5).next_to(self.commiter, LEFT).shift(UP*1.3)
        self.commitment = MathTex(r"C = p({{\tau}}) \cdot {{G_1}}", color = SECONDARY_COLOR).next_to(self.commiter, LEFT+DOWN, buff = 0.4).shift(UP)
        self.commitment_copy = MathTex(r"C = p({{\tau}}) \cdot {{G_1}}", color = SECONDARY_COLOR).next_to(self.commiter, LEFT+DOWN, buff = 0.4).shift(UP)

        self.point = ValueTracker(-1.849)
        a = Curve.from_x(self.point.get_value())
        self.p = DotOnCurve(self.chart.ax, "(z, y)", a)
        self.p.label.shift(LEFT*1.1)
        self.point_tau = ValueTracker(2)
        a_tau = Curve.from_x(self.point_tau.get_value())
        self.p_tau = DotOnCurve(self.chart.ax, r"({{\tau}}, {{?}})", a_tau)
        self.p_tau.label.shift(DOWN*0.15+LEFT*0.15).scale(1.1)

        self.trusted_setup = MathTex(r"{{\tau^1}} \cdot {{G_1}} + {{\tau^2}} \cdot {{G_1}} + {{\cdots}} + {{\tau^n}} \cdot {{G_1}} ", color = SECONDARY_COLOR).next_to(self.commiter_label, DOWN, buff = 0).shift(RIGHT*1.5)
        self.trusted_setup1 = MathTex(r"\left[ {{\tau^1}} + {{\tau^2}} + {{\cdots}} + {{\tau^n}} \right] \cdot {{G_1}} ", color = SECONDARY_COLOR).next_to(self.commiter_label, DOWN, buff = 0).shift(RIGHT*1.5)
        self.trusted_setup2 = MathTex(r"p({{\tau}}) \cdot{{G_1}} = \left[ {{\tau^1}} + {{\tau^2}} + {{\cdots}} + {{\tau^n}} \right] \cdot {{G_1}} ", color = SECONDARY_COLOR).next_to(self.commiter_label, DOWN, buff = 0).shift(RIGHT*1.5)
 
        self.opening = MathTex(r"p(z) = y", color = SECONDARY_COLOR).shift(2*UP)
        self.tex = Tex(load("zkmarek/video/slides/e4/properties.tex"), color=SECONDARY_COLOR)
        self.envelope_body_closed = Polygon(
            [-3, -1, 0], [3, -1, 0], [3, 1, 0], [-3, 1, 0],
            fill_color=PRIMARY_COLOR, fill_opacity=0.5
        ).scale(0.6)

        self.envelope_flap_closed = Polygon(
            [-3, 1, 0], [3, 1, 0], [0, -0.6, 0],
            fill_color=HIGHLIGHT_COLOR, fill_opacity=0.5
        ).scale(0.58)

        self.outline_closed = VGroup(
            self.envelope_body_closed.copy().set_fill(opacity=0.2),
            self.envelope_flap_closed.copy().set_fill(opacity=0.2)
        )
        self.envelope_body = Polygon(
            [-3, -1, 0], [3, -1, 0], [3, 1, 0], [-3, 1, 0],
            fill_color=PRIMARY_COLOR, fill_opacity=0.5
        ).scale(0.6)
        self.envelope_flap = Polygon(
            [-3, 1, 0], [3, 1, 0], [0, 3, 0], 
            fill_color=HIGHLIGHT_COLOR, fill_opacity=0.5
        ).scale(0.59)
        self.envelope_body.next_to(self.commiter, LEFT)
        self.envelope_body_closed.next_to(self.commiter, LEFT)

        self.envelope_flap.next_to(self.envelope_body, UP, buff= 0)
        self.envelope_flap_closed.next_to(self.envelope_body_closed, UP, buff = -0.95)
        self.message.next_to(self.commiter, RIGHT, buff = 0.1)
        self.lock = ImageMobject("data/images/Locked@2x.png").scale(0.25).next_to(self.message, RIGHT, buff = 0.1)

        self.circle = Circle(radius = 0.3, color = HIGHLIGHT2_COLOR).next_to(self.p.dot, UP, buff=-0.5)

    def animate_in(self, scene):
        self.new_subsection(scene, "envelope", "data/sound/e4/slide2-1.mp3")
        scene.play(Write(self.title))
        scene.play(FadeIn(self.commiter))
        scene.play(Write(self.commiter_label))
        scene.wait(1.5)
        scene.play(FadeIn(self.envelope_body_closed, self.envelope_flap_closed))
        scene.wait(2)
        scene.play(Write(self.message))
        scene.play(FadeIn(self.lock))
        secret_message = Group(self.lock, self.message)
        secret_message.generate_target()
        secret_message.target.next_to(self.commiter, LEFT, buff = 0.1)
        scene.play(TransformMatchingShapes(self.envelope_flap_closed, self.envelope_flap))
        scene.play(MoveToTarget(secret_message))
        scene.play(FadeOut(secret_message))


        scene.play(TransformMatchingShapes(self.envelope_flap, self.envelope_flap_closed))

        self.tex.scale(0.8).next_to(self.commiter, RIGHT, buff = 1)
        scene.play(Write(self.tex))

        self.new_subsection(scene, "hiding", "data/sound/e4/slide2-1a.mp3")
        scene.wait(0.4)
        scene.play(Indicate(self.tex[0][1:7], color = HIGHLIGHT_COLOR))

        self.new_subsection(scene, "binding", "data/sound/e4/slide2-1b.mp3")
        scene.wait(1.2)
        scene.play(Indicate(self.tex[0][8:15], color = HIGHLIGHT_COLOR))   

        self.new_subsection(scene, "polynomial commitments", "data/sound/e4/slide2-2.mp3")
        scene.play(FadeOut(self.envelope_body_closed, self.envelope_flap_closed), FadeOut(self.tex))
        scene.play(Write(self.chart.ax), Write(self.chart.graph), Write(self.chart.labels))

        self.new_subsection(scene, "committer creates a commitment", "data/sound/e4/slide2-3.mp3")
        scene.play(FadeIn(self.verifier))
        scene.play(Write(self.verifier_label))
        scene.wait(1)

        scene.play(Indicate(self.chart.graph, color = HIGHLIGHT_COLOR))
        self.envelope_body.next_to(self.commiter, LEFT+DOWN)
        self.envelope_body_closed.next_to(self.commiter, LEFT+DOWN)
        self.envelope_flap.next_to(self.envelope_body, UP, buff = 0)
        self.envelope_flap_closed.next_to(self.envelope_body, UP, buff = -0.95)
        scene.wait(2)
        scene.play(Create(self.p_tau))
        scene.play(TransformMatchingShapes(self.p_tau.label[1].copy(), self.commitment))
        scene.play(Indicate(self.commitment[1], color = HIGHLIGHT_COLOR))
        scene.wait(0.6)
        scene.play(Indicate(self.commitment[3], color = HIGHLIGHT_COLOR))
        self.images = Group(self.commiter, self.commiter_label, self.verifier, self.verifier_label)
        self.images.generate_target()
        self.images.target.shift(UP*1.5)
        scene.play(MoveToTarget(self.images), run_time=1)
        scene.play(FadeIn(self.trusted_setup))
        scene.play(TransformMatchingShapes(self.trusted_setup, self.trusted_setup1))
        scene.wait(0.5)
        scene.play(TransformMatchingShapes(self.trusted_setup1, self.trusted_setup2))
        scene.wait(0.5)
        scene.play(FadeOut(self.trusted_setup2))
        self.images.generate_target()
        self.images.target.shift(DOWN*1.5)
        scene.play(MoveToTarget(self.images), run_time=1)

        self.new_subsection(scene, "commitment is sent", "data/sound/e4/slide2-4.mp3")
        scene.play(FadeIn(self.envelope_body, self.envelope_flap))
        self.commitment.generate_target()
        self.commitment.target.next_to(self.commiter, LEFT+DOWN, buff = 0.4).shift(0.3*LEFT)

        scene.play(MoveToTarget(self.commitment), TransformMatchingShapes(self.envelope_flap, self.envelope_flap_closed))

        commitment_sent = VGroup(self.commitment, self.envelope_body, self.envelope_flap_closed)
        commitment_sent.generate_target()
        commitment_sent.target.shift(9.7*RIGHT)
        self.envelope_flap.shift(9.7*RIGHT)
        scene.play(MoveToTarget(commitment_sent))

        self.new_subsection(scene, "validate the commitment", "data/sound/e4/slide2-5.mp3")
        speech_text = Tex(r"Hey, can you let me\\ open the commitment?", font_size=32, color = PRIMARY_COLOR)

        bubble = RoundedRectangle(corner_radius=0.5, width=speech_text.width + 1, height=speech_text.height + 0.5, color = PRIMARY_COLOR).next_to(self.verifier, UP+RIGHT, buff = -1).shift(0.2*DOWN)
        
        bubble.shift(UP) 

        speech_text.move_to(bubble.get_center())
        scene.wait(5)
        scene.play(Create(bubble), Write(speech_text))
        self.envelope_flap = Polygon(
            [-3, 1, 0], [3, 1, 0], [0, 3, 0], 
            fill_color=HIGHLIGHT_COLOR, fill_opacity=0.5
        ).scale(0.59).next_to(self.envelope_body, UP, buff= 0)
        scene.play(Transform(self.envelope_flap_closed, self.envelope_flap), FadeIn(self.envelope_flap), FadeOut(self.envelope_flap_closed))
        self.commitment.generate_target()
        self.commitment.target.shift(UP*2)
        scene.play(MoveToTarget(self.commitment))

        self.new_subsection(scene, "open the commitment", "data/sound/e4/slide2-6.mp3")
        scene.play(FadeOut(bubble, speech_text))

        scene.play(Create(self.p.dot))
        scene.play(Write(self.p.label))
        scene.play(Create(self.circle))
        scene.play(TransformMatchingShapes(VGroup(self.circle, self.p.label.copy()), self.opening))

        self.new_subsection(scene, "committer proves that he knows the polynomial", "data/sound/e4/slide2-7.mp3")
        self.opening.generate_target()
        self.opening.target.next_to(commitment_sent, UP, buff = 1.3)
        scene.play(MoveToTarget(self.opening))
        scene.wait(2)
        scene.play(Indicate(self.chart.graph, color = HIGHLIGHT2_COLOR))
        scene.play(FadeOut(self.commitment))


    def animate_out(self, scene):
        scene.play(FadeOut(self.commiter, self.verifier, self.commiter_label, self.verifier_label, self.opening, self.chart.ax, self.chart.labels, self.chart.graph, self.p_tau, self.p, self.title, self.envelope_flap, self.envelope_body))

