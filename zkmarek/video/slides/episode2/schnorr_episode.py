from zkmarek.video.slides.episode2.schnorr import SchnorrSlide
from zkmarek.video.slides.common.code_slide import CodeSlide
from zkmarek.video.slides.common.tex_slide import TexSlide

EPISODE7 = [
    SchnorrSlide(),
    CodeSlide("Verify Schnorr signature with ECRecover ", "data/schnorr/schnorr.sol"),
    TexSlide("Sources", "data/schnorr/sources.tex"),
]