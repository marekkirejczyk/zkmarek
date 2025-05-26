from manim import Text, Write, UP
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT
class Proofs(SlideBase):
    def __init__(self)-> None:
        super().__init__("Proofs")
        
    def construct(self):
        self.title_label = Text("Proofs", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size = 40).to_edge(UP)
        
        
        
    
    def animate_in(self, scene):
        self.new_subsection(scene, "85: proof C, opening", "data/sound/e7/slide5-1.mp3")
        scene.play(Write(self.title_label), run_time=0.7)
        
        
        self.new_subsection(scene, "multi-level", "data/sound/e7/slide5-2.mp3")
        
        self.new_subsection(scene, "C0, opening, proof pi", "data/sound/e7/slide5-3.mp3")
        
        self.new_subsection(scene, "parent commitment, opening", "data/sound/e7/slide5-4.mp3")
        
        self.new_subsection(scene, "root, proof, opening", "data/sound/e7/slide5-5.mp3")
        
        self.new_subsection(scene, "3 commitments, 3 openings, 3 proofs", "data/sound/e7/slide5-6.mp3")
        
        self.new_subsection(scene, "different weight", "data/sound/e7/slide5-6a.mp3")
        
        self.new_subsection(scene, "IPA", "data/sound/e7/slide5-6b.mp3")
        
        self.new_subsection(scene, "total 1728", "data/sound/e7/slide5-6c.mp3")
        
        self.new_subsection(scene, "KZG", "data/sound/e7/slide5-6d.mp3")
        
        self.new_subsection(scene, "total 384 b", "data/sound/e7/slide5-6e.mp3")
        
        self.new_subsection(scene, "much smaller but pairings", "data/sound/e7/slide5-6f.mp3")
        
        self.new_subsection(scene, "3 proofs - to verify", "data/sound/e7/slide5-6g.mp3")
        
        self.new_subsection(scene, "simplified to sinlge proof", "data/sound/e7/slide5-7.mp3")