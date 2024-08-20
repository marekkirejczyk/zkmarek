from manim import LEFT, RIGHT, FadeIn, ImageMobject, Text, DOWN, UP, Write, MathTex, MoveToTarget, FadeOut, Indicate, Arrow, ValueTracker, Create, TransformMatchingShapes, Unwrite

from zkmarek.video.constant import SECONDARY_COLOR, PRIMARY_FONT, PRIMARY_COLOR, HIGHLIGHT_COLOR
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
        self.verifier = ImageMobject("data/images/person.png").shift(RIGHT*1.5)
        self.commiter = ImageMobject("data/images/person_blue.png").shift(LEFT*1.5)

        self.commiter_label = Text("Commiter", color = PRIMARY_COLOR, font=PRIMARY_FONT).next_to(self.commiter, DOWN, buff = 0.4)
        self.verifier_label = Text("Verifier", color = PRIMARY_COLOR, font=PRIMARY_FONT).next_to(self.verifier, DOWN, buff = 0.4)

        self.message = Text("message", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size=50)

        self.chart = Chart(include_details=True).scale(0.4).to_edge(LEFT+UP).shift(DOWN*0.3)
        self.commitment = MathTex(r"C = P({{\tau}}) \cdot {{G_1}}", color = SECONDARY_COLOR).next_to(self.chart, DOWN, buff = 0.2)
        self.commitment_copy = MathTex(r"C = P({{\tau}}) \cdot {{G_1}}", color = SECONDARY_COLOR).next_to(self.verifier, UP+RIGHT, buff = 0.2)

        self.point = ValueTracker(-1.849)
        a = Curve.from_x(self.point.get_value())
        self.p = DotOnCurve(self.chart.ax, "(z, y)", a)

        self.point_tau = ValueTracker(2)
        a_tau = Curve.from_x(self.point_tau.get_value())
        self.p_tau = DotOnCurve(self.chart.ax, r"({{\tau}}, {{?}})", a_tau)

        self.trusted_setup = MathTex(r"{{\tau^1}} \cdot {{G_1}} + {{\tau^2}} \cdot {{G_1}} + {{\cdots}} + {{\tau^n}} \cdot {{G_1}} ").next_to(self.commiter, DOWN, buff = 0.1).shift(RIGHT)
        self.trusted_setup1 = MathTex(r"\left[ {{\tau^1}} + {{\tau^2}} + {{\cdots}} + {{\tau^n}} \right] \cdot {{G_1}} ").next_to(self.commiter, DOWN, buff = 0.1).shift(RIGHT)
        self.trusted_setup2 = MathTex(r"P({{\tau}}) \cdot{{G_1}} = \left[ {{\tau^1}} + {{\tau^2}} + {{\cdots}} + {{\tau^n}} \right] \cdot {{G_1}} ").next_to(self.commiter, DOWN, buff = 0.1).shift(RIGHT)

        self.opening = MathTex(r"p(z) = y", color = SECONDARY_COLOR).shift(3*UP)

        self.polynomial = MathTex("p(x)", color = PRIMARY_COLOR).next_to(self.chart, DOWN, buff = 0).scale(0.4)

    def animate_in(self, scene):
        self.new_subsection(scene, "intro", "data/sound/e4/slide3-1.mp3")
        scene.wait(1.5)
        scene.play(FadeIn(self.commiter))
        scene.play(Write(self.commiter_label))
        scene.play(Write(self.chart.ax), Write(self.chart.graph), Write(self.chart.labels))
        scene.wait(1)
        scene.play(FadeIn(self.verifier))
        scene.play(Write(self.verifier_label))
        scene.wait(1.5)
        scene.play(Indicate(self.chart.graph, color = HIGHLIGHT_COLOR))

        self.new_subsection(scene, "committing", "data/sound/e4/slide3-2.mp3")
        scene.wait(4)
    
        scene.play(Create(self.p_tau))
        scene.wait(1.5)
        scene.play(Indicate(self.p_tau[1], color = HIGHLIGHT_COLOR))
        scene.play(Create(self.commitment))

        self.new_subsection(scene, "security of the commitment", "data/sound/e4/slide3-3.mp3")
        scene.wait(2.5)
        # scene.play(Indicate(self.commitment[1], color = PRIMARY_COLOR))
        scene.play(Indicate(self.commitment[3], color = PRIMARY_COLOR))

        scene.wait(2.5)
        scene.play(Indicate(self.chart.graph, color = HIGHLIGHT_COLOR))

        self.new_subsection(scene, "what is verifiers job", "data/sound/e4/slide3-4.mp3")
        scene.play(TransformMatchingShapes(self.commitment.copy(), self.commitment_copy))
        scene.wait(1.5)

        self.arrow = Arrow(start=self.polynomial.get_top(), end=self.chart.graph.get_bottom(), color =PRIMARY_COLOR)

        scene.wait(2)
        scene.play(Indicate(self.commitment[1], color = PRIMARY_COLOR))

        self.new_subsection(scene, "how to know what is tau?", "data/sound/e4/slide3-5.mp3")
        scene.wait(1.5)
        tau = MathTex(r"\tau = ?", color = SECONDARY_COLOR).next_to(self.verifier, RIGHT, buff = 0)
        scene.play(Write(tau))

        self.new_subsection(scene, "trusted setup", "data/sound/e4/slide3-6.mp3")
        scene.play(Unwrite(tau))
        scene.wait(2)
        scene.play(FadeIn(self.trusted_setup))
        scene.play(TransformMatchingShapes(self.trusted_setup, self.trusted_setup1))
        scene.wait(2)
        scene.play(TransformMatchingShapes(self.trusted_setup1, self.trusted_setup2))
        scene.wait(2.5)
        scene.play(Indicate(self.trusted_setup2[3], color = HIGHLIGHT_COLOR))
        scene.wait(1.5)
        scene.play(Indicate(self.trusted_setup2[1], color = HIGHLIGHT_COLOR))
        

        self.new_subsection(scene, "opening", "data/sound/e4/slide3-7.mp3")
        scene.play(Create(self.p.dot))
        scene.play(Write(self.p.label))
        scene.play(FadeOut(self.commitment))
        scene.wait(2)
        scene.play(TransformMatchingShapes(self.p.label.copy(), self.opening))
        scene.play(Write(self.polynomial))
        scene.play(Write(self.arrow))

        self.new_subsection(scene, "enough info", "data/sound/e4/slide3-8.mp3")
        scene.wait(2)
        scene.play(Indicate(self.verifier, color = HIGHLIGHT_COLOR))
        scene.wait(2)
        scene.play(Indicate(self.opening, color = HIGHLIGHT_COLOR), Indicate(self.p, color = HIGHLIGHT_COLOR))
        scene.wait(2)
        scene.play(Indicate(self.chart.graph, color = HIGHLIGHT_COLOR))

    def animate_out(self, scene):
        scene.play(FadeOut(self.commiter, self.verifier, self.commiter_label, self.verifier_label, self.opening, self.chart))

