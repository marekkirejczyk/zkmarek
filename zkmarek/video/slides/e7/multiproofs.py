from manim import Text, UP, FadeOut, Write
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT

class Multiproofs(SlideBase):
    def __init__(self):
        super().__init__("Multiproofs")
        
    def construct(self):
        self.title_label = Text("Multiproofs", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 40).to_edge(UP)
        
    def animate_in(self, scene):
        self.new_subsection(scene, "pi0, pi1, pi2, ..., pin", "data/sound/e7/slide6-1.mp3")
        scene.play(Write(self.title_label))
        
        self.new_subsection(scene, "data vector: polynomial", "data/sound/e7/slide6-2.mp3")
        
        self.new_subsection(scene, "opening p(xi)=ai", "data/sound/e7/slide6-3.mp3")
        
        self.new_subsection(scene, "p(xi)-ai=0", "data/sound/e7/slide6-4.mp3")
        
        self.new_subsection(scene, "root x=xi", "data/sound/e7/slide6-5.mp3")
        
        self.new_subsection(scene, "factored form", "data/sound/e7/slide6-6.mp3")
        
        self.new_subsection(scene, "quotient poly", "data/sound/e7/slide6-7.mp3")
        
        self.new_subsection(scene, "divide x-xi", "data/sound/e7/slide6-8.mp3")
        
        self.new_subsection(scene, "multiproofs", "data/sound/e7/slide6-9.mp3")
        
        self.new_subsection(scene, "3 proofs, 3 openings, 3 commitments", "data/sound/e7/slide6-10.mp3")
        
        self.new_subsection(scene, "random linear combinations", "data/sound/e7/slide6-11.mp3")
        
        self.new_subsection(scene, "random point t", "data/sound/e7/slide6-12.mp3")
        
        self.new_subsection(scene, "verkle multiproof", "data/sound/e7/slide6-13.mp3")
        
        self.new_subsection(scene, "verify once", "data/sound/e7/slide6-14.mp3")
        
        self.new_subsection(scene, "if tree deep - savings", "data/sound/e7/slide6-15.mp3")
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.title_label))
        