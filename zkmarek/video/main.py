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
from zkmarek.video.slides.common.code_slide import CodeSlide

from zkmarek.video.slides.common.subscribe import Subscribe
from zkmarek.video.slides.common.tex_slide import TexSlide
from zkmarek.video.slides.credits import Credits
from zkmarek.video.slides.ec.addition_to_infinity import AdditionToInfinity
from zkmarek.video.slides.ec.digital_signature_interface import DigitalSignatureInterface
from zkmarek.video.slides.ec.double_and_add import DoubleAndAdd
from zkmarek.video.slides.ec.operations import Operations
from zkmarek.video.slides.ec.scalar_mulitplication import ScalarMultiplication
from zkmarek.video.slides.ec.signature import Signature
from zkmarek.video.slides.ec.standards import Standards
from zkmarek.video.slides.ec.subgroups import Subgroups
from zkmarek.video.slides.episode3.KZG import KZG
from zkmarek.video.slides.episode3.ceremony import Ceremony
from zkmarek.video.slides.episode3.ceremony_verification import CeremonyVerification
from zkmarek.video.slides.episode3.pairing import Pairing
from zkmarek.video.slides.episode3.trusted_setup import TrustedSetup
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
from zkmarek.video.slides.episode2.schnorr import SchnorrSlide

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
    #PreviouslyOn(),
    TitleSlide("Digital Signature Algorithm", pre_wait_time=1.5),
    DigitalSignatureInterface(),
    Signature(),
    TexSlide("Deterministic signature", "data/ec/deterministic_signature.tex"),
    ECRecoverSlide(),
    EthereumTransaction(),
    CodeSlide("ECDSA sign", "data/ec/signature.py"),
    CodeSlide("ecrecover", "data/ec/recover.py"),
    SchnorrSlide(),
    CodeSlide("Verify Schnorr signature with ECRecover ", "data/schnorr/schnorr.sol"),
    TexSlide("Sources", "data/schnorr/sources.tex"),
    Subscribe("data/sound/episode1/s28.wav")
]

EPISODE3 = [
    TitleSlide("Pairing"),
    Pairing(),
    TitleSlide("Trusted setup"),
    TrustedSetup(),
    Ceremony(),
    CeremonyVerification(),
    TitleSlide("KZG", subtitle="Kate, Zaverucha and Goldberg"),
    KZG()
]

DECKS = {
    "TEASER": TEASER,
    "E1": EPISODE1,
    "E2": EPISODE2,
    "E3": EPISODE3,
}

DEFAULT_DECK = "E3"


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
