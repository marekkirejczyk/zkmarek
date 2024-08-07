from manim import LEFT, RIGHT, FadeIn, ImageMobject, Text, DOWN, UP, Write, MathTex, TransformMatchingShapes, Brace, Group, MoveToTarget, FadeOut, Indicate, Arrow

from zkmarek.video.constant import SECONDARY_COLOR, PRIMARY_FONT, PRIMARY_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.e4.chart import Chart

class Commitment(SlideBase):
    chart: Chart

    def __init__(self):
        super().__init__("Commitment")

    def construct(self):
        self.title = Text("Commitment", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size=80).to_edge(UP)
        self.verifier = ImageMobject("data/images/person.png").shift(RIGHT*3)
        self.commiter = ImageMobject("data/images/person_blue.png").shift(LEFT*3)

        self.commiter_label = Text("Commiter", color = PRIMARY_COLOR, font=PRIMARY_FONT).next_to(self.commiter, DOWN, buff = 0.4)
        self.verifier_label = Text("Verifier", color = PRIMARY_COLOR, font=PRIMARY_FONT).next_to(self.verifier, DOWN, buff = 0.4)

        person = ImageMobject("data/images/person.png").scale(0.4)

        self.person1 = person.copy().shift(LEFT)
        self.person2 = person.copy().shift(RIGHT)
        self.person3 = person.copy().shift(UP)
        self.person4 = person.copy().shift(DOWN)
        self.tau = MathTex(r"\tau", font_size = 60, color = SECONDARY_COLOR)
        self.tau_encrypted = MathTex(r"\tau \cdot G", font_size = 60, color = SECONDARY_COLOR)

        self.commitment = MathTex(r"C = P({{\tau}}) \cdot {{G_1}}", color = SECONDARY_COLOR)
        self.ec_point = Brace(self.commitment, DOWN, color = PRIMARY_COLOR)
        self.ec_point_label = Text(r"elliptic curve point", font_size=15, color=PRIMARY_COLOR, font = PRIMARY_FONT)
        self.ec_point.put_at_tip(self.ec_point_label)
        self.chart = Chart(include_details=True).scale(0.6)

    def animate_in(self, scene):
        self.new_subsection(scene, "intro", "data/sound/e4/slide2-0.mp3")
        scene.wait(4)
        scene.play(FadeIn(self.commiter))
        scene.play(FadeIn(self.verifier))
        scene.wait(0.5)
        scene.play(Write(self.commiter_label))
        scene.play(Write(self.verifier_label))

        self.new_subsection(scene, "committing", "data/sound/e4/slide2-1.mp3")
        scene.wait(2)
        scene.play(FadeIn(self.person1), run_time=0.5)
        scene.play(FadeIn(self.person2), run_time=0.5)
        scene.play(FadeIn(self.person3), run_time=0.5)
        scene.play(FadeIn(self.person4), run_time=0.5)
        scene.play(FadeIn(self.tau), run_time=0.5)
        scene.wait(4)
        scene.play(TransformMatchingShapes(self.tau, self.tau_encrypted))

        self.trusted_setup = Group(self.person1, self.person2, self.person3, self.person4, self.tau_encrypted)
        self.trusted_setup.generate_target()
        self.trusted_setup.target.to_edge(UP+RIGHT).scale(0.4)
        scene.wait(2)
        scene.play(MoveToTarget(self.trusted_setup))

        self.new_subsection(scene, "what is commitment", "data/sound/e4/slide2-2.mp3")
        scene.wait(1.5)
        scene.play(Write(self.commitment))
        scene.wait(1.5)
        scene.play(Indicate(self.commitment[1], color = PRIMARY_COLOR))
        scene.wait(1.5)
        scene.play(Indicate(self.commitment[3], color = PRIMARY_COLOR))
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
        scene.wait(1.5)
        self.commitment.generate_target()
        self.commitment.target.shift(UP*1.5)
        scene.play(MoveToTarget(self.commitment))

        self.chart.next_to(self.commitment, DOWN)
        create_arrow(self.commitment, self.chart)
        scene.play(Write(self.chart))
        scene.wait(2)
        scene.play(Indicate(self.commitment[1], color = PRIMARY_COLOR))
        scene.wait(1)
        scene.play(Indicate(self.trusted_setup))
        
        self.new_subsection(scene, "quotient", "data/sound/e4/slide2-4.mp3")

    def animate_out(self, scene):
        scene.play(FadeOut(self.trusted_setup, self.commiter, self.verifier, self.commiter_label, self.verifier_label, self.commitment))

def create_arrow(start, end):
    return Arrow(
        start=start.get_bottom(),
        end=end[0].get_top(),
        color=PRIMARY_COLOR,
        buff=0,
        max_tip_length_to_length_ratio=0.1,
        max_stroke_width_to_length_ratio=1)