from manim import (DOWN, LEFT, RIGHT, UP, AddTextLetterByLetter, Angle, Create,
                   Dot, FadeOut, Flash, GrowFromPoint, Indicate, MathTex,
                   ReplacementTransform, ShowPassingFlash, SingleStringMathTex,
                   TransformMatchingTex, ValueTracker, Write, linear)

from zkmarek.crypto.cec_affine import CECAffine
from zkmarek.video.constant import (HIGHLIGHT_COLOR, PRIMARY_COLOR,
                                    SECONDARY_COLOR)
from zkmarek.video.mobjects.continuous_elliptic_chart import \
    ContinuousEllipticChart
from zkmarek.video.mobjects.dot_on_curve import DotOnCurve
from zkmarek.video.mobjects.line_through_points import LineThroughDots
from zkmarek.video.mobjects.sidebar import Sidebar
from zkmarek.video.slides.common.slide_base import SlideBase


class Addition(SlideBase):
    chart: ContinuousEllipticChart
    sidebar: Sidebar
    line1: LineThroughDots
    line2: LineThroughDots
    line1_tmp: LineThroughDots
    line2_tmp: LineThroughDots
    p1: DotOnCurve
    p2: DotOnCurve
    p3: DotOnCurve
    p4: DotOnCurve
    p4_tmp: DotOnCurve
    point_at_infinity: DotOnCurve
    point_at_label: MathTex
    equation1: MathTex
    equation2: MathTex
    p1_x: ValueTracker
    p1_sgn: int
    angle: Angle


    def __init__(self):
        super().__init__("Elliptic Curves Addition")

    def construct(self):
        self.chart = ContinuousEllipticChart(include_details=False)
        self.p1_x = ValueTracker(1)
        self.p1_sgn = 1
        a = CECAffine.from_x(self.p1_x.get_value())
        b = CECAffine.from_x(3)
        c = a + b
        self.p1 = DotOnCurve(self.chart.ax, "A", a)
        self.p2 = DotOnCurve(self.chart.ax, "B", b, label_direction=(LEFT + 0.5 * UP))
        self.p3 = DotOnCurve(
            self.chart.ax, "A + B", c, label_direction=(LEFT + 0.5 * UP)
        )
        self.p4 = DotOnCurve(
            self.chart.ax, "-(A + B)", -c, label_direction=(LEFT + 0.5 * DOWN)
        )
        self.p4_tmp = DotOnCurve(
            self.chart.ax, "C", -c, label_direction=(LEFT + 0.5 * DOWN)
        )
        self.point_at_infinity = Dot(self.chart.ax.coords_to_point(6, 7),
                                     color=PRIMARY_COLOR)
        self.point_at_label = SingleStringMathTex("\infty", color=PRIMARY_COLOR)
        self.line1 = LineThroughDots(self.p4, self.p2)
        self.line1_tmp = LineThroughDots(self.p2, self.p4)
        self.line2 = LineThroughDots(self.p4, self.p3)
        self.line2_tmp = LineThroughDots(self.p4, self.p3)
        self.sidebar = Sidebar(
            "Addition", tex_path="data/cec/add.tex", code_path="data/cec/add.py"
        )
        self.equation1 = MathTex("{{A}} + {{B}} + {{C}} = 0", color=PRIMARY_COLOR)
        self.equation2 = MathTex("{{C}} = -({{A}} + {{B}})", color=PRIMARY_COLOR)
        self.equation1.to_corner(DOWN + LEFT)
        self.equation2.to_corner(DOWN + LEFT)

    def update_p1(self, p1):
        new_a = CECAffine.from_x(self.p1_x.get_value(), self.p1_sgn)
        new_c = new_a + self.p2.p
        self.p1.set_p(new_a)
        self.p2.set_p(CECAffine.from_x(3))
        self.p3.set_p(new_c)
        self.p4.set_p(-new_c)

        if abs(self.p1.p.x - self.p2.p.x) < 0.4 and self.p1_sgn < 0:
            self.line1.update_start_and_end(self.p1, self.p2)
        else:
            sorted_dots = sorted([self.p1, self.p2, self.p4], key=lambda d: d.p.x)
            self.line1.update_start_and_end(sorted_dots[0], sorted_dots[-1])

        self.line2.update_start_and_end(self.p3, self.p4)

    def animate_addition_base(self, scene):
        self.new_subsection(scene,
            "Two points",
            sound="data/sound/episode/s8-1.wav")
        self.chart.animate_in(scene)
        scene.play(Create(self.p1.dot))
        scene.play(Create(self.p2.dot))
        scene.play(Write(self.p1.label))
        scene.play(Write(self.p2.label))

        scene.add(self.p1)
        scene.add(self.p2)
        scene.add(self.p1_x)

        self.new_subsection(scene,
            "Line through points",
            sound="data/sound/episode/s8-2.wav")
        scene.play(GrowFromPoint(self.line1, point=self.p2.to_coord(), run_time=5))
        self.p4_tmp.animate_in(scene)
        scene.add(self.p4_tmp)

        self.new_subsection(scene,
            "Addition definition",
            sound="data/sound/episode/s8-3.wav")
        scene.play(AddTextLetterByLetter(self.equation1), run_time=5)

        self.new_subsection(scene,
            "Addition formula",
            sound="data/sound/episode/s8-4.wav")
        scene.play(TransformMatchingTex(self.equation1, self.equation2), run_time=2)
        scene.wait(3)
        scene.play(
            ReplacementTransform(self.equation2, self.p4),
            FadeOut(self.p4_tmp),
            run_time=2)

        self.new_subsection(scene,
            "Point reflection",
            sound="data/sound/episode/s8-5.wav")
        scene.play(GrowFromPoint(self.line2, point=self.p4.to_coord(), run_time=3))
        self.p3.animate_in(scene)
        scene.add(self.p3)

    def animate_addition_base_summary(self, scene):
        self.new_subsection(scene,
            "Addition summary",
            sound="data/sound/episode/s8-6.wav")

        self.p1.add_updater(self.update_p1)
        scene.wait(2)
        scene.play(
            ShowPassingFlash(self.line1_tmp.set_color(SECONDARY_COLOR),
            time_width=1,
            run_time=1))
        scene.play(Indicate(self.p4))
        scene.wait(2)
        scene.play(
            ShowPassingFlash(self.line2_tmp.set_color(SECONDARY_COLOR),
            time_width=1,
            run_time=1))
        scene.play(Indicate(self.p3))

    def animate_addition_math_and_code(self, scene):
        self.new_subsection(scene,
            "Sidebar addition math",
            sound="data/sound/episode/s8b-1.wav")
        scene.play(self.chart.animate.align_on_border(LEFT, buff=0.8))
        self.sidebar.animate_show_label(scene)
        self.sidebar.animate_show_math(scene)
        math = self.sidebar.math
        scene.wait(3.5)
        math[0][0:12].set_color(HIGHLIGHT_COLOR)
        scene.wait(1)
        self.angle = Angle(self.line1,
            self.chart.ax.x_axis,
            other_angle=True,
            color=SECONDARY_COLOR)
        scene.play(Write(self.angle))
        scene.play(Indicate(self.angle))
        scene.wait(4.5)
        math[0][12:24].set_color(HIGHLIGHT_COLOR)
        scene.wait(0.5)
        math[0][24:38].set_color(HIGHLIGHT_COLOR)

        self.new_subsection(scene,
            "Sidebar addition code",
            sound="data/sound/episode/s8b-2.wav")
        math[0][0:38].set_color(PRIMARY_COLOR)
        self.sidebar.animate_show_code(scene)

        scene.wait(3)
        self.sidebar.indicate_code(scene, "def __add__(self, other)")
        scene.wait(1)
        self.sidebar.indicate_code(scene,
            "slope = (other.y - self.y) / (other.x - self.x)")
        self.sidebar.indicate_code(scene, "x = slope ** 2 - self.x - other.x")
        self.sidebar.indicate_code(scene, "y = slope * (self.x - x) - self.y")
        scene.play(FadeOut(self.angle))


    def animate_infinity_point(self, scene):
        self.new_subsection(scene,
            "Addition - move around",
            sound="data/sound/episode/s8c-1.wav")
        scene.wait(1)
        scene.play(Indicate(self.p4.dot))

        self.new_subsection(scene,
            "Addition - move around",
            sound="data/sound/episode/s8c-2.wav")
        target_x = -(7 ** (1.0 / 3))
        scene.play(self.p1_x.animate(run_time=6, rate_func=linear).set_value(target_x))
        self.p1_sgn = -1
        scene.play(self.p1_x.animate(run_time=6, rate_func=linear).set_value(-0.5))


        scene.play(self.p1_x.animate(run_time=10, rate_func=linear).set_value(2.99))
        self.point_at_infinity.move_to(self.chart.ax.coords_to_point(6, 7))
        self.point_at_label.next_to(self.point_at_infinity, RIGHT)

        scene.wait(5)

        self.sidebar.math[0][8:13].set_color(SECONDARY_COLOR)

        self.new_subsection(scene,
            "Addition - point at infinity",
            sound="data/sound/episode/s8c-3.wav")

        scene.wait(3)
        scene.play(Create(self.point_at_infinity))
        scene.wait(3)
        scene.play(Flash(self.point_at_infinity))
        scene.wait(1)
        scene.play(Create(self.point_at_label))
        self.sidebar.math[0][8:13].set_color(PRIMARY_COLOR)

        self.new_subsection(scene,
            "Addition - point at infinity - math",
            sound="data/sound/episode/s8c-4.wav")

        self.sidebar.animate_hide_code(scene)
        self.sidebar.animate_replace_math(scene, "data/cec/add_inf.tex")
        scene.wait(1)
        self.sidebar.math[0][0:6].set_color(SECONDARY_COLOR)
        self.new_subsection(scene,
            "Addition - point at infinity - neutral element",
            sound="data/sound/episode/s8c-5.wav")

        scene.wait(12)
        self.sidebar.animate_replace_math(scene, "data/cec/add_inf2.tex")
        self.sidebar.math[0][6:11].set_color(SECONDARY_COLOR)
        scene.wait(3)
        self.sidebar.math[0][11:16].set_color(SECONDARY_COLOR)
        self.new_subsection(scene,
            "Addition - point at infinity - code",
            sound="data/sound/episode/s8c-6.wav")

        scene.wait(2)
        self.sidebar.animate_hide_math(scene)
        self.sidebar.animate_show_code(scene)

        self.new_subsection(scene,
            "Addition - point at infinity - code",
            sound="data/sound/episode/s8c-7.wav")
        scene.wait(1)
        self.sidebar.animate_replace_code(scene, "data/cec/add_inf.py")

        scene.wait(4)
        self.sidebar.indicate_code(scene,
            "self.x == other.x and self.y == -other.y")
        self.sidebar.indicate_code(scene, "self == INFINITY")
        self.sidebar.indicate_code(scene, "other == INFINITY")
        scene.wait(3)

        self.sidebar.indicate_code(scene,
            "slope = (other.y - self.y) / (other.x - self.x)")
        self.sidebar.indicate_code(scene, "x = slope ** 2 - self.x - other.x")
        self.sidebar.indicate_code(scene, "y = slope * (self.x - x) - self.y")
        self.sidebar.indicate_code(scene, "return CECAffine(x, y)")

        scene.play(FadeOut(self.point_at_label))
        scene.play(FadeOut(self.point_at_infinity))

    def animate_doubling(self, scene):
        self.new_subsection(scene, "Point doubling - move around",
            sound="data/sound/episode/s8d-1.m4a")
        target_x = -(7 ** (1.0 / 3))
        scene.play(self.p1_x.animate(run_time=10, rate_func=linear).set_value(target_x))
        self.new_subsection(scene, "Point doubling - move around",
            sound="data/sound/episode/s8d-1b.wav")

        self.p1_sgn = 1
        scene.play(self.p1_x.animate(run_time=10, rate_func=linear).set_value(3))

        self.new_subsection(scene, "Point doubling - tangent line",
            sound="data/sound/episode/s8d-2.wav")
        scene.wait(10)
        line_double = self.line1.copy()
        self.chart.add(line_double)
        scene.play(line_double.animate(run_time=2).scale(1.8))

        self.sidebar.animate_hide_code(scene)
        self.sidebar.animate_show_math(scene)
        self.sidebar.animate_replace_math(scene, "data/cec/add_double.tex")
        scene.wait(1)
        self.sidebar.math[0][19:31].set_color(SECONDARY_COLOR)
        scene.wait(1)
        self.sidebar.math[0][16:19].set_color(SECONDARY_COLOR)

        self.new_subsection(scene, "Point doubling - code",
            sound="data/sound/episode/s8d-3.wav")
        self.sidebar.animate_hide_math(scene)
        self.sidebar.animate_show_code(scene)
        self.sidebar.animate_replace_code(scene, "data/cec/add_double.py")
        self.sidebar.indicate_code(scene, "if self.x == other.x and self.y == other.y:")

        self.new_subsection(scene, "Point doubling - extract doubling",
            sound="data/sound/episode/s8d-4.wav")
        scene.wait(3)
        self.sidebar.indicate_code(scene, "return self.double()")
        scene.wait(1)
        self.sidebar.animate_replace_code(scene, "data/cec/double.py")
        self.sidebar.indicate_code(scene, "def double(self):")
        scene.wait(5)
        self.sidebar.indicate_code(scene, "slope = (3 * self.x ** 2) / (2 * self.y)")

        scene.play(line_double.animate(run_time=2).scale(0.5))
        self.chart.remove(line_double)

    def animate_in(self, scene):
        self.animate_addition_base(scene)
        self.animate_addition_base_summary(scene)
        self.animate_addition_math_and_code(scene)
        self.animate_infinity_point(scene)
        self.animate_doubling(scene)

    def animate_out(self, scene):
        self.new_subsection(scene, "Point addition - clean up")
        self.sidebar.animate_out(scene)
        scene.play(
            FadeOut(self.p3),
            FadeOut(self.line2),
            FadeOut(self.p4),
            FadeOut(self.line1),
            FadeOut(self.p2),
            FadeOut(self.p1),
            FadeOut(self.chart),
        )
