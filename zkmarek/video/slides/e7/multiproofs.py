from manim import (Text, UP, DOWN, RIGHT, LEFT, FadeOut, Write, MathTex, TransformMatchingShapes, VGroup,
                   Axes, RoundedRectangle, FadeIn, ValueTracker, Indicate, MoveToTarget)
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR, HIGHLIGHT_COLOR
from zkmarek.video.mobjects.dot_on_curve import DotOnCurve
from zkmarek.video.slides.e7.curve import Curve

class Multiproofs(SlideBase):
    def __init__(self):
        super().__init__("Multiproofs")
        
    def construct(self):
        self.title_label = Text("Multiproofs", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 40).to_edge(UP)
        
        self.pi0 = MathTex(r"\pi^0", color=PRIMARY_COLOR, font_size=36).shift(LEFT*2)
        self.pi1 = MathTex(r"\pi^1", color=PRIMARY_COLOR, font_size=36)
        self.pi2 = MathTex(r"\pi^2", color=PRIMARY_COLOR, font_size=36).shift(RIGHT*2)
        
        self.all_pis = MathTex(r"\pi", color = PRIMARY_COLOR, font_size = 40).shift(UP*1.5)
        
        vector = [r"a_0", r"a_1", r"a_2", r"a_3", r"a_4", r"a_5", r"a_6", r"a_7",
                 r"a_8", r"a_9", r"a_{10}", r"a_{11}", r"a_{12}", r"a_{13}", r"a_{14}", r"a_{15}"]
        self.vector = VGroup(*[MathTex(i, color = PRIMARY_COLOR, font_size = 30) for i in vector]).arrange(RIGHT, buff=0.1)
        rectangle = RoundedRectangle(height = 1, width = 1, corner_radius=0.05, color=HIGHLIGHT_COLOR, fill_opacity=0.2, stroke_width = 0.0).scale(0.5).set_color(HIGHLIGHT_COLOR)
        rectangles_of_values = [rectangle.copy() for _ in range(16)]
        self.rectangles_values = VGroup(*rectangles_of_values).arrange(RIGHT, buff=0.2).shift(DOWN*1.5)
        for i in range(16):
            self.vector[i].move_to(self.rectangles_values[i].get_center())
        
        self.commtiment_C = MathTex(r"C_0^0", color=PRIMARY_COLOR, font_size=40).shift(UP*1.5)
    
        self.opening1 = MathTex(r"p({6})=a_{6}", color = PRIMARY_COLOR, font_size=35)
        self.opening = MathTex(r"p_{i}=a_i", color = PRIMARY_COLOR, font_size=35)
        
        self.new_polynomial = MathTex(r"p(x)-a_i=0", color = PRIMARY_COLOR, font_size=35).shift(RIGHT * 4.5+DOWN)
        
    def animate_in(self, scene):
        self.new_subsection(scene, "pi0, pi1, pi2, ..., pin", "data/sound/e7/slide6-1.mp3")
        scene.play(Write(self.title_label))
        scene.wait(1)
        scene.play(Write(self.pi0), run_time=1)
        scene.play(Write(self.pi1), run_time=1)
        scene.play(Write(self.pi2), run_time=1)
        scene.play(TransformMatchingShapes(VGroup(self.pi0.copy(), self.pi1.copy(), self.pi2.copy()), self.all_pis), run_time=1)
        
        self.new_subsection(scene, "data vector: polynomial", "data/sound/e7/slide6-2.mp3")
        scene.play(FadeOut(self.pi0, self.pi1, self.pi2, self.all_pis), run_time=1)
        scene.play(FadeIn(self.commtiment_C), run_time=1)
        scene.wait(0.5)
        scene.play(Write(self.vector), run_time=1)
        scene.play(Write(self.rectangles_values), run_time=1)
        scene.play(self.vector.animate.shift(DOWN*1.3), self.rectangles_values.animate.shift(DOWN), run_time=1)
        self.animate_polynomial()
        scene.play(FadeIn(self.polynomial_chart), run_time=1)
        scene.wait(1)
        
        self.new_subsection(scene, "opening p(xi)=ai", "data/sound/e7/slide6-3.mp3")
        self.opening1.shift(RIGHT * 4.5)
        for i in range(6):
            scene.play(Indicate(self.vector[i]), run_time=0.3)
        scene.play(self.vector[6].animate.set_color(SECONDARY_COLOR), run_time=1)

        scene.play(FadeIn(self.dots[6]), Write(self.opening1), run_time=1)
        scene.play(FadeOut(self.vector, self.rectangles_values))
        self.polynomial_graph.generate_target()
        self.polynomial_graph.target.shift(DOWN * 0.65)
        scene.play(MoveToTarget(self.polynomial_graph), run_time=1)
        scene.play(FadeOut(self.dots[6]))
        
        self.new_subsection(scene, "p(xi)-ai=0", "data/sound/e7/slide6-4.mp3")
        scene.play(TransformMatchingShapes(self.opening1, self.opening), run_time=1)
        scene.play(Write(self.new_polynomial), run_time=1)
        
        self.new_subsection(scene, "root x=xi", "data/sound/e7/slide6-5.mp3")
        
        self.new_subsection(scene, "factored form", "data/sound/e7/slide6-6.mp3")
        
        self.new_subsection(scene, "quotient poly", "data/sound/e7/slide6-7.mp3")
        
        self.new_subsection(scene, "divide x-xi", "data/sound/e7/slide6-8.mp3")
        
        self.new_subsection(scene, "multiproofs", "data/sound/e7/slide6-9.mp3")
        
        self.new_subsection(scene, "3 proofs, 3 openings, 3 commitments", "data/sound/e7/slide6-10.mp3")
        
        self.new_subsection(scene, "random linear combinations", "data/sound/e7/slide6-11.mp3")
        
        self.new_subsection(scene, "random point t", "data/sound/e7/slide6-12.mp3")
        
        self.new_subsection(scene, "verkle multiproof", "data/sound/e7/slide6-13.mp3")
        
        self.new_subsection(scene, "verify once", "data/sound/e7/slide6-14.mp3")
        
        self.new_subsection(scene, "if tree deep - savings", "data/sound/e7/slide6-15.mp3")
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.title_label))
    
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
    