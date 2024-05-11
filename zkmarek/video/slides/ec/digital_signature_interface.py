from manim import ReplacementTransform, Code, DOWN, Indicate, FadeOut, Scene
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
        self.new_subsection(scene, "intro", "data/sound/episode2/slide4-1.mp3")
        super().animate_in(scene)

        self.new_subsection(
            scene, "sign and verify", "data/sound/episode2/slide5-0.mp3"
        )
        scene.wait(3.8)
        fragments = ["sign", "verify"]
        for fragment in fragments:
            self.indicate_code(scene, fragment, 0, run_time=0.5)

        self.play_sound(scene, "data/sound/episode2/slide5-1.mp3")
        scene.wait(0.8)
        sign = ["message", "secret_key", "signature"]
        self.indicate_code(scene, sign[0], 0, run_time=0.5)
        self.indicate_code(scene, sign[1], 1, run_time=0.5)
        self.indicate_code(scene, sign[2], 0, run_time=0.5)

        self.play_sound(scene, "data/sound/episode2/slide5-2.mp3")
        verify = ["signature", "public_key", "bool"]
        self.indicate_code(scene, verify[0], 1, run_time=1)
        self.indicate_code(scene, verify[1], 1, run_time=1)
        self.indicate_code(scene, verify[2], 0, run_time=1)
        scene.wait(2)

        self.play_sound(scene, "data/sound/episode2/slide5-3.mp3")
        scene.wait(4)
        self.replace_code(scene, "data/ec/signature_interface2.py")
        scene.wait(4)

        self.play_sound(scene, "data/sound/episode2/slide5-4.mp3")
        scene.wait(8)

        self.replace_code(scene, "data/ec/signature_interface3.py")
        scene.wait(1)
        self.replace_code(scene, "data/ec/signature_interface4.py", font_size=18)

    def replace_code(self, scene, path: str, font_size=24):
        code = self._get_code(path, font_size)
        code.next_to(self.title_text, DOWN, buff=0.5)
        scene.play(ReplacementTransform(self.code, code))
        self.code = code
        if path == "data/ec/signature_interface4.py":
            scene.play(FadeOut(code))

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
