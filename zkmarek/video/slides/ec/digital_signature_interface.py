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
        scene.wait(2)
        self.replace_code(scene, "data/ec/signature_interface3.py")

    def replace_code(self, scene, path: str):
        code = self._get_code(path)
        code.next_to(self.title_text, DOWN, buff=0.5)
        scene.play(ReplacementTransform(self.code, code))
        self.code = code

    @staticmethod
    def _get_code(path: str):
        return Code(
            path,
            font_size=24,
            background='rectangle',
            insert_line_no=False,
            font="Monospace",
            margin=0.2,
            style="fruity",
            line_no_buff=0.2,
        )
