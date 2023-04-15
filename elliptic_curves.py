from src.cpoint import CPoint
from src.mobjects.sidebar import Sidebar
from src.mobjects.line_through_points import LineThroughPoints
from src.mobjects.point_on_curve import PointOnCurve
from src.mobjects.continuous_elliptic_chart import ContinuousEllipticChart
from src.slides.title import TitleSlide
from src.slides.equation import EquationSlide
from manim import *
from manim_editor import PresentationSectionType

config.width = 16
config.height = 9

class EllipticCurves(Scene):
    def construct(self):
        self.play_slide(TitleSlide())
        self.next_section("Elliptic Curve equation", type=PresentationSectionType.NORMAL)
        self.play_slide(EquationSlide())

        # self.next_section("Chart", type=PresentationSectionType.NORMAL)
        # group, ax = self.elliptic_chart()

        # self.next_section("Operations", type=PresentationSectionType.NORMAL)
        # operations = self.operations(group, ax)

        # self.next_section("Negation", type=PresentationSectionType.NORMAL)
        # self.play(FadeOut(operations), Wait())
        # negation = self.negation(ax)

        # self.next_section("Addition", type=PresentationSectionType.NORMAL)
        # self.play(FadeOut(negation), Wait())
        # addition = self.addition(ax)

        # self.play(FadeOut(addition), Wait())

    def play_slide(self, slide):
        for a in slide.animate_in():
            self.play(a, Wait())
        for a in slide.animate_out():
            self.play(a, Wait())

    def elliptic_chart(self):
        chart = ContinuousEllipticChart()
        self.play(Create(chart))
        return [chart, chart.ax]

    def operations(self, group, ax):
        a = CPoint.from_compressed(1)
        p1 = PointOnCurve(ax, "A(x, y)", a)
        p2 = PointOnCurve(ax, "A", a, include_coords=True)
        self.play(p1.animate_appear(), Wait())
        self.play(ReplacementTransform(p1, p2), Wait())
        self.play(FadeOut(p2), Wait())

        self.play(group.animate.shift(LEFT * 3.2), Wait())
        sidebar = Sidebar(group, "Operations", tex_filename="data/operations.tex")
        self.play(Write(sidebar), Wait())
        self.play(FadeOut(sidebar), Wait())

    def negation(self, ax):
        sidebar = Sidebar(ax, "Negation", tex_filename="data/neg.tex", code_filename="data/neg.py")
        a = CPoint.from_compressed(2)
        p1 = PointOnCurve(ax, "A", a, include_lines=True)
        p2 = PointOnCurve(ax, "-A", -a, include_lines=True)
        self.play(p1.animate_appear(), p2.animate_appear(), Wait())
        self.play(Write(sidebar), Wait())
        return VGroup(p1, p2, sidebar)

    def addition(self, ax):
        a = CPoint.from_compressed(2)
        b = CPoint.from_compressed(3)
        c = a + b
        p1 = PointOnCurve(ax, "A", a)
        p2 = PointOnCurve(ax, "B", b)
        p3 = PointOnCurve(ax, "A + B", c, label_direction=LEFT)
        p4 = PointOnCurve(ax, "-(A + B)", -c, label_direction=LEFT)
        self.play(p1.animate_appear(), Wait())
        self.play(p2.animate_appear(), Wait())
        line1 = LineThroughPoints(p1, p2)
        self.play(Write(line1), Wait(2))
        self.play(p4.animate_appear(), Wait())
        line2 = LineThroughPoints(p3, p4)
        self.play(Write(line2), Wait(2))
        self.play(p3.animate_appear(), Wait())
        sidebar = Sidebar(ax, "Addition", tex_filename="data/add.tex", code_filename="data/add.py")
        return VGroup(p1, p2, p3, p4, line1, line2, sidebar)


