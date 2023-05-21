import os

from manim import Scene, config

from presentation import Presentation
from slides.addition import AdditionSlide
from slides.equation import EquationSlide
from slides.negation import NegationSlide
from slides.operations import OperationsSlide
from slides.title import TitleSlide
from slides.discrete_elliptic_curves import DiscreteEllipticCurves

from zkmarek.video.slides.test_slide import TestSlide # noqa: F401 # pyright: ignore

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
                TitleSlide("Discrete Elliptic Curves"),
                DiscreteEllipticCurves(),
            ]
        Presentation(self).play(scenes)
