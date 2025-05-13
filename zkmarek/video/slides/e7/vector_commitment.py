from manim import (
    FadeIn,
    FadeOut,
    Text,
    MathTex,
    Create,
    LEFT,
    RIGHT,
    UP,
    DOWN,
    Write,
    TransformMatchingShapes,
    MoveToTarget,
    Indicate,
    VGroup,
    ValueTracker,
    ImageMobject,
    Axes,
    Arrow,
    StealthTip,
    Polygon,
    GrowArrow,
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
from zkmarek.video.mobjects.dot_on_curve import DotOnCurve
from zkmarek.video.slides.e6.curve import Curve


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
            ImageMobject("data/images/person.png")
            .scale(0.7)
            .to_edge(LEFT)
            .shift(RIGHT*2 + UP * 1.5)
        )
        self.verifier = (
            ImageMobject("data/images/person_blue.png")
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

        self.envelope_body_closed = RoundedRectangle(width = 6, height = 3, 
            fill_color=PRIMARY_COLOR,
            fill_opacity=0.3,
            corner_radius=0.1,
            stroke_width = 0.0
        ).scale(0.3)

        self.envelope_flap_closed = Polygon(
            [-3, 1, 0],
            [3, 1, 0],
            [0, -1.5, 0],
            fill_color=HIGHLIGHT_COLOR,
            fill_opacity=0.2,
            stroke_width = 0.0
        ).scale(0.3)
        self.envelope_body_closed.next_to(self.prover, RIGHT, buff=0.6)
        self.envelope_flap_closed.next_to(self.envelope_body_closed, UP, buff=-0.48).shift(DOWN*0.25)

        self.commitment = Text("C", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 30).move_to(self.envelope_body_closed.get_center())
        
        sixteen_element_vector = [4, 16, 22, 24, 22, 19, 20, 20]
        self.sixteen_element_vector = VGroup(*[Text(str(i), color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 20) for i in sixteen_element_vector]).arrange(RIGHT, buff=0.05)
        rectangle = RoundedRectangle(height = 1, width = 1, corner_radius=0.05, color=SECONDARY_COLOR, fill_opacity=0.5, stroke_width = 0.0).scale(0.3).move_to(self.sixteen_element_vector.get_center()).set_color(SECONDARY_COLOR)
        rectangles_of_values = [rectangle.copy() for _ in range(8)]
        self.rectangles_values = VGroup(*rectangles_of_values).next_to(self.prover, DOWN, buff = 1.5).arrange(RIGHT, buff=0.07).shift(LEFT*3.7+DOWN*0.3)
        for i in range(8):
            self.sixteen_element_vector[i].move_to(self.rectangles_values[i].get_center())

        self.data_vector = VGroup(
            self.sixteen_element_vector,
            self.rectangles_values)
        
        self.envelope = VGroup(self.envelope_body_closed, self.envelope_flap_closed, self.commitment)
        
        self.opening2 = MathTex(r"\mathrm{opening} \  a_{{{i}}} = 22", color = SECONDARY_COLOR, font_size=40).next_to(self.prover, RIGHT, buff = 1.0)
        self.opening = MathTex(r"\mathrm{opening} \ a_{{{i}}}", color = SECONDARY_COLOR, font_size=40).next_to(self.prover, RIGHT, buff = 1.0)
        self.proof_pi = MathTex(r"\mathrm{proof } \ \pi", color = SECONDARY_COLOR, font_size=40).next_to(self.opening, DOWN, buff = 0.2)
        
        indeces = ["0", "1", "2", "...", "i", "..."]
        indeces = [Text(i, color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 20) for i in indeces]
        self.indeces = []
        for i in range(len(indeces)):
            if i == 3 or i == 5:                
                index = indeces[i]
                index.next_to(self.rectangles_values[i], DOWN, buff = 0.2)
                self.indeces.append(index)
            else:
                index = indeces[i]
                index.next_to(self.rectangles_values[i], DOWN, buff = 0.1)
                self.indeces.append(index)
        self.indeces = VGroup(*self.indeces)
        

    def animate_in(self, scene):
        self.new_subsection(
            scene, "kzg commitment scheme", "data/sound/e7/slide1-14.mp3"
        )
        scene.play(Write(self.title_label), run_time=0.7)
        scene.play(FadeIn(self.prover, self.verifier), Write(self.commiter_label), Write(self.verifier_label), run_time=1)
        scene.wait(0.5)
        scene.play(Write(self.data_vector), run_time=0.7)
        scene.wait(0.5)
        scene.play(TransformMatchingShapes(self.data_vector.copy(), self.envelope))
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
        scene.play(Indicate(self.indeces[4], color = HIGHLIGHT_COLOR, scale_factor=1.5), run_time=1)
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
        scene.play(Indicate(self.data_vector[0][4], color=HIGHLIGHT_COLOR),
                   Indicate(self.data_vector[1][4], color = HIGHLIGHT_COLOR, scale_factor=1.5), run_time=1)
        scene.play(Indicate(self.opening, color=HIGHLIGHT_COLOR), run_time=1)
        scene.wait(0.5)
        scene.play(Indicate(self.opening[1], color=HIGHLIGHT_COLOR, scale_factor=1.5), run_time=1)
        

        self.new_subsection(scene, "vector commitment", "data/sound/e7/slide1-17.mp3")
        self.animate_polynomial()
        scene.play(Create(self.new_axes), run_time=2)
        scene.wait(1)
        values_y = [4, 16, 22, 23, 22, 20.5, 19.5, 20]
        self.points_dots = []
        values = [
            (0, 4), (1, 16), (2, 22), (3, 23), (4, 22), (5, 20.5), (6, 19.5), (7, 20),
        ]
        for i, (x, y) in enumerate(values):
            tracker = ValueTracker(x)
            curve = Curve.from_x(tracker.get_value())
            dot = DotOnCurve(self.new_axes, f"({{{x}}}, {{{y}}})", curve).dot
            self.points_dots.append(dot)
            
        for i in range(8):
            dot = self.points_dots[i]
            dot.move_to(self.new_axes.c2p(i, values_y[i]))

            scene.play(Create(dot), run_time=0.1)
        scene.wait(1)
        scene.play(Create(self.polynomial_graph), run_time=1.5)
        self.polynomial = VGroup(self.new_axes, self.polynomial_graph, *self.points_dots)
        scene.play(Write(self.data_points), FadeOut(self.polynomial), run_time=0.3)
        scene.play(GrowArrow(self.arrow_data_interpolation), run_time=0.3)
        scene.play(Write(self.interpolation), run_time=0.3)
        scene.play(GrowArrow(self.arrow_interpolation_vector), run_time=0.3)
        scene.play(Write(self.vector_commitment), run_time=0.3)
        scene.wait(1)

     
    def animate_out(self, scene):
        scene.play(FadeOut(self.title_label, self.data_vector, self.envelope, self.arrow_data_interpolation, self.arrow_interpolation_vector, 
                           self.opening, self.proof_pi, self.verifier, self.prover, self.verifier_label, self.indeces, self.commiter_label, 
                           self.data_points, self.interpolation, self.vector_commitment, self.commitment), run_time=1)

    def animate_polynomial(self):
        self.new_axes = Axes(
            x_range=[-0.5, 8, 1],
            y_range=[-3, 25, 500],
            x_length=7,
            axis_config={
                "include_numbers": True,
                "color": PRIMARY_COLOR,
                "decimal_number_config": {
                    "color": PRIMARY_COLOR,
                    "num_decimal_places": 0
                }
            }
        ).scale(0.6)
        
        self.polynomial_graph = self.new_axes.plot_implicit_curve(lambda x, y: (-0.013005328649673187  * x ** (4) + 0.44002953745582507 * x ** (3) 
                                                                  -4.368305697782954 * x ** (2) + 15.731787164922928 * x ** (1)
                                                                  +4.2790892673006296 * x ** (0)) - y, color=SECONDARY_COLOR)
        self.polynomial_chart = VGroup(self.new_axes, self.polynomial_graph)
        

  