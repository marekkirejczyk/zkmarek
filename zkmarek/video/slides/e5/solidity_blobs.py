from manim import (DOWN, FadeIn, Write, Indicate, Scene, Text, PINK, TEAL_E, RIGHT, MoveToTarget, 
                   LEFT, Arrow, StealthTip, GREY_A, FadeOut, GrowArrow, UP, ImageMobject, MAROON_C, Brace)

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR, HIGHLIGHT2_COLOR
from zkmarek.video.slides.common.code_slide import CodeSlide
from zkmarek.video.utils import find_in_code

class BlobsSolidity(CodeSlide):


    def __init__(self):
        super().__init__("Blobs in Solidity", "zkmarek/video/slides/e5/blobs.sol")

    def construct(self):
        super().construct()
        self.code.next_to(self.title_text, DOWN, buff = 0).scale(0.9)
        self.commitment = "bytes48 commitment"
        self.x = "bytes32 x"
        self.y = "bytes32 y"
        self.proof = "bytes48 proof"
        self.blobIndex = "uint256 blobIndex"
        
        self.input_data = "bytes memory data = abi.encodePacked(commitment, x, y, proof);"

        self.precompile = "data.verifyKZGProof();"
        
        self.success = "success"
        self.blobhash = "blobhash"
        self.commitmentHash = "bytes32 commitmentHash"
        
        self.false_if = "if (commitmentHash == bytes32(0)) return false;"
        
        self.verify_blobhash = "verifyBlobHash"
        self.smart_contract_1 = "return success && verifyBlobHash(commitmentHash, commitment);"
        self.commitmentHash2 = "commitmentHash"
        
        self.return_success = "return success"
        
        self.blob = ImageMobject("data/images/blob.png").scale(0.5).shift(UP*0.7+LEFT*3)
        self.blobIndex_text = Text("blobIndex", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 24).move_to(self.blob.get_center())
        
        self.blob_hash_text = Text("blobhash(blobIndex)", font_size= 28, font = PRIMARY_FONT).set_color_by_gradient([TEAL_E, PRIMARY_COLOR, HIGHLIGHT2_COLOR]).next_to(self.blob, DOWN).shift(DOWN+LEFT*1)
        self.version_hash = Text("0x01 SHA 256 (KZG commitment)", font=PRIMARY_FONT, font_size=28).next_to(self.blob_hash_text, RIGHT).shift(RIGHT*2)
        self.arrow_hash_ec = Arrow(self.blob_hash_text.get_right(), self.version_hash.get_left(), tip_shape=StealthTip, 
                               stroke_width=2, max_tip_length_to_length_ratio=0.15).scale(0.7).set_color_by_gradient([HIGHLIGHT2_COLOR, GREY_A])
        self.version_hash_part1 = self.version_hash[0:4]
        self.version_hash_part1.set_color_by_gradient([TEAL_E, PRIMARY_COLOR])
        self.brace_version = Brace(self.version_hash_part1, DOWN).set_color_by_gradient([PINK, MAROON_C])
        self.version_hash_part2 = self.version_hash[4:25]
        self.version_hash_part2.set_color_by_gradient([SECONDARY_COLOR, MAROON_C, PINK])
        self.brace_hash = Brace(self.version_hash_part2, DOWN).set_color_by_gradient([SECONDARY_COLOR, MAROON_C, PINK])
        self.text_version = Text("version", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 24)
        self.brace_version.put_at_tip(self.text_version)
        self.text_hash = Text("last 31 bytes", color = MAROON_C, font= PRIMARY_FONT, font_size = 24)
        self.brace_hash.put_at_tip(self.text_hash)
        
        self.commitment_real = "commitment"
        
        
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
        scene.wait(4.5)
        
        self.new_subsection(scene, "bytes 32 - not 48", "data/sound/e5/slide6-1e.mp3")
        scene.wait(1)
        self.indicate_code(scene, self.code, self.commitment, 0, run_time=0.8, color = PINK)
        self.indicate_code(scene, self.code, self.proof, 0, run_time=0.8, color = PINK)
        
        scene.wait(1)
        self.indicate_code(scene, self.code, self.x, 0, run_time=0.8, color = PINK)
        self.indicate_code(scene, self.code, self.y, 0, run_time=0.8, color = PINK)
        scene.wait(1.5)
        
        self.new_subsection(scene, "pack into byte array", "data/sound/e5/slide6-2.mp3")
        kzg_input = [self.x, self.y, self.commitment, self.proof]
        scene.wait(1)
        for input in kzg_input:
            self.indicate_code(scene, self.code, input, 0, run_time=0.4, color = MAROON_C)
        scene.wait(0.5)
        self.indicate_code(scene, self.code, self.input_data, 0, run_time=1)
        
        self.new_subsection(scene, "matching 0x0a", "data/sound/e5/slide6-3.mp3")
        scene.wait(1.5)
        scene.wait(1)
        self.indicate_code(scene, self.code, self.precompile, 0, run_time=0.8, color = TEAL_E)
        scene.wait(0.5)
        scene.wait(3.5)
        self.indicate_code(scene, self.code, self.success, 0, run_time=0.9)
        scene.wait(5.5)
        
        self.new_subsection(scene, "blobhash()", "data/sound/e5/slide6-4.mp3")
        scene.wait(1)
        self.indicate_code(scene, self.code, self.commitmentHash, 0, run_time=0.9)
        scene.wait(4.5)
        self.indicate_code(scene, self.code, self.blobhash, run_time=0.9, color = PINK)
        self.code.generate_target()
        self.code.target.scale(0.4).shift(RIGHT*3+UP)
        scene.play(MoveToTarget(self.code))
        scene.play(Write(self.blob_hash_text), FadeIn(self.blob))
        
        self.new_subsection(scene, "blobindex - 32 bytes", "data/sound/e5/slide6-4a.mp3")
        scene.wait(1.2)
        scene.play(Indicate(self.blob_hash_text[9:18], color = PINK))
        scene.play(Write(self.version_hash), GrowArrow(self.arrow_hash_ec))
        scene.wait(1)
        scene.play(FadeIn(self.brace_hash, self.brace_version))

        
        self.new_subsection(scene, "SHA256", "data/sound/e5/slide6-4b.mp3")
        scene.play(Write(self.text_version), Write(self.text_hash))
        scene.wait(0.5)
        scene.play(Indicate(self.text_version, color = PRIMARY_COLOR), run_time=0.7)
        scene.wait(1.3)
        scene.play(Indicate(self.text_hash, color = PRIMARY_COLOR))
        scene.wait(1)
        scene.play(Indicate(self.version_hash[4:10], color = MAROON_C))
        scene.wait(2)
        scene.play(FadeOut(self.blob, self.text_hash, self.text_version, self.version_hash, self.brace_hash, self.brace_version, self.arrow_hash_ec, self.blob_hash_text))
        self.code.generate_target()
        self.code.target.scale(1/0.4).next_to(self.title_text, DOWN, buff = 0).shift(DOWN*0.1)
        scene.play(MoveToTarget(self.code))
        scene.wait(1.5)
        self.indicate_code(scene, self.code, self.false_if, 0, run_time=1)
        scene.wait(2.5)
        
        
        self.new_subsection(scene, "verifyBlobHash", "data/sound/e5/slide6-5.mp3")
        scene.wait(1)
        self.indicate_code(scene, self.code, self.verify_blobhash, 0, run_time=0.9, color = TEAL_E)
        scene.wait(1)
        self.indicate_code(scene, self.code, self.commitment_real, 5, run_time=0.9, color = PINK)
        scene.wait(2)
        self.indicate_code(scene, self.code, self.commitmentHash2, 2, run_time=1)
        scene.wait(3.5)
        self.indicate_code(scene, self.code, self.return_success, 0, run_time=0.9)
        scene.wait(3)
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.code, self.title_text))
        
    def indicate_code(self, scene: Scene, code, fragment: str, index=0, run_time=0.5, color = SECONDARY_COLOR):
        chars = find_in_code(code, fragment)
        scene.play(Indicate(chars[index]), color=color, run_time=run_time)
