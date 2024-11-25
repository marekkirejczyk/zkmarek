from manim import (DOWN, UP, FadeIn, Write)

# from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT
# from zkmarek.video.mobjects.array import Array
from zkmarek.video.slides.common.code_slide import CodeSlide


class BlobsSolidity(CodeSlide):


    def __init__(self):
        super().__init__("Blobs in Solidity", "zkmarek/video/slides/e5/blobs.sol")

    def construct(self):
        super().construct()
        self.code.next_to(self.title_text, DOWN, buff = 0).scale(0.67).shift(UP*1.2)
        
    def animate_in(self, scene):
        # self.new_subsection(scene, "code in solidity", "data/sound/e5/slide6-0.mp3")
        scene.play(Write(self.title_text))
        scene.play(FadeIn(self.code))
        
        # self.new_subsection(scene, "contract verifier a polynomial", "data/sound/e5/slide6-1.mp3")
        
        # self.new_subsection(scene, "constant", "data/sound/e5/slide6-2.mp3")
        
        # self.new_subsection(scene, "verifyBlobKZG", "data/sound/e5/slide6-3.mp3")
        
        # self.new_subsection(scene, "blobIndex", "data/sound/e5/slide6-3a.mp3")
        
        # self.new_subsection(scene, "encodes inputs: commitment, eval point, ex, proof", "data/sound/e5/slide6-3b.mp3")
        
        # self.new_subsection(scene, "ec points", "data/sound/e5/slide6-3c.mp3")
        
        # self.new_subsection(scene, "verify Versioned Hash", "data/sound/e5/slide6-3.mp3")
        
        # self.new_subsection(scene, "matching 0x01", "data/sound/e5/slide6-4a.mp3")
        
        # self.new_subsection(scene, "hash of the commitment to match", "data/sound/e5/slide6-4b.mp3")
        
        
        