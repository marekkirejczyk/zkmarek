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
from zkmarek.video.slides.credits import Credits
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
from zkmarek.video.slides.teaser_reference import TeaserReference
from zkmarek.video.slides.wallet import WalletSlide
from zkmarek.video.utils import get_slides_from_names, get_deck_name

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
    Subscribe("data/sound/teaser/s8.wav")
]

EPISODE1 = [
    Intro(),
    TitleSlide(
        "Elliptic curves",
        subtitle="in Ethereum wallet",
        sound="data/sound/episode1/s2-1.wav"),
    TeaserReference(),
    InThisEpisode(),
    TitleSlide("Elliptic Curves", sound="data/sound/episode1/s5.wav"),
    EquationSlide(),
    CECOperations(),
    CECNegation(),
    CECAddition(),

    TitleSlide("Prime Fields",
        sound="data/sound/episode1/s10.wav"),
    PrimeFields(),

    TitleSlide("Discrete Elliptic Curves", pre_wait_time=2,
        sound="data/sound/episode1/s12.m4a"),
    ECIntroduction(),
    TitleSlide("Discrete Elliptic Curves Operations", pre_wait_time=2,
        sound="data/sound/episode1/s14.wav"),

    ECNegation(),
    ECAddition(),
    AdditionToInfinity(),

    TitleSlide("Scalar multiplication", pre_wait_time=2,
        sound="data/sound/episode1/s18.m4a"),
    ScalarMultiplication(),
    DoubleAndAdd(),

    TitleSlide("Subgroups", sound="data/sound/episode1/s21.m4a"),
    Subgroups(),

    Operations(),
    TitleSlide("Elliptic Curve Standards",
        sound="data/sound/episode1/s24.m4a"),
    Standards(),
    TitleSlide("Ethereum Wallet", pre_wait_time=3, sound="data/sound/episode1/s26.wav"),
    WalletSlide(),
    Subscribe("data/sound/episode1/s28.wav"),
    Credits()
]

EPISODE2 = [
    Intro(),
    TitleSlide("Digital Signature Algorithm", pre_wait_time=1.5,
        sound="data/sound/episode2/s26.wav"),
    Signature(),
    ECRecoverSlide(),
    EthereumTransaction(),
    Subscribe("data/sound/episode1/s30.wav")
]

DECKS = {
    "TEASER": TEASER,
    "E1": EPISODE1,
    "E2": EPISODE2,
}

DEFAULT_DECK = "E1"


class EllipticCurves(Scene):
    def construct(self):
        register_font('data/brand/Oxanium-Regular.ttf')

        name = get_deck_name(DEFAULT_DECK)
        deck = DECKS[name]

        env_slides = dict(os.environ).get("SLIDES")
        slides = get_slides_from_names(env_slides, deck, globals())
        presentation = Presentation(self, deck, slides)
        presentation.print_slides(name)
        presentation.play()
