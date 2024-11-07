from manim import FadeIn, FadeOut, ImageMobject, Text, LEFT, RIGHT, DOWN, UP, Write, Polygon, MathTex, RoundedRectangle, Tex, Create, MoveToTarget, VGroup, Rectangle, GrowArrow, Arrow, GRAY, Line, WHITE, Indicate
from zkmarek.crypto.field_element import FieldElement
from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR, HIGHLIGHT_COLOR, PRIMARY_FONT
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
        self.tau = FieldElement(33, 41)
        self.value_at_tau = poly(self.tau)
        self.z = FieldElement(13, 41)
        self.y = poly(self.z)
        self.chart_label_x0 = self.chart.add_xaxis_label(self.z.value, r"x_0")
        self.chart_label_tau = self.chart.add_xaxis_label(self.tau.value, r"\tau")

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
        self.envelope_body.next_to(self.committer, RIGHT+DOWN, buff = 0.4)
        self.envelope_body_closed.next_to(self.committer, RIGHT+DOWN, buff = 0.4)

        self.envelope_flap.next_to(self.envelope_body, UP, buff= 0)
        self.envelope_flap_closed.next_to(self.envelope_body_closed, UP, buff = -0.63)
        self.lock = ImageMobject("data/images/Locked@2x.png").scale(0.2)
        self.commitment = MathTex(r"{{C}} = {{p(\tau)}} \cdot {{G_1}}", font_size = 32, color=PRIMARY_COLOR)
        self.proof = MathTex(r"{{\pi}} = {{q(\tau)}} \cdot {{G_1}}", font_size=32, color=PRIMARY_COLOR)
        self.proof.next_to(self.verifier_label, DOWN)
        self.opening = MathTex(r"p(x_0)=y_0", font_size=32, color = SECONDARY_COLOR).next_to(self.commitment, DOWN)
        self.commitment.next_to(self.committer, RIGHT, buff = 0)
        self.chart.next_to(self.committer_label, DOWN, buff = -1).scale(0.3).shift(UP)

    def animate_in(self, scene):
        self.new_subsection(scene, "In previous episode...", "data/sound/e5/slide0-1.mp3")
        scene.play(Write(self.title_label))
        scene.play(FadeIn(self.committer, self.committer_label))
        scene.play(FadeIn(self.verifier, self.verifier_label))
        self.chart.gen_points()
        scene.play(Create(self.chart))
        self.dots = VGroup(*self.chart.dots)
        
        scene.play(FadeIn(self.envelope_body_closed, self.envelope_flap_closed, self.commitment))
        scene.play(FadeOut(self.envelope_flap_closed), FadeIn(self.envelope_flap))
        self.commitment.generate_target()
        self.commitment.target.move_to(self.envelope_body_closed.get_center())

        scene.play(FadeOut(self.envelope_flap), FadeIn(self.envelope_flap_closed), 
                   MoveToTarget(self.commitment), run_time=2)
        commitment_sent = VGroup(self.envelope_body_closed, self.envelope_flap_closed, self.commitment)
        commitment_sent.generate_target()
        commitment_sent.target.shift(5.5*RIGHT+DOWN*2)
        self.envelope_flap.shift(5.5*RIGHT+DOWN*2)

        scene.play(MoveToTarget(commitment_sent), run_time=1)
        speech_text_verifier = Tex(r"$p(x_0) = \ ?$", font_size=32, color = SECONDARY_COLOR)
        bubble_verifier = RoundedRectangle(corner_radius=0.5, width=speech_text_verifier.width + 1, height=speech_text_verifier.height + 1.2, color = SECONDARY_COLOR).next_to(self.verifier, DOWN+LEFT, buff = -1).shift(1.3*LEFT+DOWN*0.5)
        bubble_verifier.shift(UP) 
        speech_text_verifier.move_to(bubble_verifier.get_center())
        tail_verifier = Polygon(
            [0, 0, 0], 
            [0, -0.9, 0], 
            [0.78, 0.1, 0], 
            color=SECONDARY_COLOR,
            fill_opacity=0.4
        ).next_to(bubble_verifier, RIGHT, buff=-0.8).scale(0.4).shift(0.58*RIGHT)

        
        self.new_subsection(scene, "key feature", "data/sound/e5/slide0-2.mp3")
        scene.play(Create(bubble_verifier), Create(tail_verifier))
        scene.play(Create(speech_text_verifier))
        bubble_opening = RoundedRectangle(corner_radius=0.5, width=self.opening.width + 0.7, 
                                          height=self.opening.height + 1.5, 
                                          color = PRIMARY_COLOR).next_to(self.committer, RIGHT, buff = -0.3).shift(RIGHT*0.7+DOWN*0.5)
        tail = Polygon(
            [0, 0.03, 0], 
            [-0.9, 0.2, 0], 
            [0, -1, 0], 
            color=PRIMARY_COLOR,
            fill_opacity=0.4
        ).next_to(bubble_opening, LEFT, buff=-0.8).scale(0.4).shift(LEFT*0.54)

        self.opening.move_to(bubble_opening.get_center())
        self.opening.shift(UP*0.3)
        self.proof.next_to(self.opening, DOWN, buff = 0.3)
        scene.play(Create(bubble_opening), Create(tail))
        scene.play(FadeIn(self.opening, self.proof))
        scene.wait(0.5)
        self.chart.indicate_xaxis_label(scene, self.chart_label_x0)
        scene.play(Indicate(self.dots, color = SECONDARY_COLOR))
        scene.play(FadeOut(bubble_verifier, tail_verifier, bubble_verifier, speech_text_verifier))
        scene.play(FadeOut(bubble_opening, tail))
        self.opening.generate_target()
        self.opening.target.next_to(self.verifier_label, DOWN) 
        self.proof.generate_target()
        self.proof.target.next_to(self.verifier_label, DOWN).shift(DOWN*0.5)
        scene.play(MoveToTarget(self.opening), MoveToTarget(self.proof))
        self.commitment.generate_target()
        self.commitment.target.next_to(self.proof, DOWN)
        scene.play(FadeOut(self.envelope_body_closed, self.envelope_flap_closed))
        scene.play(MoveToTarget(self.commitment))
        
        self.new_subsection(scene, "biggest scalling challenges", "data/sound/e5/slide0-3.mp3")
        scene.play(FadeOut(self.chart, self.verifier, self.verifier_label, self.commitment, self.committer, self.committer_label, self.opening, self.proof))
        block1 = Rectangle(width=3, height=3)
        block1.set_color_by_gradient([WHITE, HIGHLIGHT_COLOR, PRIMARY_COLOR])
        prev_hash1 = Text("Prev hash", font = PRIMARY_FONT, color = SECONDARY_COLOR).scale(0.5).next_to(block1.get_top(), DOWN)
        tx1 = Text("transaction 1", font = PRIMARY_FONT).scale(0.4).next_to(prev_hash1, DOWN)
        tx2 = Text("transaction 2", font = PRIMARY_FONT).scale(0.4).next_to(tx1, DOWN)
        pow_text1 = Text("Proof of work", color=PRIMARY_COLOR, font = PRIMARY_FONT).scale(0.5).next_to(block1.get_bottom(), UP)
        line1_1 = Line(block1.get_left(), block1.get_right(), color=GRAY).shift(UP*0.85)
        line1_2 = line1_1.copy().shift(DOWN*1.6)
        self.three_dot = Text(".\n.\n.", font=PRIMARY_FONT).scale(0.3).next_to(tx1, DOWN).shift(DOWN*0.35)
        
        self.block1_group = VGroup(block1, prev_hash1, tx1, tx2, pow_text1, line1_1, line1_2, self.three_dot)
        self.block1_group.shift(LEFT * 4)
        
        block2 = block1.copy().shift(RIGHT * 4)
        prev_hash2 = Text("Prev hash", font = PRIMARY_FONT, color = SECONDARY_COLOR).scale(0.5).next_to(block2.get_top(), DOWN)
        tx3 = Text("transaction 3", font = PRIMARY_FONT).scale(0.4).next_to(prev_hash2, DOWN)
        tx4 = Text("transaction 4", font = PRIMARY_FONT).scale(0.4).next_to(tx3, DOWN)
        pow_text2 = Text("Proof of work", color=PRIMARY_COLOR, font = PRIMARY_FONT).scale(0.5).next_to(block2.get_bottom(), UP)
        line2_1 =Line(block2.get_left(), block2.get_right(), color=GRAY).shift(UP*0.85)
        line2_2 = line2_1.copy().shift(DOWN*1.6)
        self.three_dot2 = Text(".\n.\n.", font=PRIMARY_FONT).scale(0.3).next_to(tx3, DOWN).shift(DOWN*0.35)
        
        self.block2_group = VGroup(block2, prev_hash2, tx3, tx4, pow_text2, line2_1, line2_2, self.three_dot2)
        
        block3 = block2.copy().shift(RIGHT * 4)
        prev_hash3 = Text("Prev hash", font = PRIMARY_FONT, color = SECONDARY_COLOR).scale(0.5).next_to(block3.get_top(), DOWN)
        tx5 = Text("transaction 5", font = PRIMARY_FONT).scale(0.4).next_to(prev_hash3, DOWN)
        tx6 = Text("transaction 6", font = PRIMARY_FONT).scale(0.4).next_to(tx5, DOWN)
        pow_text3 = Text("Proof of work", color=PRIMARY_COLOR, font = PRIMARY_FONT).scale(0.5).next_to(block3.get_bottom(), UP)
        line3_1 =Line(block3.get_left(), block3.get_right(), color=GRAY).shift(UP*0.85)
        line3_2 = line3_1.copy().shift(DOWN*1.6)
        self.three_dot3 = Text(".\n.\n.", font=PRIMARY_FONT).scale(0.3).next_to(tx5, DOWN).shift(DOWN*0.35)    
        self.block3_group = VGroup(block3, prev_hash3, tx5, tx6, pow_text3, line3_1, line3_2, self.three_dot3)
        
        self.arrow = Arrow(block1.get_right(), block2.get_left(), color=SECONDARY_COLOR)
        self.arrow2 = Arrow(block2.get_right(), block3.get_left(), color=SECONDARY_COLOR)
        
        scene.play(Create(self.block1_group))
        scene.wait(1)
        scene.play(GrowArrow(self.arrow))
        scene.wait(0.5)
        scene.play(Create(self.block2_group))
        scene.play(GrowArrow(self.arrow2))
        scene.wait(0.5)
        scene.play(Create(self.block3_group))
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.arrow, self.arrow2, self.block1_group, self.block2_group, self.block3_group, self.title_label))