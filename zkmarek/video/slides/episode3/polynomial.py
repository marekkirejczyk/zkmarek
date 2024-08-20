from manim import FadeIn, FadeOut, Write, LEFT, RIGHT, UP, DOWN, MathTex, TransformMatchingShapes, VGroup, Text, Indicate, ImageMobject, Arrow, GrowArrow, MoveToTarget, ValueTracker, Create, Rectangle
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

SETUP_G1_P = [
    r"{{P_0}}",
    r"{{P_1}}",
    r"..." ,
    r"{{P_n}}"]


class Polynomial(SlideBase):
    def __init__(self):
        super().__init__("Evaluating the polynomial")

    def construct(self):
        self.title_label = Text("Evaluating a Polynomial for ", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size=40).to_edge(UP)
        self.title_tau = MathTex(r"\tau", color = PRIMARY_COLOR, font_size=55).next_to(self.title_label, RIGHT, buff=0.25)
        self.title_label2 = Text("Stay tuned!", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size=40).to_edge(UP)
        self.vector = TexArray(SETUP_G1_1).next_to(self.title_label, DOWN)
        self.vector2 = TexArray(SETUP_G1_P).next_to(self.title_label, DOWN)
        self.polynomial = MathTex(r"F({{ x }}) = 2\cdot {{ x^2 }} -3\cdot {{ x }} - 7", font_size = 60, color = SECONDARY_COLOR)
        self.polynomial_nunber = MathTex(r"F({{ 2 }}) = 2\cdot {{ 2^2 }} -3\cdot {{ 2 }} - 7 = -5", font_size = 60, color = SECONDARY_COLOR)

        self.polynomial_G = MathTex(r"F({{x}}) {{\cdot G}} = [2\cdot {{x^2}} -3\cdot {{x}} - 7] {{\cdot G}}", font_size = 60, color = SECONDARY_COLOR)
        self.polynomial_tau0 = MathTex(r"F({{\tau}}){{\cdot G}} = [2\cdot {{\tau^2}} -3\cdot {{\tau}} - 7 ] {{\cdot G}}", font_size = 60, color = SECONDARY_COLOR)
        self.chart = ContinuousEllipticChart(include_details=False).scale(0.6).next_to(self.title_label, DOWN)
        self.polynomial_tau = MathTex(r"F({{\tau)\cdot G}} = {{2\cdot}} [{{\tau^2 \cdot G}}] {{-3\cdot}} [{{\tau \cdot G}}] {{- 7 \cdot [G]}}", font_size = 60, color = SECONDARY_COLOR)
        self.polynomial_P = MathTex(r"F({{\tau}}) {{\cdot G}} = {{2\cdot}} [{{P_1}}] {{-3\cdot}} [{{P_0}}] {{- 7 \cdot [G]}}", font_size = 60, color = SECONDARY_COLOR)

        self.p1_x = ValueTracker(-1.491)
        a = CECAffine.from_x(self.p1_x.get_value())
        self.p1 = DotOnCurve(self.chart.ax, "\tau", a)
        self.tau = MathTex(r"\tau\cdot G", color = HIGHLIGHT_COLOR, font_size = 40).next_to(self.p1, LEFT, buff = 0.6)

    def animate_in(self, scene):
        self.new_subsection(scene, "intro to evaluating", "data/sound/episode3_1/slide8-0_new.mp3")
        scene.play(Write(self.title_label), run_time=2.2)
        scene.play(Write(self.title_tau))

        self.new_subsection(scene, "given by the formula", "data/sound/episode3/slide8-2.mp3")
        scene.wait(2)
        scene.play(Write(self.polynomial))

        self.new_subsection(scene, "evaluating at number", "data/sound/episode3/slide8-3.mp3")

        scene.play(TransformMatchingShapes(self.polynomial[1], self.polynomial_nunber[1]), TransformMatchingShapes(self.polynomial[3], self.polynomial_nunber[3]), TransformMatchingShapes(self.polynomial[5], self.polynomial_nunber[5]), TransformMatchingShapes(self.polynomial, self.polynomial_nunber), run_time=2)
        scene.wait(1)
        
        scene.play(TransformMatchingShapes(self.polynomial_nunber, self.polynomial))

        self.new_subsection(scene, "encrypting by G", "data/sound/episode3_1/slide8-3_1.mp3")
        scene.wait(2)
        scene.play(TransformMatchingShapes(self.polynomial, self.polynomial_G))

        self.new_subsection(scene, "tau instead of number", "data/sound/episode3/slide8-4.mp3")
        scene.play(Write(self.vector))
        scene.play(Indicate(self.vector.cells[0][1][0], color = HIGHLIGHT_COLOR), run_time=0.7)
        scene.play(Indicate(self.vector.cells[1][1][0], color = HIGHLIGHT_COLOR), run_time=0.7)
        scene.play(Indicate(self.vector.cells[3][1][0], color = HIGHLIGHT_COLOR), run_time=0.7)

        self.new_subsection(scene, "combine coefficients", "data/sound/episode3/slide8-5.mp3")
        scene.play(TransformMatchingShapes(VGroup(self.vector[0][1].copy(), self.vector[1][1].copy(), self.polynomial_G), self.polynomial_tau0))
        scene.wait(2)
        scene.play(TransformMatchingShapes(self.polynomial_tau0, self.polynomial_tau))
        scene.wait(2)
        scene.play(TransformMatchingShapes(self.polynomial_tau, self.polynomial_P))
        self.vector.animate_transform_matching_shapes(scene, SETUP_G1_P)

        self.polynomial_P.generate_target()
        self.polynomial_P.target.to_edge(DOWN+RIGHT).scale(0.5)
        scene.play(FadeOut(self.vector), MoveToTarget(self.polynomial_P))
        self.chart.animate_in(scene)
        scene.play(Create(self.p1.dot))
        scene.play(Write(self.tau))
        scene.wait(2)
        
        self.new_subsection(scene, "commitments and teaser", "data/sound/episode3/slide8-6.mp3")
        scene.play(FadeOut(self.polynomial_P, self.chart, self.p1.dot, self.tau))
        self.animate_tree(scene)
        scene.play(TransformMatchingShapes(VGroup(self.title_label, self.title_tau), self.title_label2))

        self.new_subsection(scene, "next?", "data/sound/episode3_1/slide8-7.mp3")
        self.animtion_commitment(scene)

    def animtion_commitment(self, scene):
        committer = ImageMobject("data/images/person.png").shift(LEFT*3).scale(0.5)
        verifier = ImageMobject("data/images/person_blue.png").shift(RIGHT * 3).scale(0.5)
        committer_label = Text("Committer", font = PRIMARY_FONT, font_size=40, color = PRIMARY_COLOR).next_to(committer, DOWN)
        verifier_label = Text("Verifier", font = PRIMARY_FONT, font_size=40, color = PRIMARY_COLOR).next_to(verifier, DOWN)
        commitment = ImageMobject("data/images/Docs.png").scale(0.5)
        
        scene.play(FadeIn(committer, committer_label, verifier, verifier_label, commitment))
        arrow1 = Arrow(committer.get_right(), verifier.get_left(), color = HIGHLIGHT_COLOR).shift(DOWN)
        scene.play(GrowArrow(arrow1))
        
        scene.wait(0.5)
        scene.play(FadeOut(arrow1, commitment, committer, committer_label, verifier, verifier_label))

    def animate_out(self, scene):
        scene.play(FadeOut(self.title_label2))

    def animate_tree(self, scene):
        tree = VerkleTree().scale(0.8).shift(UP*1.5)
        scene.wait(0.4)
        scene.play(Create(tree))
        scene.wait(1.2)
        scene.play(FadeOut(tree))

    def animate_miniature(self, scene):
        rectangle = Rectangle(color=PRIMARY_COLOR, width=15, height=8)
        text = Text("Evaluating a polynomial", color=SECONDARY_COLOR,
            font=PRIMARY_FONT, font_size=50).scale(0.65)
        self.vector.shift(DOWN*2)
        self.add(rectangle, self.polynomial, self.polynomial_G, self.vector, self.polynomial_tau0, self.tau, self.p1.dot)
        self.scale(0.65)
        text.next_to(rectangle, DOWN, buff=0.4)
        self.vector.scale(1.2)
        scene.play(FadeIn(text, rectangle, self.vector))
        self.add(text)
        scene.wait(0.1)
        scene.play(Indicate(self.vector.cells[0][1][0], color = HIGHLIGHT_COLOR), run_time=0.7)
        scene.play(Indicate(self.vector.cells[1][1][0], color = HIGHLIGHT_COLOR), run_time=0.7)
        scene.play(Indicate(self.vector.cells[3][1][0], color = HIGHLIGHT_COLOR), run_time=0.7)
        scene.play(Indicate(self.vector.cells[0][1][2], color = HIGHLIGHT_COLOR), run_time=0.7)
        scene.play(Indicate(self.vector.cells[1][1][2], color = HIGHLIGHT_COLOR), run_time=0.7)
        scene.play(Indicate(self.vector.cells[3][1][2], color = HIGHLIGHT_COLOR), run_time=0.7)
        scene.wait(3)
        
        self.new_subsection(scene, "polynomial", "data/sound/e4/slide0-4.mp3")
        self.vector.generate_target()
        self.vector.target.shift(UP*2).scale(5/6).shift(DOWN*0.5)
        scene.play(MoveToTarget(self.vector), FadeIn(self.polynomial), run_time=1)
        scene.wait(1.5)
        scene.play(TransformMatchingShapes(self.polynomial, self.polynomial_G))
        scene.wait(3)
        scene.play(TransformMatchingShapes(VGroup(self.vector[0][1].copy(), self.vector[1][1].copy(), self.polynomial_G), self.polynomial_tau0))

        scene.wait(1.5)
        scene.play(FadeOut(self.polynomial_tau0, self.vector, text, rectangle))
