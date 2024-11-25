from manim import (DOWN, FadeIn, Write, Indicate, Scene, Text, PURPLE_C, PINK, TEAL_E, RIGHT, MoveToTarget, 
                   LEFT, ORIGIN, Arrow, StealthTip, GREY_A, FadeOut, GrowArrow, UP)

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR, HIGHLIGHT2_COLOR
from zkmarek.video.slides.common.code_slide import CodeSlide
from zkmarek.video.utils import find_in_code

class BlobsSolidity(CodeSlide):


    def __init__(self):
        super().__init__("Blobs in Solidity", "zkmarek/video/slides/e5/blobs.sol")

    def construct(self):
        super().construct()
        self.code.next_to(self.title_text, DOWN, buff = 0).scale(0.67).shift(UP*1.2)
        self.commitment = "bytes48 commitment"
        self.x = "bytes32 x"
        self.y = "bytes32 y"
        self.proof = "bytes48 proof"
        self.blobIndex = "uint256 blobIndex"
        
        self.input_data = "bytes memory data = abi.encodePacked(commitment, x, y, proof);"

        self.address = "0x0a"
        self.assembly = "assembly"
        self.success = "success"
        self.blobhash = "blobhash"
        self.commitmentHash = "bytes32 commitmentHash"
        
        self.ec_to_hash = Text("bytes 48 EC point", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size=24).shift(LEFT*3+DOWN)
        self.hash_func = Text("SHA256", font = PRIMARY_FONT, font_size=24).set_color_by_gradient([SECONDARY_COLOR, PURPLE_C, PINK]).shift(6*LEFT+DOWN)
        self.ec_commitment = Text("bytes 32 EC hash", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size=24).shift(DOWN+RIGHT*1.5)
        self.arrow_hash_ec = Arrow(self.ec_to_hash.get_right(), self.ec_commitment.get_left(), tip_shape=StealthTip, 
                               stroke_width=2, max_tip_length_to_length_ratio=0.15).scale(0.7).set_color_by_gradient([HIGHLIGHT2_COLOR, GREY_A])
        
        self.false_if = "if (commitmentHash == bytes32(0)) return false;"
        
        self.verify_blobhash = "verifyBlobHash"
        self.smart_contract_1 = "return success && verifyBlobHash(commitmentHash, commitment);"
        
    def animate_in(self, scene):
        self.new_subsection(scene, "pseudo code: inputs", "data/sound/e5/slide6-1.mp3")
        scene.play(Write(self.title_text))
        scene.play(FadeIn(self.code))
        
        self.new_subsection(scene, "commitment", "data/sound/e5/slide6-1a.mp3")
        scene.wait(0.5)
        self.indicate_code(scene, self.code, self.commitment, 0, run_time=0.9, color = PINK)

        self.new_subsection(scene, "x and y", "data/sound/e5/slide6-1b.mp3")
        scene.wait(0.5)
        self.indicate_code(scene, self.code, self.x, 0, run_time=0.7, color = PINK)
        self.indicate_code(scene, self.code, self.y, 0, run_time=0.7, color = PINK)
        
        self.new_subsection(scene, "proof", "data/sound/e5/slide6-1c.mp3")
        scene.wait(0.5)
        self.indicate_code(scene, self.code, self.proof, 0, run_time=0.9, color = PINK)
        
        self.new_subsection(scene, "blobIndex", "data/sound/e5/slide6-1d.mp3")
        scene.wait(1)
        self.indicate_code(scene, self.code, self.blobIndex, 0, run_time=0.9)
        
        self.new_subsection(scene, "bytes 32 - not 48", "data/sound/e5/slide6-1e.mp3")
        scene.wait(1)
        self.indicate_code(scene, self.code, self.commitment, 0, run_time=0.8, color = PINK)
        self.indicate_code(scene, self.code, self.proof, 0, run_time=0.8, color = PINK)
        
        scene.wait(1)
        self.indicate_code(scene, self.code, self.x, 0, run_time=0.8, color = PINK)
        self.indicate_code(scene, self.code, self.y, 0, run_time=0.8, color = PINK)
        
        self.new_subsection(scene, "pack into byte array", "data/sound/e5/slide6-2.mp3")
        scene.wait(1.5)
        self.indicate_code(scene, self.code, self.x, 0, run_time=0.6)
        scene.wait(0.5)
        self.indicate_code(scene, self.code, self.y, 0, run_time=0.6)
        scene.wait(0.5)
        self.indicate_code(scene, self.code, self.commitment, 0, run_time=0.6)
        scene.wait(0.7)
        self.indicate_code(scene, self.code, self.proof, 0, run_time=0.6)
        
        self.indicate_code(scene, self.code, self.input_data, 0, run_time=1)
        
        self.new_subsection(scene, "matching 0x0a", "data/sound/e5/slide6-3.mp3")
        scene.wait(1.5)
        self.indicate_code(scene, self.code, self.assembly, 1, run_time=0.9, color = PURPLE_C)
        scene.wait(1.5)
        self.indicate_code(scene, self.code, self.address, 0, run_time=0.9, color = TEAL_E)
        scene.wait(2)
        self.indicate_code(scene, self.code, self.success, 1, run_time=0.9)
        self.indicate_code(scene, self.code, self.success, 0, run_time=0.9)
        
        self.new_subsection(scene, "blobhash()", "data/sound/e5/slide6-4.mp3")
        scene.wait(1)
        self.indicate_code(scene, self.code, self.commitmentHash, 0, run_time=0.9)
        scene.wait(3)
        self.indicate_code(scene, self.code, self.blobhash, run_time=0.9, color = PINK)
        
        self.new_subsection(scene, "blobindex - 32 bytes", "data/sound/e5/slide6-4a.mp3")
        scene.wait(1.5)
        self.indicate_code(scene, self.code, self.blobIndex, 0, run_time=0.9, color = PINK)
        scene.wait(1)
        self.indicate_code(scene, self.code, self.commitmentHash, 0, run_time=0.9,  color = PURPLE_C)
        
        self.new_subsection(scene, "SHA256", "data/sound/e5/slide6-4b.mp3")
        self.code.generate_target()
        self.code.target.scale(0.4).shift(RIGHT*3+UP)
        scene.play(MoveToTarget(self.code))
        scene.play(Write(self.ec_to_hash))
        scene.wait(2)
        scene.play(Write(self.hash_func), GrowArrow(self.arrow_hash_ec))
        scene.play(Write(self.ec_commitment))
        self.code.generate_target()
        self.code.target.scale(1/0.4).move_to(ORIGIN).shift(DOWN)
        scene.play(FadeOut(self.ec_commitment, self.ec_to_hash, self.hash_func, self.arrow_hash_ec))
        scene.play(MoveToTarget(self.code))
        scene.wait(1.5)
        self.indicate_code(scene, self.code, self.false_if, 0, run_time=1)
        
        
        self.new_subsection(scene, "verifyBlobHash", "data/sound/e5/slide6-5.mp3")
        scene.wait(1)
        self.indicate_code(scene, self.code, self.verify_blobhash, 0, run_time=0.9, color = TEAL_E)
        scene.wait(1)
        self.indicate_code(scene, self.code, self.commitmentHash, 0, run_time=0.9, color = PINK)
        
        scene.wait(2)
        self.indicate_code(scene, self.code, self.smart_contract_1, 0, run_time=1)
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.code, self.title_text))
        
    def indicate_code(self, scene: Scene, code, fragment: str, index=0, run_time=0.5, color = SECONDARY_COLOR):
        chars = find_in_code(code, fragment)
        scene.play(Indicate(chars[index]), color=color, run_time=run_time)
