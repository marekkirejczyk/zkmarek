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
from zkmarek.video.slides.ec.digital_signature_interface import (
    DigitalSignatureInterface,
)
from zkmarek.video.slides.ec.double_and_add import DoubleAndAdd
from zkmarek.video.slides.ec.operations import Operations
from zkmarek.video.slides.ec.scalar_mulitplication import ScalarMultiplication
from zkmarek.video.slides.ec.signature import Signature
from zkmarek.video.slides.ec.standards import Standards
from zkmarek.video.slides.ec.subgroups import Subgroups
from zkmarek.video.slides.episode3.KZG import KZG
from zkmarek.video.slides.episode3.PCS import PolynomialCommitment
from zkmarek.video.slides.episode3.verkle import Verkle
from zkmarek.video.slides.episode3.ceremony import Ceremony
from zkmarek.video.slides.episode3.ceremony_verification import CeremonyVerification
from zkmarek.video.slides.episode3.ceremony_verification_2 import CeremonyVerification2
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
from zkmarek.video.slides.episode2.previously import PreviouslyOn
from zkmarek.video.slides.episode2.support import Sponsored
from zkmarek.video.slides.episode2.credits import Credits as Credits2
from zkmarek.video.slides.episode2.deterministic import Deterministic
from zkmarek.video.slides.episode2.ecdsa import ECDSA
from zkmarek.video.slides.episode2.ecdsarec import ECDSARec
from zkmarek.video.slides.teaser2.eth_teaser import EthereumTransaction as ETHteaser
from zkmarek.video.slides.teaser2.ec_rec_teaser import ECRecoverSlide as ECRteaser
from zkmarek.video.slides.teaser2.sponsored import Sponsored as SponsoredTeaser
from zkmarek.video.slides.teaser3.signature import SignatureMath
from zkmarek.video.slides.teaser3.intuition import Intuition
from zkmarek.video.slides.teaser3.previously import Episode2Reference

config.width = 16
config.height = 9


TEASER = [
    Intro(
        sound="data/sound/teaser/s1.wav",
        background_sound="data/sound/teaser/background.mp3",
    ),
    TitleSlide("Episode 1", subtitle="Teaser"),
    ZKPSTitle(),
    SeasonTeaser(),
    ECCTitleSlide(),
    ECRecoverSlideTeaser(),
    EthereumTransactionTeaser(),
    ListSlide(),
    Subscribe("data/sound/teaser/s8.wav"),
]

EPISODE1 = [
    Intro(
        sound="data/sound/episode1/s1.wav",
        background_sound="data/sound/episode1/background.m4a",
    ),
    TitleSlide(
        "Elliptic curves",
        subtitle="in Ethereum wallet",
        sound="data/sound/episode1/s2-1.wav",
    ),
    TeaserReference(),
    InThisEpisode(),
    TitleSlide("Elliptic Curves", sound="data/sound/episode1/s5.wav"),
    EquationSlide(),
    CECOperations(),
    CECNegation(),
    CECAddition(),
    TitleSlide("Prime Fields", sound="data/sound/episode1/s10.wav"),
    PrimeFields(),
    TitleSlide(
        "Discrete Elliptic Curves", pre_wait_time=2, sound="data/sound/episode1/s12.m4a"
    ),
    ECIntroduction(),
    TitleSlide(
        "Discrete Elliptic Curves Operations",
        pre_wait_time=2,
        sound="data/sound/episode1/s14.wav",
    ),
    ECNegation(),
    ECAddition(),
    AdditionToInfinity(),
    TitleSlide(
        "Scalar multiplication", pre_wait_time=2, sound="data/sound/episode1/s18.m4a"
    ),
    ScalarMultiplication(),
    DoubleAndAdd(),
    TitleSlide("Subgroups", sound="data/sound/episode1/s21.m4a"),
    Subgroups(),
    Operations(),
    TitleSlide("Elliptic Curve Standards", sound="data/sound/episode1/s24.m4a"),
    Standards(),
    TitleSlide("Ethereum Wallet", pre_wait_time=3, sound="data/sound/episode1/s26.wav"),
    WalletSlide(),
    Subscribe("data/sound/episode1/s28.wav"),
    Credits(),
]

TEASER2 = [
    Intro(
        sound="data/sound/teaser2/slide0-0.mp3",
        background_sound="data/sound/teaser2/backgroundt.mp3",
    ),
    SponsoredTeaser(),
    ECRteaser(),
    ETHteaser(),
    Subscribe("data/sound/teaser2/slide2-0.mp3"),
]

EPISODE2 = [
    Intro(
        sound="data/sound/episode2/slide1-0.mp3",
        background_sound="data/sound/episode2/background.mp3",
    ),
    Sponsored(),
    PreviouslyOn(),
    TitleSlide(
        "Digital Signature Algorithm",
        pre_wait_time=1.5,
        sound="data/sound/episode2/slide4-0.mp3",
    ),
    DigitalSignatureInterface(),
    Signature(),
    Deterministic(),
    ECRecoverSlide(),
    EthereumTransaction(),
    ECDSA("ECDSA sign", "data/ec/signature.py"),
    ECDSARec("ECDSA Recover", "data/ec/recover.py"),
    Subscribe("data/sound/episode1/s28.wav"),
    Credits2(),
]

TEASER3 = [
    Intro(
        sound="data/sound/teaser2/slide0-0.mp3",
        background_sound="data/sound/teaser2/backgroundt.mp3",
    ),
    Sponsored(),
    TitleSlide(
        "Intuition behind digital signature", sound="data/sound/teaser3/slide3.mp3"
    ),
    Intuition(),
]

EPISODE3 = [
    # Intro(sound="data/sound/teaser2/slide0-0.mp3"),
    # Sponsored(),
    TitleSlide("Pairing"),
    Pairing(),
    TitleSlide("Trusted setup"),
    TrustedSetup(),
    Ceremony(),
    CeremonyVerification(),
    CeremonyVerification2(),
    TitleSlide("KZG", subtitle="Kate, Zaverucha and Goldberg"),
    PolynomialCommitment(),
    KZG(),
    Verkle(),
    Subscribe("data/sound/episode1/s28.wav"),
    Credits2(),
]

EPISODE4 = [
    # Intro("data/sound/episode2/slide1-0.mp3"),
    # Sponsored(),
    Verkle(),
    Subscribe("data/sound/episode1/s28.wav"),
]

EPISODE5 = [
    SchnorrSlide(),
    CodeSlide("Verify Schnorr signature with ECRecover ", "data/schnorr/schnorr.sol"),
    TexSlide("Sources", "data/schnorr/sources.tex"),
]

DECKS = {
    "TEASER": TEASER,
    "E1": EPISODE1,
    "T2": TEASER2,
    "E2": EPISODE2,
    "T3": TEASER3,
    "E3": EPISODE3,
    "E4": EPISODE4,
    "E5": EPISODE5,
}

DEFAULT_DECK = "T3"


class EllipticCurves(Scene):
    def construct(self):
        register_font("data/brand/Oxanium-Regular.ttf")

        name = get_deck_name(DEFAULT_DECK)
        deck = DECKS[name]

        env_slides = dict(os.environ).get("SLIDES")
        slides = get_slides_from_names(env_slides, deck, globals())
        presentation = Presentation(self, deck, slides)
        presentation.print_slides(name)
        presentation.play()
