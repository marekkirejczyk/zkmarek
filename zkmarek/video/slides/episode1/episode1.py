from slides.episode1.cec.addition import Addition as CECAddition
from slides.episode1.cec.negation import Negation as CECNegation
from slides.episode1.cec.operations import Operations as CECOperations
from slides.common.title import TitleSlide
from zkmarek.video.slides.episode1.addition import Addition as ECAddition
from zkmarek.video.slides.episode1.introduction import Introduction as ECIntroduction
from zkmarek.video.slides.episode1.negation import Negation as ECNegation
from zkmarek.video.slides.episode1.equation import EquationSlide
from zkmarek.video.slides.common.subscribe import Subscribe
from zkmarek.video.slides.common.credits import Credits
from zkmarek.video.slides.episode1.addition_to_infinity import AdditionToInfinity
from zkmarek.video.slides.episode1.double_and_add import DoubleAndAdd
from zkmarek.video.slides.episode1.operations import Operations
from zkmarek.video.slides.episode1.scalar_mulitplication import ScalarMultiplication
from zkmarek.video.slides.episode1.in_this_episode import InThisEpisode
from zkmarek.video.slides.common.intro import Intro
from zkmarek.video.slides.episode1.prime_fields import PrimeFields
from zkmarek.video.slides.episode1.standards import Standards
from zkmarek.video.slides.episode1.subgroups import Subgroups
from zkmarek.video.slides.episode1.teaser_reference import TeaserReference
from zkmarek.video.slides.episode1.wallet import WalletSlide

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