from manim import ReplacementTransform, Code, DOWN, Indicate, FadeOut

from zkmarek.video.slides.common.code_slide import CodeSlide
from zkmarek.video.utils import find_in_code, load

# from zkmarek.video.slides.common.code_slide import code_pa


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
        code_params = {
            "background": "window",
            "insert_line_no": True,
            "font": "Monospace",
            "font_size": 18,
            "margin": 0.2,
            "style": "fruity",
            "line_no_buff": 0.2,
        }

        code_params.update(self.kwargs)
        super().animate_in(scene)
        self.new_subsection(
            scene, "sign and verify", "data/sound/episode2/slide5-0.mp3"
        )
        fragments = ["sign(", "verify"]
        for fragment in fragments:
            part = find_in_code(self.code, fragment)
            scene.play(Indicate(*part), run_time=1)
        scene.wait(2)

        self.play_sound(scene, "data/sound/episode2/slide5-1.mp3")
        scene.wait(1)
        sign = ["n(message", " secret_key)"]
        for fragment in sign:
            part = find_in_code(self.code, fragment)
            scene.play(Indicate(*part), run_time=1)

        self.play_sound(scene, "data/sound/episode2/slide5-2.mp3")
        verify = ["signature,", "e, public_key", "bool"]
        for fragment in verify:
            part = find_in_code(self.code, fragment)
            scene.play(Indicate(*part), run_time=1)
        scene.wait(2)
        self.play_sound(scene, "data/sound/episode2/slide5-3.mp3")
        scene.wait(4)
        self.replace_code(scene, "data/ec/signature_interface2.py")
        scene.wait(4)
        self.play_sound(scene, "data/sound/episode2/slide5-4.mp3")
        scene.wait(1)
        recover = ["recover", "(message, signature)"]
        code_recover = self._get_code("data/ec/signature_interface2.py", font_size=24)
        for fragment in recover:
            part = find_in_code(code_recover, fragment)
            scene.play(Indicate(*part), run_time=1)

        scene.wait(3)
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
            # scene.play(FadeOut(self.title))

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
