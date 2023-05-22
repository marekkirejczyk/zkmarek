import os

from manim import Scene, config

from presentation import Presentation
from slides.title import TitleSlide
from slides.equation import EquationSlide
from slides.cec.addition import Addition
from slides.cec.negation import Negation as CECNegation
from slides.cec.operations import Operations as CECOperations
from slides.ec.negation import Negation as ECNegation
from slides.ec.addition import Addition as ECAddition

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
                CECOperations(),
                CECNegation(),
                Addition(),
                TitleSlide("Discrete Elliptic Curves"),
                ECNegation(),
                ECAddition(),
            ]
        Presentation(self).play(scenes)
