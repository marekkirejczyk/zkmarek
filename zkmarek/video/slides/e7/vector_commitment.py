from manim import (
    FadeIn,
    FadeOut,
    Text,
    MathTex,
    LEFT,
    RIGHT,
    UP,
    DOWN,
    Write,
    TransformMatchingShapes,
    MoveToTarget,
    Indicate,
    VGroup,
    ImageMobject,
    Arrow,
    StealthTip,
    Polygon,
    RoundedRectangle,
)
from manim import BLUE_D, GREEN_E, MAROON_E

from zkmarek.video.constant import (
    SECONDARY_COLOR,
    PRIMARY_COLOR,
    PRIMARY_FONT,
    HIGHLIGHT_COLOR,
)
from zkmarek.video.slides.common.slide_base import SlideBase


class PreviouslyVectorCommitment(SlideBase):
    def __init__(self) -> None:
        super().__init__("Previously on zkMarek")

    def construct(self):
        self.title_label = (
            Text(
                "Previously on zkMarek...",
                font=PRIMARY_FONT,
                color=PRIMARY_COLOR,
                font_size=40,
            )
            .to_edge(UP)
        )
        self.prover = (
            ImageMobject("data/images/person_new.png")
            .scale(0.7)
            .to_edge(LEFT)
            .shift(RIGHT*2 + UP * 1.5)
        )
        self.verifier = (
            ImageMobject("data/images/person_new2.png")
            .scale(0.7)
            .to_edge(RIGHT)
            .shift(LEFT*2 + UP * 1.5)
        )
        self.commiter_label = Text(
            "Prover", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=27
        ).next_to(self.prover, DOWN)
        self.verifier_label = Text(
            "Verifier", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=27
        ).next_to(self.verifier, DOWN)

        self.data_points = Text(
            "data vector", font=PRIMARY_FONT, color=BLUE_D, font_size=35
        ).shift(UP*2)
        self.interpolation = Text(
            "interplolation", font=PRIMARY_FONT, color=GREEN_E, font_size=35
        ).next_to(self.data_points, DOWN, buff=1.5)
        self.vector_commitment = Text(
            "vector commitment", font=PRIMARY_FONT, color=MAROON_E, font_size=35
        ).next_to(self.interpolation, DOWN, buff=1.5)

        self.arrow_data_interpolation = Arrow(
            self.data_points.get_bottom(),
            self.interpolation.get_top(),
            tip_shape=StealthTip,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.15,
        ).set_color_by_gradient([BLUE_D, GREEN_E])
        self.arrow_interpolation_vector = Arrow(
            self.interpolation.get_bottom(),
            self.vector_commitment.get_top(),
            color=PRIMARY_COLOR,
            tip_shape=StealthTip,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.15,
        ).set_color_by_gradient([GREEN_E, MAROON_E])

        self.envelope_body_closed = RoundedRectangle(width = 8, height = 3, 
            fill_color=PRIMARY_COLOR,
            fill_opacity=0.3,
            corner_radius=0.1,
            stroke_width = 0.0
        ).scale(0.3)

        self.envelope_flap_closed = Polygon(
            [-4, 1, 0],
            [4, 1, 0],
            [0, -1.5, 0],
            fill_color=HIGHLIGHT_COLOR,
            fill_opacity=0.2,
            stroke_width = 0.0
        ).scale(0.3)
        self.envelope_body_closed.next_to(self.prover, RIGHT, buff=0.6)
        self.envelope_flap_closed.next_to(self.envelope_body_closed, UP, buff=-0.48).shift(DOWN*0.25)

        self.commitment = Text("commitment  C", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 22).move_to(self.envelope_body_closed.get_center())
        
        self.data_vector_ai = MathTex(r"[{{a_0}}, {{a_1}}, {{a_2}}, {{\ldots}}, {{a_i}}, {{\ldots}}]", color = PRIMARY_COLOR, font_size=40).next_to(self.prover, DOWN, buff = 0.5)
        
        self.envelope = VGroup(self.envelope_body_closed, self.envelope_flap_closed, self.commitment)
        
        self.opening2_text = Text("opening:   ", color = SECONDARY_COLOR, font = PRIMARY_FONT, font_size = 30)
        self.opening2_math = MathTex(r"a_{{{i}}} = 22", color = SECONDARY_COLOR, font_size=40).next_to(self.opening2_text, RIGHT, buff = 0.1)
        self.opening2 = VGroup(self.opening2_text, self.opening2_math).next_to(self.prover, RIGHT, buff = 1.0)
        
        self.opening = MathTex(r"a_{{{i}}} = 22", color = SECONDARY_COLOR, font_size=40).next_to(self.prover, RIGHT, buff = 1.0)
        
        self.pi = MathTex(r"\pi", color = PRIMARY_COLOR, font_size=40)
        self.proof = Text("proof  ", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 30).next_to(self.pi, LEFT, buff = 0.1)
        self.proof_pi = VGroup(self.pi, self.proof).next_to(self.opening, DOWN, buff = 0.2)
        
        indeces = ["0", "1", "2", "...", "i", "..."]
        indeces = [Text(i, color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 20) for i in indeces]
        self.indeces = []
        for i in range(len(indeces)):
            if i == 3 or i == 5:             
                index = indeces[i]
                index.next_to(self.data_vector_ai[2*i+1], DOWN, buff = 0.3)
                self.indeces.append(index)
            else:
                index = indeces[i]
                index.next_to(self.data_vector_ai[2*i+1], DOWN, buff = 0.1)
                self.indeces.append(index)
        self.indeces = VGroup(*self.indeces)
        

    def animate_in(self, scene):
        self.new_subsection(
            scene, "kzg commitment scheme", "data/sound/e7/slide1-14.mp3"
        )
        # scene.play(Write(self.title_label), run_time=0.7)
        scene.play(FadeIn(self.prover, self.verifier), Write(self.commiter_label), Write(self.verifier_label), run_time=1)
        scene.wait(0.5)
        scene.play(Write(self.data_vector_ai), run_time=0.7)
        scene.wait(0.5)
        scene.play(TransformMatchingShapes(self.data_vector_ai.copy(), self.envelope))
        scene.wait(0.5)
        self.envelope.generate_target()
        self.envelope.target.next_to(self.verifier_label, DOWN, buff=0.5)
        scene.play(MoveToTarget(self.envelope), run_time=1)
        scene.wait(1)

        self.new_subsection(scene, "proof", "data/sound/e7/slide1-15.mp3")
        scene.play(Write(self.indeces), run_time=1)
        scene.wait(0.2)
        scene.play(Write(self.opening2), run_time=1)
        scene.wait(2)
        scene.play(Indicate(self.indeces[4], color = HIGHLIGHT_COLOR, scale_factor=2), run_time=1)
        scene.play(FadeOut(self.opening2), FadeIn(self.opening), run_time=0.4)
        scene.play(Write(self.proof_pi), run_time=1)
        scene.wait(1)
        self.proof_pi.generate_target()
        self.proof_pi.target.next_to(self.envelope, DOWN, buff = 0.5)
        self.opening.generate_target()
        self.opening.target.next_to(self.proof_pi.target, DOWN, buff = 0.5)
        scene.play(MoveToTarget(self.opening), MoveToTarget(self.proof_pi), run_time=1)
        scene.wait(1)

        self.new_subsection(scene, "proof convinces", "data/sound/e7/slide1-16.mp3")
        scene.play(Indicate(self.proof_pi, color=HIGHLIGHT_COLOR, scale_factor=1.5), run_time=1)
        scene.play(Indicate(self.verifier, color=PRIMARY_COLOR), run_time=1)
        scene.wait(0.7)
        scene.play(Indicate(self.data_vector_ai[9], color = HIGHLIGHT_COLOR, scale_factor=1.5), run_time=1)
        scene.play(Indicate(self.opening, color=HIGHLIGHT_COLOR), run_time=1)
        scene.wait(0.5)
        scene.play(Indicate(self.opening[1], color=HIGHLIGHT_COLOR, scale_factor=1.5), run_time=1)
        scene.wait(1.5)
        scene.play(Indicate(self.data_vector_ai, color = HIGHLIGHT_COLOR), run_time=1)
        scene.wait(1)
     
    def animate_out(self, scene):
        scene.play(FadeOut(self.title_label, self.data_vector_ai, self.envelope, 
                           self.opening, self.proof_pi, self.verifier, self.prover, 
                           self.verifier_label, self.indeces, self.commiter_label, self.commitment), run_time=1)

