import os

from manim import Scene, config

from presentation import Presentation
from slides.addition import AdditionSlide
from slides.equation import EquationSlide
from slides.negation import NegationSlide
from slides.operations import OperationsSlide
from slides.title import TitleSlide
from slides.discreet_elliptic_curves import DiscreetEllipticCurves

config.width = 16
config.height = 9

class EllipticCurves(Scene):
    def construct(self):
        if "MANIM_SLIDE" in os.environ:
            cls_name = os.environ["MANIM_SLIDE"]
            cls = globals()[cls_name]()
            scenes = [cls]
        else:
            scenes = [
                TitleSlide("Elliptic Curves"),
                EquationSlide(),
                OperationsSlide(),
                NegationSlide(),
                AdditionSlide(),
                DiscreetEllipticCurves(),
            ]
        Presentation(self).play(scenes)
