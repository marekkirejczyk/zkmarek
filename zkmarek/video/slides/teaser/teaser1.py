from zkmarek.video.slides.teaser.list import ListSlide
from zkmarek.video.slides.teaser.season_teaser import SeasonTeaser
from zkmarek.video.slides.teaser.zkps_title import ZKPSTitle
from zkmarek.video.slides.teaser.ecrecover import ECRecoverSlideTeaser
from zkmarek.video.slides.teaser.ethereum_transaction import EthereumTransactionTeaser
from zkmarek.video.slides.teaser.ecc_title import ECCTitleSlide
from slides.common.title import TitleSlide
from zkmarek.video.slides.common.intro import Intro
from zkmarek.video.slides.common.subscribe import Subscribe

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