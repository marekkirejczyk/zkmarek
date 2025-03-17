from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.episode3.ceremony import Ceremony
from zkmarek.video.slides.episode4.commitment import Commitment
from zkmarek.video.slides.episode5.vectorcommitments import VectorCommitments

class FullVideos(SlideBase):
    def __init__(self) -> None:
        super().__init__("Full videos")
        
    def construct(self):
        self.slide1 = Ceremony()
        self.slide1.construct()
        self.slide2 = Commitment()
        self.slide2.construct()
        self.slide3 = VectorCommitments()
        self.slide3.construct()
        
    def animate_in(self, scene):
        self.new_subsection(scene, "Full videos", "data/sound/e6/slide1-2d.mp3")
        self.animate_miniatures(scene)
        
    def animate_miniatures(self, scene):
        self.slide1.animate_miniature2(scene)
        self.slide2.animate_miniature(scene)
        self.slide3.animate_miniature(scene)
        