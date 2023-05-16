from manim import LEFT, UP, DOWN, FadeOut, Write, ValueTracker, linear, Wait

from zkmarek.crypto.cec_affine import CECAffine
from zkmarek.video.mobjects.continuous_elliptic_chart import ContinuousEllipticChart
from zkmarek.video.mobjects.dot_on_curve import DotOnCurve
from zkmarek.video.mobjects.line_through_points import LineThroughPoints
from zkmarek.video.mobjects.sidebar import Sidebar

from .slide_base import SlideBase


class AdditionSlide(SlideBase):
    sidebar: Sidebar
    line1: LineThroughPoints
    line2: LineThroughPoints
    p1: DotOnCurve
    p2: DotOnCurve
    p3: DotOnCurve
    p4: DotOnCurve
    p1_x: ValueTracker
    p1_sgn: int

    def __init__(self):
        SlideBase.__init__(self, title="Addition")
        self.chart = ContinuousEllipticChart()
        self.chart.align_on_border(LEFT)

        self.p1_x = ValueTracker(1)
        self.p1_sgn = 1
        a = CECAffine.from_x(self.p1_x.get_value())
        b = CECAffine.from_x(3)
        c = a + b
        self.p1 = DotOnCurve(self.chart.ax, "A", a)
        self.p2 = DotOnCurve(self.chart.ax, "B", b)
        self.p3 = DotOnCurve(
            self.chart.ax, "A + B", c, label_direction=(LEFT + 0.5 * UP)
        )
        self.p4 = DotOnCurve(
            self.chart.ax, "-(A + B)", -c, label_direction=(LEFT + 0.5 * DOWN)
        )
        self.line1 = LineThroughPoints(self.p4, self.p2)
        self.line2 = LineThroughPoints(self.p3, self.p4)
        self.sidebar = Sidebar(
            "Addition", tex_path="data/cec/add.tex", code_path="data/cec/add.py"
        )

    def update_p1(self, p1):
        new_a = CECAffine.from_x(self.p1_x.get_value(), self.p1_sgn)
        new_c = new_a + self.p2.p
        self.p1.set_p(new_a)
        self.p3.set_p(new_c)
        self.p4.set_p(-new_c)

        left = self.p1 if self.p1.p.x < self.p4.p.x else self.p4
        right = self.p2 if self.p2.p.x > self.p4.p.x else self.p4
        right = self.p1 if self.p1.p.x > right.p.x else right
        self.line1.update_start_and_end(left, right)
        self.line2.update_start_and_end(self.p3, self.p4)

    def animate_build_scene(self, scene):
        scene.play(self.chart.animate_appear())
        scene.play(self.p1.animate_appear())
        scene.play(self.p2.animate_appear())

        scene.add(self.p1)
        scene.add(self.p1_x)
        self.p1.add_updater(self.update_p1)

    def animate_add_lines(self, scene):
        scene.next_section("Line through points")
        scene.play(Write(self.line1), self.p4.animate_appear())

        scene.next_section("Mirror line")
        scene.play(Write(self.line2), self.p3.animate_appear())

    def animate_to_infinity(self, scene):
        scene.next_section("Animate addition")
        target_x = -(7 ** (1.0 / 3))
        scene.play(self.p1_x.animate(run_time=10, rate_func=linear).set_value(target_x))
        self.p1_sgn = -1
        scene.play(self.p1_x.animate(run_time=10, rate_func=linear).set_value(-0.5))

        scene.next_section("Math and code")
        self.sidebar.animate_respectively(scene)

        scene.next_section("Infinity point")
        scene.play(self.p1_x.animate(run_time=10, rate_func=linear).set_value(2.99))
        self.sidebar.animate_replace_code(scene, "data/cec/add_inf.py")

    def animate_to_double(self, scene):
        scene.next_section("Doubling")
        target_x = -(7 ** (1.0 / 3))
        scene.play(self.p1_x.animate(run_time=10, rate_func=linear).set_value(target_x))
        self.p1_sgn = 1
        scene.play(self.p1_x.animate(run_time=10, rate_func=linear).set_value(3))
        self.sidebar.animate_replace_code(scene, "data/cec/add_double.py")
        scene.play(Wait())
        self.sidebar.animate_replace_code(scene, "data/cec/double.py")
        scene.play(self.p1_x.animate(run_time=10, rate_func=linear).set_value(4))

    def animate_in(self, scene):
        self.animate_build_scene(scene)
        self.animate_add_lines(scene)
        self.animate_to_infinity(scene)
        self.animate_to_double(scene)

    def animate_out(self, scene):
        scene.play(
            FadeOut(self.chart),
            FadeOut(self.p1),
            FadeOut(self.p2),
            FadeOut(self.p3),
            FadeOut(self.p4),
            FadeOut(self.line1),
            FadeOut(self.line2),
            FadeOut(self.sidebar),
        )
