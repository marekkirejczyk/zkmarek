from zkmarek.video.slides.e6.merkle import MerkleTree
from zkmarek.video.slides.episode2.support import Sponsored
from zkmarek.video.slides.common.intro import Intro
# from zkmarek.video.slides.common.subscribe import Subscribe
from zkmarek.video.slides.common.title import TitleSlide

EPISODE6 = [
    Intro(sound="data/sound/episode3/slide0-0.mp3", background_sound="data/sound/e5/background.mp3",),
    Sponsored(),
    TitleSlide("Merkle trees", sound="data/sound/e6/slide2-0beg.mp3", wait_time=4),
    MerkleTree(),
]