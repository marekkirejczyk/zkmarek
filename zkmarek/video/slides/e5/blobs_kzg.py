from manim import (Create, DOWN, ImageMobject, RIGHT, LEFT, UP, FadeIn, Polygon, VGroup, Text, Write, FadeOut, PURPLE_A, 
                   TransformMatchingShapes, RoundedRectangle, MoveToTarget, MathTex, Circle, Indicate, Rectangle, GREY_A, WHITE, 
                   BLUE, PURPLE, PINK)

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, HIGHLIGHT_COLOR, SECONDARY_COLOR, HIGHLIGHT2_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase


class KZGBlobs2(SlideBase):

    def __init__(self):
        super().__init__("KZG in blobs")

    def construct(self):
        self.title_text_kzg = Text("KZG", font_size=40, color = PRIMARY_COLOR, font = PRIMARY_FONT).to_edge(UP)
        self.verifier = ImageMobject("data/images/person.png").shift(RIGHT*5+DOWN*1.5).scale(0.6)
        self.commiter = Rectangle(width=3, height=2, fill_opacity=0.3).set_color_by_gradient([PRIMARY_COLOR, GREY_A, WHITE]).shift(LEFT*2+DOWN*1.5).scale(0.6)
        self.commiter_label = Text("Blob", color = PRIMARY_COLOR, font=PRIMARY_FONT).scale(0.6).next_to(self.commiter, DOWN, buff = 0.4)
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
        
        self.blob_data = MathTex(r"\left[ {{a_0}}, {{a_1}}, {{a_2}}, {{\cdots}}, {{a_{4095}}} \right]", color = SECONDARY_COLOR).scale(1.2).shift(UP*2)
        

    def animate_in(self, scene):
        speech_text_verifier = MathTex(r"a_i = ?", font_size=32, color = SECONDARY_COLOR)
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
        bubble_committer = RoundedRectangle(corner_radius=0.5, width=self.blob_data.width + 1, height=self.blob_data.height + 0.5, color = PRIMARY_COLOR).next_to(self.commiter, UP+LEFT, buff = -1).shift(0.4*DOWN+LEFT*0.6)
        self.opening = MathTex(r"{{a}} {{_{x_0}}}) = {{y_0}}", font_size=32, color = PRIMARY_COLOR)
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
        self.blob_data.move_to(bubble_committer.get_center())

        self.new_subsection(scene, "sampling - random positions", "data/sound/e5/slide5-1.mp3")
        scene.play(FadeIn(self.verifier, self.verifier_label, self.commiter, self.commiter_label, self.title_text_kzg), run_time=0.7)
        scene.play(Create(self.blob_data))
        self.lock.next_to(self.blob_data, RIGHT, buff = 0).shift(UP)
        scene.play(Create(bubble_committer), FadeIn(self.lock), run_time=0.7)
        self.opening.move_to(bubble_opening.get_center())
        self.opening.shift(UP*0.3)
        scene.wait(1.5)

        self.commitment = MathTex(r"{{C = }} p({{\tau}})\cdot {{G_1}}", color = PRIMARY_COLOR).next_to(self.blob_data, DOWN).shift(DOWN*0.2)

        scene.play(Create(self.commitment), run_time=1.5)
        scene.wait(2)
        for i in range(5):
            scene.play(Indicate(self.blob_data[2*i+1], color = [HIGHLIGHT2_COLOR, PURPLE_A], scale_factor=1.2), run_time=0.25)
            

        self.new_subsection(scene, "for selected positions", "data/sound/e5/slide5-2.mp3")
        scene.wait(2)
        self.blob_data[3].set_color_by_gradient([PURPLE, BLUE, PINK])
        

        scene.play(Create(bubble_verifier), Create(tail_verifier))
        scene.play(Create(speech_text_verifier))
        self.circle = Circle(radius = 0.12, color = HIGHLIGHT2_COLOR).next_to(self.blob_data, DOWN, buff=-1).shift(LEFT*0.42+UP*0.28)
        self.circle_full = Circle(radius = 0.1, color = HIGHLIGHT2_COLOR, fill_opacity = 1).next_to(self.blob_data, DOWN, buff=-1).shift(LEFT*0.42+UP*0.28)
        scene.wait(1)
        scene.play(FadeOut(bubble_verifier, speech_text_verifier, tail_verifier))
        scene.play(Create(self.circle))
        scene.play(TransformMatchingShapes(self.circle, self.circle_full))
        self.circle_full.generate_target()
        self.circle_full.target.next_to(self.opening, LEFT, buff = 0.1)
        scene.play(FadeIn(self.opening, bubble_opening, tail), MoveToTarget(self.circle_full))
        scene.wait(0.5)
        
        self.new_subsection(scene, "commitment and proof", "data/sound/e5/slide5-3.mp3")

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
        commitment_sent.target.shift(9.5*RIGHT+DOWN*0.7)
        self.envelope_flap.shift(9.5*RIGHT+DOWN*0.7)

        scene.play(MoveToTarget(commitment_sent), run_time=1)

        scene.wait(2)
        self.proof = MathTex(r"{{\pi}} = {{q(\tau)}} \cdot {{G_1}}", color = PRIMARY_COLOR, font_size=32)
        self.proof.next_to(self.opening, DOWN, buff = 0.3)
        scene.play(Write(self.proof), FadeOut(self.circle_full), run_time=0.5)
  
        self.proof.generate_target()
        self.proof.target.next_to(self.verifier, UP)
        self.opening.generate_target()
        self.opening.target.next_to(self.verifier, UP).shift(UP)
        scene.play(FadeOut(bubble_committer, bubble_opening, tail))
        scene.play(MoveToTarget(self.proof), MoveToTarget(self.opening))
        scene.wait(0.7)
        
        self.new_subsection(scene, "blobs dont need to store data permanentlty", "data/sound/e5/slide5-4.mp3")
        scene.wait(3)
        scene.play(Indicate(self.commitment, color = PURPLE))
        scene.wait(1.5)
        scene.play(Indicate(self.proof, color = PURPLE))
        scene.wait(2)

    def animate_out(self, scene):
        scene.play(FadeOut(self.commiter, self.title_text_kzg, self.commiter_label, self.verifier, self.verifier_label, self.commitment, self.envelope_body_closed, self.envelope_flap_closed, self.blob_data, self.opening, self.lock, self.proof))