from zkmarek.video.slides.teaser3.intuition import Intuition
from zkmarek.video.slides.teaser3.credits import Credits as CreditsT3
from zkmarek.video.slides.teaser3.e2_reference import TitleSlide as E2Reference
from zkmarek.video.slides.episode2.support import Sponsored
from zkmarek.video.slides.common.intro import Intro
from zkmarek.video.slides.common.subscribe import Subscribe

TEASER3 = [
    Intro(sound="data/sound/teaser3/slide0-0.mp3", background_sound="data/sound/teaser3/background.mp3"),
    Sponsored(),
    E2Reference("Intuition behind digital signature", sound="data/sound/teaser3/slide3.mp3", pre_wait_time=1.5),
    Intuition(),
    Subscribe("data/sound/episode1/s28.wav"),
    CreditsT3(),
]