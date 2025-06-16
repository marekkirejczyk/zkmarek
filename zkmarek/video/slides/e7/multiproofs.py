from manim import (Text, UP, DOWN, RIGHT, LEFT, FadeOut, Write, MathTex, TransformMatchingShapes, VGroup,
                   Axes, RoundedRectangle, FadeIn, ValueTracker, Indicate, MoveToTarget, Line, ImageMobject,
                   CurvedArrow, StealthTip, Arrow, Group)
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR, HIGHLIGHT_COLOR
from zkmarek.video.mobjects.dot_on_curve import DotOnCurve
from zkmarek.video.slides.e7.curve import Curve
from zkmarek.video.slides.e7.proofs import Proofs

class Multiproofs(SlideBase):
    def __init__(self):
        super().__init__("Multiproofs")
        
    def construct(self):
        self.title_label = Text("Multiproofs", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 40).to_edge(UP)
        
        self.pi0 = MathTex(r"\pi^0", color=PRIMARY_COLOR, font_size=45).shift(LEFT*2)
        self.pi1 = MathTex(r"\pi^1", color=PRIMARY_COLOR, font_size=45)
        self.pi2 = MathTex(r"\pi^2", color=PRIMARY_COLOR, font_size=45).shift(RIGHT*2)
        
        self.all_pis = MathTex(r"\pi", color = PRIMARY_COLOR, font_size = 50).shift(RIGHT*2.5+DOWN*1.2)
        
        vector = [r"a_0", r"a_1", r"a_2", r"a_3", r"a_4", r"a_5", r"a_6", r"a_7",
                 r"a_8", r"a_9", r"a_{10}", r"a_{11}", r"a_{12}", r"a_{13}", r"a_{14}", r"a_{15}"]
        self.vector = VGroup(*[MathTex(i, color = PRIMARY_COLOR, font_size = 30) for i in vector]).arrange(RIGHT, buff=0.1)
        rectangle = RoundedRectangle(height = 1, width = 1, corner_radius=0.05, color=HIGHLIGHT_COLOR, fill_opacity=0.2, stroke_width = 0.0).scale(0.5).set_color(HIGHLIGHT_COLOR)
        rectangles_of_values = [rectangle.copy() for _ in range(16)]
        self.rectangles_values = VGroup(*rectangles_of_values).arrange(RIGHT, buff=0.2).shift(DOWN*1.5)
        for i in range(16):
            self.vector[i].move_to(self.rectangles_values[i].get_center())
        
        self.commtiment_C = MathTex(r"C_0^0", color=PRIMARY_COLOR, font_size=40).shift(UP*1.5)
    
        self.opening1 = MathTex(r"p_0({6})=a_{6}", color = PRIMARY_COLOR, font_size=35)
        self.opening = MathTex(r"p_i({x_i})=a_i", color = PRIMARY_COLOR, font_size=35)
        
        self.new_polynomial = MathTex(r"{{r(x)}} = {{p(x)}}-{{a_i}} {{}}", color = PRIMARY_COLOR, font_size=35).shift(RIGHT * 2.5+UP*0.5)
        self.new_polynomial2 = MathTex(r"r({{x_i}}) = {{p(x_i)}}-{{a_i}}={{0}}", color = PRIMARY_COLOR, font_size=35).shift(RIGHT * 2.5+UP*0.5)
        self.new_polynomial3 = MathTex(r"{{r(x)}} = {{(x-x_i)}}{{(...)}}", color = PRIMARY_COLOR, font_size=35).shift(RIGHT * 2.5+UP*0.5)
        self.new_polynomial4 = MathTex(r"{{r(x)}} = {{(x-x_i)}}{{(q(x))}}", color = PRIMARY_COLOR, font_size=35).shift(RIGHT * 2.5+UP*0.5)
        self.quotient = MathTex(r"\frac{r(x)}{(x-x_i)} = q(x)", color = PRIMARY_COLOR, font_size=35).shift(RIGHT * 2.5+UP*0.5)
        self.quotient2 = MathTex(r"q(x) = \frac{r(x)}{(x-x_i)}", color = PRIMARY_COLOR, font_size=35).shift(RIGHT * 2.5+UP*0.5)
        self.quotient3 = MathTex(r"q(x) = \frac{p(x)-a_i}{(x-x_i)}", color = PRIMARY_COLOR, font_size=35).shift(RIGHT * 2.5+UP*0.5)
        
        ## prover query
        self.prover = ImageMobject("data/images/person_blue.png").scale(0.5).shift(LEFT * 2.5 + UP * 2)
        self.commitment1 = MathTex(r"{{C_0^0}} \ \rightarrow p_0(x),", color=PRIMARY_COLOR, font_size=40).next_to(self.prover, RIGHT, buff=0.3)
        self.commitment2 = MathTex(r"{{C_0^1}} \ \rightarrow p_1(x),", color=HIGHLIGHT_COLOR, font_size=40).next_to(self.commitment1, DOWN, buff=0.3)
        self.commitment3 = MathTex(r"{{C_0^2}} \ \rightarrow p_2(x),", color=SECONDARY_COLOR, font_size=40).next_to(self.commitment2, DOWN, buff=0.3)
        self.opening_1 = MathTex(r"p_0({{x_0}}) - {{a_0}}=0", color=PRIMARY_COLOR, font_size=35).next_to(self.commitment1, RIGHT, buff=0.3)
        self.opening_2 = MathTex(r"p_1({{x_1}}) - {{a_1}}=0", color=HIGHLIGHT_COLOR, font_size=35).next_to(self.commitment2, RIGHT, buff=0.3)
        self.opening_3 = MathTex(r"p_2({{x_2}}) - {{a_2}}=0", color=SECONDARY_COLOR, font_size=35).next_to(self.commitment3, RIGHT, buff=0.3)
        self.bg_image_prover = RoundedRectangle(corner_radius=0.15, width = 6, height = 3, fill_opacity=0.2, color=HIGHLIGHT_COLOR, stroke_width=0.0).move_to(self.commitment2.get_center()).shift(RIGHT*1.5)
        
        self.quotient_g = MathTex(
            r"g(x) = {{r^0}} \cdot {{\frac{p_0(x)-a_0}{x - x_0}}} + {{r^1}} \cdot {{\frac{p_1(x)-a_1}{x - x_1}}} + {{r^2}} \cdot {{\frac{p_2(x)-a_2}{x - x_2}}}",
            color=PRIMARY_COLOR,
            font_size=35
        ).shift(DOWN*1.5)
        self.quotient_g2 = MathTex(
            r"g(s) = {{r^0}} \cdot {{\frac{p_0(s)-a_0}{s - x_0}}} + {{r^1}} \cdot {{\frac{p_1(s)-a_1}{s - x_1}}} + {{r^2}} \cdot {{\frac{p_2(s)-a_2}{s - x_2}}}",
            color=PRIMARY_COLOR,
            font_size=35
        ).shift(DOWN*1.5)
        self.prover.shift(DOWN)

        self.quotient_g[3].set_color(PRIMARY_COLOR)
        self.quotient_g[7].set_color(HIGHLIGHT_COLOR)
        self.quotient_g[11].set_color(SECONDARY_COLOR)
        
        self.powers_of_r = MathTex(r"r\sim \texttt{hash}({{C_0^0}}, {{C_0^1}}, {{C_0^2}}, {{x_0}}, {{x_1}}, {{x_2}}, {{a_0}}, {{a_1}}, {{a_2}})", color = PRIMARY_COLOR, font_size = 35).next_to(self.quotient_g, DOWN, buff = 0.5)
        self.powers_of_r[1].set_color(PRIMARY_COLOR)
        self.powers_of_r[3].set_color(HIGHLIGHT_COLOR)
        self.powers_of_r[5].set_color(SECONDARY_COLOR)
        self.powers_of_r[7].set_color(PRIMARY_COLOR)
        self.powers_of_r[9].set_color(HIGHLIGHT_COLOR)
        self.powers_of_r[11].set_color(SECONDARY_COLOR)
        self.powers_of_r[13].set_color(PRIMARY_COLOR)
        self.powers_of_r[15].set_color(HIGHLIGHT_COLOR)
        self.powers_of_r[17].set_color(SECONDARY_COLOR)
        self.opening.shift(RIGHT * 4.5+UP*1.5)
        self.curved_arrow_proof = CurvedArrow(self.quotient3.get_right(), self.opening.get_right()+LEFT * 2+RIGHT*0.2, stroke_width=1.6, 
                                                tip_shape=StealthTip, color=PRIMARY_COLOR)
        self.proof_label_arrow = Text("quotient corresponding \n       to the opening", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 18).next_to(self.curved_arrow_proof, RIGHT, buff = 0.1)
        
        self.random_t = MathTex(r"s\sim \texttt{hash(...)}", color = PRIMARY_COLOR, font_size = 30).next_to(self.quotient_g, DOWN, buff = 0.5)
        
        self.proof_to_g = MathTex(r"\pi", color = PRIMARY_COLOR, font_size = 40).next_to(self.quotient_g2, DOWN, buff = 0.5)
        self.arrow_proof_to_g = Arrow(self.quotient_g2.get_bottom(), self.proof_to_g.get_top(),
                                      tip_shape=StealthTip, stroke_width=2,
                                      max_tip_length_to_length_ratio=0.15).set_color_by_gradient([PRIMARY_COLOR, HIGHLIGHT_COLOR])
        self.proofs = Proofs()
        self.proofs.construct()
        self.tree = self.proofs.tree
        self.tree.scale(0.7).shift(LEFT * 3)
        self.verify_func = MathTex(r"\texttt{VerkleProof}({{\pi^0}}, {{\pi^1}}, {{\pi^2}}, {{C^0_0}}, {{C_0^1}})", color = PRIMARY_COLOR, font_size = 35).shift(RIGHT * 2+UP*1.5)
        
        self.commitment_D_aggregate = MathTex(r"D", color=PRIMARY_COLOR, font_size=40).next_to(self.all_pis, UP, buff =1.)
        self.arrow_D_pi = Arrow(self.commitment_D_aggregate.get_bottom(), self.all_pis.get_top(), tip_shape = StealthTip, max_tip_length_to_length_ratio=0.3, max_stroke_width_to_length_ratio=0.5).set_color(PRIMARY_COLOR)
        
        self.indices = VGroup(*[Text(str(i), font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=30) for i in range(16)]).arrange(RIGHT, buff = 0.42).next_to(self.vector, DOWN, buff = 0.2).shift(1.3 * DOWN)
        
        self.opening__0 = MathTex(r"p_0({x_0})=a_0", color=SECONDARY_COLOR, font_size=35).next_to(self.opening, DOWN, buff=0.5)
        self.opening__1 = MathTex(r"p_1({x_{0}})=\texttt{hash}(C_0^0)", color=SECONDARY_COLOR, font_size=35).next_to(self.opening__0, DOWN, buff=0.5)
        self.opening__2 = MathTex(r"p_2({x_{0}})=\texttt{hash}(C_0^1)", color=SECONDARY_COLOR, font_size=35).next_to(self.opening__1, DOWN, buff=0.5)
        
    def animate_in(self, scene):
        self.new_subsection(scene, "VP: three proofs, three commitments", "data/sound/e7/slide6-1.mp3")
        scene.play(Write(self.title_label))
        scene.wait(1)
        scene.play(FadeIn(self.tree), run_time=1)
        scene.play(Write(self.verify_func), run_time=1)
        scene.wait(1)
        scene.play(Indicate(self.verify_func[1:6], scale_factor=1.3), run_time=1)
        scene.play(Indicate(self.verify_func[7:9], scale_factor=1.3), run_time=1)
        
        self.new_subsection(scene, "multiproof: commitment D, commitments path", "data/sound/e7/slide6-1a.mp3")
        scene.play(FadeIn(self.all_pis), run_time=1)
        scene.wait(1.5)
        scene.play(self.tree[2][0].animate.set_color(PRIMARY_COLOR),
                   Indicate(self.tree[2][0]), run_time=1)
        scene.play(self.tree[1][0].animate.set_color(PRIMARY_COLOR),
                   Indicate(self.tree[1][0]), run_time=1)
        scene.play(self.tree[0][0].animate.set_color(PRIMARY_COLOR),
                   Indicate(self.tree[0][0]), run_time=1)
        scene.play(TransformMatchingShapes(self.verify_func[7:].copy(), self.commitment_D_aggregate), run_time=1)
        scene.play(Write(self.arrow_D_pi), run_time=1)
        
        self.new_subsection(scene, "how?", "data/sound/e7/slide6-1b.mp3")
        scene.wait(1.5)
        scene.play(FadeOut(self.tree, self.verify_func, self.arrow_D_pi, self.all_pis, self.commitment_D_aggregate), run_time=1)
        
        self.new_subsection(scene, "data vector: polynomial", "data/sound/e7/slide6-2.mp3")
        scene.play(FadeIn(self.commtiment_C), run_time=1)
        scene.wait(0.5)
        scene.play(Write(self.vector), run_time=1)
        scene.play(Write(self.rectangles_values), run_time=1)
        scene.play(self.vector.animate.shift(DOWN*1.3), self.rectangles_values.animate.shift(DOWN * 1.3), run_time=1)
        self.animate_polynomial()
        scene.play(FadeIn(self.polynomial_chart), run_time=1)
        scene.wait(1)
        
        self.new_subsection(scene, "opening p(xi)=ai", "data/sound/e7/slide6-3.mp3")
        self.opening1.shift(RIGHT * 4.5+UP*1.5)
        for i in range(6):
            scene.play(Indicate(self.vector[i]), run_time=0.3)
        scene.play(self.vector[6].animate.set_color(SECONDARY_COLOR), run_time=1)
        scene.play(Indicate(self.vector[6], scale_factor=1.5), run_time=1)
        scene.wait(1)
        self.opening.move_to(self.opening1.get_center())
        scene.play(FadeIn(self.dots[6], self.line_ai), Write(self.opening), run_time=1)
        scene.wait(3)
        scene.play(Indicate(self.new_axes[0]))
        scene.play(Indicate(self.indices))
        
        scene.play(self.polynomial_chart.animate.shift(LEFT * 2),
                   self.commtiment_C.animate.shift(LEFT * 2),
                   self.dots[6].animate.shift(LEFT *2),
                   self.line_ai.animate.shift(LEFT * 2), run_time=1)
        scene.play(self.opening.animate.shift(LEFT * 1.5), run_time=1)
        scene.play(Write(self.opening__0), run_time=1)
        scene.play(Write(self.opening__1), run_time=1)
        scene.play(Write(self.opening__2), run_time=1)
        scene.wait(1.5)
        
        scene.play(FadeOut(self.vector, self.rectangles_values, self.indices,
                           self.opening__0, self.opening__1, self.opening__2), run_time=1)
        
        self.new_subsection(scene, "p(xi)-ai=0", "data/sound/e7/slide6-4.mp3")
        scene.play(Write(self.new_polynomial), run_time=1)
        scene.wait(0.5)
        self.polynomial_graph.generate_target()
        self.polynomial_graph.target.shift(DOWN * 0.65)
        scene.play(MoveToTarget(self.polynomial_graph), run_time=1)
        scene.play(FadeOut(self.dots[6], self.line_ai), run_time=1)
        
        self.new_subsection(scene, "root x=xi", "data/sound/e7/slide6-5.mp3")
        scene.play(TransformMatchingShapes(self.new_polynomial, self.new_polynomial2), run_time=1)
        scene.wait(1.5)
        scene.play(Indicate(self.new_polynomial2[1], scale_factor=1.2), run_time=1)
        
        self.new_subsection(scene, "factored form", "data/sound/e7/slide6-6.mp3")
        scene.wait(1)
        scene.play(TransformMatchingShapes(self.new_polynomial2, self.new_polynomial3), run_time=2)
        scene.wait(1)
        scene.play(TransformMatchingShapes(self.new_polynomial3, self.new_polynomial4), run_time=1)
        
        self.new_subsection(scene, "quotient poly", "data/sound/e7/slide6-7.mp3")
        scene.play(Indicate(self.new_polynomial4[3]), run_time=1)
        scene.wait(1)
        scene.play(TransformMatchingShapes(self.new_polynomial4, self.quotient), run_time=1)
        scene.wait(1)
        scene.play(TransformMatchingShapes(self.quotient, self.quotient2), run_time=1)
        
        self.new_subsection(scene, "divide x-xi", "data/sound/e7/slide6-8.mp3")
        scene.wait(1)
        scene.play(TransformMatchingShapes(self.quotient2, self.quotient3), run_time=1)
        scene.wait(2)
        scene.play(Write(self.curved_arrow_proof), run_time=1)
        scene.play(Write(self.proof_label_arrow), run_time=1)
        scene.wait(2)
        
        self.new_subsection(scene, "multiproofs", "data/sound/e7/slide6-9.mp3")
        scene.play(FadeOut(self.polynomial_chart, self.curved_arrow_proof, self.proof_label_arrow, self.commtiment_C, self.quotient3, self.opening), run_time=2)
        
        self.new_subsection(scene, "3 proofs, 3 openings, 3 commitments", "data/sound/e7/slide6-10.mp3")
        scene.play(FadeIn(self.prover, self.bg_image_prover), run_time=1)
        scene.play(Write(self.opening_1), run_time=0.4)
        scene.play(Write(self.opening_2), run_time=0.4)
        scene.play(Write(self.opening_3), run_time=0.4)
        scene.wait(1)
        scene.play(Write(self.commitment1), run_time=0.4)
        scene.play(Write(self.commitment2), run_time=0.4)
        scene.play(Write(self.commitment3), run_time=0.4)
        scene.wait(1)
        scene.play(FadeIn(self.quotient_g[3]), run_time=1)
        scene.play(FadeIn(self.quotient_g[7]), run_time=1)
        scene.play(FadeIn(self.quotient_g[11]), run_time=1)
        
        self.new_subsection(scene, "random linear combinations", "data/sound/e7/slide6-11.mp3")
        scene.play(FadeIn(self.quotient_g[0:3], self.quotient_g[4:7], self.quotient_g[8:11], self.quotient3[12:]), run_time=1)
        scene.wait(1)
        scene.play(Indicate(self.quotient_g[1], scale_factor=1.3), run_time=0.5)
        scene.play(Indicate(self.quotient_g[5], scale_factor=1.3), run_time=0.5)
        scene.play(Indicate(self.quotient_g[9], scale_factor=1.3), run_time=0.5)
        scene.play(FadeIn(self.powers_of_r), run_time=1)
        scene.wait(2)
        scene.play(Indicate(self.quotient_g[0], scale_factor=1.3), run_time=1)
        
        self.new_subsection(scene, "commitment D", "data/sound/e7/slide6-12.mp3")
        scene.wait(1.5)
        scene.play(Indicate(self.quotient_g, scale_factor=1.3), run_time=1)
        scene.wait(1)
        scene.play(FadeOut(self.powers_of_r), run_time=1)
        scene.wait(1)
        commitment_D = MathTex(r"D = \texttt{commit}({{g}})", color=PRIMARY_COLOR, font_size=35).next_to(self.quotient_g, DOWN, buff=0.5)
        scene.play(FadeIn(commitment_D), run_time=1)
        
        self.new_subsection(scene, "g(s)", "data/sound/e7/slide6-13.mp3")
        scene.wait(2)
        scene.play(TransformMatchingShapes(self.quotient_g, self.quotient_g2), run_time=1)
        scene.play(commitment_D.animate.shift(LEFT * 2.5))
        scene.play(FadeIn(self.random_t), run_time=1)
        scene.wait(1)
        
        self.new_subsection(scene, "pi - multiproof", "data/sound/e7/slide6-14.mp3")
        scene.play(FadeOut(self.random_t))
        scene.play(Write(self.proof_to_g), run_time=1)
        scene.play(FadeIn(self.arrow_proof_to_g), run_time=1)
        scene.wait(2)
        
        self.new_subsection(scene, "verify only once", "data/sound/e7/slide6-15.mp3")
        scene.wait(9)
        self.all_terms = Group(self.bg_image_prover, self.prover, self.commitment1, commitment_D, self.commitment2,
                               self.commitment3, self.opening_1, self.opening_2, self.opening_3,
                                self.quotient_g2, self.proof_to_g, self.arrow_proof_to_g)
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.title_label, self.all_terms))
    
    def animate_polynomial(self):
        self.new_axes = Axes(
            x_range=[-0.5, 15.5, 1],
            y_range=[-3, 90, 500],
            x_length=7,
            axis_config={
                "include_numbers": True,
                "color": PRIMARY_COLOR,
                "decimal_number_config": {
                    "color": PRIMARY_COLOR,
                    "num_decimal_places": 0
                }
            }
        ).scale(0.5)
        
        self.polynomial_graph = self.new_axes.plot_implicit_curve(lambda x, y: (-0.013005328649673187  * x ** (4) + 0.44002953745582507 * x ** (3) 
                                                                  -4.368305697782954 * x ** (2) + 15.731787164922928 * x ** (1)
                                                                  +4.2790892673006296 * x ** (0)) - y, color=SECONDARY_COLOR)
        self.polynomial_chart = VGroup(self.new_axes, self.polynomial_graph).shift(DOWN * 0.5)
        values = [
            (0, 4), (1, 16), (2, 22), (3, 23), (4, 22), (5, 20), (6, 20), (7, 20),
            (8, 22), (9, 28), (10, 35), (11, 45), (12, 55), (13, 66), (14, 76), (15, 85)
        ]
        self.dots = VGroup()
        for i, (x, y) in enumerate(values):
            tracker = ValueTracker(x)
            curve = Curve.from_x(tracker.get_value())
            dot = DotOnCurve(self.new_axes, f"({{{x}}}, {{{y}}})", curve).dot
            self.dots.add(dot)
            
        self.line_ai = Line(self.dots[6].get_center(), self.new_axes.c2p(6, 0), color=SECONDARY_COLOR, stroke_width=2)
    