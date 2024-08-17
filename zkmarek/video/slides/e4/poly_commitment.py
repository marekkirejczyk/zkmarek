from manim import LEFT, RIGHT, FadeIn, ImageMobject, Text, DOWN, UP, Write, MathTex, Brace, MoveToTarget, FadeOut, Indicate, Arrow, AddTextLetterByLetter, ReplacementTransform, ValueTracker, Create, TransformMatchingShapes

from zkmarek.video.constant import SECONDARY_COLOR, PRIMARY_FONT, PRIMARY_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.mobjects.dot_on_curve import DotOnCurve
from zkmarek.video.slides.e4.chart import Chart
from zkmarek.video.slides.e4.curve import Curve

class PolynomialCommitment(SlideBase):
    chart: Chart

    def __init__(self):
        super().__init__("Commitment")

    def construct(self):
        self.title = Text("Commitment", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size=80).to_edge(UP)
        self.verifier = ImageMobject("data/images/person.png").shift(RIGHT*3)
        self.commiter = ImageMobject("data/images/person_blue.png").shift(LEFT*3)

        self.commiter_label = Text("Commiter", color = PRIMARY_COLOR, font=PRIMARY_FONT).next_to(self.commiter, DOWN, buff = 0.4)
        self.verifier_label = Text("Verifier", color = PRIMARY_COLOR, font=PRIMARY_FONT).next_to(self.verifier, DOWN, buff = 0.4)

        self.message = Text("message", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size=50)

        self.chart = Chart(include_details=True).scale(0.8).to_edge(LEFT)
        self.commitment = MathTex(r"C = P({{\tau}}) \cdot {{G_1}}", color = SECONDARY_COLOR).next_to(self.chart, UP, buff = 0.2)

        self.point = ValueTracker(-1.849)
        a = Curve.from_x(self.point.get_value())
        self.p = DotOnCurve(self.chart.ax, "(z, y)", a)

        self.point_tau = ValueTracker(2)
        a_tau = Curve.from_x(self.point_tau.get_value())
        self.p_tau = DotOnCurve(self.chart.ax, r"(\tau, ?)", a_tau)

        self.opening = MathTex(r"p(z) = y", color = SECONDARY_COLOR).shift(2*UP)

        self.polynomial = MathTex("p(x)", color = PRIMARY_COLOR).next_to(self.chart, DOWN, buff = 0.3)

    def animate_in(self, scene):
        self.new_subsection(scene, "intro", "data/sound/e4/slide3-1.mp3")
        scene.wait(1.5)
        scene.play(FadeIn(self.commiter))
        scene.play(Write(self.commiter_label))
        scene.play(Write(self.chart.ax), Write(self.chart.graph), Write(self.chart.labels))
        scene.wait(2)
        scene.play(FadeIn(self.verifier))
        scene.wait(0.5)
        scene.play(Write(self.verifier_label))

        self.new_subsection(scene, "committing", "data/sound/e4/slide3-2.mp3")


        self.new_subsection(scene, "what is commitment", "data/sound/e4/slide3-3.mp3")
        scene.wait(1.5)
        scene.play(Indicate(self.commitment[1], color = PRIMARY_COLOR))
        scene.play(Indicate(self.commitment[3], color = PRIMARY_COLOR))



        self.new_subsection(scene, "what is verifiers job", "data/sound/e4/slide3-4.mp3")
        self.commiter.generate_target()
        self.commiter.target.to_edge(LEFT)
        
        self.verifier.generate_target()
        self.verifier.target.to_edge(RIGHT)

        self.commiter_label.generate_target()
        self.commiter_label.target.to_edge(LEFT)

        self.verifier_label.generate_target()
        self.verifier_label.target.to_edge(RIGHT)

        scene.play(MoveToTarget(self.commiter), MoveToTarget(self.commiter_label), MoveToTarget(self.verifier), MoveToTarget(self.verifier_label))
        scene.wait(1.5)
        self.commitment.generate_target()
        self.commitment.target.shift(UP*2)
        scene.play(MoveToTarget(self.commitment))

        self.arrow = Arrow(start=self.polynomial.get_top(), end=self.chart.graph.get_bottom(), color =PRIMARY_COLOR)

        scene.wait(2)
        scene.play(Indicate(self.commitment[1], color = PRIMARY_COLOR))
        scene.wait(1)
        scene.play(Create(self.p_tau))

        self.new_subsection(scene, "opening", "data/sound/e4/slide3-5.mp3")
        scene.wait(1.5)

        scene.play(Create(self.p.dot))
        scene.play(Write(self.p.label))
        scene.play(FadeOut(self.commitment))
        scene.wait(2)
        scene.play(TransformMatchingShapes(self.p.label.copy(), self.opening))
        scene.play(Write(self.polynomial))
        scene.play(Write(self.arrow))
        scene.wait(5.5)

    def animate_out(self, scene):
        scene.play(FadeOut(self.commiter, self.verifier, self.commiter_label, self.verifier_label, self.opening, self.chart))

