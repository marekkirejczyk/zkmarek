from manim import (FadeIn, FadeOut, Indicate, MoveToTarget, Write, Create, Text,
                   MathTex, UP, RoundedRectangle, VGroup, RIGHT, DOWN, Axes, LEFT, ValueTracker,
                   ImageMobject, Polygon, Arrow, StealthTip, Transform, rate_functions)
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, HIGHLIGHT_COLOR, SECONDARY_COLOR, HIGHLIGHT2_COLOR
from zkmarek.video.slides.e7.curve import Curve
from zkmarek.video.slides.e6.tree import MerkleTree
from zkmarek.video.mobjects.dot_on_curve import DotOnCurve

class SingleLevelVerkleTree(SlideBase):
    def __init__(self) -> None:
        super().__init__("Single level Verkle tree")
        
    def construct(self):
        self.title_label = Text("Single level Verkle tree", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size=40).to_edge(UP)
        
        self.sixteen_element_vector = Text("4162224221920202228354555657585", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 30)
        sixteen_element_vector = [4, 16, 22, 24, 22, 19, 20, 20, 22, 28, 35, 45, 55, 65, 75, 85]
        self.sixteen_element_vector = VGroup(*[Text(str(i), color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 30) for i in sixteen_element_vector]).arrange(RIGHT, buff=0.1)
        rectangle = RoundedRectangle(height = 1, width = 1, corner_radius=0.05, color=SECONDARY_COLOR, fill_opacity=0.5, stroke_width = 0.0).scale(0.5).move_to(self.sixteen_element_vector.get_center()).set_color(SECONDARY_COLOR)
        rectangles_of_values = [rectangle.copy() for _ in range(16)]
        self.rectangles_values = VGroup(*rectangles_of_values).arrange(RIGHT, buff=0.1)
        for i in range(16):
            self.sixteen_element_vector[i].move_to(self.rectangles_values[i].get_center())
    
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
        
        self.prover = ImageMobject("data/images/person_blue.png").scale(0.4).to_edge(LEFT).shift(UP*1.5)
        self.envelope = RoundedRectangle(width = 8 * 0.3, height = 2 * 0.3, fill_opacity = 0.3, stroke_width = 0.0, corner_radius=0.1).set_color(PRIMARY_COLOR)
        self.envelope_flap_closed = Polygon(
            [-4.3, 1, 0],
            [4.3, 1, 0],
            [0, -0.6, 0],
            fill_color=HIGHLIGHT_COLOR,
            fill_opacity=0.2,
            stroke_width = 0.0
        ).scale(0.27).shift(DOWN*0.12)
        
        self.commitment = Text("C", color = HIGHLIGHT_COLOR, font = PRIMARY_FONT, font_size = 30).move_to(self.envelope.get_center())
        
        self.verifier = ImageMobject("data/images/person.png").scale(0.7).to_edge(RIGHT).shift(UP*1.5+LEFT)
        
        self.proof = MathTex(r"{{\pi}}", color = HIGHLIGHT_COLOR, font_size = 37).next_to(self.verifier, DOWN, buff = 0.5)
        self.opening = MathTex(r"{{a_6}} = 1", color = PRIMARY_COLOR, font_size = 37).next_to(self.proof, DOWN, buff = 0.5)
        self.elliptic_curve_point = Text("EC points", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 30).next_to(self.envelope, RIGHT, buff = 0.8)
        self.arrow_ec_commitment = Arrow(self.elliptic_curve_point.get_left(), self.envelope.get_right(), 
            color=PRIMARY_COLOR,
            buff=0.2,
            max_tip_length_to_length_ratio=0.1,
            stroke_width=1.5,
            tip_shape=StealthTip,
            tip_length=0.15,)
        self.arrow_ec_proof = Arrow(self.elliptic_curve_point.get_right(), self.proof.get_left(), 
            color=PRIMARY_COLOR,
            buff=0.2,
            max_tip_length_to_length_ratio=0.1,
            stroke_width=1.5,
            tip_shape=StealthTip,
            tip_length=0.15,)
        
        self.dots2048 = Text("...", color = SECONDARY_COLOR, font = PRIMARY_FONT, font_size = 40)
        indeces = [0, 1, 2, 3, 4, 2043, 2044, 2045, 2046, 2047]
        self.indeces = VGroup(*[Text(str(i), color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 17) for i in indeces]).arrange(RIGHT, buff=0.1)
        indeces256 = [0, 1, 2, 3, 4, 251, 252, 253, 254, 255]
        self.indeces256 = VGroup(*[Text(str(i), color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 17) for i in indeces256]).arrange(RIGHT, buff=0.1)

    def animate_in(self, scene):
        self.new_subsection(scene, "16 element vector", "data/sound/e7/slide3-1.mp3")
        scene.play(Create(self.title_label), run_time=0.5)
        scene.play(Write(self.sixteen_element_vector), run_time=0.5)
        scene.play(Create(self.rectangles_values), run_time=0.5)
        self.vector_values.generate_target()
        self.vector_values.target.shift(DOWN*3)
        scene.play(MoveToTarget(self.vector_values), run_time=1)
        scene.play(Create(self.new_axes), run_time=2)
        scene.wait(1)
        values_y = [4, 16, 22, 23, 22, 20, 20, 20, 22, 27.5, 35, 45, 55, 67, 77, 86]
        
        for i in range(16):
            dot = self.dots[i]
            dot.move_to(self.new_axes.c2p(i, values_y[i]))
            if i == 13 or i == 14 or i == 15:
                dot.shift(DOWN*0.1)

            scene.play(Create(dot), run_time=0.1)
        scene.wait(1)
        scene.play(Create(self.polynomial_graph), run_time=1.5)
        scene.wait(2)
        self.chart = VGroup(self.polynomial_chart, *self.dots)
        scene.play(self.chart.animate.scale(0.1).set_opacity(0.1), FadeIn(self.envelope, self.envelope_flap_closed), run_time=0.8)
        self.vector_values.generate_target()
        self.vector_values.target.shift(UP)
        scene.play(MoveToTarget(self.vector_values), run_time=1)
        
        scene.play(Create(self.commitment), FadeOut(self.chart))
        self.arrows = []
        for i in range(16):
            self.create_arrow(self.envelope, self.rectangles_values[i])
            
        for i in range(16):
            scene.play(Create(self.arrows[i]), run_time=0.1)
        
        self.new_subsection(scene, "number belongs to vector", "data/sound/e7/slide3-1a.mp3")
        scene.play(FadeIn(self.verifier), run_time=0.7)
        scene.wait(1)
        scene.play(Indicate(self.rectangles_values[6], color = PRIMARY_COLOR),
                   Indicate(self.sixteen_element_vector[6], color = PRIMARY_COLOR), run_time=0.9)
        scene.play(Indicate(self.rectangles_values, color = HIGHLIGHT_COLOR),
                   Indicate(self.sixteen_element_vector, color = HIGHLIGHT_COLOR), run_time=0.9)
        scene.wait(1)
        scene.play(Indicate(self.commitment, color = SECONDARY_COLOR), run_time=0.7)
        scene.play(Write(self.proof), run_time=0.7)
        scene.wait(1)
        scene.play(Write(self.opening), run_time=0.7)
        scene.wait(1)
        
        self.new_subsection(scene, "tree modification", "data/sound/e7/slide3-1b.mp3")
        self.create_merkle_tree(scene)
        
        
        self.new_subsection(scene, "ec points", "data/sound/e7/slide3-2.mp3")
        scene.wait(2)
        self.commitment_whole = VGroup(self.envelope, self.envelope_flap_closed, self.commitment)
        scene.play(Indicate(self.commitment_whole, color = HIGHLIGHT_COLOR), run_time=0.5)
        scene.play(Indicate(self.proof, color = HIGHLIGHT2_COLOR), run_time=1)
        scene.wait(1)
        scene.play(Write(self.elliptic_curve_point), run_time=0.5)
        scene.play(Create(self.arrow_ec_commitment), run_time=0.5)
        scene.play(Create(self.arrow_ec_proof), run_time=0.5)
        scene.wait(1)
        scene.play(FadeOut(self.arrow_ec_commitment), FadeOut(self.arrow_ec_proof), FadeOut(self.elliptic_curve_point), run_time=0.5)
        
        
        self.new_subsection(scene, "16->2048", "data/sound/e7/slide3-3.mp3")
        scene.wait(1)
        scene.play(Indicate(self.commitment_whole, color = SECONDARY_COLOR), run_time=0.9)
        scene.play(Indicate(self.proof, color = SECONDARY_COLOR), run_time=0.9)
        for i in range(16):
            scene.play(Indicate(self.rectangles_values[i], color = SECONDARY_COLOR),
                       Indicate(self.sixteen_element_vector[i]), run_time=0.1)
            
        scene.play(FadeOut(self.vector_values[0][5:11], self.vector_values[1][5:11]))
        scene.play(self.vector_values[0][0:5].animate.shift(LEFT*0.05), self.vector_values[1][0:5].animate.shift(LEFT*0.05),
                   self.vector_values[0][11:].animate.shift(RIGHT*0.05), self.vector_values[1][11:].animate.shift(RIGHT*0.05), run_timr=1)
        
        self.dots2048.next_to(self.rectangles_values[4], buff = 1.0).shift(RIGHT*0.8)
        scene.play(Write(self.dots2048), run_time=0.5)
        for i in range(5):
            self.indeces[i].next_to(self.rectangles_values[i], DOWN, buff = 0.3)
            self.indeces256[i].next_to(self.rectangles_values[i], DOWN, buff = 0.3).shift(RIGHT*0.3)
        for i in range(11, 16):
            self.indeces[i-6].next_to(self.rectangles_values[i], DOWN, buff = 0.3)
            self.indeces256[i-6].next_to(self.rectangles_values[i], DOWN, buff = 0.3).shift(LEFT*0.3)
            
        scene.play(Write(self.indeces), run_time=0.5)
        scene.play(self.vector_values[0][0:5].animate.shift(RIGHT * 0.3),
        self.vector_values[1][0:5].animate.shift(RIGHT * 0.3),
        self.vector_values[0][11:].animate.shift(LEFT * 0.3),
        self.vector_values[1][11:].animate.shift(LEFT * 0.3),
        Transform(self.indeces, self.indeces256), run_time=1)
        scene.wait(1)
        blob = ImageMobject("data/images/blob.png").scale(0.3).shift(LEFT*5)
        blob.generate_target()
        blob.target.shift(RIGHT*3)
        scene.play(MoveToTarget(blob, rate_func = rate_functions.ease_out_bounce), run_time=2)
        
        
        self.new_subsection(scene, "ETh VT 256", "data/sound/e7/slide3-4.mp3")
        scene.play(FadeOut(blob), run_time=0.5)
        
        self.new_subsection(scene, "BLS12-381", "data/sound/e7/slide3-5.mp3")
        
        
        self.new_subsection(scene, "pi C are 48 B", "data/sound/e7/slide3-5a.mp3")
        
        self.new_subsection(scene, "vec el < 32", "data/sound/e7/slide3-5b.mp3")
        
        
        self.new_subsection(scene, "VT struct is different", "data/sound/e7/slide3-5c.mp3")
        
        
        self.new_subsection(scene, "11 belongs to level", "data/sound/e7/slide3-6.mp3")
        
        
        self.new_subsection(scene, "Commitment, proof, opening, total", "data/sound/e7/slide3-7.mp3")
        
        
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.title_label), run_time=0.5)
        
        
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
        
        
    def create_arrow(self, start, end):
        arrow = Arrow(start.get_bottom(), end.get_top(), buff = 0.1, 
            color=PRIMARY_COLOR,
            max_tip_length_to_length_ratio=0.1,
            stroke_width=1.5,
            tip_shape=StealthTip,
            tip_length=0.15,)
        self.arrows.append(arrow)
        
    def create_merkle_tree(self, scene):
        self.merkle = MerkleTree(num_children=2, num_levels=4, include_labels=False).stretch(2, 1).scale(0.5).shift(LEFT*3+UP*5)
        scene.play(Create(self.merkle), run_time=1.5)
        scene.wait(1)
        self.node_change = self.merkle.get_node(3, 0)
        self.node_change1 = self.merkle.get_node(2, 0)
        self.node_change2 = self.merkle.get_node(1, 0)
        self.node_change3 = self.merkle.get_node(0, 0)
        scene.play(self.node_change.animate.set_color(HIGHLIGHT2_COLOR), run_time=0.5)
        scene.play(self.node_change1.animate.set_color(HIGHLIGHT2_COLOR), run_time=0.5)
        scene.play(self.node_change2.animate.set_color(HIGHLIGHT2_COLOR), run_time=0.5)
        scene.play(self.node_change3.animate.set_color(HIGHLIGHT2_COLOR), run_time=0.5)
        scene.wait(1)
        scene.play(self.node_change.animate.set_color(HIGHLIGHT_COLOR),
                   self.node_change1.animate.set_color(HIGHLIGHT_COLOR),
                   self.node_change2.animate.set_color(HIGHLIGHT_COLOR),
                   self.node_change3.animate.set_color(HIGHLIGHT_COLOR), run_time=0.5)
    
        self.node_verify = self.merkle.get_node(3, 3)
        
        self.merkle_proof = [self.merkle.get_node(3, 2), self.merkle.get_node(2, 0), self.merkle.get_node(1, 1)]
        scene.play(self.node_verify.animate.set_color(SECONDARY_COLOR).set_opacity(0.2), run_time=0.5)
        scene.wait(0.5)
        for i in range(3):
            scene.play(self.merkle_proof[i].animate.set_color(SECONDARY_COLOR).set_opacity(0.1), run_time=0.5)
        scene.wait(4)
        scene.play(FadeOut(self.merkle), run_time=0.5)
        
        
        

        
        


        