from zkmarek.video.slides.episode3.ceremony import Ceremony
from zkmarek.video.slides.episode3.ceremony_verification import CeremonyVerification
from zkmarek.video.slides.episode3.ceremony_verification_2 import CeremonyVerification2
from zkmarek.video.slides.episode3.pairing import Pairing
from zkmarek.video.slides.episode3.trusted_setup import TrustedSetup
from zkmarek.video.slides.episode3.introduction import Introduction
from zkmarek.video.slides.episode3.polynomial import Polynomial
from zkmarek.video.slides.episode3.toxic import ToxicWaste
from zkmarek.video.slides.episode3.credits import Credits as CreditsE3
from zkmarek.video.slides.common.intro import Intro
from zkmarek.video.slides.common.subscribe import Subscribe
from zkmarek.video.slides.common.title import TitleSlide
from zkmarek.video.slides.episode2.support import Sponsored

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