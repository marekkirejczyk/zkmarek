from manim import Create, Write, DOWN, UP, FadeOut, Scene, Indicate, Code, Text, MoveToTarget, Circle, LEFT, RIGHT
from zkmarek.video.slides.common.code_slide import CodeSlide
from zkmarek.video.constant import SECONDARY_COLOR, PRIMARY_COLOR, PRIMARY_FONT
from zkmarek.video.utils import find_in_code

class MerkleProof(CodeSlide):
    def __init__(self):
        super().__init__(
            "Merkle Proof",
            "zkmarek/video/slides/e6/get_proof.ts",
            background="rectangle",
        )
    
    def construct(self):
        super().construct()
        self.code = Code("zkmarek/video/slides/e6/get_proof.ts", background="rectangle")
        self.title_label = Text("Merkle Proof", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 40).to_edge(UP)
        self.code.scale(0.8).next_to(self.title_label, DOWN, buff=1)
        
        self.code_in_solidity = Code("zkmarek/video/slides/e6/merkle_proof.sol", background="rectangle")
        
    
    def animate_in(self, scene):
        self.new_subsection(scene, "code to get proof", "data/sound/e6/slide2-3b.mp3")
        scene.play(Write(self.title_label), run_time=0.7)
        scene.play(Create(self.code))

        self.new_subsection(scene, "takes two arguments: tree and leaf", "data/sound/e6/slide2-3c.mp3")
        scene.wait(0.8)
        # self.indicate_code(scene, self.code, "tree")
        self.indicate_with_circle(scene, self.code.get_top()+LEFT*1.2+DOWN*0.5)
        scene.wait(1)
        # self.indicate_code(scene, self.code, "index")
        self.indicate_with_circle(scene, self.code.get_top()+RIGHT*1.9+DOWN*0.5)
        
        self.new_subsection(scene, "singling of every hash", "data/sound/e6/slide2-3d.mp3")
        scene.wait(1)
        # self.indicate_code(scene, self.code, "siblingIndex(index)")
        self.indicate_with_circle(scene, self.code.get_center()+DOWN*0.1+LEFT*0.1, scale_circle=2)
        
        self.new_subsection(scene, "returns array of hashes", "data/sound/e6/slide2-3e.mp3")
        scene.wait(0.5)
        # self.indicate_code(scene, self.code, "const proof: HexString[] = [];")
        self.indicate_with_circle(scene, self.code.get_center()+UP*0.43+LEFT*2.1, scale_circle=1.7)
        scene.wait(5.5)
        
        self.new_subsection(scene, "code in solidity", "data/sound/e6/slide2-3e2.mp3")
        self.code.generate_target()
        self.code.target.scale(0.6).next_to(self.title_label, DOWN, buff = 0.3)
        scene.play(MoveToTarget(self.code))
        self.code_in_solidity.scale(0.6).next_to(self.code, DOWN, buff=0.3)
        scene.play(Create(self.code_in_solidity))
        scene.wait(1)
        # self.indicate_code(scene, self.code_in_solidity, "verify")
        self.indicate_with_circle(scene, self.code_in_solidity.get_top()+DOWN*0.65+LEFT*4.2, scale_circle=1)
        scene.wait(1.7)
        # self.indicate_code(scene, self.code_in_solidity, "leaf")
        self.indicate_with_circle(scene, self.code_in_solidity.get_top()+DOWN*0.64+RIGHT*2.2, scale_circle=1)
        scene.wait(0.5)
        # self.indicate_code(scene, self.code_in_solidity, "proof")
        self.indicate_with_circle(scene, self.code_in_solidity.get_top()+DOWN*0.64+RIGHT*0.42, scale_circle=1)
        scene.wait(2)
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.code, self.code_in_solidity), FadeOut(self.title_label))
        
    def indicate_with_circle(self, scene: Scene, location, run_time=0.8, scale_circle = 1):
        circle_to_indicate = Circle(color=SECONDARY_COLOR, radius=0.5).stretch(0.5, 1)
        scene.play(Create(circle_to_indicate.scale(scale_circle).move_to(location)), run_time=run_time)
        scene.play(FadeOut(circle_to_indicate), run_time=0.3)

    def indicate_code(self, scene: Scene, code, fragment: str, index=0, run_time=1):
         chars = find_in_code(code, fragment)
         scene.play(Indicate(chars[index]), color=SECONDARY_COLOR, run_time=run_time)
         
    @staticmethod
    def _get_code(path: str):
        return Code(
            path,
            background="rectangle",
        )        