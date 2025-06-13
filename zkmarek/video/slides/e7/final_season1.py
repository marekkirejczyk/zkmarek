from manim import FadeIn, Text, UP
from zkmarek.video.constant import PRIMARY_FONT, PRIMARY_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.e6.merkle import MerkleTree
from zkmarek.video.slides.episode3.ceremony import Ceremony
from zkmarek.video.slides.episode5.layer2 import Layer2
from zkmarek.video.slides.episode4.commitment import Commitment
from zkmarek.video.slides.episode2.previously import PreviouslyOn

class FinalSeason1(SlideBase):
    def __init__(self):
        super().__init__("Final Season 1")
        
    def animate_in(self, scene):

        self.title_label = Text(
            "Final episode: Season 1",
            font=PRIMARY_FONT,
            color=PRIMARY_COLOR,
            font_size=40,
        ).to_edge(UP)
        
        self.slide_merkle = MerkleTree()
        self.slide_merkle.construct()
        
        self.slide_trusted_setup = Ceremony()
        self.slide_trusted_setup.construct()
        
        self.slide_blobs = Layer2()
        self.slide_blobs.construct()
        
        self.slide_kzg = Commitment()
        self.slide_kzg.construct()
        
        self.slide_ec = PreviouslyOn()
        self.slide_ec.construct()
        
        
        self.new_subsection(scene, "Final Season 1", "data/sound/e7/slide0-3.mp3")
        scene.play(FadeIn(self.title_label))
        scene.wait(2)
        
        self.slide_ec.animate_miniature(scene)
        self.slide_trusted_setup.animate_miniature_final_season(scene)
        self.slide_kzg.animate_miniature_final_season(scene)
        
        self.slide_merkle.animate_miniature_final_season(scene)
        self.slide_blobs.animate_miniature_final_season(scene)
        scene.wait(3)
        
        
        