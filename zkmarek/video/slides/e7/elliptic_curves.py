from manim import (
    FadeIn,
    CurvedArrow,
    Write,
    Text,
    Create,
    RIGHT,
    UP,
    DOWN,
    LEFT,
    MathTex,
    ImageMobject,
    StealthTip,
    FadeOut,
    Circle,
    MoveToTarget,
    Indicate,
    ApplyWave,
    VGroup,
)
from zkmarek.video.constant import (
    PRIMARY_COLOR,
    PRIMARY_FONT,
    SECONDARY_COLOR,
    HIGHLIGHT_COLOR,
)
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.episode5.discrete_polynomial_chart_BLS import (
    PolynomialOnCurve,
)
from zkmarek.video.slides.episode4.discreete_polynomial_chart import (
    DiscreetePolynomialChart,
)
from zkmarek.crypto.field_element import FieldElement
from zkmarek.crypto.weierstrass_curve import BLS12381_137
from zkmarek.crypto.weierstrass_curve import BanderSnatch
from zkmarek.video.mobjects.continuous_elliptic_chart import ContinuousEllipticChart
from zkmarek.video.slides.episode4.chart import Chart


def poly(x):
    output = (
        FieldElement(4, x.order) * x**3
        - FieldElement(8, x.order) * x**2
        - FieldElement(17, x.order) * x
        + FieldElement(30, x.order)
    )
    return output


def poly2(x):
    output = (
        FieldElement(2, x.order) * x**3
        - FieldElement(8, x.order) * x**2
        - FieldElement(17, x.order) * x
        + FieldElement(19, x.order)
    )
    return output


class EllipticCurves(SlideBase):
    def __init__(self) -> None:
        super().__init__("Elliptic curves")

    def construct(self):
        self.title_label = Text(
            "Elliptic curves", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=40
        ).to_edge(UP)

        self.chart_ec_continuous = ContinuousEllipticChart(
            include_details=False, curve_color=HIGHLIGHT_COLOR, b=4
        ).scale(0.8)
        self.formula_bls = MathTex(
            r"{{y^2}} = {{x^3}} + {{4}}", color=HIGHLIGHT_COLOR, font_size=34
        ).next_to(self.chart_ec_continuous, DOWN)
        self.blob = (
            ImageMobject("data/images/blob.png")
            .scale(0.3)
            .next_to(self.chart_ec_continuous, LEFT + UP * 0.2, buff=0.1)
            .shift(LEFT * 0.8 + DOWN)
        )
        self.blob2 = self.blob.copy().scale(0.75).next_to(self.blob, RIGHT, buff=0.0)
        self.blob3 = self.blob.copy().scale(0.75).next_to(self.blob, LEFT, buff=0.0)
        self.chart_scalar = (
            DiscreetePolynomialChart(
                p=41,
                f=poly,
                label="r",
                include_numbers=False,
                dot_color=SECONDARY_COLOR,
            )
            .scale(0.7)
            .shift(RIGHT * 3 + DOWN * 0.5)
        )
        self.chart_scalar_Fq = (
            DiscreetePolynomialChart(
                p=41,
                f=poly2,
                label="q",
                include_numbers=False,
                dot_color=PRIMARY_COLOR,
            )
            .scale(0.7)
            .shift(RIGHT * 3 + DOWN * 0.5)
            .scale(0.7)
            .shift(DOWN * 1.)
        )
        self.chart_ec = (
            PolynomialOnCurve(
                curve=BLS12381_137,
                dot_color=HIGHLIGHT_COLOR,
                label="p",
                include_numbers=False,
            )
            .scale(0.7)
            .shift(DOWN * 0.5)
        )
        self.chart_bander = (
            PolynomialOnCurve(
                curve=BanderSnatch,
                dot_color=HIGHLIGHT_COLOR,
                label="p",
                include_numbers=False,
            )
            .scale(0.7)
            .shift(LEFT * 3 + DOWN * 0.5)
        )

        self.p = (
            MathTex(r"{{p}} \approx 2^{381}", color=HIGHLIGHT_COLOR, font_size=32)
            .next_to(self.chart_ec, LEFT, buff=1.0)
            .shift(UP * 0.2)
        )
        self.r = (
            MathTex(r"{{r}} \approx 2^{256}", color=SECONDARY_COLOR, font_size=32)
            .next_to(self.chart_scalar, RIGHT, buff=0.0)
            .shift(UP * 0.2+LEFT*0.1)
        )
        self.q = (
            MathTex(r"{{q}} \approx 2^{253}", color=SECONDARY_COLOR, font_size=32)
            .next_to(self.chart_scalar, RIGHT, buff=0.0).scale(0.7)
        )
        self.bytes_p2 = MathTex(
            r"\sim {{48}} \ \mathrm{B}", color=HIGHLIGHT_COLOR, font_size=32
        ).next_to(self.p[1], DOWN)

        self.bytes_of_el = Text("32 B", font=PRIMARY_FONT, font_size=24).set_color(
            SECONDARY_COLOR
        )
        self.bytes_of_el.next_to(self.r, DOWN)
        self.sim_32 = MathTex(r"\sim", color=SECONDARY_COLOR, font_size=32).next_to(
            self.bytes_of_el, LEFT, buff=0.1
        )
        self.curve_ec = Text(
            "BLS12-381", color=HIGHLIGHT_COLOR, font=PRIMARY_FONT, font_size=34
        ).next_to(self.chart_ec, RIGHT, buff=0.3).shift(UP)
        self.curve_ec_bander = Text(
            "BanderSnatch", color=HIGHLIGHT_COLOR, font=PRIMARY_FONT, font_size=34
        )

        self.base_field = (
            Text("Base field", color=HIGHLIGHT_COLOR, font=PRIMARY_FONT, font_size=28)
            .next_to(self.chart_ec, LEFT + UP)
            .shift(RIGHT * 0.3)
        )
        self.arrow_base_field = (
            CurvedArrow(
                self.base_field.get_right(),
                self.chart_ec.get_top() + LEFT + UP * 0.6,
                tip_shape=StealthTip,
                stroke_width=2,
            )
            .set_color_by_gradient([HIGHLIGHT_COLOR, HIGHLIGHT_COLOR])
            .scale(0.6)
            .rotate(angle=3.14, axis=[1, 0, 0])
        )
        self.scalar_field = (
            Text("Scalar field", color=SECONDARY_COLOR, font=PRIMARY_FONT, font_size=28)
            .next_to(self.chart_scalar, RIGHT + UP, buff=0)
            .shift(LEFT * 1)
        )
        self.arrow_scalar_field = (
            CurvedArrow(
                self.scalar_field.get_left() + DOWN * 0.05,
                self.chart_scalar.get_top() + RIGHT * 0.3,
                tip_shape=StealthTip,
                stroke_width=2,
            )
            .set_color(SECONDARY_COLOR)
            .scale(0.6)
        )
        self.formula_bls = (
            MathTex(r"{{y^2}} = {{x^3}} + {{4}}", color=HIGHLIGHT_COLOR, font_size=34)
            .next_to(self.curve_ec, DOWN)
            .shift(DOWN * 0.3)
        )
        self.formula_polynomial = MathTex(
            r"{{P(x)}} = \sum_{k=0}^{4095} {{a_k}}  {{x^k}}",
            color=SECONDARY_COLOR,
            font_size=32,
        ).next_to(self.chart_scalar, DOWN)

        self.chart_polynomial_continuous = (
            Chart(include_details=False).scale(0.6).shift(DOWN * 0.2)
        )

        self.point_to_generator = self.chart_ec.get_point(FieldElement(4, 137))
        self.circle_gen = Circle(radius=0.3, color=SECONDARY_COLOR).move_to(
            self.point_to_generator.get_center()
        )
        self.point_to_generator_label = MathTex(
            r"{{G_1 \cdot k}}", color=SECONDARY_COLOR, font_size=32
        ).next_to(self.point_to_generator, RIGHT, buff=0.2)

        self.dot_48b = self.chart_ec.get_point(FieldElement(50, 137))

        self.pairing_def = MathTex(
            r"e({{G_1}}, {{G_2}}) \rightarrow {{G_T}}",
            color=PRIMARY_COLOR,
            font_size=36,
        )

        self.weierstrass_formula = MathTex(r"y^2 = x^3 + {{a}}x + {{b}}", color=HIGHLIGHT_COLOR, font_size=32)

    def animate_in(self, scene):
        self.new_subsection(scene, "kzg->elliptic curves", "data/sound/e7/slide2-1.mp3")
        scene.play(Write(self.title_label), run_time=0.7)
        scene.wait(0.5)
        scene.play(Create(self.chart_ec_continuous), run_time=2)

        self.new_subsection(scene, "BLS12-381", "data/sound/e7/slide2-1a.mp3")
        scene.wait(2)
        scene.play(Write(self.curve_ec), run_time=0.7)
        scene.wait(2.5)
        scene.play(Write(self.formula_bls), run_time=0.7)
        scene.wait(2)
        scene.play(FadeIn(self.blob), run_time=1)
        scene.play(FadeIn(self.blob2), run_time=0.3)
        scene.play(FadeIn(self.blob3), run_time=0.3)

        self.new_subsection(scene, "over finite field", "data/sound/e7/slide2-2.mp3")
        scene.play(FadeOut(self.blob, self.blob2, self.blob3), run_time=0.5)
        scene.wait(1.5)
        scene.play(ApplyWave(self.chart_ec_continuous.ax[0]), run_time=0.5)
        scene.play(ApplyWave(self.chart_ec_continuous.ax[1]), run_time=0.5)
        scene.play(
            FadeOut(self.chart_ec_continuous), FadeIn(self.chart_ec), run_time=1.5
        )

        self.new_subsection(scene, "2^381", "data/sound/e7/slide2-3.mp3")
        scene.wait(2)
        scene.play(Indicate(self.curve_ec, color=SECONDARY_COLOR), run_time=0.9)
        scene.wait(1.7)
        scene.play(Write(self.p), run_time=0.7)

        self.new_subsection(scene, "48 bytes", "data/sound/e7/slide2-4.mp3")
        scene.play(self.dot_48b.animate.set_color(SECONDARY_COLOR), run_time=0.5)
        value_at_4 = poly(FieldElement(50, 137))
        self.labelx0 = self.chart_ec.add_xaxis_label(FieldElement(50, 137).value, r"x_0")
        self.labely0 = self.chart_ec.add_yaxis_label(value_at_4.value, r"y_0")
        
        scene.wait(0.5)
        scene.play(
            Indicate(self.chart_ec.labels[0], color=SECONDARY_COLOR), FadeIn(self.labelx0), run_time=0.7
        )
        scene.play(
            Indicate(self.chart_ec.labels[1], color=SECONDARY_COLOR), FadeIn(self.labely0), run_time=0.7
        )
        scene.wait(0.6)
        scene.play(FadeIn(self.bytes_p2), FadeOut(self.dot_48b))

        self.new_subsection(scene, "generator", "data/sound/e7/slide2-5.mp3")
        scene.wait(1)
        scene.play(Create(self.circle_gen), run_time=1)
        scene.play(Create(self.point_to_generator), run_time=0.5)
        scene.play(Write(self.point_to_generator_label), run_time=0.5)

        self.new_subsection(scene, "scalar field", "data/sound/e7/slide2-6.mp3")
        self.chart_ec.generate_target()
        self.chart_ec.target.shift(LEFT * 3)
        self.point_to_generator_label.generate_target()
        self.point_to_generator_label.target.shift(LEFT * 3)
        self.point_to_generator.generate_target()
        self.point_to_generator.target.shift(LEFT * 3)
        self.circle_gen.generate_target()
        self.circle_gen.target.shift(LEFT * 3)
        self.curve_ec.generate_target()
        self.curve_ec.target.next_to(self.chart_ec.target, UP, buff=0.3)
        self.formula_bls.generate_target()
        self.formula_bls.target.next_to(self.chart_ec.target, DOWN, buff=0.3)
        self.p.generate_target()
        self.p.target.next_to(self.chart_ec.target, LEFT, buff=0.1).shift(UP * 0.2)
        self.bytes_p2.generate_target()
        self.bytes_p2.target.next_to(self.p.target, DOWN)
    
        scene.play(
            MoveToTarget(self.chart_ec),
            MoveToTarget(self.curve_ec),
            MoveToTarget(self.p),
            MoveToTarget(self.bytes_p2),
            MoveToTarget(self.formula_bls),
            MoveToTarget(self.point_to_generator),
            MoveToTarget(self.point_to_generator_label),
            MoveToTarget(self.circle_gen),
            run_time=1,
        )
        self.chart_scalar.gen_points()
        scene.play(Create(self.chart_scalar), run_time=1)
        scene.wait(1)
        scene.play(
            Write(self.scalar_field), Write(self.arrow_scalar_field), run_time=0.5
        )
        scene.wait(2)
        scene.play(Write(self.r), run_time=0.7)
        scene.wait(1)
        scene.play(Write(self.bytes_of_el), Write(self.sim_32), run_time=0.7)

        self.new_subsection(
            scene, "kzg: eval scalars, proof ec", "data/sound/e7/slide2-7.mp3"
        )
        scene.wait(1)
        scene.play(Write(self.formula_polynomial), run_time=0.7)
        scene.wait(1)
        scene.play(Indicate(self.bytes_of_el), run_time=0.9)
        scene.wait(2)
        scene.play(Indicate(self.bytes_p2), run_time=0.9)

        self.new_subsection(scene, "BanderSnatch", "data/sound/e7/slide2-8.mp3")
        scene.wait(1)
        self.curve_ec_bander.next_to(self.chart_ec, UP, buff=0.3)
        self.weierstrass_formula.next_to(self.chart_ec, DOWN, buff=0.3)
        scene.play(
            FadeOut(
                self.point_to_generator_label, self.circle_gen, self.point_to_generator
            ),
            run_time=0.3,
        )
        scene.play(FadeOut(self.chart_ec), FadeIn(self.chart_bander), run_time=1)
        scene.play(
            FadeOut(self.curve_ec),
            FadeIn(self.curve_ec_bander),
            FadeOut(self.formula_bls),
            FadeIn(self.weierstrass_formula),
            FadeOut(self.formula_polynomial),
            run_time=1,
        )
        scene.wait(5)
        scene.play(Indicate(self.weierstrass_formula[1], color = SECONDARY_COLOR, scale_factor=1.5), run_time=0.9)
        scene.play(Indicate(self.weierstrass_formula[3], color = SECONDARY_COLOR, scale_factor=1.5), run_time=0.9)
        scene.wait(0.3)

        self.new_subsection(scene, "pairings", "data/sound/e7/slide2-9.mp3")
        self.all_mobjects = VGroup(
            self.chart_bander,
            self.p,
            self.r,
            self.sim_32,
            self.curve_ec_bander,
            self.bytes_of_el,
            self.bytes_p2,
            self.scalar_field,
            self.arrow_scalar_field,
            self.weierstrass_formula,
            self.chart_scalar,
        )

        self.all_mobjects.generate_target()
        self.all_mobjects.target.scale(0.7).shift(DOWN * 1.)
        scene.play(MoveToTarget(self.all_mobjects), run_time=1)
        self.pairing_def.next_to(self.all_mobjects, UP, buff=1.2)
        self.point_to_generator2 = self.chart_bander.get_point(FieldElement(10, 137))
        self.circle_gen2 = Circle(radius=0.3, color=SECONDARY_COLOR).move_to(
            self.point_to_generator2.get_center()
        )
        self.point_to_generator_label2 = MathTex(
            r"{{G_2 \cdot k}}", color=PRIMARY_COLOR, font_size=32
        ).next_to(self.point_to_generator2, RIGHT, buff=0.5)
        self.chart_scalar_Fq.move_to(
            self.chart_scalar.get_center())
        self.q.move_to(self.r.get_center())
        
        scene.play(Write(self.pairing_def), run_time=0.7)
        scene.wait(2)
        scene.play(Indicate(self.curve_ec_bander, color=SECONDARY_COLOR), run_time=0.9)
        scene.wait(3)
        scene.play(Indicate(self.pairing_def[3], color=SECONDARY_COLOR), run_time=0.9)
        scene.play(Create(self.circle_gen2), run_time=0.5)
        scene.play(Write(self.point_to_generator_label2), run_time=0.5)
        scene.wait(1)
        self.chart_scalar_Fq.gen_points()
        scene.play(FadeOut(self.chart_scalar, self.r), FadeIn(self.chart_scalar_Fq, self.q), run_time=1)
        scene.wait(2.5)

    def animate_out(self, scene):
        scene.play(
            FadeOut(
                self.title_label,
                self.chart_bander,
                self.curve_ec_bander,
                self.bytes_of_el,
                self.bytes_p2,
                self.q,
                self.p,
                self.sim_32,
                self.scalar_field,
                self.arrow_scalar_field,
                self.chart_scalar_Fq,
                self.circle_gen2,
                self.point_to_generator_label2,
                self.pairing_def,
                self.weierstrass_formula,
            ),
            run_time=0.5,
        )
        scene.wait(0.5)
