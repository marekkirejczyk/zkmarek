import os

from manim import Scene, config
from presentation import Presentation
from slides.cec.addition import Addition as CECAddition
from slides.cec.negation import Negation as CECNegation
from slides.cec.operations import Operations as CECOperations
from slides.ec.discrete_elliptic_curves import DiscreteEllipticCurves
from slides.equation import EquationSlide
from slides.title import TitleSlide
from zkmarek.video.slides.code_slide import CodeSlide
from zkmarek.video.slides.slide_base import SlideBase
from zkmarek.video.slides.test_slide import \
    TestSlide  # noqa: F401 # pyright: ignore
from zkmarek.video.utils import get_slides_from_names

config.width = 16
config.height = 9

SLIDES = [
    TitleSlide("Elliptic Curves"),
    EquationSlide(),
    CECOperations(),
    CECNegation(),
    CECAddition(),
    TitleSlide("Discrete Elliptic Curves"),
    DiscreteEllipticCurves(),
    TitleSlide("Multiplication by scalar"),
    CodeSlide("Double and add", "data/ec/double_and_add.py")
]


class EllipticCurves(Scene):
    def construct(self):
        env_slides = get_slides_from_names(dict(os.environ).get("SLIDES"), globals())
        slides = slides = SLIDES if env_slides is None else env_slides

        print("Rendering slides: ")
        SlideBase.print(slides)

        Presentation(self).play(slides)
