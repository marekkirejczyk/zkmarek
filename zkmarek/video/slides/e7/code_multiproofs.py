from manim import FadeIn, Text, UP, Write, Indicate, Code, Scene, FadeOut, DOWN
from zkmarek.video.constant import PRIMARY_FONT, PRIMARY_COLOR, SECONDARY_COLOR
from zkmarek.video.slides.common.code_slide import CodeSlide
from zkmarek.video.utils import find_in_code

class Multiproofs(CodeSlide):
    def __init__(self) -> None:
        super().__init__("Multiproofs", "zkmarek/video/slides/e7/make_multiproof.py")

    def construct(self):
        self.title_label = (
            Text(
                "Multiproofs",
                font=PRIMARY_FONT,
                color=PRIMARY_COLOR,
                font_size=40,
            )
            .to_edge(UP)
        )
        self.code = Code("zkmarek/video/slides/e7/make_multiproof.py", 
                         background="rectangle", 
            language="python",).scale(0.55).shift(DOWN * 0.7)
        
    def animate_in(self, scene):
        self.new_subsection(scene, "prover quoery", "data/sound/e7/slide7-1.mp3")
        scene.play(Write(self.title_label))
        scene.play(FadeIn(self.code))
        
        self.new_subsection(scene, "+ list of polynomials", "data/sound/e7/slide7-2.mp3")
        # self.new_subsection(scene, "prover quoery", "data/sound/e7/slide7-1.mp3")
        # scene.play(FadeOut(self.code_prover_query))
        # scene.wait(1)
        # scene.play(FadeIn(self.code))
        
        self.new_subsection(scene, "challenge scalar r", "data/sound/e7/slide7-3.mp3")
        
        self.new_subsection(scene, "set up openings", "data/sound/e7/slide7-4.mp3")
        
        self.new_subsection(scene, "g - random linear combination", "data/sound/e7/slide7-5.mp3")
        
        self.new_subsection(scene, "for each opening - quotient", "data/sound/e7/slide7-6.mp3")
        
        self.new_subsection(scene, "quotient verifies opening", "data/sound/e7/slide7-7.mp3")
        
        self.new_subsection(scene, "commit to g", "data/sound/e7/slide7-8.mp3")
        
        self.new_subsection(scene, "random s -> g(s)", "data/sound/e7/slide7-9.mp3")
        
        self.new_subsection(scene, "generate proof", "data/sound/e7/slide7-10.mp3")
        
        self.new_subsection(scene, "pi - multiproof", "data/sound/e7/slide7-11.mp3")

        
    def animate_out(self, scene):
        scene.play(FadeOut(self.code))
        scene.play(FadeOut(self.title_label))
        
        
    def indicate_code(self, scene: Scene, code, fragment: str, index=0, run_time=1):
        chars = find_in_code(code, fragment)
        scene.play(Indicate(chars[index]), color=SECONDARY_COLOR, run_time=run_time)

    @staticmethod
    def _get_code(path: str):
        return Code(
            path,
            background="rectangle",
        )
