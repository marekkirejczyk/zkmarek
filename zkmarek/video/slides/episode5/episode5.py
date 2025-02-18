from zkmarek.video.slides.episode5.e4reference import Episode4Recap
from zkmarek.video.slides.episode5.layer2 import Layer2
from zkmarek.video.slides.episode5.blobs import Blobs
from zkmarek.video.slides.episode5.vectorcommitments import VectorCommitments
from zkmarek.video.slides.episode5.kzg import KZGBlobs
from zkmarek.video.slides.episode5.solidity_blobs import BlobsSolidity
from zkmarek.video.slides.episode5.blobsEth import BlobsBlockchain
from zkmarek.video.slides.episode5.credits import Credits as CreditsE5
from slides.common.title import TitleSlide
from zkmarek.video.slides.common.intro import Intro
from zkmarek.video.slides.common.subscribe import Subscribe
from zkmarek.video.slides.episode2.support import Sponsored

EPISODE5 = [
    Intro(sound="data/sound/episode3/slide0-0.mp3", background_sound="data/sound/e5/background.mp3",),
    Sponsored(),
    Episode4Recap(),
    TitleSlide("Layer 2", subtitle="Rollups", sound="data/sound/e5/slide1-0.mp3", wait_time=3),
    Layer2(),
    TitleSlide("Blobs", subtitle="Binary Large Objects", sound="data/sound/e5/slide1-3.mp3", wait_time=0.5),
    Blobs(),
    TitleSlide("Vector commitments", sound = "data/sound/e5/slide3-0a.mp3"),
    VectorCommitments(),
    KZGBlobs(),
    TitleSlide("Blobs on Ethereum", sound = "data/sound/e5/slide5-0.mp3", wait_time=0.7),
    BlobsBlockchain(),
    BlobsSolidity(),
    Subscribe("data/sound/episode1/s28.wav"),
    CreditsE5(),
]
