from manim import Create, Write, DOWN, UP, FadeOut, Scene, Indicate, Code, Text, Circle #, MoveToTarget
from zkmarek.video.slides.common.code_slide import CodeSlide
from zkmarek.video.constant import SECONDARY_COLOR, PRIMARY_COLOR, PRIMARY_FONT
from zkmarek.video.utils import find_in_code

class MerkleProof(CodeSlide):
    def __init__(self):
        super().__init__(
            "Merkle Proof",
            "zkmarek/video/slides/e6/merkle_proof.sol",
            background="rectangle",
        )
    
    def construct(self):
        super().construct()
        self.code = Code("zkmarek/video/slides/e6/merkle_proof.sol", code_string = """    function verify(bytes32[] memory proof, bytes32 root, bytes32 leaf) internal pure returns (bool) {
        bytes32 computedHash = leaf;
        
        for (uint256 i = 0; i < proof.length; i++) { 
            computedHash = commutativeKeccak256(computedHash, proof[i]); 
        }

        return computedHash == root;
    }""", background="rectangle", language="solidity")
        self.title_label = Text("Merkle Proof", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 40).to_edge(UP)
        self.code.scale(0.6).next_to(self.title_label, DOWN, buff=1)
        
        # self.code_keccak = Code("zkmarek/video/slides/e6/keccak.sol", background="rectangle", language="solidity")
        print(self.code.code_lines.__dict__) 
        # print(self.code.code_json) 
    
    def animate_in(self, scene):
        self.new_subsection(scene, "code to get proof", "data/sound/e6/slide2-3b.mp3")
        scene.play(Write(self.title_label), run_time=0.7)
        scene.play(Create(self.code))

        self.new_subsection(scene, "verifies given leaf to root", "data/sound/e6/slide2-3c.mp3")
        scene.wait(0.8)
        self.indicate_code(scene, self.code, "verify")
        scene.wait(1)
        # self.indicate_code(scene, self.code, "leaf")
        scene.wait(1)
        # self.indicate_code(scene, self.code, "root")
        scene.wait(1)
        # self.indicate_code(scene, self.code, "proof")
        
        # self.new_subsection(scene, "computed hash", "data/sound/e6/slide2-3d.mp3")
        # scene.wait(2)
        # self.indicate_code(scene, self.code, "bytes32 computedHash = leaf;")
        
        # self.new_subsection(scene, "iteration over every leaf", "data/sound/e6/slide2-3e.mp3")
        # scene.wait(1.5)
        # self.indicate_code(scene, self.code, "proof.length")
        # scene.wait(1.5)
        # self.indicate_code(scene, self.code, "computedHash = commutativeKeccak256(computedHash, proof[i]);")
        # scene.wait(3)
        
        # # self.new_subsection(scene, "code in solidity", "data/sound/e6/slide2-3f.mp3")
        # self.code.generate_target()
        # self.code.target.next_to(self.title_label, DOWN, buff = 1.0)
        # scene.play(MoveToTarget(self.code))
        # self.code_keccak.scale(0.6).next_to(self.code, DOWN, buff=0.3)
        # scene.play(Create(self.code_keccak))
        # scene.wait(1)
        # self.indicate_code(scene, self.code_keccak, "bytes32 a, bytes32 b")
        # scene.wait(1.7)
        
        # self.new_subsection(scene, "smaller hash is always placed first", "data/sound/e6/slide2-3g.mp3")
        # scene.wait(1)
        # self.indicate_code(scene, self.code_keccak, "return a < b ?")
        # scene.wait(0.5)
        # self.indicate_code(scene, self.code_keccak, "efficientKeccak256(a, b)")
        # scene.wait(0.5)
        # self.indicate_code(scene, self.code_keccak, "efficientKeccak256(b, a)")
        # scene.wait(2)
        
        # self.new_subsection(scene, "w/o knowledge of leafs exact pos", "data/sound/e6/slide2-3h.mp3")
        
    # def animate_out(self, scene):
    #     scene.play(FadeOut(self.code, self.code_keccak), FadeOut(self.title_label))
        
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