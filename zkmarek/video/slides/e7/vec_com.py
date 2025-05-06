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
    Group,
    ORIGIN,
    RoundedRectangle,
)
from manim import BLUE_D, GREEN_E, MAROON_E, PURPLE_B
from zkmarek.video.slides.episode4.discreete_polynomial_chart import (
    DiscreetePolynomialChart,
)
from zkmarek.video.constant import (
    SECONDARY_COLOR,
    PRIMARY_COLOR,
    PRIMARY_FONT,
    HIGHLIGHT_COLOR,
)
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.crypto.field_element import FieldElement
from zkmarek.video.mobjects.dot_on_curve import DotOnCurve
from zkmarek.video.slides.episode4.chart import Chart
from zkmarek.video.slides.e6.curve import Curve
from zkmarek.video.slides.e6.tree import MerkleTree
import numpy as np
from scipy.special import factorial


def poly(x):
    output = (
        FieldElement(1, x.order) * x**3
        - FieldElement(49, x.order) * x**2
        + FieldElement(567, x.order) * x
    )
    return output


class Previously(SlideBase):
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
        self.polynomial_chart = (
            DiscreetePolynomialChart(
                p=41,
                f=poly,
                label="r",
                include_numbers=False,
                dot_color=SECONDARY_COLOR,
            )
            .scale(0.3)
            .to_edge(LEFT)
            .shift(RIGHT + DOWN * 1.5)
        )
        self.polynomial_label = (
            MathTex(r"{{}} {{p(x)}} {{}}", color=PRIMARY_COLOR, font_size=30)
            .next_to(self.polynomial_chart, direction=UP, buff=0)
            .shift(DOWN * 0.1)
        )
        self.prover = (
            ImageMobject("data/images/person.png")
            .scale(0.5)
            .to_edge(LEFT)
            .shift(RIGHT + UP * 1.5)
        )
        self.verifier = (
            ImageMobject("data/images/person_blue.png")
            .scale(0.5)
            .to_edge(RIGHT)
            .shift(LEFT + UP * 1.5)
        )
        self.commiter_label = Text(
            "Prover", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=27
        ).next_to(self.prover, DOWN)
        self.verifier_label = Text(
            "Verifier", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=27
        ).next_to(self.verifier, DOWN)

        self.polynomial_opening_label = MathTex(
            r"{{r(x)}} = {{p(x)}} - {{y_0}}", color=PRIMARY_COLOR, font_size=32
        ).next_to(self.polynomial_chart, UP, buff=0.5)

        self.opening = (
            MathTex(r"{{}}p({{x_0}}) {{}} = {{y_0}}", font_size=30, color=PRIMARY_COLOR)
            .next_to(self.verifier_label, DOWN, buff=0.7)
            .shift(DOWN * 0.7)
        )

        self.opening2 = MathTex(
            r"{{r(x)}} = {{p(x)}} - {{y_0}} {{}}", font_size=35, color=PRIMARY_COLOR
        ).next_to(self.opening, DOWN, buff=1.2)
        self.new_polynomial_label = (
            Text("new   polynomial", color=GREEN_E, font_size=16, font=PRIMARY_FONT)
            .next_to(self.opening2, LEFT, buff=0.1)
            .shift(UP * 0.14)
        )
        self.opening3 = MathTex(
            r"{{a}}{{(x-x_1)}}{{(x - x_2)}}{{(x-x_0)}} = {{p(x)}} - {{y_0}} {{}}",
            font_size=30,
            color=PRIMARY_COLOR,
        )
        self.x_one = FieldElement(3, 41)
        self.x_two = FieldElement(33, 41)
        self.value_at_x_one = poly(self.x_one)
        self.value_at_x_two = poly(self.x_two)
        self.dots = MathTex(r"\cdots", color=PRIMARY_COLOR)

        self.quotient_deriviation_3 = MathTex(
            r"{{q(x)}} = \frac{p(x) - y_0}{x-x_0}", font_size=30, color=PRIMARY_COLOR
        )

        self.pairing_verifiaction_0 = (
            MathTex(
                r"e( {{\pi}}, ({{\tau}} -{{x_0}}) {{\cdot G_2}} ) = e({{C}} - {{y_0}} {{\cdot G_1}}, {{G_2}})",
                color=BLUE_D,
                font_size=30,
            )
            .to_edge(DOWN)
        )
        self.pairing_verifiaction_1 = (
            MathTex(
                r"e( {{\pi}}{{}}, {{(\tau-x_0)}} {{\cdot G_2}} ) = e({{p(\tau)}} \cdot {{G_1}} - {{y_0}} {{\cdot G_1}}, {{G_2}})",
                color=BLUE_D,
                font_size=30,
            )
            .to_edge(DOWN)
        )
        self.pairing_verifiaction_2 = (
            MathTex(
                r"e( {{q(\tau)}}\cdot {{~G_1}}, {{(\tau-x_0)}} {{\cdot G_2}} ) = e({{[p(\tau)}} - {{y_0}}] {{\cdot G_1}}, {{G_2}})",
                color=BLUE_D,
                font_size=30,
            )
            .to_edge(DOWN)
        )
        self.pairing_verifiaction_2a = (
            MathTex(
                r"e( {{q(\tau)}}{{\cdot}}{{(\tau-x_0)}}{{~G_1}}, {{\cdot G_2}} ) = e([{{p(\tau)}} - {{y_0}}] {{\cdot G_1}}, {{G_2}})",
                color=BLUE_D,
                font_size=30,
            )
            .to_edge(DOWN)
        )
        self.pairing_verifiaction_3 = (
            MathTex(
                r"q({{\tau}}) {{\cdot}} {{(\tau-x_0)}} = {{p(\tau)}} - {{y_0}}",
                font_size=30,
                color=PURPLE_B,
            )
            .next_to(self.pairing_verifiaction_2, UP, buff=1.0)
            .shift(UP*1.2)
        )
        self.pairing_verifiaction_4 = (
            MathTex(
                r"q({{\tau}}) = \frac{p(\tau) - y_0}{\tau - x_0}",
                font_size=30,
                color=PURPLE_B,
            )
            .next_to(self.pairing_verifiaction_2, UP, buff=1.0)
            .shift(UP * 1.2)
        )

        self.tau = FieldElement(20, 41)
        self.value_at_tau = poly(self.tau)
        self.z = FieldElement(13, 41)
        self.y = poly(self.z)

        self.chart_interpolation = Chart(include_details=True).scale(0.7).shift(LEFT*2)
        self.chart_interpolation.ax = Axes(
            x_range=[0, 11, 1],
            y_range=[-13, 10.5, 10],
            x_length=7,
            axis_config={
                "include_numbers": True,
                "color": PRIMARY_COLOR,
                "decimal_number_config": {
                    "color": PRIMARY_COLOR,
                    "num_decimal_places": 0,
                },
            },
        ).scale(0.7).shift(LEFT*2.5)

        self.chart_interpolation.labels[0].next_to(
            self.chart_interpolation.ax[0], RIGHT + UP, buff=0.0
        )
        self.chart_interpolation.labels[1].next_to(
            self.chart_interpolation.ax[1], RIGHT + UP, buff=0.0
        )
        self.chart_interpolation_graph4 = (
            self.chart_interpolation.ax.plot_implicit_curve(
                lambda x, y: sum(
                    ((x + 1) ** k * np.sin(k * np.pi * (x + 1) / 3) + 0.3)
                    / factorial(k)
                    / k**k
                    / factorial(k)
                    / k**k
                    / k
                    for k in range(1, 101)
                )
                - y,
                color=SECONDARY_COLOR,
            )
        )#.scale(0.7).shift(LEFT*2)
        self.vector_values = (
            MathTex(
                r"\left[{{2, }}{{3, }}{{1, }}{{-3, }}{{-4, }}{{\cdots}} \right]",
                color=SECONDARY_COLOR,
            )
            .next_to(self.chart_interpolation.ax, RIGHT, buff=1.0)
        )

        self.indeces_over_vector = MathTex(
            r"{{0}}{{1}}{{2}}{{3}}{{4}}{{\cdots}}", color=PRIMARY_COLOR, font_size=30
        )
        for i in range(len(self.indeces_over_vector)):
            self.indeces_over_vector[i].next_to(self.vector_values[i + 1], UP, buff=0.2)
            if i == 5:
                self.indeces_over_vector[i].next_to(
                    self.vector_values[i + 1], UP, buff=0.45
                )

        self.data_points = Text(
            "data vector", font=PRIMARY_FONT, color=BLUE_D, font_size=35
        ).next_to(self.chart_interpolation, RIGHT, buff = 1.0).shift(UP*2)
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

        self.tree = (
            MerkleTree(num_children=2, num_levels=3, include_labels=False)
            .shift(RIGHT * 2.5 + UP * 1.5)
            .scale(0.3)
        )
        self.tree.stretch(2, dim=1)

        self.envelope_body_closed = RoundedRectangle(width = 8, height = 2, 
            fill_color=PRIMARY_COLOR,
            fill_opacity=0.3,
            corner_radius=0.1,
            stroke_width = 0.0
        ).scale(0.3)

        self.envelope_flap_closed = Polygon(
            [-4, 1, 0],
            [4, 1, 0],
            [0, -0.6, 0],
            fill_color=HIGHLIGHT_COLOR,
            fill_opacity=0.2,
            stroke_width = 0.0
        ).scale(0.3)
        self.envelope_body_closed.next_to(self.prover, RIGHT, buff=0.6)
        self.envelope_flap_closed.next_to(self.envelope_body_closed, UP, buff=-0.48)

        self.commitment = MathTex(
            r"{{C}} = {{p(\tau)}} \cdot {{G_1}}", font_size=30, color=PRIMARY_COLOR
        ).move_to(self.envelope_body_closed.get_center())
        self.proof = MathTex(
            r"\pi = q(\tau) \cdot G_1", font_size=30, color=PRIMARY_COLOR
        ).next_to(self.opening, DOWN, buff=0.2)
        self.x_zero = FieldElement(13, 41)
        self.value_at_x_zero = poly(self.x_zero)

        self.poly_eval0 = MathTex(r"P(0)=2", color=PRIMARY_COLOR, font_size=30).next_to(
            self.vector_values[3], DOWN, buff=0.2
        )
        self.poly_eval1 = MathTex(r"P(1)=3", color=PRIMARY_COLOR, font_size=30).next_to(
            self.poly_eval0, RIGHT, buff=0.5
        )
        self.poly_eval2 = MathTex(r"P(2)=1", color=PRIMARY_COLOR, font_size=30).next_to(
            self.poly_eval0, DOWN, buff=0.2
        )
        self.poly_eval3 = MathTex(
            r"P(3)=-3", color=PRIMARY_COLOR, font_size=30
        ).next_to(self.poly_eval2, RIGHT, buff=0.5)
        self.dots_poly_eval = (
            MathTex(r"\cdots", color=PRIMARY_COLOR, font_size=30)
            .next_to(self.poly_eval3, LEFT + DOWN, buff=0.5)
            .shift(RIGHT * 0.7)
        )

    def animate_in(self, scene):
        self.new_subsection(
            scene, "kzg commitment scheme", "data/sound/e6/slide1-0a.mp3"
        )
        scene.play(Write(self.title_label), run_time=0.7)
        scene.play(FadeIn(self.prover), Write(self.commiter_label), run_time=1)
        self.y0_x0(scene)
        self.prover.generate_target()
        self.prover.target.set_opacity(0.5).shift(RIGHT * 0.3)
        self.verifier.generate_target()
        self.verifier.target.set_opacity(0.5).shift(LEFT * 0.3)

        self.commitment.generate_target()
        self.commitment.target.move_to(ORIGIN).shift(UP * 2)
        self.proof.generate_target()
        self.proof.target.next_to(self.commitment.target, DOWN, buff=0.2)
        self.opening.generate_target()
        self.opening.target.next_to(self.proof.target, DOWN, buff=0.2)
        scene.wait(1)

        self.new_subsection(scene, "proof", "data/sound/e6/slide1-0c.mp3")
        scene.play(
            FadeOut(
                self.verifier_label,
                self.commiter_label,
                self.line_correct_y,
                self.line_z,
            ),
            MoveToTarget(self.prover),
            MoveToTarget(self.verifier),
            MoveToTarget(self.proof),
            MoveToTarget(self.opening),
            MoveToTarget(self.commitment),
            run_time=1,
        )
        self.opening2.next_to(self.opening, DOWN, buff=0.3)
        self.polynomial_opening_label.next_to(self.polynomial_chart, UP, buff=0.0)
        self.new_polynomial_label.next_to(self.opening2, LEFT, buff=0.2)
        self.opening3.next_to(self.opening2, DOWN, buff=0.2)
        self.dots.next_to(self.opening3, DOWN, buff=0.2)
        self.quotient_deriviation_3.next_to(self.dots, DOWN, buff=0.5)
        scene.play(
            TransformMatchingShapes(self.opening.copy(), self.opening2),
            FadeIn(self.new_polynomial_label),
        )

        scene.wait(2)
        self.dots_poly = VGroup(*self.polynomial_chart.dots)
        scene.play(Indicate(self.dots_poly, color=GREEN_E, scale_factor=1.3))

        scene.play(Indicate(self.opening[4], color=GREEN_E))
        scene.wait(1.3)
        self.polynomial_chart.animate_shift_dots_with_fade(scene, self.y.value)
        self.polynomial_chart.remove(self.line_z)
        self.polynomial_chart.remove(self.line_correct_y)
        self.polynomial_chart.animate_shift_dots_wrap_fix(scene, self.y.value)
        scene.play(
            Indicate(self.opening[1], color=GREEN_E),
            TransformMatchingShapes(
                self.polynomial_label, self.polynomial_opening_label
            ),
        )
        scene.wait(0.6)

        self.new_subsection(scene, "roots", "data/sound/e6/slide1-0d.mp3")

        labelx1 = self.polynomial_chart.add_xaxis_label(self.x_one.value, r"x_1")
        labelx2 = self.polynomial_chart.add_xaxis_label(self.x_two.value, r"x_2")
        scene.wait(0.5)
        scene.play(
            TransformMatchingShapes(self.opening2.copy(), self.opening3),
            FadeOut(self.new_polynomial_label),
        )
        for i in range(3):
            labels = [self.label_x, labelx1, labelx2]
            roots = [self.opening3[3], self.opening3[1], self.opening3[2]]
            scene.play(
                Indicate(roots[i], color=GREEN_E, scale_factor=1.3), run_time=0.5
            )
            self.polynomial_chart.indicate_xaxis_label(scene, labels[i], runtime=0.5)


        self.quotient_deriviation_3.next_to(self.dots, DOWN, buff=0.2)
        scene.play(Write(self.quotient_deriviation_3))
        scene.wait(2)

        self.new_subsection(
            scene, "comparing two pairings", "data/sound/e7/slide1-14a.mp3"
        )
        scene.wait(0.2)
        scene.play(Indicate(self.commitment, color = SECONDARY_COLOR, scale_factor=1.2), run_time=0.7)
        scene.play(Indicate(self.proof, color = SECONDARY_COLOR, scale_factor=1.2), run_time=0.7)
        scene.wait(1.8)
        scene.play(Indicate(self.opening[0:3], color = SECONDARY_COLOR, scale_factor=1.2), run_time=0.7)
        scene.wait(1.8)
        scene.play(Indicate(self.opening[4], color = SECONDARY_COLOR, scale_factor=1.2), run_time=0.7)
        scene.wait(1)
        self.pairing_eqn = MathTex(r"e({{G_1}}, {{G_2}})\rightarrow {{G_T}}", color=SECONDARY_COLOR, font_size=30).next_to(self.quotient_deriviation_3, DOWN, buff = 1.0)
        scene.play(Write(self.pairing_eqn))
        scene.wait(1)

        self.new_subsection(scene, "real data", "data/sound/e6/slide1-2.mp3")
        scene.wait(2.5)
        scene.play(
            FadeOut(
                self.quotient_deriviation_3,
                self.opening,
                self.proof,
                self.commitment,
                self.polynomial_opening_label,
                self.opening2,
                self.opening3,
                self.pairing_eqn,
            ),
            run_time=0.7,
        )
        rest = Group(self.polynomial_chart, self.verifier, self.prover)
        scene.wait(1.5)
        scene.play(FadeOut(rest), run_time=1.0)

        self.new_subsection(scene, "interpolation", "data/sound/e6/slide1-2a.mp3")
        scene.play(
            FadeIn(self.chart_interpolation.ax, self.chart_interpolation.labels),
            run_time=0.7,
        )
        scene.wait(0.8)
        self.dots_defining(scene)
        scene.play(Create(self.chart_interpolation_graph4))

        self.new_subsection(scene, "interpolation", "data/sound/e6/slide1-2aa.mp3")
        scene.wait(1.5)
        scene.play(Create(self.poly_eval0), Indicate(self.p0), run_time=0.7)
        scene.play(Create(self.poly_eval1), Indicate(self.p1), run_time=0.7)
        scene.play(Create(self.poly_eval2), Indicate(self.p2), run_time=0.5)
        scene.play(Create(self.poly_eval3), Indicate(self.p3), run_time=0.5)
        scene.play(Create(self.dots_poly_eval), run_time=0.5)
        scene.wait(0.7)

        self.new_subsection(scene, "vector commitment", "data/sound/e6/slide1-2b.mp3")

        interpolation = VGroup(
            self.chart_interpolation.ax,
            self.chart_interpolation.labels,
            self.chart_interpolation_graph4,
            self.point,
        )
        scene.play(FadeOut(self.indeces_over_vector, self.vector_values, self.poly_eval0,
            self.dots_poly_eval,
            self.poly_eval1,
            self.poly_eval2,
            self.poly_eval3,), run_time=0.2)
        scene.play(Write(self.data_points))
        scene.play(GrowArrow(self.arrow_data_interpolation))
        scene.play(Write(self.interpolation))
        scene.play(GrowArrow(self.arrow_interpolation_vector))
        scene.play(Write(self.vector_commitment))

        scene.play(
            FadeOut(
                interpolation,
                self.interpolation,
                self.vector_commitment,
                self.data_points,
                self.arrow_data_interpolation,
                self.arrow_interpolation_vector,
            )
        )

    def animate_out(self, scene):
        scene.play(FadeOut(self.title_label))

    def y0_x0(self, scene):
        self.polynomial_chart.gen_points()
        scene.wait(1)
        scene.play(
            FadeIn(self.polynomial_chart), Write(self.polynomial_label), run_time=1
        )
        scene.play(FadeIn(self.verifier, self.verifier_label), run_time=1)
        scene.wait(1)
        scene.play(FadeIn(self.commitment))
        scene.wait(1.5)
        scene.play(Indicate(self.commitment[4], color=SECONDARY_COLOR), run_time=0.9)
        self.dots_poly = VGroup(*self.polynomial_chart.dots)
        scene.wait(1.4)
        scene.play(Indicate(self.dots_poly, color=GREEN_E, scale_factor=1.3))
        scene.wait(1)
        label_tau = self.polynomial_chart.add_xaxis_label(self.tau.value, r"\tau")
        scene.play(Indicate(self.commitment[2], color=SECONDARY_COLOR), run_time=0.8)
        scene.play(FadeIn(label_tau), run_time=0.5)
        scene.play(FadeIn(self.envelope_body_closed, self.envelope_flap_closed))
        self.commitment_sent = VGroup(
            self.commitment, self.envelope_body_closed, self.envelope_flap_closed
        )
        self.opening.next_to(self.commitment, DOWN, buff=0.5)
        self.commitment_sent.generate_target()
        self.commitment_sent.target.next_to(self.verifier_label, DOWN, buff=0.5)
        scene.play(MoveToTarget(self.commitment_sent))
        
        self.new_subsection(scene, "opening - proof pi", "data/sound/e6/slide1-0b.mp3")
        scene.wait(1.5)
        scene.play(Write(self.opening), FadeOut(label_tau))
        self.polynomial_chart.remove(label_tau)
        self.label_y = self.polynomial_chart.add_yaxis_label(
            self.value_at_x_zero.value, r"y_0"
        )
        self.line_correct_y = self.polynomial_chart.animate_create_horizontal_line(
            scene, self.y.value, 0, self.z.value
        )
        scene.play(FadeIn(self.label_y), run_time=0.5)
        self.label_x = self.polynomial_chart.add_xaxis_label(self.x_zero.value, r"x_0")
        self.line_z = self.polynomial_chart.animate_create_vertical_line(
            scene, self.z.value, self.y.value
        )
        scene.play(FadeIn(self.label_x), run_time=0.5)
        scene.wait(0.8)
        scene.play(Indicate(self.prover, color=GREEN_E), run_time=0.7)
        self.proof.next_to(self.opening, DOWN)
        scene.wait(1.5)
        scene.play(FadeIn(self.proof), run_time=0.5)
        self.commitment_sent.generate_target()
        self.commitment_sent.target.next_to(self.verifier_label, DOWN, buff=0.5)
        self.proof.generate_target()
        self.proof.target.next_to(self.commitment_sent, DOWN, buff=0.3)
        self.opening.generate_target()
        self.opening.target.next_to(self.proof.target, DOWN, buff=0.3)
        scene.wait(2)
        scene.play(
            MoveToTarget(self.proof),
            MoveToTarget(self.opening),
            run_time=0.7,
        )
        scene.play(
            FadeOut(self.envelope_body_closed, self.envelope_flap_closed), run_time=0.5
        )

    def dots_defining(self, scene):
        point0 = ValueTracker(0)
        a0 = Curve.from_x(point0.get_value())
        self.p0 = DotOnCurve(self.chart_interpolation.ax, "", a0)
        point1 = ValueTracker(1)
        a1 = Curve.from_x(point1.get_value())
        self.p1 = DotOnCurve(self.chart_interpolation.ax, "", a1)
        point2 = ValueTracker(2)
        a2 = Curve.from_x(point2.get_value())
        self.p2 = DotOnCurve(self.chart_interpolation.ax, "", a2)
        point3 = ValueTracker(3)
        a3 = Curve.from_x(point3.get_value())
        self.p3 = DotOnCurve(self.chart_interpolation.ax, "", a3)
        point4 = ValueTracker(4)
        a4 = Curve.from_x(point4.get_value())
        self.p4 = DotOnCurve(self.chart_interpolation.ax, "", a4)
        point5 = ValueTracker(5)
        a5 = Curve.from_x(point5.get_value())
        self.p5 = DotOnCurve(self.chart_interpolation.ax, "", a5)
        point6 = ValueTracker(6)
        a6 = Curve.from_x(point6.get_value())
        self.p6 = DotOnCurve(self.chart_interpolation.ax, "", a6)
        point7 = ValueTracker(7)
        a7 = Curve.from_x(point7.get_value())
        self.p7 = DotOnCurve(self.chart_interpolation.ax, "", a7)
        point8 = ValueTracker(8)
        a8 = Curve.from_x(point8.get_value())
        self.p8 = DotOnCurve(self.chart_interpolation.ax, "", a8)
        point9 = ValueTracker(9)
        a9 = Curve.from_x(point9.get_value())
        self.p9 = DotOnCurve(self.chart_interpolation.ax, "", a9)

        scene.play(
            Create(self.p0),
            FadeIn(
                self.vector_values[1],
                self.vector_values[0],
                self.indeces_over_vector[0],
            ),
            run_time=0.2,
        )
        scene.play(
            Create(self.p1),
            FadeIn(self.vector_values[2], self.indeces_over_vector[1]),
            run_time=0.2,
        )
        scene.play(
            Create(self.p2),
            FadeIn(self.vector_values[3], self.indeces_over_vector[2]),
            run_time=0.2,
        )
        scene.play(
            Create(self.p3),
            FadeIn(self.vector_values[4], self.indeces_over_vector[3]),
            run_time=0.2,
        )
        scene.play(
            Create(self.p4),
            FadeIn(self.vector_values[5], self.indeces_over_vector[4]),
            run_time=0.2,
        )
        scene.play(
            Create(self.p5),
            FadeIn(
                self.vector_values[6],
                self.vector_values[7],
                self.indeces_over_vector[5],
            ),
            run_time=0.2,
        )
        scene.play(Create(self.p6), run_time=0.2)
        scene.play(Create(self.p7), run_time=0.2)
        scene.play(Create(self.p8), run_time=0.2)
        scene.play(Create(self.p9), run_time=0.2)
        self.point = VGroup(
            self.p0,
            self.p1,
            self.p2,
            self.p3,
            self.p4,
            self.p5,
            self.p6,
            self.p7,
            self.p8,
            self.p9,
        )
