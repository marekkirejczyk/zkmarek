import os

from manim import Scene, config
from manimpango import register_font
from presentation import Presentation
from slides.cec.addition import Addition as CECAddition
from slides.cec.negation import Negation as CECNegation
from slides.cec.operations import Operations as CECOperations
from slides.common.title import TitleSlide
from slides.ec.addition import Addition as ECAddition
from slides.ec.introduction import Introduction as ECIntroduction
from slides.ec.negation import Negation as ECNegation
from slides.equation import EquationSlide

from zkmarek.video.slides.common.subscribe import Subscribe
from zkmarek.video.slides.debug.code_style_slide import \
    CodeStyleSlide  # noqa: F401 # pyright: ignore
from zkmarek.video.slides.debug.font_slide import \
    FontSlide  # noqa: F401 # pyright: ignore
from zkmarek.video.slides.debug.test_slide import \
    TestSlide  # noqa: F401 # pyright: ignore
from zkmarek.video.slides.ec.addition_to_infinity import AdditionToInfinity
from zkmarek.video.slides.ec.double_and_add import DoubleAndAdd
from zkmarek.video.slides.ec.operations import Operations
from zkmarek.video.slides.ec.scalar_mulitplication import ScalarMultiplication
from zkmarek.video.slides.ec.signature import Signature
from zkmarek.video.slides.ec.standards import Standards
from zkmarek.video.slides.ec.subgroups import Subgroups
from zkmarek.video.slides.eth.ecrecover import ECRecoverSlide
from zkmarek.video.slides.eth.ethereum_transaction import EthereumTransaction
from zkmarek.video.slides.teaser.ecrecover import ECRecoverSlideTeaser
from zkmarek.video.slides.teaser.ethereum_transaction import EthereumTransactionTeaser
from zkmarek.video.slides.teaser.ecc_title import ECCTitleSlide
from zkmarek.video.slides.teaser.in_this_episode import InThisEpisode
from zkmarek.video.slides.intro import Intro
from zkmarek.video.slides.prime_fields import PrimeFields
from zkmarek.video.slides.teaser.list import ListSlide
from zkmarek.video.slides.teaser.season_teaser import SeasonTeaser
from zkmarek.video.slides.teaser.zkps_title import ZKPSTitle
from zkmarek.video.utils import get_slides_from_names

config.width = 16
config.height = 9

TEASER = [
    Intro(),
    TitleSlide(
        "Episode 1",
        subtitle="Teaser"),
    ZKPSTitle(),
    SeasonTeaser(),
    ECCTitleSlide(),
    ECRecoverSlideTeaser(),
    EthereumTransactionTeaser(),
    ListSlide(),
    Subscribe()
]

MAIN_SLIDES = [
    Intro(),
    TitleSlide(
        "Elliptic curves and Digital signature",
        subtitle="used in Ethereum",
        sound="data/sound/episode/s2.wav"),
    InThisEpisode(),
    TitleSlide("Elliptic Curves", sound="data/sound/episode/s4.wav"),
    EquationSlide(),
    CECOperations(),
    CECNegation(),
    CECAddition(),

    TitleSlide("Prime Fields", post_wait_time=2,
        sound="data/sound/episode/s9.wav"),
    PrimeFields(),

    TitleSlide("Discrete Elliptic Curves", pre_wait_time=2,
        sound="data/sound/episode/s11.m4a"),
    ECIntroduction(),
    TitleSlide("Discrete Elliptic Curves Operations", pre_wait_time=2,
        sound="data/sound/episode/s13.wav"),

    ECNegation(),
    ECAddition(),
    AdditionToInfinity(),

    TitleSlide("Scalar multiplication", pre_wait_time=2,
        sound="data/sound/episode/s17.m4a"),
    ScalarMultiplication(),
    DoubleAndAdd(),

    TitleSlide("Subgroups", sound="data/sound/episode/s20.m4a"),
    Subgroups(),

    Operations(),
    TitleSlide("Elliptic Curve Standards",
        sound="data/sound/episode/s23.m4a"),
    Standards(),

    TitleSlide("Digital Signature", pre_wait_time=1.5,
        post_wait_time=3, sound="data/sound/episode/s25.wav"),
    Signature(),
    EthereumTransaction(),
    ECRecoverSlide(),

    Subscribe()
]

SLIDES = MAIN_SLIDES

class EllipticCurves(Scene):
    def construct(self):
        register_font('data/brand/Oxanium-Regular.ttf')
        slides = get_slides_from_names(
            dict(os.environ).get("SLIDES"), SLIDES, globals()
        )
        presentation = Presentation(self, SLIDES, slides)
        presentation.print_slides()
        presentation.play()
