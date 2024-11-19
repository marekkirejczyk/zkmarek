import os

from manim import Scene, config
from manimpango import register_font
from presentation import Presentation
from zkmarek.video.utils import get_slides_from_names, get_deck_name
from slides.episode1.cec.addition import Addition as CECAddition
from slides.episode1.cec.negation import Negation as CECNegation
from slides.episode1.cec.operations import Operations as CECOperations
from slides.common.title import TitleSlide
from zkmarek.video.slides.episode1.addition import Addition as ECAddition
from zkmarek.video.slides.episode1.introduction import Introduction as ECIntroduction
from zkmarek.video.slides.episode1.negation import Negation as ECNegation
from zkmarek.video.slides.episode1.equation import EquationSlide
from zkmarek.video.slides.common.code_slide import CodeSlide
from zkmarek.video.slides.common.subscribe import Subscribe
from zkmarek.video.slides.common.tex_slide import TexSlide
from zkmarek.video.slides.common.credits import Credits
from zkmarek.video.slides.episode1.addition_to_infinity import AdditionToInfinity
from zkmarek.video.slides.episode2.digital_signature_interface import DigitalSignatureInterface
from zkmarek.video.slides.episode1.double_and_add import DoubleAndAdd
from zkmarek.video.slides.episode1.operations import Operations
from zkmarek.video.slides.episode1.scalar_mulitplication import ScalarMultiplication
from zkmarek.video.slides.episode2.signature import Signature
from zkmarek.video.slides.episode1.standards import Standards
from zkmarek.video.slides.episode1.subgroups import Subgroups
from zkmarek.video.slides.episode2.ecrecover import ECRecoverSlide
from zkmarek.video.slides.episode2.ethereum_transaction import EthereumTransaction
from zkmarek.video.slides.teaser.ecrecover import ECRecoverSlideTeaser
from zkmarek.video.slides.teaser.ethereum_transaction import EthereumTransactionTeaser
from zkmarek.video.slides.teaser.ecc_title import ECCTitleSlide
from zkmarek.video.slides.episode1.in_this_episode import InThisEpisode
from zkmarek.video.slides.common.intro import Intro
from zkmarek.video.slides.episode1.prime_fields import PrimeFields
from zkmarek.video.slides.teaser.list import ListSlide
from zkmarek.video.slides.teaser.season_teaser import SeasonTeaser
from zkmarek.video.slides.teaser.zkps_title import ZKPSTitle
from zkmarek.video.slides.episode1.teaser_reference import TeaserReference
from zkmarek.video.slides.episode1.wallet import WalletSlide
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
from zkmarek.video.slides.teaser3.intuition import Intuition
from zkmarek.video.slides.teaser3.credits import Credits as CreditsT3
from zkmarek.video.slides.teaser3.e2_reference import TitleSlide as E2Reference
from zkmarek.video.slides.episode3.ceremony import Ceremony
from zkmarek.video.slides.episode3.ceremony_verification import CeremonyVerification
from zkmarek.video.slides.episode3.ceremony_verification_2 import CeremonyVerification2
from zkmarek.video.slides.episode3.pairing import Pairing
from zkmarek.video.slides.episode3.trusted_setup import TrustedSetup
from zkmarek.video.slides.episode3.introduction import Introduction
from zkmarek.video.slides.episode3.polynomial import Polynomial
from zkmarek.video.slides.episode3.toxic import ToxicWaste
from zkmarek.video.slides.episode3.credits import Credits as CreditsE3
from zkmarek.video.slides.e4.proof2 import Verification
from zkmarek.video.slides.e4.proof import Proof1
from zkmarek.video.slides.e4.polynomials import Polynomials
from zkmarek.video.slides.e4.commitment import Commitment
from zkmarek.video.slides.e4.e3_reference import Episode3Reference
from zkmarek.video.slides.e4.credits import Credits as CreditsE4
from zkmarek.video.slides.e4.security import Security
from zkmarek.video.slides.e4.kzg import KZG
from zkmarek.video.slides.e5.e4reference import Episode4Recap
from zkmarek.video.slides.e5.layer2 import Layer2
from zkmarek.video.slides.e5.blobs import Blobs
from zkmarek.video.slides.e5.vectorcommitments import VectorCommitments
from zkmarek.video.slides.e5.kzg import KZGBlobs
from zkmarek.video.slides.e5.blobs_kzg import KZGBlobs2
config.width = 16
config.height = 9


TEASER = [
    Intro(sound="data/sound/teaser/s1.wav", background_sound="data/sound/teaser/background.mp3"),
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
    Intro(sound="data/sound/episode1/s1.wav", background_sound="data/sound/episode1/background.m4a"),
    TitleSlide("Elliptic curves", subtitle="in Ethereum wallet", sound="data/sound/episode1/s2-1.wav"),
    TeaserReference(),
    InThisEpisode(),
    TitleSlide("Elliptic Curves", sound="data/sound/episode1/s5.wav"),
    EquationSlide(),
    CECOperations(),
    CECNegation(),
    CECAddition(),
    TitleSlide("Prime Fields", sound="data/sound/episode1/s10.wav"),
    PrimeFields(),
    TitleSlide("Discrete Elliptic Curves", pre_wait_time=2, sound="data/sound/episode1/s12.m4a"),
    ECIntroduction(),
    TitleSlide("Discrete Elliptic Curves Operations", pre_wait_time=2, sound="data/sound/episode1/s14.wav"),
    ECNegation(),
    ECAddition(),
    AdditionToInfinity(),
    TitleSlide("Scalar multiplication", pre_wait_time=2, sound="data/sound/episode1/s18.m4a"),
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
    Intro(sound="data/sound/teaser2/slide0-0.mp3", background_sound="data/sound/teaser2/backgroundt.mp3"),
    SponsoredTeaser(),
    ECRteaser(),
    ETHteaser(),
    Subscribe("data/sound/teaser2/slide2-0.mp3"),
]

EPISODE2 = [
    Intro(sound="data/sound/episode2/slide1-0.mp3", background_sound="data/sound/episode2/background.mp3"),
    Sponsored(),
    PreviouslyOn(),
    TitleSlide("Digital Signature Algorithm", pre_wait_time=1.5, sound="data/sound/episode2/slide4-0.mp3"),
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
    Intro(sound="data/sound/teaser3/slide0-0.mp3", background_sound="data/sound/teaser3/background.mp3"),
    Sponsored(),
    E2Reference("Intuition behind digital signature", sound="data/sound/teaser3/slide3.mp3", pre_wait_time=1.5),
    Intuition(),
    Subscribe("data/sound/episode1/s28.wav"),
    CreditsT3(),
]

EPISODE3 = [
    Intro(sound="data/sound/episode3/slide0-0.mp3", background_sound="data/sound/episode3/background.mp3",),
    Sponsored(),
    Introduction(),
    TitleSlide("Trusted setup", sound="data/sound/episode3_1/slide3-0_new.mp3", wait_time=1.5),
    TrustedSetup(),
    TitleSlide("Ceremony", sound="data/sound/episode3/slide4-4.mp3", wait_time=3),
    Ceremony(),
    TitleSlide("Pairing", sound="data/sound/episode3_1/slide1_4_new.mp3", wait_time=3.5),
    Pairing(),
    CeremonyVerification(),
    CeremonyVerification2(),
    TitleSlide("Toxic Waste", sound="data/sound/episode3_1/slide7.5-00.mp3", wait_time=1.5),
    ToxicWaste(),
    TitleSlide("The use of trusted setup", sound="data/sound/episode3_1/slide8-00.mp3", wait_time=1),
    Polynomial(),
    Subscribe("data/sound/episode1/s28.wav"),
    CreditsE3(),
]

EPISODE4 = [    
    Intro(sound="data/sound/episode3/slide0-0.mp3", background_sound="data/sound/e4/background.mp3",),
    Sponsored(),
    Episode3Reference(),
    TitleSlide("Polynomials", sound="data/sound/e4/slide0-5.mp3", wait_time=5),
    Polynomials(),
    TitleSlide("Polynomial Commitments", sound="data/sound/e4/slide2-0a.mp3", wait_time=2),
    Commitment(),
    TitleSlide("KZG Commitment Scheme", subtitle="Kate, Zaverucha, Goldberg (2010)", sound = "data/sound/e4/slide2-4.mp3"),
    KZG(),
    TitleSlide("Proof", sound = "data/sound/e4/slide3-0.mp3", wait_time=0.5),
    Proof1(),
    Verification(),
    TitleSlide("Security", sound = "data/sound/e4/slide5-0.mp3", wait_time=2),
    Security(),
    Subscribe("data/sound/episode1/s28.wav"),
    CreditsE4(),
]

EPISODE5 = [
    # Sponsored(),
    Episode4Recap(),
    TitleSlide("Layer 2", subtitle="ZK rollups", sound="data/sound/e5/slide1-0.mp3", wait_time=3),
    Layer2(),
    TitleSlide("Blobs", subtitle="Binary Large OBject", sound="data/sound/e5/slide1-3.mp3", wait_time=2),
    Blobs(),
    TitleSlide("Vector commitments", sound = "data/sound/e5/slide3-0a.mp3"),
    VectorCommitments(),
    KZGBlobs(),
    TitleSlide("KZG in blobs", sound = "data/sound/e5/slide5-0.mp3", wait_time=2),
    KZGBlobs2(),
]

EPISODE6 = [
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
    "E6": EPISODE6,
}

DEFAULT_DECK = "E5"


class Episode5(Scene):
    def construct(self):
        register_font("data/brand/Oxanium-Regular.ttf")

        name = get_deck_name(DEFAULT_DECK)
        deck = DECKS[name]

        env_slides = dict(os.environ).get("SLIDES")
        slides = get_slides_from_names(env_slides, deck, globals())
        presentation = Presentation(self, deck, slides)
        presentation.print_slides(name)
        presentation.play()
