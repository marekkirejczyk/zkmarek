from manim import Create, Write, DOWN, UP, FadeOut, Scene, Indicate, Code, Text
from zkmarek.video.slides.common.code_slide import CodeSlide
from zkmarek.video.constant import SECONDARY_COLOR, PRIMARY_COLOR, PRIMARY_FONT
from zkmarek.video.utils import find_in_code

class MerkleProof(CodeSlide):
    def __init__(self):
        super().__init__(
            "Merkle Proof",
            "zkmarek/video/slides/e6/get_proof.ts",
            font_size=24,
            background="rectangle",
            insert_line_no=False,
        )
    
    def construct(self):
        super().construct()
        self.title_label = Text("Merkle Proof", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 40).to_edge(UP)
        self.code.scale(0.9).next_to(self.title_label, DOWN, buff=1)
    
    def animate_in(self, scene):
        self.new_subsection(scene, "code to get proof", "data/sound/e6/slide2-3b.mp3")
        scene.play(Write(self.title_label), run_time=0.7)
        scene.play(Create(self.code))

        self.new_subsection(scene, "takes two arguments: tree and leaf", "data/sound/e6/slide2-3c.mp3")
        scene.wait(0.8)
        self.indicate_code(scene, self.code, "tree")
        scene.wait(1)
        self.indicate_code(scene, self.code, "index")
        
        self.new_subsection(scene, "singling of every hash", "data/sound/e6/slide2-3d.mp3")
        scene.wait(1)
        self.indicate_code(scene, self.code, "siblingIndex(index)")
        
        self.new_subsection(scene, "returns array of hashes", "data/sound/e6/slide2-3e.mp3")
        scene.wait(0.5)
        self.indicate_code(scene, self.code, "const proof: HexString[] = [];")
        scene.wait(5.5)
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.code), FadeOut(self.title_label))

    def indicate_code(self, scene: Scene, code, fragment: str, index=0, run_time=1):
        chars = find_in_code(code, fragment)
        scene.play(Indicate(chars[index]), color=SECONDARY_COLOR, run_time=run_time)

    @staticmethod
    def _get_code(path: str, font_size: int):
        return Code(
            path,
            font_size=font_size,
            background="rectangle",
            insert_line_no=False,
            # font="Monospace",
            # margin=0.2,
            style="fruity",
            line_no_buff=0.2,
        )        