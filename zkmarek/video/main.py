import os

from manim import Scene, config
from presentation import Presentation
from slides.cec.addition import Addition as CECAddition
from slides.cec.negation import Negation as CECNegation
from slides.cec.operations import Operations as CECOperations
from slides.common.title import TitleSlide
from slides.ec.introduction import Introduction as ECIntroduction
from slides.ec.negation import Negation as ECNegation
from slides.ec.addition import Addition as ECAddition
from slides.equation import EquationSlide

from zkmarek.video.slides.common.code_slide import CodeSlide
from zkmarek.video.slides.common.image_slide import ImageSlide
from zkmarek.video.slides.common.test_slide import \
    TestSlide  # noqa: F401 # pyright: ignore
from zkmarek.video.slides.common.tex_slide import TexSlide
from zkmarek.video.slides.ec.addition_to_infinity import AdditionToInfinity
from zkmarek.video.slides.ec.signature import Signature
from zkmarek.video.slides.ec.standards import Standards
from zkmarek.video.slides.ec.subgroups import Subgroups
from zkmarek.video.slides.prime_fields import PrimeFields
from zkmarek.video.utils import get_slides_from_names

config.width = 16
config.height = 9

SLIDES = [
    TitleSlide("Elliptic Curves"),
    EquationSlide(),
    CECOperations(),
    CECNegation(),
    CECAddition(),

    TitleSlide("Prime Fields"),
    PrimeFields(),
    CodeSlide("Example amateur implementation", "data/pf/field.py"),
    CodeSlide("Example pro implementation", "data/pf/add.rs", language="rust"),
    ImageSlide("Extended Euclidean algorithm", "data/pf/xgcd.png"),
    CodeSlide("Extended Euclidean algorithm", "data/pf/xgcd.py"),
    ImageSlide(
        "Square root", "data/pf/sqrt.png", image_scale=0.7
    ),
    CodeSlide("Tonelli Shanks algorithm", "data/pf/sqrt.py"),
    TitleSlide("Discrete Elliptic Curves"),
    ECIntroduction(),
    ECNegation(),
    ECAddition(),
    AdditionToInfinity(),

    TitleSlide("Multiplication by scalar"),
    CodeSlide("Double and add", "data/ec/double_and_add.py"),
    CodeSlide("Double and always add", "data/ec/double_and_always_add.py"),

    TitleSlide("Subgroups"),
    Subgroups(),

    TitleSlide("Elliptic Curve Standards"),
    Standards(),

    TexSlide("Discrete Elliptic Curves operations", "data/ec/operations.tex"),
    ImageSlide("Groups", "data/groups.png", image_scale=0.85),

    TitleSlide("Signatures"),
    Signature(),
    CodeSlide("Recover", "data/ec/recover.sol", language="solidity"),

    TitleSlide("Coordination systems"),
    ImageSlide(
        "Coordination systems", "data/ec/coords_conversions.png", image_scale=0.75
    ),
    ImageSlide("Coordination systems (costs)", "data/ec/coords_costs.png"),
    TitleSlide("Constant time operations"),
    CodeSlide("Constant time conditional swap", "data/ct/cswap.py", language="python"),
    CodeSlide("Constant time equal", "data/ct/ct_eq.rs", language="rust"),
]


class EllipticCurves(Scene):
    def construct(self):
        slides = get_slides_from_names(
            dict(os.environ).get("SLIDES"), SLIDES, globals()
        )
        presentation = Presentation(self, SLIDES, slides)
        presentation.print_slides()
        presentation.play()
