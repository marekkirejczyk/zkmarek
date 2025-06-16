from manim import (FadeIn, Text, UP, FadeOut, Indicate)
from zkmarek.video.constant import PRIMARY_FONT, PRIMARY_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase

class MerkleVerkle(SlideBase):
    def __init__(self) -> None:
        super().__init__("Merkle Verkle Trees")

    def construct(self):
        self.title_label = (
            Text(
                "Merkle vs Verkle Trees",
                font=PRIMARY_FONT,
                color=PRIMARY_COLOR,
                font_size=40,
            )
            .to_edge(UP)
        )
    
    def animate_in(self, scene):
        self.new_subsection(scene, "depth -MT", "data/sound/e7/slide8-1.mp3")
        
        self.new_subsection(scene, "depth VT", "data/sound/e7/slide8-2.mp3")
        
        self.new_subsection(scene, "proof sizes", "data/sound/e7/slide8-3.mp3")
        
        self.new_subsection(scene, "MT proof size", "data/sound/e7/slide8-4.mp3")
        
        self.new_subsection(scene, "MT: 4 kB", "data/sound/e7/slide8-5.mp3")
        
        self.new_subsection(scene, "MT: 4 MB", "data/sound/e7/slide8-6.mp3")
        
        self.new_subsection(scene, "VT: efficient", "data/sound/e7/slide8-7.mp3")
        
        self.new_subsection(scene, "IPA VT: 1.3 kB, KZG VP: 600 B ", "data/sound/e7/slide8-8.mp3")
        
        self.new_subsection(scene, "1000 VP: 45 kB, 1000 VP: 15 kB", "data/sound/e7/slide8-9.mp3")
        
        self.new_subsection(scene, "more efficient", "data/sound/e7/slide8-10.mp3")
        
        self.new_subsection(scene, "can be the future", "data/sound/e7/slide8-11.mp3")
        