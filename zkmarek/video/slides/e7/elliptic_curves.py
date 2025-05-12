from manim import (
    FadeIn,
    Write,
    Text,
    Create,
    RIGHT,
    UP,
    DOWN,
    LEFT,
    MathTex,
    ImageMobject,
    TransformMatchingShapes,
    FadeOut,
    Circle,
    MoveToTarget,
    Indicate,
    VGroup,
    RoundedRectangle,
    Polygon,
    rate_functions,
    Line,
    Axes,
    ApplyWave,
)
from zkmarek.video.constant import (
    PRIMARY_COLOR,
    PRIMARY_FONT,
    SECONDARY_COLOR,
    HIGHLIGHT_COLOR,
    HIGHLIGHT2_COLOR,
)
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.episode5.discrete_polynomial_chart_BLS import (
    PolynomialOnCurve,
)
from zkmarek.crypto.field_element import FieldElement
from zkmarek.crypto.weierstrass_curve import BLS12381_137
from zkmarek.crypto.weierstrass_curve import BanderSnatch
from zkmarek.video.mobjects.continuous_elliptic_chart import ContinuousEllipticChart

from zkmarek.video.slides.e7.comparisonIPAKZG import TableKZGIPA

class EllipticCurves(SlideBase):
    def __init__(self) -> None:
        super().__init__("Elliptic curves")
        
    def construct(self):
        self.title_label = Text(
            "Elliptic curves", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=40
        ).to_edge(UP)
        self.title_label2 = Text(
            "Elliptic curves in the Verkle trees", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=40
        ).to_edge(UP)

        self.chart_ec_continuous = ContinuousEllipticChart(
            include_details=False, curve_color=HIGHLIGHT_COLOR, b=4
        ).scale(0.8).shift(DOWN * 0.5)
        self.formula_bls = MathTex(
            r"{{y^2}} = {{x^3}} + {{4}}", color=HIGHLIGHT_COLOR, font_size=34
        ).next_to(self.chart_ec_continuous, DOWN)
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
                dot_color=HIGHLIGHT2_COLOR,
                label="p'",
                include_numbers=False,
            )
            .scale(0.7)
            .shift(RIGHT * 3 + DOWN * 0.5)
        )

        self.p = (
            MathTex(r"{{p}} \approx 2^{381}", color=HIGHLIGHT_COLOR, font_size=32)
            .shift(UP * 1.5+RIGHT * 3)
        )
        self.ec_points = Text("EC points", color = HIGHLIGHT_COLOR, font = PRIMARY_FONT, font_size=24).next_to(self.p, LEFT, buff = 0.4)
        
        self.bytes_p2 = MathTex(
            r"\sim {{48}} \ \mathrm{B}", color=HIGHLIGHT_COLOR, font_size=32
        ).next_to(self.p, RIGHT, buff = 0.7)
        
        self.curve_ec = Text(
            "BLS12-381", color=HIGHLIGHT_COLOR, font=PRIMARY_FONT, font_size=34
        ).next_to(self.chart_ec, UP, buff=0.3)
        self.curve_ec_bander = Text(
            "BanderSnatch", color=HIGHLIGHT2_COLOR, font=PRIMARY_FONT, font_size=34
        )
        self.r = (
            MathTex(r"{{r}} \approx 2^{255}", color=SECONDARY_COLOR, font_size=32)
            .next_to(self.p, DOWN, buff = 1.0).shift(DOWN*0.5)
        )
        self.base_field_bls = MathTex(r"F_p \sim 381 \ \mathrm{b}", font_size = 40).shift(RIGHT*3+UP*1.5)
        self.scalar_Fr = MathTex(r"F_r \sim 255 \ \mathrm{b}", font_size = 40).shift(RIGHT*3)
        self.scalar_Fq = MathTex(r"k'\in F_q", font_size = 40).next_to(self.scalar_Fr, DOWN, buff = 1.0).shift(DOWN)
        
        self.bytes_p2 = Text(
            "48 B", color=HIGHLIGHT_COLOR, font_size=24, font = PRIMARY_FONT
        ).next_to(self.base_field_bls, RIGHT, buff = 0.7)
        self.sim_48 = MathTex(r"\sim", color = HIGHLIGHT_COLOR, font_size = 32).next_to(self.bytes_p2, LEFT, buff = 0.1)
        self.bytes_p2 = VGroup(self.sim_48, self.bytes_p2)
        self.scalars = Text("scalars", color = SECONDARY_COLOR, font = PRIMARY_FONT, font_size=24).next_to(self.r, LEFT, buff=0.4)
        self.bytes_of_el = Text("32 B", font=PRIMARY_FONT, font_size=24).set_color(
            SECONDARY_COLOR
        )
        self.bytes_of_el.next_to(self.scalar_Fr, RIGHT, buff = 0.7)
        self.sim_32 = MathTex(r"<", color=SECONDARY_COLOR, font_size=32).next_to(
            self.bytes_of_el, LEFT, buff=0.1
        )
        self.bytes_of_el = VGroup(self.sim_32, self.bytes_of_el)

        self.dot_48b = self.chart_ec.get_point(FieldElement(50, 137))

        self.pairing_def = MathTex(
            r"e({{G_1}}, {{G_2}}) \rightarrow {{G_T}}",
            color=PRIMARY_COLOR,
            font_size=36,
        )
        self.animate_polynomial()

        self.envelope = RoundedRectangle(width = 8 * 0.3, height = 4 * 0.3, fill_opacity = 0.3, stroke_width = 0.0, corner_radius=0.1).set_color(PRIMARY_COLOR)
        self.envelope_flap_closed = Polygon(
            [-4.3, 1, 0],
            [4.3, 1, 0],
            [0, -1.6, 0],
            fill_color=HIGHLIGHT_COLOR,
            fill_opacity=0.2,
            stroke_width = 0.0
        ).scale(0.27).shift(UP*0.55)
        
        self.kzg_commitment = Text("KZG", color = HIGHLIGHT_COLOR, font = PRIMARY_FONT, font_size = 30).move_to(self.envelope.get_center())
        
        self.prover = ImageMobject("data/images/person_blue.png").scale(0.8).to_edge(LEFT).shift(UP*1+RIGHT)
        self.verifier = ImageMobject("data/images/person.png").scale(0.8).to_edge(RIGHT).shift(UP*1+LEFT)
        self.blob = (
            ImageMobject("data/images/blob.png")
            .scale(0.3)
            .next_to(self.chart_ec_continuous, LEFT + UP * 0.2, buff=0.1)
            .shift(LEFT * 0.8 + DOWN+UP*5)
        )
        self.blob.generate_target()
        self.blob.target.next_to(self.chart_ec_continuous, LEFT + UP * 0.2, buff=0.1).shift(LEFT * 2 + DOWN)
        
        self.chart_ec.shift(LEFT * 3)
        self.point_to_generator = self.chart_ec.get_point(FieldElement(4, 137))
        self.circle_gen = Circle(radius=0.15, color=SECONDARY_COLOR).move_to(
            self.point_to_generator.get_center()
        )
        self.point_to_generator_label = MathTex(
            r"{{G_1 \cdot k}}", color=SECONDARY_COLOR, font_size=32
        ).next_to(self.point_to_generator, RIGHT, buff=0.2)
        self.point_to_generator2 = self.chart_ec.get_point(FieldElement(51, 137))
        self.circle_gen2 = Circle(radius=0.15, color=PRIMARY_COLOR).move_to(
            self.point_to_generator2.get_center()
        )
        self.point_to_generator_label2 = MathTex(
            r"{{G_2 \cdot k'}}", color=PRIMARY_COLOR, font_size=32
        ).next_to(self.point_to_generator2, RIGHT, buff=0.2)
        self.chart_ec.shift(RIGHT * 3)
        
        self.pairings = MathTex(r"e({{G_1}}, {{G_2}}) \rightarrow {{G_T}}", color = PRIMARY_COLOR, font_size = 30).next_to(self.scalar_Fr, DOWN, buff = 1.0)
        self.cross_out_pairings = Line(LEFT, RIGHT, color = PRIMARY_COLOR, stroke_width = 2).scale(0.9).move_to(self.pairings.get_center())
        self.kzg = Text("KZG", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 30)
        self.cross_out_line = Line(LEFT, RIGHT, color = PRIMARY_COLOR, stroke_width = 2).scale(0.4).move_to(self.kzg.get_center())
        self.ipa = Text("Inner Product Argument", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 30).shift(RIGHT*3)
        self.ipa2 = Text("IPA", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 30).shift(RIGHT * 3)
        
        self.pairing_operation_bls = self.pairings.copy()
        self.pairing_operatio_bander = self.pairings.copy()
        self.line_cross_out_pairings = Line(LEFT, RIGHT, color = PRIMARY_COLOR, stroke_width = 2).move_to(self.pairing_operatio_bander.get_center())
        self.pairing_operatio_bander = VGroup(self.pairing_operatio_bander, self.line_cross_out_pairings)
        
        self.thumb_up = ImageMobject("data/images/Thumb_up.png").scale(0.3)
        
        self.kzg_ipa_table = TableKZGIPA()
        self.base_field_bander = MathTex(r"F_p' \sim 255 \ \mathrm{b}", font_size = 40).next_to(self.chart_bander, DOWN, buff = 0.5).shift(LEFT*1.5)
        self.scalar_field_bander = MathTex(r"F_r' \sim 253 \ \mathrm{b}", font_size = 40).next_to(self.base_field_bander, RIGHT, buff = 1.5)
        self.size_base_field_bander = Text("< 32 B", font_size = 25).next_to(self.base_field_bander, RIGHT, buff = 0.1)
        self.size_scalar_bander = self.size_base_field_bander.copy().next_to(self.scalar_field_bander, RIGHT, buff = 0.1)
        
        self.ipa_proof = MathTex(r"\pi \sim \log_2(n)", color = PRIMARY_COLOR, font_size = 30)
        self.ipa_commtiment = MathTex(r"C \sim {{a_1}} {{G_1}} + \cdots + {{a_n}} {{G_n}}", color = PRIMARY_COLOR, font_size = 30)
        
    def animate_in(self, scene):
        self.new_subsection(scene, "kzg commitment", "data/sound/e7/slide2-1.mp3")
        scene.play(Write(self.title_label), run_time=0.7)
        scene.play(Create(self.new_axes), run_time=1)
        scene.play(Create(self.polynomial_graph), run_time=1.5)
        scene.play(FadeIn(self.prover, self.verifier), run_time=1)
        scene.play(MoveToTarget(self.blob, rate_func = rate_functions.ease_out_bounce), run_time=1)
        scene.play(self.polynomial_chart.animate.set_opacity(0.3).scale(0.1).move_to(self.envelope.get_center()),
                           FadeIn(self.envelope, self.envelope_flap_closed), FadeOut(self.blob), run_time=1)
        scene.play(FadeOut(self.polynomial_chart), Write(self.kzg_commitment), run_time=0.5)
    
        self.new_subsection(scene, "BLS Fp Fr sizes", "data/sound/e7/slide2-2.mp3")
        scene.play(FadeOut(self.envelope_flap_closed, self.envelope, self.kzg_commitment, self.prover, self.verifier), run_time=1)
        self.chart_ec.gen_points()
        scene.play(Create(self.chart_ec), run_time=2)
        scene.wait(0.5)
        scene.play(ApplyWave(self.chart_ec.labels[0]), run_time=1.5)
        scene.play(ApplyWave(self.chart_ec.labels[1]), run_time=1.5)
        self.chart_ec.generate_target()
        self.chart_ec.target.shift(LEFT * 3)
        scene.wait(1)
        scene.play(MoveToTarget(self.chart_ec), run_time=1)
        scene.play(Write(self.base_field_bls), run_time=1)
        scene.wait(1.5)
        scene.play(Write(self.scalar_Fr), run_time=1)
        scene.wait(1.5)
        scene.play(Write(self.bytes_p2), run_time=1)
        scene.wait(2)
        scene.play(Write(self.bytes_of_el), run_time=1)
        scene.wait(1)
     
        self.new_subsection(scene, "subgroups G1 G2", "data/sound/e7/slide2-2a.mp3")
        scene.wait(1)
        scene.play(Create(self.circle_gen), run_time=1)
        scene.play(Write(self.point_to_generator_label), run_time=1)
        scene.wait(1)
        scene.play(Create(self.circle_gen2), run_time=1)
        scene.play(Write(self.point_to_generator_label2), run_time=1)
        scene.wait(1)
        scene.play(Write(self.pairings), run_time=1)
        scene.wait(1)
        
        self.new_subsection(scene, "not KZG - trusted setup, pairings", "data/sound/e7/slide2-3.mp3")
        scene.wait(1)
        scene.play(TransformMatchingShapes(self.title_label, self.title_label2, run_time=1.5))
        scene.wait(1)
        scene.play(Write(self.kzg))
        scene.wait(1)
        scene.play(Write(self.cross_out_line), run_time=1)
        scene.wait(0.6)
        scene.play(Write(self.cross_out_pairings), run_time=1)
        
        self.new_subsection(scene, "Pedersen commitments & Bandersnatch", "data/sound/e7/slide2-3a.mp3")
        self.base_field_bls.generate_target()
        self.base_field_bls.target.next_to(self.chart_ec, DOWN, buff = 0.5).shift(LEFT)
        self.scalar_Fr.generate_target()
        self.scalar_Fr.target.next_to(self.base_field_bls.target, RIGHT, buff = 0.5)
        scene.play(FadeOut(self.kzg, self.pairings, self.cross_out_line, self.cross_out_pairings, 
                           self.bytes_p2, self.bytes_of_el), MoveToTarget(self.base_field_bls), MoveToTarget(self.scalar_Fr), run_time=2)
        scene.play(Write(self.ipa), run_time=1)
        scene.wait(1)
        scene.play(TransformMatchingShapes(self.ipa, self.ipa2), run_time=1)
        scene.wait(1)
        self.ipa2.generate_target()
        self.ipa2.target.next_to(self.chart_bander, RIGHT, buff = 0.0)
        scene.play(MoveToTarget(self.ipa2), run_time=1)
        self.chart_bander.gen_points()
        scene.play(Create(self.chart_bander), run_time=1)

        self.new_subsection(scene, "Bandersnatch F p' Fr'", "data/sound/e7/slide2-4.mp3")
        scene.wait(1)
        scene.play(Indicate(self.scalar_Fr, color = SECONDARY_COLOR), run_time=1)
        scene.play(Write(self.base_field_bander), run_time=1)
        scene.wait(2)
        scene.play(Write(self.size_base_field_bander), run_time=1)
        scene.wait(1)
        
        self.new_subsection(scene, "many generators", "data/sound/e7/slide2-4a.mp3")
        self.animate_generators(scene)
        scene.wait(1)
        self.chart_bander.generate_target()
        self.chart_bander.target.scale(0.8).shift(UP*1.2)
        self.chart_whole = VGroup(self.chart_ec, self.point_to_generator_label2, self.point_to_generator_label,
                                 self.circle_gen2, self.circle_gen, self.base_field_bls, self.scalar_Fr)
        self.chart_whole.generate_target()
        self.chart_whole.target.scale(0.8).shift(UP*1.2)
        scene.play(MoveToTarget(self.chart_bander), MoveToTarget(self.chart_whole), run_time=1)
        scene.wait(1)
        self.ipa_commtiment.next_to(self.chart_bander, DOWN, buff = 1.0).shift(DOWN+LEFT * 1.5)
        scene.play(Write(self.ipa_commtiment), run_time=1)
        scene.wait(1)
        
        self.new_subsection(scene, "scalars 253 bit", "data/sound/e7/slide2-4b.mp3")
        scene.wait(1)
        self.scalar_field_bander.scale(0.8).next_to(self.chart_bander, DOWN, buff = 0.5).shift(LEFT * 1.5)
        self.size_scalar_bander.scale(0.8).next_to(self.scalar_field_bander, RIGHT, buff = 1.5)
        scene.play(Write(self.scalar_field_bander), run_time=1)
        scene.play(Write(self.size_scalar_bander), run_time=1)
        scene.wait(1)
        
        self.new_subsection(scene, "IPA proof log2(n)", "data/sound/e7/slide2-5.mp3")
        self.ipa_proof.next_to(self.ipa_commtiment, RIGHT, buff = 1.5)
        scene.play(Write(self.ipa_proof), run_time=1)
        scene.wait(1)
        
        
        self.new_subsection(scene, "sizes", "data/sound/e7/slide2-6.mp3")
        scene.wait(1)
        scene.play(FadeOut(self.base_field_bander, self.size_base_field_bander, 
                           self.scalar_field_bander, self.size_scalar_bander, self.chart_bander,
                           self.chart_ec, self.scalar_Fr, self.point_to_generator_label,
                           self.point_to_generator_label2, self.circle_gen, self.circle_gen2, 
                           self.bytes_of_el, self.bytes_p2, self.ipa_commtiment, self.ipa_proof), run_time=1)
        
        scene.play(Create(self.kzg_ipa_table), run_time=1)
        
        
        self.new_subsection(scene, "KZG commitment", "data/sound/e7/slide2-6a.mp3")
        
        self.new_subsection(scene, "IPA proof", "data/sound/e7/slide2-6b.mp3")
        
        self.new_subsection(scene, "openings", "data/sound/e7/slide2-6c.mp3")
        
        self.new_subsection(scene, "trusted setup", "data/sound/e7/slide2-6d.mp3")
       
       
       
    def animate_out(self, scene):
        scene.play(FadeOut(self.title_label, self.chart_bander, self.curve_ec_bander,
                           self.r, self.bytes_of_el, self.kzg, self.ipa2), run_time=0.5)

      
    def animate_polynomial(self):
        self.new_axes = Axes(
            x_range=[-0.5, 15.5, 1],
            y_range=[-3, 90, 30],
            x_length=7,
            axis_config={
                "include_numbers": True,
                "color": PRIMARY_COLOR,
                "decimal_number_config": {
                    "color": PRIMARY_COLOR,
                    "num_decimal_places": 0
                }
            }
        ).scale(0.7)
        
        # self.polynomial_graph = self.new_axes.plot_implicit_curve(lambda x, y: (4.26713027e-09 * x ** (15) 
        #                                                           -5.00493029e-07 * x ** (14) +  2.67032132e-05 * x ** (13) 
        #                                                           -8.57314665e-04* x ** (12) +1.84604634e-02 * x ** (11) 
        #                                                           -2.81249901e-01* x ** (10) +  3.11615153e+00 * x ** (9) 
        #                                                           -2.54062977e+01 * x ** (8) +1.52442624e+02 * x ** (7) 
        #                                                           -6.66027523e+02 * x ** (6) +  2.07111066e+03 * x ** (5) 
        #                                                           -4.40664678e+03 * x ** (4) +5.99848486e+03 * x ** (3) 
        #                                                           -4.60965478e+03 * x ** (2) + 1.47784469e+03 * x ** (1)
        #                                                           + 7.99999698e+00 * x ** (0))*0.3 - y, color=SECONDARY_COLOR)
        
        self.polynomial_graph = self.new_axes.plot_implicit_curve(lambda x, y: (-0.013005328649673187  * x ** (4) + 0.44002953745582507 * x ** (3) 
                                                                  -4.368305697782954 * x ** (2) + 15.731787164922928 * x ** (1)
                                                                  +4.2790892673006296 * x ** (0)) - y, color=SECONDARY_COLOR)
        self.polynomial_chart = VGroup(self.new_axes, self.polynomial_graph)
        
        
        
    def animate_generators(self, scene):
        self.point_to_generator3 = self.chart_bander.get_point(FieldElement(3, 137))
        self.circle_gen3 = Circle(radius=0.15, color=PRIMARY_COLOR).move_to(
            self.point_to_generator3.get_center()
        )
        self.point_to_generator4 = self.chart_bander.get_point(FieldElement(14, 137))
        self.circle_gen4 = Circle(radius=0.15, color=PRIMARY_COLOR).move_to(
            self.point_to_generator4.get_center()
        )
        self.point_to_generator5 = self.chart_bander.get_point(FieldElement(43, 137))
        self.circle_gen5 = Circle(radius=0.15, color=PRIMARY_COLOR).move_to(
            self.point_to_generator5.get_center()
        )
        self.commitment_ipa = Text("C(IPA)", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 25).next_to(self.circle_gen5, RIGHT, buff =0.1)
        
        self.point_to_generator6 = self.chart_bander.get_point(FieldElement(61, 137))
        self.circle_gen6 = Circle(radius=0.15, color=PRIMARY_COLOR).move_to(
            self.point_to_generator6.get_center()
        )
        self.point_to_generator7 = self.chart_bander.get_point(FieldElement(86, 137))
        self.circle_gen7 = Circle(radius=0.15, color=PRIMARY_COLOR).move_to(
            self.point_to_generator7.get_center()
        )
        self.point_to_generator8 = self.chart_bander.get_point(FieldElement(113, 137))
        self.circle_gen8 = Circle(radius=0.15, color=PRIMARY_COLOR).move_to(
            self.point_to_generator8.get_center()
        )
        circles = [self.circle_gen3, self.circle_gen4, self.circle_gen5, self.circle_gen6, self.circle_gen7, self.circle_gen8]
        for i in range(6):
            if i != 0:
                scene.play(Create(circles[i]), FadeOut(circles[i-1]), run_time=0.2)
            else:
                scene.play(Create(circles[i]), run_time=0.2)
        scene.play(FadeOut(circles[5]))
        scene.wait(2)
        scene.play(Create(self.circle_gen5), run_time=0.8)
        scene.play(Write(self.commitment_ipa), run_time=0.8)
        scene.wait(1)
        scene.play(Indicate(self.commitment_ipa, color=SECONDARY_COLOR), run_time=1)
        scene.wait(1)
        scene.play(FadeOut(self.circle_gen5, self.commitment_ipa), run_time=0.5)



        