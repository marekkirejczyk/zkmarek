from manim import (
    ReplacementTransform,
    Code,
    DOWN,
    Indicate,
    Scene,
    TransformMatchingShapes,
)
from zkmarek.video.constant import SECONDARY_COLOR

from zkmarek.video.slides.common.code_slide import CodeSlide
from zkmarek.video.utils import find_in_code


class DigitalSignatureInterface(CodeSlide):
    def __init__(self):
        super().__init__(
            "Digital Signature Interface",
            "data/ec/signature_interface.py",
            font_size=24,
            background="rectangle",
            insert_line_no=False,
        )

    def animate_in(self, scene):
        code_recover = self._get_code("data/ec/signature_interface2.py", 24)
        code_ec = self._get_code("data/ec/signature_interface3.py", 24)
        code_ec_more = self._get_code("data/ec/signature_interface4.py", 18)

        self.new_subsection(scene, "intro", "data/sound/episode2/slide4-1.mp3")
        super().animate_in(scene)

        self.new_subsection(
            scene, "sign and verify", "data/sound/episode2/slide5-0.mp3"
        )
        scene.wait(3.8)
        fragments = ["generate_key_pair", "sign", "verify"]
        for fragment in fragments:
            self.indicate_code(scene, fragment, 0, run_time=0.5)

        generate = ["secret_key", "public_key"]
        self.new_subsection(scene, "generate", "data/sound/episode2/slide5-1.mp3")
        scene.wait(1)
        self.indicate_code(scene, generate[0], 0, run_time=0.7)
        self.indicate_code(scene, generate[1], 0, run_time=0.7)
        scene.wait(4)
        self.play_sound(scene, "data/sound/episode2/slide5-2.mp3")
        scene.wait(0.8)
        sign = ["message", "secret_key", "signature"]
        self.indicate_code(scene, sign[0], 0, run_time=0.7)
        self.indicate_code(scene, sign[1], 1, run_time=0.7)
        self.indicate_code(scene, sign[2], 0, run_time=0.7)

        self.play_sound(scene, "data/sound/episode2/slide5-3.mp3")
        verify = ["message", "signature", "public_key", "bool"]
        scene.wait(0.2)
        self.indicate_code(scene, verify[0], 1, run_time=0.9)
        self.indicate_code(scene, verify[1], 1, run_time=0.9)
        self.indicate_code(scene, verify[2], 1, run_time=0.9)
        self.indicate_code(scene, verify[3], 0, run_time=0.9)
        scene.wait(2)

        self.play_sound(scene, "data/sound/episode2/slide5-4.mp3")
        scene.wait(7)
        self.replace_code(scene, code_recover)
        scene.wait(2.5)
        recover = ["recover", "message", "signature", "public_key"]
        self.indicate_code(scene, recover[0], 0, run_time=0.7)
        self.play_sound(scene, "data/sound/episode2/slide5-5.mp3")
        scene.wait(2.3)
        self.indicate_code(scene, recover[1], 2, run_time=0.7)
        self.indicate_code(scene, recover[2], 2, run_time=0.75)
        scene.wait(1)
        self.indicate_code(scene, recover[3], 2, run_time=0.7)
        scene.wait(4)

        self.replace_code(scene, code_ec)
        self.new_subsection(scene, "prefix ec", "data/sound/episode2/slide5-6.mp3")
        scene.wait(5)
        prefix_ec = ["ec_"]
        self.indicate_code(scene, prefix_ec[0], 0, run_time=0.5)
        self.indicate_code(scene, prefix_ec[0], 1, run_time=0.5)
        self.indicate_code(scene, prefix_ec[0], 2, run_time=0.5)
        self.replace_code(scene, code_ec_more)

        self.new_subsection(scene, "ec_sign", "data/sound/episode2/slide5-7.mp3")
        scene.wait(2.9)
        ec_sign = [
            "ec_sign",
            "message: Scalar",
            "secret_key: Scalar",
            "signature: (r: Scalar, s: Scalar, v: ?)",
        ]
        self.indicate_code(scene, ec_sign[0], 0, run_time=1)
        scene.wait(0.5)
        self.indicate_code(scene, ec_sign[1], 0, run_time=0.5)
        self.indicate_code(scene, ec_sign[2], 1, run_time=0.5)
        scene.wait(0.5)
        self.indicate_code(scene, ec_sign[3], 0, run_time=1)

        self.new_subsection(scene, "ec_verify", "data/sound/episode2/slide5-8.mp3")
        ec_verify = [
            "ec_verify",
            "message: Scalar",
            "signature: (r: Scalar, s: Scalar, v: ?)",
            "public_key: ECPoint",
            "bool",
        ]
        self.indicate_code(scene, ec_verify[0], 0, run_time=1)
        self.indicate_code(scene, ec_verify[1], 1, run_time=0.75)
        self.indicate_code(scene, ec_verify[2], 1, run_time=1.15)
        self.indicate_code(scene, ec_verify[3], 1, run_time=1.1)
        self.indicate_code(scene, ec_verify[4], 0, run_time=1.8)

        self.new_subsection(scene, "v value", "data/sound/episode2/slide5-9.mp3")

        v_value = ["v: ?"]
        for i in range(0, 3):
            self.indicate_code(scene, v_value[0], i, run_time=0.35)

        scene.wait(1.5)

    def replace_code(self, scene, code):
        code.next_to(self.title_text, DOWN, buff=0.5)
        scene.play(TransformMatchingShapes(self.code, code))
        self.code = code

    def indicate_code(self, scene: Scene, fragment: str, index=0, run_time=0.5):
        chars = find_in_code(self.code, fragment)
        scene.play(Indicate(chars[index]), color=SECONDARY_COLOR, run_time=run_time)

    @staticmethod
    def _get_code(path: str, font_size: int):
        return Code(
            path,
            font_size=font_size,
            background="rectangle",
            insert_line_no=False,
            font="Monospace",
            margin=0.2,
            style="fruity",
            line_no_buff=0.2,
        )
