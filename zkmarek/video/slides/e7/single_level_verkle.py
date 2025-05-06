from manim import (FadeIn, FadeOut, Indicate, MoveToTarget, Write, Create, Text,
                   MathTex, UP, RoundedRectangle, VGroup, RIGHT, DOWN, Axes, LEFT, ValueTracker,
                   ImageMobject, Polygon)
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, HIGHLIGHT_COLOR, SECONDARY_COLOR
from zkmarek.video.slides.e7.curve import Curve
from zkmarek.video.mobjects.dot_on_curve import DotOnCurve

class SingleLevelVerkleTree(SlideBase):
    def __init__(self) -> None:
        super().__init__("Single level Verkle tree")
        
    def construct(self):
        self.title_label = Text("Single level Verkle tree", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size=40).to_edge(UP)
        
        self.sixteen_element_vector = Text("8375471035643653", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 30)

        rectangle = RoundedRectangle(height = 1, width = 1, corner_radius=0.05, color=SECONDARY_COLOR, fill_opacity=0.5, stroke_width = 0.0).scale(0.5).move_to(self.sixteen_element_vector.get_center()).set_color(SECONDARY_COLOR)
        rectangles_of_values = [rectangle.copy() for _ in range(16)]
        self.rectangles_values = VGroup(*rectangles_of_values).arrange(RIGHT, buff=0.1)
        for i in range(16):
            self.sixteen_element_vector[i].move_to(self.rectangles_values[i].get_center())
    
        self.formula = MathTex(r"a_{15}\cdot {{x^{15}}} + a_{14}\cdot {{x^{14}}} + \cdots {{a_{0}}}]", color = PRIMARY_COLOR, font_size = 20).shift(RIGHT*2+DOWN*1.5)
        self.animate_polynomial()
        values = [
            (0, 8), (1, 3), (2, 7), (3, 5), (4, 4), (5, 7), (6, 1), (7, 0),
            (8, 3), (9, 5), (10, 6), (11, 4), (12, -6), (13, -17), (14, -42), (15, -50)
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
        values_y = [8, 3, 7, 5, 4, 7, 1, 0, 3, 5, 5.5, 4.2, -6, -17, -42, -50]
        for i in range(16):
            dot = self.dots[i]
            dot.move_to(self.new_axes.c2p(i, values_y[i]*0.1))
            if i == 13 or i == 14 or i == 15:
                dot.shift(DOWN*0.1)

            scene.play(Create(dot), run_time=0.1)
        scene.wait(1)
        scene.play(Create(self.polynomial_graph), run_time=1.5)
        scene.wait(2)
        self.chart = VGroup(self.polynomial_chart, *self.dots)
        scene.play(self.chart.animate.scale(0.1).set_opacity(0.1), FadeIn(self.envelope, self.envelope_flap_closed), run_time=0.8)
        scene.wait(1)
        scene.play(Create(self.commitment), FadeOut(self.chart))
        
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
        
        
        self.new_subsection(scene, "ec points", "data/sound/e7/slide3-2.mp3")
        
        
        self.new_subsection(scene, "16->2048", "data/sound/e7/slide3-3.mp3")
        
        self.new_subsection(scene, "ETh VT 256", "data/sound/e7/slide3-4.mp3")
        
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
            y_range=[-22, 20, 500],
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
        
        self.polynomial_graph = self.new_axes.plot_implicit_curve(lambda x, y: (4.26713027e-09 * x ** (15) 
                                                                  -5.00493029e-07 * x ** (14) +  2.67032132e-05 * x ** (13) 
                                                                  -8.57314665e-04* x ** (12) +1.84604634e-02 * x ** (11) 
                                                                  -2.81249901e-01* x ** (10) +  3.11615153e+00 * x ** (9) 
                                                                  -2.54062977e+01 * x ** (8) +1.52442624e+02 * x ** (7) 
                                                                  -6.66027523e+02 * x ** (6) +  2.07111066e+03 * x ** (5) 
                                                                  -4.40664678e+03 * x ** (4) +5.99848486e+03 * x ** (3) 
                                                                  -4.60965478e+03 * x ** (2) + 1.47784469e+03 * x ** (1)
                                                                  + 7.99999698e+00 * x ** (0))*0.1 - y, color=SECONDARY_COLOR)
        
        self.polynomial_chart = VGroup(self.new_axes, self.polynomial_graph)
        
        
        


        