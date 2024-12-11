from manim import (FadeIn, FadeOut, ImageMobject, Text, LEFT, RIGHT, DOWN, UP, Write, Polygon, MathTex, 
Tex, Create, MoveToTarget, VGroup, Rectangle, GrowArrow, Arrow, WHITE, Indicate, Group, StealthTip, PURPLE, PINK)
from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR, HIGHLIGHT_COLOR, PRIMARY_FONT, HIGHLIGHT2_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.e4.discreete_polynomial_chart import DiscreetePolynomialChart

def poly(x):
    return x * x * x - x * x * 2 + x * 3 + 7


class Episode4Recap(SlideBase):
    def __init__(self) -> None:
        super().__init__(title="Episode 4 Recap")
        
    def construct(self):
        self.title_label = Text("Previously on zkMarek...", font_size = 40, font=PRIMARY_FONT, color = PRIMARY_COLOR).to_edge(UP)
        self.committer = ImageMobject("data/images/person_blue.png").scale(0.7)
        self.verifier = ImageMobject("data/images/person.png").scale(0.7)
        self.committer_label = Text("Committer", font = PRIMARY_FONT, color = PRIMARY_COLOR).scale(0.7)
        self.verifier_label = Text("Verifier", font = PRIMARY_FONT, color = PRIMARY_COLOR).scale(0.7)
        
        self.committer.shift(LEFT*4+UP*1.5)
        self.verifier.shift(RIGHT*4+UP*1.5)
        self.committer_label.next_to(self.committer, DOWN)
        self.verifier_label.next_to(self.verifier, DOWN)
        self.chart = DiscreetePolynomialChart(41, poly)


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
        self.ethereum_logo = ImageMobject("data/images/ethereum_logo.png").scale(0.3)
        self.envelope_body.next_to(self.committer, RIGHT+DOWN, buff = 0.4).shift(DOWN)
        self.envelope_body_closed.next_to(self.committer, RIGHT+DOWN, buff = 0.4).shift(DOWN)

        self.envelope_flap.next_to(self.envelope_body, UP, buff= 0)
        self.envelope_flap_closed.next_to(self.envelope_body_closed, UP, buff = -0.63)
        self.lock = ImageMobject("data/images/Locked@2x.png").scale(0.2)
        self.commitment = MathTex(r"{{C}} = {{p(\tau)}} \cdot {{G_1}}", font_size = 32, color=PRIMARY_COLOR)
        self.proof = MathTex(r"{{\pi}} = {{q(\tau)}} \cdot {{G_1}}", font_size=32, color=PRIMARY_COLOR)
        self.proof.next_to(self.verifier_label, DOWN)
        self.opening = MathTex(r"p(x_0)=y_0", font_size=32, color = SECONDARY_COLOR)

        self.chart.next_to(self.committer_label, DOWN, buff = -1).scale(0.3).shift(UP)

    def animate_in(self, scene):
        self.new_subsection(scene, "In previous episode...", "data/sound/e5/slide0-1.mp3")
        scene.play(Write(self.title_label), run_time=0.7)
        scene.play(FadeIn(self.committer, self.committer_label), FadeIn(self.verifier, self.verifier_label), run_time=1.7)
        self.chart.gen_points()
        scene.play(Create(self.chart))
        self.dots = VGroup(*self.chart.dots)
        
        self.new_subsection(scene, "key feature", "data/sound/e5/slide0-2.mp3")
        scene.wait(1.5)
        scene.play(Indicate(self.dots, color = SECONDARY_COLOR))
        
        self.new_subsection(scene, "key feature", "data/sound/e5/slide0-2a.mp3")
        scene.play(FadeIn(self.envelope_body_closed, self.envelope_flap_closed, self.commitment))
        scene.play(FadeOut(self.envelope_flap_closed), FadeIn(self.envelope_flap))
        self.commitment.generate_target()
        self.commitment.target.move_to(self.envelope_body_closed.get_center())

        scene.play(FadeOut(self.envelope_flap), FadeIn(self.envelope_flap_closed), 
                   MoveToTarget(self.commitment), run_time=0.7)
        commitment_sent = VGroup(self.envelope_body_closed, self.envelope_flap_closed, self.commitment)
        commitment_sent.generate_target()
        commitment_sent.target.shift(5.5*RIGHT+DOWN)
        self.envelope_flap.shift(5.5*RIGHT+DOWN)

        scene.play(MoveToTarget(commitment_sent), run_time=0.7)

        self.opening.next_to(self.verifier_label, DOWN) 
        self.proof.next_to(self.verifier_label, DOWN).shift(DOWN*0.5)
        scene.play(FadeIn(self.opening, self.proof))
        self.commitment.generate_target()
        self.commitment.target.next_to(self.proof, DOWN)
        
        scene.play(FadeOut(self.envelope_body_closed, self.envelope_flap_closed), MoveToTarget(self.commitment))
        scene.play(Indicate(self.commitment, color = PINK))
        scene.wait(0.7)
        scene.play(Indicate(self.opening, color = [PURPLE, PINK]))
        scene.wait(0.5)
        scene.play(Indicate(self.proof, color = [PURPLE, PINK]))
        scene.wait(2)
        
        self.new_subsection(scene, "biggest scalling challenges", "data/sound/e5/slide0-3.mp3")
        scene.play(FadeOut(self.chart, self.verifier, self.verifier_label, self.commitment, 
                           self.committer, self.committer_label, self.opening, self.proof))
        block1 = Rectangle(width=1.6, height=1.2, fill_opacity = 0.3)
        block1.set_color_by_gradient([WHITE, PURPLE, HIGHLIGHT2_COLOR])
        self.ethereum_logo.move_to(block1.get_center())
        self.block1_group = Group(block1, self.ethereum_logo)
        self.block1_group.shift(LEFT * 4)
        
        block2 = block1.copy().shift(RIGHT * 4)
        self.ethereum_logo2 = self.ethereum_logo.copy()
        self.ethereum_logo2.move_to(block2.get_center())
        self.block2_group = Group(block2, self.ethereum_logo2)
        
        block3 = block2.copy().shift(RIGHT * 4)
        self.ethereum_logo3 = self.ethereum_logo.copy()
        self.ethereum_logo3.move_to(block3.get_center()) 
        self.block3_group = Group(block3, self.ethereum_logo3)
        
        self.arrow = Arrow(block1.get_right(), block2.get_left(), color=SECONDARY_COLOR, tip_shape=StealthTip, 
                           stroke_width=2, max_tip_length_to_length_ratio=0.15).set_color_by_gradient([SECONDARY_COLOR, WHITE])
        self.arrow2 = Arrow(block2.get_right(), block3.get_left(), color=SECONDARY_COLOR, tip_shape=StealthTip, 
                            stroke_width=2, max_tip_length_to_length_ratio=0.15).set_color_by_gradient([SECONDARY_COLOR, WHITE])
        
        scene.play(FadeIn(self.block1_group))
        
        scene.play(GrowArrow(self.arrow))
        
        scene.play(FadeIn(self.block2_group))
        scene.play(GrowArrow(self.arrow2))
        scene.play(FadeIn(self.block3_group))
        
        self.new_subsection(scene, "blobs", "data/sound/e5/slide0-4.mp3")
        scene.wait(2.3)
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.arrow, self.arrow2, self.block1_group, self.block2_group, self.block3_group, self.title_label))