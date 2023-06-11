from manim import (DOWN, GREEN, LEFT, RIGHT, UP, Create, Dot, FadeOut, Flash,
                   GrowFromPoint, MathTex, Succession, ValueTracker, linear)

from zkmarek.crypto.cec_affine import CECAffine
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
    p1: DotOnCurve
    p2: DotOnCurve
    p3: DotOnCurve
    p4: DotOnCurve
    point_at_infinity: DotOnCurve
    point_at_label: MathTex
    p1_x: ValueTracker
    p1_sgn: int

    def __init__(self):
        super().__init__("Elliptic Curves addition")

    def construct(self):
        self.chart = ContinuousEllipticChart()
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
        self.point_at_infinity = Dot(self.chart.ax.coords_to_point(6, 7), color=GREEN)
        self.point_at_label = MathTex("\infty")
        self.line1 = LineThroughDots(self.p4, self.p2)
        self.line2 = LineThroughDots(self.p3, self.p4)
        self.sidebar = Sidebar(
            "Addition", tex_path="data/cec/add.tex", code_path="data/cec/add.py"
        )

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

    def animate_update_chart_position(self, scene):
        scene.play(
            self.chart.animate.next_to(self.sidebar, LEFT, buff=0.5).align_on_border(UP)
        )

    def animate_build_scene(self, scene):
        self.chart.animate_in(scene)
        self.p1.animate_in(scene)
        self.p2.animate_in(scene)
        scene.add(self.p1)
        scene.add(self.p2)
        scene.add(self.p1_x)

        self.new_subsection(scene, "Line through points")
        scene.play(GrowFromPoint(self.line1, point=self.p2.to_coord(), run_time=5))
        self.p4.animate_in(scene)
        scene.add(self.p4)

        self.new_subsection(scene, "Point reflection")
        scene.play(GrowFromPoint(self.line2, point=self.p4.to_coord(), run_time=3))
        self.p3.animate_in(scene)
        scene.add(self.p3)

        self.p1.add_updater(self.update_p1)

    def animate_addition(self, scene):
        self.new_subsection(scene, "Move around")
        target_x = -(7 ** (1.0 / 3))
        scene.play(self.p1_x.animate(run_time=10, rate_func=linear).set_value(target_x))
        self.p1_sgn = -1
        scene.play(self.p1_x.animate(run_time=10, rate_func=linear).set_value(-0.5))

        scene.play(self.chart.animate.align_on_border(LEFT))
        self.sidebar.animate_in(scene, self)
        self.animate_update_chart_position(scene)

    def animate_infinity_point(self, scene):
        self.new_subsection(scene, "Point at infinity - move to negation")
        scene.play(self.p1_x.animate(run_time=10, rate_func=linear).set_value(2.99))
        self.point_at_infinity.move_to(self.chart.ax.coords_to_point(6, 7))
        self.point_at_label.next_to(self.point_at_infinity, RIGHT)

        self.new_subsection(scene, "Point at infinity - show point")
        scene.play(Create(self.point_at_infinity))
        scene.play(Create(self.point_at_label))

        scene.play(Flash(self.point_at_infinity))
        self.new_subsection(scene, "Point at infinity - math")
        self.sidebar.animate_hide_code(scene)
        self.sidebar.animate_replace_math(scene, "data/cec/add_inf.tex")
        self.new_subsection(scene, "Point at infinity - code")
        self.sidebar.animate_hide_math(scene)
        self.sidebar.animate_show_code(scene)
        self.sidebar.animate_replace_code(scene, "data/cec/add_inf.py")
        scene.play(FadeOut(self.point_at_label))
        scene.play(FadeOut(self.point_at_infinity))

    def animate_doubling(self, scene):
        self.new_subsection(scene, "Point doubling - move around")
        target_x = -(7 ** (1.0 / 3))
        scene.play(self.p1_x.animate(run_time=10, rate_func=linear).set_value(target_x))
        self.p1_sgn = 1
        scene.play(self.p1_x.animate(run_time=10, rate_func=linear).set_value(3))

        self.new_subsection(scene, "Point doubling - tangent line")
        line_double = self.line1.copy()
        self.chart.add(line_double)
        scene.play(line_double.animate(run_time=2).scale(2))

        self.new_subsection(scene, "Point doubling - math")
        self.sidebar.animate_hide_code(scene)
        self.sidebar.animate_show_math(scene)
        self.sidebar.animate_replace_math(scene, "data/cec/add_double.tex")
        self.animate_update_chart_position(scene)
        self.new_subsection(scene, "Point doubling - code")
        self.sidebar.animate_hide_math(scene)
        self.sidebar.animate_show_code(scene)
        self.new_subsection(scene, "Point doubling - code v1")
        self.sidebar.animate_replace_code(scene, "data/cec/add_double.py")
        self.new_subsection(scene, "Point doubling - code v2")
        self.sidebar.animate_replace_code(scene, "data/cec/double.py")

        scene.play(line_double.animate(run_time=2).scale(0.5))
        self.chart.remove(line_double)
        scene.play(self.p1_x.animate(run_time=3, rate_func=linear).set_value(3.5))

    def animate_in(self, scene):
        self.animate_build_scene(scene)
        self.animate_addition(scene)
        self.animate_infinity_point(scene)
        self.animate_doubling(scene)

    def animate_out(self, scene):
        self.new_subsection(scene, "Point addition - clean up")
        self.sidebar.animate_out(scene)
        scene.play(
            Succession(
                FadeOut(self.p3),
                FadeOut(self.line2),
                FadeOut(self.p4),
                FadeOut(self.line1),
                FadeOut(self.p2),
                FadeOut(self.p1),
                FadeOut(self.chart),
            )
        )
