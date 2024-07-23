from zkmarek.video.slides.episode3.ceremony import Ceremony
from zkmarek.video.slides.episode3.ceremony_verification import CeremonyVerification
from zkmarek.video.slides.episode3.ceremony_verification_2 import CeremonyVerification2
from zkmarek.video.slides.episode3.pairing import Pairing
from zkmarek.video.slides.episode3.trusted_setup import TrustedSetup
from zkmarek.video.slides.episode3.introduction import Introduction
from zkmarek.video.slides.episode3.polynomial import Polynomial
from zkmarek.video.slides.episode3.toxic import ToxicWaste
from zkmarek.video.slides.episode3.credits import Credits as CreditsE3
from zkmarek.video.slides.intro import Intro
from zkmarek.video.slides.episode2.support import Sponsored
from slides.common.title import TitleSlide
from zkmarek.video.slides.common.subscribe import Subscribe

EPISODE3 = [
    Intro(sound="data/sound/episode3/slide0-0.mp3", background_sound="data/sound/episode3/background.mp3",),
    Sponsored(),
    Introduction(),
    TitleSlide("Pairing", sound="data/sound/episode3/slide1-4.mp3", wait_time=3.5),
    Pairing(),
    TitleSlide("Trusted setup", sound="data/sound/episode3/slide3-0.mp3", wait_time=1.5),
    TrustedSetup(),
    TitleSlide("Ceremony", sound="data/sound/episode3/slide4-4.mp3", wait_time=3),
    Ceremony(),
    CeremonyVerification(),
    CeremonyVerification2(),
    ToxicWaste(),
    Polynomial(),
    Subscribe("data/sound/episode1/s28.wav"),
    CreditsE3(),
]