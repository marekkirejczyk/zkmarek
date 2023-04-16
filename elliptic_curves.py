import os

from manim import *

from src.presentation import Presentation
from src.slides.addition import AdditionSlide
from src.slides.equation import EquationSlide
from src.slides.negation import NegationSlide
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
                TitleSlide("Elliptic Curves"),
                EquationSlide(),
                OperationsSlide(),
                NegationSlide(),
                AdditionSlide()
            ]
        Presentation(self).play(scenes)
