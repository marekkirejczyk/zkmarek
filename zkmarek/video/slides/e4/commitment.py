from manim import LEFT, RIGHT, FadeIn, ImageMobject, Text, DOWN, UP, Write, MathTex, TransformMatchingShapes, Brace, VGroup, MoveToTarget, FadeOut

from zkmarek.video.constant import SECONDARY_COLOR, PRIMARY_FONT, PRIMARY_COLOR, HIGHLIGHT_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.mobjects.tex_array import TexArray

PARTICIPANT_1 = [
    r"{{\tau_0^1}}  {{G_1}}",
    r"{{\tau_0^2}} {{G_1}}",
    r". . .",
    r"{{\tau_0^n}}  {{G_1}}"
]

PARTICIPANT_2 = [
    r"\tau_1^1 G_1",
    r"\tau_1^2 G_1",
    ". . .",
    r"\tau_1^n G_1"
]

PARTICIPANT_N = [
    r"\tau_i^1 G_1",
    r"\tau_i^2 G_1",
    r". . .",
    r"\tau_i^n G_1"
]

class Commitment(SlideBase):

    def __init__(self):
        super().__init__("Commitment")

    def construct(self):
        self.title = Text("Commitment", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size=80).to_edge(UP)
        self.verifier = ImageMobject("data/images/person.png").shift(LEFT*3)
        self.commiter = ImageMobject("data/images/person_blue.png").shift(RIGHT*3)

        self.commiter_label = Text("Commiter", color = PRIMARY_COLOR, font=PRIMARY_FONT).next_to(self.commiter, DOWN, buff = 0.4)
        self.verifier_label = Text("Verifier", color = PRIMARY_COLOR, font=PRIMARY_FONT).next_to(self.verifier, DOWN, buff = 0.4)

        person = ImageMobject("data/images/person.png").scale(0.4)

        self.person1 = person.copy().shift(3*LEFT)
        self.person2 = person.copy().shift(3*RIGHT)
        self.person3 = person.copy().shift(2*UP)
        self.person4 = person.copy().shift(2*DOWN)
        self.tau = MathTex(r"\tau", font_size = 60, color = SECONDARY_COLOR)
        self.tau_encrypted = MathTex(r"\tau \cdot G", font_size = 60, color = SECONDARY_COLOR)

        self.commitment = MathTex(r"C = P(\tau)\cdot G_1", color = SECONDARY_COLOR)
        self.ec_point = Brace("elliptic curve point", DOWN, color = PRIMARY_COLOR)
        self.ec_point_label = Text(r"Subgroups of points on elliptic curve", font_size=30, color=PRIMARY_COLOR, font = PRIMARY_FONT)
        self.ec_point.put_at_tip(self.ec_point_label)

        self.vector_0 = TexArray(PARTICIPANT_1)
        self.vector_1 = TexArray(PARTICIPANT_2)
        self.vector_k = TexArray(PARTICIPANT_N)
        self.three_dot = Text(".\n.\n.", font=PRIMARY_FONT, color=SECONDARY_COLOR).scale(0.5)

        self.vector_0.next_to(self.title, DOWN)
        self.vector_1.next_to(self.vector_0, DOWN, buff = 0.4)
        self.three_dot.next_to(self.vector_1, DOWN, buff=0.4)
        self.vector_k.next_to(self.three_dot, DOWN, buff=0.4)


    def animate_in(self, scene):
        self.new_subsection(scene, "intro", "data/sound/e4/slide2-0.mp3")
        scene.wait(4)
        scene.play(FadeIn(self.commiter))
        scene.play(FadeIn(self.verifier))
        scene.wait(2)
        scene.play(Write(self.commiter_label))
        scene.play(Write(self.verifier_label))

        self.new_subsection(scene, "committing", "data/sound/e4/slide2-1.mp3")
        scene.wait(2)
        scene.play(FadeIn(self.person1), run_time=0.5)
        scene.play(FadeIn(self.person2), run_time=0.5)
        scene.play(FadeIn(self.person3), run_time=0.5)
        scene.play(FadeIn(self.person4), run_time=0.5)
        scene.play(FadeIn(self.tau), run_time=0.5)
        scene.wait(1.5)
        scene.play(TransformMatchingShapes(self.tau, self.tau_encrypted))

        self.trusted_setup = VGroup(self.person1, self.person2, self.person3, self.person4, self.tau_encrypted)
        self.trusted_setup.generate_target()
        self.trusted_setup.target.to_corner(UP+RIGHT).scale(0.8)
        scene.wait(2)
        scene.play(MoveToTarget(self.trusted_setup))

        self.new_subsection(scene, "what is commitment", "data/sound/e4/slide2-2.mp3")
        scene.wait(3)
        scene.play(Write(self.commitment))
        scene.wait(2)
        scene.play(FadeIn(self.ec_point_label))
        scene.play(FadeIn(self.ec_point))
        scene.wait(3)
        scene.play(FadeOut(self.ec_point, self.ec_point_label))

        self.new_subsection(scene, "what is verifiers job", "data/sound/e4/slide2-3.mp3")
        self.commiter.generate_target()
        self.commiter.target.to_edge(LEFT)
        
        self.verifier.generate_target()
        self.verifier.target.to_edge(RIGHT)

        self.commiter_label.generate_target()
        self.commiter_label.target.to_edge(LEFT)

        self.verifier_label.generate_target()
        self.verifier_label.target.to_edge(RIGHT)

        scene.play(MoveToTarget(self.commiter), MoveToTarget(self.commiter_label), MoveToTarget(self.verifier), MoveToTarget(self.verifier_label))
        scene.play(Write(self.vector_0), run_time=0.7)
        scene.play(Write(self.vector_1), run_time=0.7)
        scene.play(Write(self.three_dot), run_time=0.7)
        scene.play(Write(self.vector_k), run_time=0.7)


        self.new_subsection(scene, "what trusted setup?", "data/sound/e4/slide2-4.mp3")

        self.new_subsection(scene, "encrypted polynomial", "data/sound/e4/slide2-5.mp3")

        self.new_subsection(scene, "quotient", "data/sound/e4/slide2-4.mp3")

    def animate_out(self, scene):
        scene.play(FadeOut(self.trusted_setup, self.commiter, self.verifier, self.commiter_label, self.verifier_label, self.commitment))