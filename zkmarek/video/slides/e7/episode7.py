from zkmarek.video.slides.common.intro import Intro
from zkmarek.video.slides.episode2.support import Sponsored
from zkmarek.video.slides.e7.recap import Recap
from zkmarek.video.slides.e7.watch_other import FullVideos
from zkmarek.video.slides.common.title import TitleSlide
from zkmarek.video.slides.e7.elliptic_curves import EllipticCurves
from zkmarek.video.slides.e7.single_level_verkle import SingleLevelVerkleTree
from zkmarek.video.slides.e7.three_level_vt import ThreeLevelVerkleTree
from zkmarek.video.slides.e7.proofs import Proofs
from zkmarek.video.slides.e7.multiproofs import Multiproofs
from zkmarek.video.slides.e7.code_multiproofs import Multiproofs as CodeMultiproofs
from zkmarek.video.slides.e7.final_season1 import FinalSeason1
from zkmarek.video.slides.e7.merkle_verkle import MerkleVerkle
from zkmarek.video.slides.e6.credits import Credits
from zkmarek.video.slides.common.subscribe import Subscribe

EPISODE7 = [
    Intro(
        sound="data/sound/e7/slide0-0.mp3",
        background_sound="data/sound/e7/background.mp3",
    ),
    Sponsored(),
    FinalSeason1(),
    TitleSlide("Verkle Trees", wait_time=1.5),
    Recap(),
    FullVideos(),
    TitleSlide("Elliptic curves", sound = "data/sound/e7/slide2-0.mp3", 
               wait_time=2, subtitle="in the Verkle trees", wait_time_for_subtitle=1),
    EllipticCurves(),
    TitleSlide("Verkle trees", sound = "data/sound/e7/slide2-7.mp3", wait_time=2),
    SingleLevelVerkleTree(),
    TitleSlide("Multi-level Verkle Tree", sound = "data/sound/e7/slide4-0.mp3", wait_time=2),
    ThreeLevelVerkleTree(),
    TitleSlide("Proofs", sound = "data/sound/e7/slide5-0.mp3", wait_time=2),
    Proofs(),
    TitleSlide("Multiproofs", wait_time=2),
    Multiproofs(),
    TitleSlide("Code"),
    CodeMultiproofs(),
    TitleSlide("Merkle vs Verkle Trees", sound = "data/sound/e7/slide8-0.mp3", wait_time=2),
    MerkleVerkle(),
    Subscribe("data/sound/episode1/s28.wav"),
    Credits(),
]