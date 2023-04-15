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
from src.slides.negation import NegationSlide
from src.slides.addition import AdditionSlide

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
                NegationSlide(),
                AdditionSlide()
            ]
        Presentation(self).play(scenes)

        # self.next_section("Elliptic Curve equation", type=PresentationSectionType.NORMAL)
        # self.next_section("Negation", type=PresentationSectionType.NORMAL)
        # self.next_section("Addition", type=PresentationSectionType.NORMAL)
