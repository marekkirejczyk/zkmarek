from manim import FadeIn, FadeOut, Write, LEFT, RIGHT, UP, DOWN, MathTex, TransformMatchingShapes, VGroup, Text, Indicate, ImageMobject, Arrow, GrowArrow, MoveToTarget, ValueTracker, Create
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import SECONDARY_COLOR, PRIMARY_FONT, PRIMARY_COLOR, HIGHLIGHT_COLOR
from zkmarek.video.mobjects.tex_array import TexArray
from zkmarek.video.slides.episode3.chart import ContinuousEllipticChart
from zkmarek.video.mobjects.dot_on_curve import DotOnCurve
from zkmarek.crypto.cec_affine import CECAffine
from zkmarek.video.mobjects.verkle_tree import VerkleTree


SETUP_G1_1 = [
    r"{{ \tau^1 }} \cdot {{G}}",
    r"{{ \tau^2 }} \cdot {{G}}",
    r"..." ,
    r"{{ \tau^n }} \cdot {{G}}"]


class Polynomial(SlideBase):
    def __init__(self):
        super().__init__("Evaluating the polynomial")

    def construct(self):
        self.title_label = Text("Evaluating a Polynomial Using Trusted Setup", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size=40).to_edge(UP)
        self.subtitle = Text("Secure evaluation without knowing tau", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size=32).next_to(self.title_label, DOWN)
        
        self.vector = TexArray(SETUP_G1_1).next_to(self.subtitle, DOWN)
        self.polynomial = MathTex(r"P(x) = 2\cdot x^2 -3\cdot x - 7", font_size = 60, color = SECONDARY_COLOR)
        self.polynomial_nunber = MathTex(r"P(2) = 2\cdot 2^2 -3\cdot 2 - 7 = -5", font_size = 60, color = SECONDARY_COLOR)
        self.polynomial_tau = MathTex(r"P(\tau)\cdot G = 2\cdot [\tau^2 \cdot G] -3\cdot [\tau \cdot G] - 7 \cdot [G]", font_size = 60, color = SECONDARY_COLOR)
        self.chart = ContinuousEllipticChart(include_details=False).scale(0.6).next_to(self.subtitle, DOWN)
        self.p1_x = ValueTracker(-1.491)
        a = CECAffine.from_x(self.p1_x.get_value())
        self.p1 = DotOnCurve(self.chart.ax, "\tau", a)
        self.tau = MathTex(r"\tau\cdot G", color = HIGHLIGHT_COLOR, font_size = 40).next_to(self.p1, LEFT, buff = 0.6)

    def animate_in(self, scene):
        self.new_subsection(scene, "intro to evaluating", "data/sound/episode3/slide8-0.mp3")
        scene.play(Write(self.title_label))
        scene.play(Write(self.subtitle))

        self.new_subsection(scene, "we know a sequence", "data/sound/episode3/slide8-1.mp3")
        scene.play(Write(self.vector))
        scene.play(Indicate(self.vector.cells[0][1][0], color = HIGHLIGHT_COLOR), run_time=0.7)
        scene.play(Indicate(self.vector.cells[1][1][0], color = HIGHLIGHT_COLOR), run_time=0.7)
        scene.play(Indicate(self.vector.cells[3][1][0], color = HIGHLIGHT_COLOR), run_time=0.7)
        scene.play(Indicate(self.vector.cells[0][1][2], color = HIGHLIGHT_COLOR), run_time=0.7)
        scene.play(Indicate(self.vector.cells[1][1][2], color = HIGHLIGHT_COLOR), run_time=0.7)
        scene.play(Indicate(self.vector.cells[3][1][2], color = HIGHLIGHT_COLOR), run_time=0.7)

        self.new_subsection(scene, "given by the formula", "data/sound/episode3/slide8-2.mp3")
        scene.wait(2)
        scene.play(Write(self.polynomial))

        self.new_subsection(scene, "evaluating at number", "data/sound/episode3/slide8-3.mp3")
        scene.play(TransformMatchingShapes(self.polynomial, self.polynomial_nunber))
        scene.wait(2)
        scene.play(TransformMatchingShapes(self.polynomial_nunber, self.polynomial))

        self.new_subsection(scene, "tau instead of number", "data/sound/episode3/slide8-4.mp3")
        scene.play(Indicate(self.vector.cells[0][1], color = HIGHLIGHT_COLOR), run_time=0.7)
        scene.play(Indicate(self.vector.cells[1][1], color = HIGHLIGHT_COLOR), run_time=0.7)
        scene.play(Indicate(self.vector.cells[3][1], color = HIGHLIGHT_COLOR), run_time=0.7)

        self.new_subsection(scene, "combine coefficients", "data/sound/episode3/slide8-5.mp3")
        scene.play(TransformMatchingShapes(VGroup(self.vector[0][1].copy(), self.vector[1][1].copy(), self.polynomial), self.polynomial_tau))
        scene.wait(4)
        
        self.polynomial_tau.generate_target()
        self.polynomial_tau.target.to_edge(DOWN+RIGHT).scale(0.5)
        scene.play(FadeOut(self.vector), MoveToTarget(self.polynomial_tau))
        self.chart.animate_in(scene)
        scene.play(Create(self.p1.dot))
        scene.play(Write(self.tau))

        self.new_subsection(scene, "commitments and teaser", "data/sound/episode3/slide8-6.mp3")
        scene.play(FadeOut(self.polynomial_tau, self.chart, self.p1.dot, self.tau))
        self.animate_tree(scene)
        self.animtion_commitment(scene)

    def animtion_commitment(self, scene):
        committer = ImageMobject("zkmarek/video/slides/teaser3/person.png").shift(LEFT*3).scale(0.5)
        verifier = ImageMobject("zkmarek/video/slides/episode3/person_blue.png").shift(RIGHT * 3).scale(0.5)
        committer_label = Text("Committer", font = PRIMARY_FONT, font_size=40, color = PRIMARY_COLOR).next_to(committer, DOWN)
        verifier_label = Text("Verifier", font = PRIMARY_FONT, font_size=40, color = PRIMARY_COLOR).next_to(verifier, DOWN)
        commitment = ImageMobject("zkmarek/video/slides/teaser3/Docs.png").scale(0.5)
        
        scene.play(FadeIn(committer, committer_label, verifier, verifier_label, commitment))
        arrow1 = Arrow(committer.get_right(), verifier.get_left(), color = HIGHLIGHT_COLOR).shift(DOWN)
        scene.play(GrowArrow(arrow1))
        
        scene.wait(0.5)
        scene.play(FadeOut(arrow1, commitment, committer, committer_label, verifier, verifier_label))

    def animate_out(self, scene):
        scene.play(FadeOut(self.title_label, self.subtitle))

    def animate_tree(self, scene):
        tree = VerkleTree().scale(0.8).shift(UP*1.5)
        scene.wait(0.4)
        scene.play(Create(tree))
        scene.wait(1)
        scene.play(FadeOut(tree))
