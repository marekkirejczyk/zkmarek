import os

from manim import Scene, config
from presentation import Presentation
from slides.cec.addition import Addition as CECAddition
from slides.cec.negation import Negation as CECNegation
from slides.cec.operations import Operations as CECOperations
from slides.common.title import TitleSlide
from slides.ec.discrete_elliptic_curves import DiscreteEllipticCurves
from slides.equation import EquationSlide

from zkmarek.video.slides.common.code_slide import CodeSlide
from zkmarek.video.slides.common.image_slide import ImageSlide
from zkmarek.video.slides.common.test_slide import \
    TestSlide  # noqa: F401 # pyright: ignore
from zkmarek.video.slides.common.tex_slide import TexSlide
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
    CodeSlide("Double and add", "data/ec/double_and_add.py"),
    CodeSlide("Double and always add", "data/ec/double_and_always_add.py"),
    TitleSlide("Coordination systems"),
    ImageSlide(
        "Coordination systems", "data/ec/coords_conversions.png", image_scale=0.75
    ),
    ImageSlide("Coordination systems (costs)", "data/ec/coords_costs.png"),
    TitleSlide("Constant time operations"),
    CodeSlide("Constant time conditional swap", "data/ct/cswap.py", language="python"),
    CodeSlide("Constant time equal", "data/ct/ct_eq.rs", language="rust"),
    TexSlide("Discrete Elliptic Curves operations", "data/ec/operations.tex"),
]


class EllipticCurves(Scene):
    def construct(self):
        slides = get_slides_from_names(
            dict(os.environ).get("SLIDES"), SLIDES, globals()
        )
        presentation = Presentation(self, SLIDES, slides)
        presentation.print_slides()
        presentation.play()
