from manim import (FadeIn, FadeOut, Indicate, MoveToTarget, Write, Create, Text, Group,
                   MathTex, UP, RoundedRectangle, VGroup, RIGHT, DOWN, Axes, LEFT, ValueTracker,
                   ImageMobject, Polygon, Arrow, StealthTip, rate_functions, TransformMatchingShapes, DashedVMobject)
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, HIGHLIGHT_COLOR, SECONDARY_COLOR
from zkmarek.video.slides.e7.curve import Curve
from zkmarek.video.mobjects.dot_on_curve import DotOnCurve

class SingleLevelVerkleTree(SlideBase):
    def __init__(self) -> None:
        super().__init__("Single level Verkle tree")
        
    def construct(self):
        self.title_label = Text("Simple Verkle tree", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size=40).to_edge(UP)
        
        sixteen_element_vector = [4, 16, 22, 24, 22, 19, 20, 20, 22, 28, 35, 45, 55, 65, 75, 85]
        vector = [r"a_0", r"a_1", r"a_2", r"a_3", r"a_4", r"a_5", r"a_6", r"a_7",
                 r"a_8", r"a_9", r"a_{10}", r"a_{11}", r"a_{12}", r"a_{13}", r"a_{14}", r"a_{15}"]
        self.vector = VGroup(*[MathTex(i, color = PRIMARY_COLOR, font_size = 30) for i in vector]).arrange(RIGHT, buff=0.1)
        self.sixteen_element_vector = VGroup(*[Text(str(i), color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 30) for i in sixteen_element_vector]).arrange(RIGHT, buff=0.1)
        rectangle = RoundedRectangle(height = 1, width = 1, corner_radius=0.05, color=SECONDARY_COLOR, fill_opacity=0.3, stroke_width = 0.0).scale(0.5).move_to(self.sixteen_element_vector.get_center()).set_color(HIGHLIGHT_COLOR)
        rectangles_of_values = [rectangle.copy() for _ in range(16)]
        self.rectangles_values = VGroup(*rectangles_of_values).arrange(RIGHT, buff=0.2)
        for i in range(16):
            self.sixteen_element_vector[i].move_to(self.rectangles_values[i].get_center())
            self.vector[i].move_to(self.rectangles_values[i].get_center())
            
    
        rectangle = RoundedRectangle(height = 1, width = 1, corner_radius=0.05, color=SECONDARY_COLOR, fill_opacity=0.3, stroke_width = 0.0).scale(0.5).move_to(self.sixteen_element_vector.get_center()).set_color(HIGHLIGHT_COLOR)
        self.formula = MathTex(r"a_{15}\cdot {{x^{15}}} + a_{14}\cdot {{x^{14}}} + \cdots {{a_{0}}}]", color = PRIMARY_COLOR, font_size = 20).shift(RIGHT*2+DOWN*1.5)
        self.animate_polynomial()
        values = [
            (0, 4), (1, 16), (2, 22), (3, 23), (4, 22), (5, 20), (6, 20), (7, 20),
            (8, 22), (9, 28), (10, 35), (11, 45), (12, 55), (13, 66), (14, 76), (15, 85)
        ]
        self.dots = []
        for i, (x, y) in enumerate(values):
            tracker = ValueTracker(x)
            curve = Curve.from_x(tracker.get_value())
            dot = DotOnCurve(self.new_axes, f"({{{x}}}, {{{y}}})", curve).dot
            self.dots.append(dot)
    
        self.vector_values = VGroup(self.sixteen_element_vector, self.rectangles_values)
        
        self.envelope = RoundedRectangle(width = 8, height = 3, 
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
        self.envelope.shift(DOWN * 0.7)
        self.envelope_flap_closed.next_to(self.envelope, UP, buff=-0.48).shift(DOWN*0.25)

        
        self.commitment = MathTex(r"\texttt{commitment}\ C^0", color = HIGHLIGHT_COLOR, font_size = 28).move_to(self.envelope.get_center())
        
        self.verifier1 = ImageMobject("data/images/person_new.png").scale(0.7).to_edge(RIGHT).shift(UP*1.5+LEFT)
        self.verifier_label = Text("verification function", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 27).next_to(self.verifier1, DOWN, buff = 0.1)
        self.verifier_label2 = Text("Verifier", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 27).next_to(self.verifier1, UP, buff = 0.1)
        self.verifier = Group(self.verifier1, self.verifier_label)
        self.prover1 = ImageMobject("data/images/person_new2.png").scale(0.7).shift(UP*1.5)
        self.prover_label = Text("Prover", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 27).next_to(self.prover1, UP, buff = 0.1)
        self.prover_label2 = Text("insert function", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 27).next_to(self.prover1, DOWN, buff = 0.1)
        
        self.proof_pi = MathTex(r"{{\pi^0}}", color = HIGHLIGHT_COLOR, font_size = 50).next_to(self.prover1, LEFT, buff = 0.1)
        self.proof = Text("proof", color = HIGHLIGHT_COLOR, font_size = 25, font=PRIMARY_FONT).next_to(self.proof_pi, LEFT, buff = 0.1).shift(DOWN * 0.1)
        self.proof = VGroup(self.proof, self.proof_pi)
        self.opening = MathTex(r"{{a_{12} }} = 55", color = PRIMARY_COLOR, font_size = 40).next_to(self.proof, DOWN, buff = 0.3)
        self.opening2 = MathTex(r"{{a_{2044} }} = 55", color = PRIMARY_COLOR, font_size = 40).next_to(self.verifier, DOWN, buff = 1.0)
        self.opening3 = MathTex(r"{{a_{252} }} = 55", color = PRIMARY_COLOR, font_size = 40).next_to(self.verifier, DOWN, buff = 1.0)
        self.elliptic_curve_point = Text("1 EC point", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 30).next_to(self.envelope, UP, buff = 0.8)
        
        self.dots2048 = Text("...", color = SECONDARY_COLOR, font = PRIMARY_FONT, font_size = 40)
        indeces = [0, 1, 2, 3, 4, 2043, 2044, 2045, 2046, 2047]
        self.indeces = VGroup(*[Text(str(i), color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 17) for i in indeces]).arrange(RIGHT, buff=0.1)
        indeces256 = [0, 1, 2, 3, 4, 251, 252, 253, 254, 255]
        self.indeces256 = VGroup(*[Text(str(i), color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 17) for i in indeces256]).arrange(RIGHT, buff=0.1)

    def animate_in(self, scene):
        self.new_subsection(scene, "16 element vector", "data/sound/e7/slide3-1.mp3")
        scene.play(Create(self.title_label), run_time=1.0)
        self.rectangles_values.next_to(self.prover1, DOWN, buff=0.3)
        for i in range(16):
            self.vector[i].move_to(self.rectangles_values[i].get_center())
            self.sixteen_element_vector[i].move_to(self.rectangles_values[i].get_center())
            
        scene.play(Create(self.rectangles_values), run_time=1.0)
        scene.play(Write(self.vector), run_time=1.0)
        scene.wait(1)
        scene.play(FadeOut(self.vector), FadeIn(self.sixteen_element_vector), run_time=1.0)
        
        
        self.new_subsection(scene, "insert function", "data/sound/e7/slide3-1a.mp3")
        self.vector_values.generate_target()
        self.vector_values.target.shift(DOWN*2.5)
        scene.play(MoveToTarget(self.vector_values), run_time=1.0)
        scene.play(FadeIn(self.prover1), Write(self.prover_label2), run_time=1)
        scene.play(Indicate(self.vector_values, color = PRIMARY_COLOR), run_time=1)
        scene.wait(0.5)
        scene.play(Write(self.prover_label), run_time=1)
        scene.wait(0.5)
        self.prover = Group(self.prover1, self.prover_label, self.prover_label2)
        sixteen_element_vector2 = [4, 16, 22, 24, 22, 19, 20, 20, 22, 5, 35, 45, 55, 65, 75, 85]
        self.sixteen_element_vector2 = VGroup(*[Text(str(i), color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 30) for i in sixteen_element_vector2]).arrange(RIGHT, buff=0.1)
        for i in range(16):
            self.sixteen_element_vector2[i].move_to(self.rectangles_values[i].get_center())
        scene.wait(0.2)
        scene.play(Indicate(self.prover, color = PRIMARY_COLOR), run_time=1)
        scene.wait(0.5)
        scene.play(self.sixteen_element_vector[9].animate.set_opacity(0.0), FadeIn(self.sixteen_element_vector2[9]),
                   Indicate(self.rectangles_values[9]), run_time=1)
        scene.wait(1)
        scene.play(self.sixteen_element_vector[9].animate.set_opacity(1.0), FadeOut(self.sixteen_element_vector2[9]), run_time=1)
        
        self.prover.generate_target()
        self.prover.target.to_edge(LEFT).shift(RIGHT)
        scene.play(MoveToTarget(self.prover), run_time=1)
        scene.play(FadeIn(self.envelope, self.envelope_flap_closed), run_time=0.8)
        scene.play(Create(self.commitment))
        
        self.arrows = []
        for i in range(16):
            self.create_arrow(self.envelope, self.rectangles_values[i], where_to_append=self.arrows)
            
        for i in range(16):
            scene.play(Create(self.arrows[i]), run_time=0.05)
        
        
        self.new_subsection(scene, "function that verifies", "data/sound/e7/slide3-1b.mp3")
        scene.wait(1.5)
        scene.play(FadeIn(self.verifier), run_time=0.7)
        scene.wait(1.5)
        scene.play(Indicate(self.rectangles_values[6], color = PRIMARY_COLOR),
                   Indicate(self.sixteen_element_vector[6], color = PRIMARY_COLOR), run_time=0.9)
        scene.play(Indicate(self.rectangles_values, color = HIGHLIGHT_COLOR),
                   Indicate(self.sixteen_element_vector, color = HIGHLIGHT_COLOR), run_time=0.9)
        scene.play(Write(self.verifier_label2), run_time=1.0)
        self.verifier.add(self.verifier_label2)
        scene.wait(3.5)
        
        scene.play(Write(self.proof), run_time=0.7)
        scene.wait(1)
        scene.play(Write(self.opening), run_time=0.7)
        scene.wait(1)
        self.proof.generate_target()
        self.proof.target.next_to(self.verifier, DOWN, buff = 0.3)
        self.opening.generate_target()
        self.opening.target.next_to(self.proof.target, DOWN, buff = 0.3)
        scene.play(MoveToTarget(self.proof), MoveToTarget(self.opening), run_time=1)
    
        self.new_subsection(scene, "ec points", "data/sound/e7/slide3-2.mp3")
        scene.wait(0.5)
        self.commitment_whole = VGroup(self.envelope, self.envelope_flap_closed, self.commitment)
        scene.play(Indicate(self.commitment_whole, color = HIGHLIGHT_COLOR), run_time=1.)
        scene.wait(0.5)
        scene.play(Write(self.elliptic_curve_point), run_time=0.5)
        scene.wait(1)
        scene.play(FadeOut(self.elliptic_curve_point), run_time=0.5)
        
        
        self.new_subsection(scene, "16->2048", "data/sound/e7/slide3-3.mp3")
        scene.wait(1)
        scene.play(Indicate(self.commitment_whole, color = SECONDARY_COLOR), run_time=0.9)

        for i in range(16):
            scene.play(Indicate(self.rectangles_values[i], color = SECONDARY_COLOR),
                       Indicate(self.sixteen_element_vector[i]), run_time=0.1)
            
        scene.play(FadeOut(self.vector_values[0][5:11], self.vector_values[1][5:11], *self.arrows[5:11]))
        scene.play(self.vector_values[0][0:5].animate.shift(LEFT*0.05), self.vector_values[1][0:5].animate.shift(LEFT*0.05),
                   self.vector_values[0][11:].animate.shift(RIGHT*0.05), self.vector_values[1][11:].animate.shift(RIGHT*0.05), run_timr=1)
        
        self.dots2048.next_to(self.rectangles_values[4], buff = 1.0).shift(RIGHT*1.1)
        scene.play(Write(self.dots2048), run_time=0.5)
        for i in range(5):
            self.indeces[i].next_to(self.rectangles_values[i], DOWN, buff = 0.3)
            self.indeces256[i].next_to(self.rectangles_values[i], DOWN, buff = 0.3).shift(RIGHT*0.3)
        for i in range(11, 16):
            self.indeces[i-6].next_to(self.rectangles_values[i], DOWN, buff = 0.3)
            self.indeces256[i-6].next_to(self.rectangles_values[i], DOWN, buff = 0.3).shift(LEFT*0.3)
            
        scene.play(Write(self.indeces), TransformMatchingShapes(self.opening, self.opening2), run_time=0.5)
        scene.wait(1)
        
        self.new_subsection(scene, "ETh VT 256", "data/sound/e7/slide3-4.mp3")
        scene.wait(1)
        scene.play(self.vector_values[0][0:5].animate.shift(RIGHT * 0.3),
        self.vector_values[1][0:5].animate.shift(RIGHT * 0.3),
        self.vector_values[0][11:].animate.shift(LEFT * 0.3),
        self.vector_values[1][11:].animate.shift(LEFT * 0.3),
        TransformMatchingShapes(self.indeces, self.indeces256),
        TransformMatchingShapes(self.opening2, self.opening3), run_time=2)
        self.arrows2 = []
        for i in range(5):
            self.create_arrow(self.envelope, self.rectangles_values[i], where_to_append=self.arrows2)
            
        for i in range(11, 16):
            self.create_arrow(self.envelope, self.rectangles_values[i], where_to_append=self.arrows2)
        scene.play(TransformMatchingShapes(VGroup(*self.arrows[0:5], *self.arrows[11:]), VGroup(*self.arrows2)), run_time=1)
        
        scene.wait(1)
        self.blob = ImageMobject("data/images/blob.png").scale(0.3).shift(UP*5)
        self.blob.generate_target()
        self.blob.target.shift(DOWN*4)
        scene.wait(2)
        scene.play(MoveToTarget(self.blob, rate_func = rate_functions.ease_out_bounce), run_time=2)
        scene.wait(2)
        self.remaining_vector_values = VGroup(self.vector_values[0][0:5], self.vector_values[1][0:5],
                                              self.vector_values[0][11:], self.vector_values[1][11:],)
        
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.title_label, self.blob, self.remaining_vector_values, 
                           self.commitment_whole, self.verifier, self.prover1, self.prover_label, 
                           *self.arrows2, self.dots2048, self.proof, self.opening3, self.indeces256,
                           self.prover_label2, self.verifier1, self.verifier_label), run_time=1)
        
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
        ).scale(0.7)
        
        self.polynomial_graph = self.new_axes.plot_implicit_curve(lambda x, y: (-0.013005328649673187  * x ** (4) + 0.44002953745582507 * x ** (3) 
                                                                  -4.368305697782954 * x ** (2) + 15.731787164922928 * x ** (1)
                                                                  +4.2790892673006296 * x ** (0)) - y, color=SECONDARY_COLOR)
        self.polynomial_chart = VGroup(self.new_axes, self.polynomial_graph)
        
        
    def create_arrow(self, start, end, where_to_append):
        arrow = Arrow(start.get_bottom(), end.get_top(), buff = 0.1, 
            color=PRIMARY_COLOR,
            max_tip_length_to_length_ratio=0.1,
            stroke_width=1.5,
            tip_shape=StealthTip,
            tip_length=0.15,)
        arrow_length = arrow.get_length()
        num_dashes = max(2, int(arrow_length * 2))
        arrow = DashedVMobject(arrow, num_dashes=num_dashes)
        
        where_to_append.append(arrow)
        
        
        

        
        


        