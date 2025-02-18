from zkmarek.video.slides.teaser2.eth_teaser import EthereumTransaction as ETHteaser
from zkmarek.video.slides.teaser2.ec_rec_teaser import ECRecoverSlide as ECRteaser
from zkmarek.video.slides.teaser2.sponsored import Sponsored as SponsoredTeaser
from zkmarek.video.slides.common.intro import Intro
from zkmarek.video.slides.common.subscribe import Subscribe

TEASER2 = [
    Intro(sound="data/sound/teaser2/slide0-0.mp3", background_sound="data/sound/teaser2/backgroundt.mp3"),
    SponsoredTeaser(),
    ECRteaser(),
    ETHteaser(),
    Subscribe("data/sound/teaser2/slide2-0.mp3"),
]