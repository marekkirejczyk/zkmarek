# from zkmarek.video.slides.common.intro import Intro
from zkmarek.video.slides.e7.recap import Recap
from zkmarek.video.slides.e7.vec_com import Previously
from zkmarek.video.slides.e7.watch_other import FullVideos
from zkmarek.video.slides.common.title import TitleSlide
from zkmarek.video.slides.e7.elliptic_curves import EllipticCurves
from zkmarek.video.slides.e7.single_level_verkle import SingleLevelVerkleTree

EPISODE7 = [
    # Intro(
    #     sound="data/sound/episode3/slide0-0.mp3",
    #     background_sound="data/sound/e7/background.mp3",
    # ),
    Recap(),
    Previously(),
    FullVideos(),
    TitleSlide("Elliptic curves", sound = "data/sound/e7/slide2-0.mp3", pre_wait_time=1, wait_time=4.5),
    EllipticCurves(),
    TitleSlide("Verkle trees", sound = "data/sound/e7/slide2-10.mp3", wait_time=2),
    SingleLevelVerkleTree(),
]