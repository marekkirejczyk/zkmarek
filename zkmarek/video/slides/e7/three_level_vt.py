from manim import Write, UP, Text, FadeOut

from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT

class ThreeLevelVerkleTree(SlideBase):
    def __init__(self) -> None:
        super().__init__("Three-level Verkle tree")
        
    def construct(self):
        self.title_label = (
            Text(
                "Three-level Verkle tree",
                font=PRIMARY_FONT,
                color=PRIMARY_COLOR,
                font_size=40,
            )
            .to_edge(UP)
        )
        
    def animate_in(self, scene):
        self.new_subsection(scene, "3 levels", "data/sound/e7/slide4-0.mp3")
        scene.play(Write(self.title_label), run_time=1)
        
        self.new_subsection(scene, "3 levels", "data/sound/e7/slide4-1.mp3")
        
        self.new_subsection(scene, "3 levels", "data/sound/e7/slide4-2.mp3")
        
        self.new_subsection(scene, "3 levels", "data/sound/e7/slide4-3.mp3")
        
        self.new_subsection(scene, "3 levels", "data/sound/e7/slide4-4.mp3")
        
        self.new_subsection(scene, "3 levels", "data/sound/e7/slide4-5.mp3")
        
        self.new_subsection(scene, "3 levels", "data/sound/e7/slide4-6.mp3")
        
        self.new_subsection(scene, "3 levels", "data/sound/e7/slide4-7.mp3")
        
        self.new_subsection(scene, "3 levels", "data/sound/e7/slide4-8.mp3")
        
        self.new_subsection(scene, "3 levels", "data/sound/e7/slide4-9.mp3")
        
        self.new_subsection(scene, "3 levels", "data/sound/e7/slide4-10.mp3")
        
        self.new_subsection(scene, "3 levels", "data/sound/e7/slide4-11.mp3")
        
        self.new_subsection(scene, "3 levels", "data/sound/e7/slide4-11a.mp3")
        
        self.new_subsection(scene, "3 levels", "data/sound/e7/slide4-11b.mp3")
        
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.title_label), run_time=1)
        
        