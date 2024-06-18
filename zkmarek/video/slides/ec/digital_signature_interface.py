from manim import (
    Code,
    DOWN,
    Indicate,
    Scene,
    ReplacementTransform,
    UP,
    RIGHT,
    LEFT,
    ApplyWave,
    VGroup,
    FadeIn,
    FadeOut,
    Write,
)
from zkmarek.video.constant import SECONDARY_COLOR, HIGHLIGHT_COLOR

from zkmarek.video.slides.common.code_slide import CodeSlide
from zkmarek.video.utils import find_in_code
from zkmarek.video.mobjects.standard import (
    secp256k1_standard,
)
from zkmarek.video.mobjects.discreet_elliptic_chart import (
    DiscreteEllipticChart,
)
from zkmarek.crypto.weierstrass_curve import Secp256k1_41


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
        code_recover = self._get_code("data/ec/signature_interface2.py", 24).next_to(
            self.title_text, DOWN, buff=0.5
        )
        code_ec = self._get_code("data/ec/signature_interface3.py", 24).next_to(
            self.title_text, DOWN, buff=0.5
        )
        self.code_ec_more = self._get_code(
            "data/ec/signature_interface4.py", 18
        ).next_to(self.title_text, DOWN, buff=0.5)
        self.curve = Secp256k1_41
        self.chart = DiscreteEllipticChart(self.curve).scale(0.8)
        self.secp256k1 = secp256k1_standard()
        self.new_subsection(scene, "intro", "data/sound/episode2/slide4-1.mp3")
        scene.play(Write(self.title_text))
        self.new_subsection(
            scene, "sign and verify", "data/sound/episode2/slide5-0.mp3"
        )
        scene.play(FadeIn(self.code), run_time=0.5)
        scene.wait(3.3)
        fragments = ["generate_key_pair", "sign", "verify"]
        for fragment in fragments:
            self.indicate_code(scene, self.code, fragment, 0, run_time=0.5)

        generate = ["secret_key", "public_key"]
        self.new_subsection(scene, "generate", "data/sound/episode2/slide5-1.mp3")
        scene.wait(1)
        self.indicate_code(scene, self.code, generate[0], 0, run_time=0.7)
        self.indicate_code(scene, self.code, generate[1], 0, run_time=0.7)
        scene.wait(4)

        self.play_sound(scene, "data/sound/episode2/slide5-2.mp3")
        scene.wait(0.5)
        sign = ["message", "secret_key", "signature"]
        self.indicate_code(scene, self.code, sign[0], 0, run_time=0.75)
        self.indicate_code(scene, self.code, sign[1], 1, run_time=0.75)
        self.indicate_code(scene, self.code, sign[2], 0, run_time=0.7)

        self.play_sound(scene, "data/sound/episode2/slide5-3.mp3")
        verify = ["message", "signature", "public_key", "bool"]
        scene.wait(0.2)
        self.indicate_code(scene, self.code, verify[0], 1, run_time=0.9)
        self.indicate_code(scene, self.code, verify[1], 1, run_time=0.9)
        self.indicate_code(scene, self.code, verify[2], 1, run_time=0.9)
        self.indicate_code(scene, self.code, verify[3], 0, run_time=0.9)
        scene.wait(2)

        self.play_sound(scene, "data/sound/episode2/slide5-4.mp3")
        scene.wait(7)
        scene.play(FadeOut(self.code), FadeIn(code_recover))
        scene.wait(2)
        recover = ["recover", "message", "signature", "public_key"]
        self.indicate_code(scene, code_recover, recover[0], 0, run_time=0.7)

        self.play_sound(scene, "data/sound/episode2/slide5-5.mp3")
        scene.wait(2.5)
        self.indicate_code(scene, code_recover, recover[1], 2, run_time=0.7)
        self.indicate_code(scene, code_recover, recover[2], 2, run_time=0.75)
        scene.wait(1)
        self.indicate_code(scene, code_recover, recover[3], 2, run_time=0.7)
        scene.wait(4)
        scene.play(ReplacementTransform(code_recover, code_ec), run_time=1.5)

        self.new_subsection(scene, "prefix ec", "data/sound/episode2/slide5-6.mp3")
        scene.wait(5)
        prefix_ec = ["ec_"]
        self.indicate_code(scene, code_ec, prefix_ec[0], 0, run_time=0.5)
        self.indicate_code(scene, code_ec, prefix_ec[0], 1, run_time=0.5)
        self.indicate_code(scene, code_ec, prefix_ec[0], 2, run_time=0.5)
        scene.play(ReplacementTransform(code_ec, self.code_ec_more), run_time=1.5)

        self.new_subsection(scene, "ec_sign", "data/sound/episode2/slide5-7.mp3")

        self.new_subsection(scene, "Scalar", "data/sound/episode2/slide5-8.mp3")
        secret = ["secret_key: Scalar"]
        self.indicate_code(scene, self.code_ec_more, secret[0], 0, run_time=0.7)
        self.indicate_code(scene, self.code_ec_more, secret[0], 1, run_time=0.7)
        scene.play(self.code_ec_more.animate.shift(RIGHT * 3).scale(0.2), run_time=1)
        scene.play(FadeIn(self.chart.scale(0.85).next_to(self.code_ec_more, LEFT)))
        dots = VGroup(*self.chart.dots)

        scene.wait(4.4)
        scene.play(Indicate(dots, color=HIGHLIGHT_COLOR, scale=1.05), run_time=1.5)
        scene.wait(3.5)
        scene.play(
            ApplyWave(self.chart.ax[0]), ApplyWave(self.chart.ax[1]), DIRECTION=UP
        )
        scene.wait(7)
        scene.play(FadeOut(self.chart), run_time=0.7)
        scene.play(self.code_ec_more.animate.shift(LEFT * 3).scale(5), run_time=1)

        self.new_subsection(scene, "public", "data/sound/episode2/slide5-9.mp3")
        public = ["public_key: ECPoint"]
        self.indicate_code(scene, self.code_ec_more, public[0], 0, run_time=0.5)
        self.indicate_code(scene, self.code_ec_more, public[0], 1, run_time=0.5)
        self.indicate_code(scene, self.code_ec_more, public[0], 2, run_time=0.5)
        scene.wait(2)

        self.new_subsection(scene, "message", "data/sound/episode2/slide5-10.mp3")
        message = ["message: Scalar"]
        self.indicate_code(scene, self.code_ec_more, message[0], 0, run_time=0.5)
        self.indicate_code(scene, self.code_ec_more, message[0], 1, run_time=0.5)
        self.indicate_code(scene, self.code_ec_more, message[0], 2, run_time=0.5)
        scene.wait(3)

        self.new_subsection(scene, "v value", "data/sound/episode2/slide5-11.mp3")
        signature_values = ["r: Scalar", "s: Scalar", "v: ?"]
        for i in range(0, 3):
            self.indicate_code(
                scene, self.code_ec_more, signature_values[0], i, run_time=0.3
            )
        for i in range(0, 3):
            self.indicate_code(
                scene, self.code_ec_more, signature_values[1], i, run_time=0.3
            )
        scene.wait(0.5)
        for i in range(0, 3):
            self.indicate_code(
                scene, self.code_ec_more, signature_values[2], i, run_time=0.35
            )

        scene.wait(1.5)

    def animate_out(self, scene):
        scene.play(FadeOut(self.code_ec_more), FadeOut(self.title_text))

    def indicate_code(self, scene: Scene, code, fragment: str, index=0, run_time=0.5):
        chars = find_in_code(code, fragment)
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
