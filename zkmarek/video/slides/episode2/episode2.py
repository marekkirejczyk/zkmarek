from zkmarek.video.slides.episode2.signature import Signature
from zkmarek.video.slides.episode2.ecrecover import ECRecoverSlide
from zkmarek.video.slides.episode2.ethereum_transaction import EthereumTransaction

from zkmarek.video.slides.episode2.digital_signature_interface import DigitalSignatureInterface
from zkmarek.video.slides.episode2.previously import PreviouslyOn
from zkmarek.video.slides.episode2.support import Sponsored
from zkmarek.video.slides.episode2.credits import Credits as Credits2
from zkmarek.video.slides.episode2.deterministic import Deterministic
from zkmarek.video.slides.episode2.ecdsa import ECDSA
from zkmarek.video.slides.episode2.ecdsarec import ECDSARec
from slides.common.title import TitleSlide
from zkmarek.video.slides.common.intro import Intro
from zkmarek.video.slides.common.subscribe import Subscribe


EPISODE2 = [
    Intro(sound="data/sound/episode2/slide1-0.mp3", background_sound="data/sound/episode2/background.mp3"),
    Sponsored(),
    PreviouslyOn(),
    TitleSlide("Digital Signature Algorithm", pre_wait_time=1.5, sound="data/sound/episode2/slide4-0.mp3"),
    DigitalSignatureInterface(),
    Signature(),
    Deterministic(),
    ECRecoverSlide(),
    EthereumTransaction(),
    ECDSA("ECDSA sign", "data/ec/signature.py"),
    ECDSARec("ECDSA Recover", "data/ec/recover.py"),
    Subscribe("data/sound/episode1/s28.wav"),
    Credits2(),
]