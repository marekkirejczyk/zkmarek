from manim import ReplacementTransform, Code, DOWN

from zkmarek.video.slides.common.code_slide import CodeSlide


class DigitalSignatureInterface(CodeSlide):
    def __init__(self):
        super().__init__(
            "Digital Signature Interface",
            "data/ec/signature_interface.py",
            font_size=24,
            background='rectangle',
            insert_line_no=False
        )

    def animate_in(self, scene):
        super().animate_in(scene)
        self.replace_code(scene, "data/ec/signature_interface2.py")
        scene.wait(1)
        self.replace_code(scene, "data/ec/signature_interface3.py")
        scene.wait(1)
        self.replace_code(scene, "data/ec/signature_interface4.py", font_size=18)

    def replace_code(self, scene, path: str, font_size=24):
        code = self._get_code(path, font_size)
        code.next_to(self.title_text, DOWN, buff=0.5)
        scene.play(ReplacementTransform(self.code, code))
        self.code = code

    @staticmethod
    def _get_code(path: str, font_size: int):
        return Code(
            path,
            font_size=font_size,
            background='rectangle',
            insert_line_no=False,
            font="Monospace",
            margin=0.2,
            style="fruity",
            line_no_buff=0.2,
        )
