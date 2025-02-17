from zkmarek.video.slides.episode4.proof2 import Verification
from zkmarek.video.slides.episode4.proof import Proof1
from zkmarek.video.slides.episode4.polynomials import Polynomials
from zkmarek.video.slides.episode4.commitment import Commitment
from zkmarek.video.slides.episode4.e3_reference import Episode3Reference
from zkmarek.video.slides.episode4.credits import Credits as CreditsE4
from zkmarek.video.slides.episode4.security import Security
from zkmarek.video.slides.episode4.kzg import KZG
from zkmarek.video.slides.common.intro import Intro
from zkmarek.video.slides.common.subscribe import Subscribe
from zkmarek.video.slides.common.title import TitleSlide
from zkmarek.video.slides.episode2.support import Sponsored

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