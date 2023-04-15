import os

from manim import *

from src.cpoint import CPoint
from src.mobjects.continuous_elliptic_chart import ContinuousEllipticChart
from src.mobjects.line_through_points import LineThroughPoints
from src.mobjects.point_on_curve import PointOnCurve
from src.mobjects.sidebar import Sidebar
from src.presentation import Presentation
from src.slides.equation import EquationSlide
from src.slides.operations import OperationsSlide
from src.slides.title import TitleSlide

config.width = 16
config.height = 9

class EllipticCurves(Scene):
    def construct(self):
        if "MANIM_SLIDE" in os.environ:
            cls_name = os.environ["MANIM_SLIDE"]
            cls = globals()[cls_name]();
            scenes = [cls]
        else:
            scenes = [
                TitleSlide(),
                EquationSlide(),
                OperationsSlide(),
            ]
        Presentation(self).play(scenes)

        # self.next_section("Elliptic Curve equation", type=PresentationSectionType.NORMAL)
        # operations = self.operations(group, ax)

        # self.next_section("Negation", type=PresentationSectionType.NORMAL)
        # self.play(FadeOut(operations), Wait())
        # negation = self.negation(ax)

        # self.next_section("Addition", type=PresentationSectionType.NORMAL)
        # self.play(FadeOut(negation), Wait())
        # addition = self.addition(ax)

        # self.play(FadeOut(addition), Wait())

    def negation(self, ax):
        sidebar = Sidebar("Negation", tex_filename="data/neg.tex", code_filename="data/neg.py")
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
        sidebar = Sidebar("Addition", tex_filename="data/add.tex", code_filename="data/add.py")
        return VGroup(p1, p2, p3, p4, line1, line2, sidebar)
