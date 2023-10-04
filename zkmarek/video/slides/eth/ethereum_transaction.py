from manim import (DOWN, RIGHT, UP, FadeIn, FadeOut, Indicate, Tex,
                   TransformMatchingTex, VGroup, Wait)

from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR
from zkmarek.video.mobjects.discreet_elliptic_chart import \
    DiscreteEllipticChart
from zkmarek.video.mobjects.equation_box import (EquationBox,
                                                 EquationBoxWithIcons)
from zkmarek.video.slides.common.code_slide import CodeSlide
from zkmarek.video.utils import find_in_code


class EthereumTransaction(CodeSlide):
    def __init__(self):
        super().__init__(
            "Ethereum Transaction",
            "data/eth/transaction.py",
            language="python")

    def animate_in(self, scene):
        self.new_subsection(scene, "Ethereum Transaction",
            sound="data/sound/episode1/s29-1.wav")

        super().animate_in(scene)

        fragments1 = [
            '"from"',
            '"to"',
            '"value"',
            '"nonce"',
            '"chainId"',
            '"hash"',
            '...']


        indications = []
        for fragment in fragments1:
            chars = find_in_code(self.code, fragment)
            indications.append(Indicate(*chars, color=SECONDARY_COLOR))

        scene.play(*indications)

        scene.wait(4)

        fragments2 = [
            '"s": "0x4a94e0265f31fd90dc414433d5acdaf28d3ebf0a7657841c4edc7564808b078b"',
            '"r": "0xa99c1ac8787f592251ae67055afaeab9ade2e36eea47a2db213aa5f76f00ba49"',
            '"v": "0x0"'
        ]

        for fragment in fragments2:
            chars = find_in_code(self.code, fragment)
            scene.play(Indicate(*chars, color=SECONDARY_COLOR, run_time=0.4))

        scene.wait(4.5)

        fragments3 = [' 0', ' 1', ' 27', ' 28']
        for fragment in fragments3:
            chars = find_in_code(self.code, fragment)
            scene.play(Indicate(*chars, color=SECONDARY_COLOR, run_time=0.5))

        self.new_subsection(scene, "Ethereum Transaction",
            sound="data/sound/episode1/s29-2.wav")

        self.signature = EquationBoxWithIcons.create(
            "⎘", "r = R_x \mod n", PRIMARY_COLOR,
            "⎘", "s = (msg + r \cdot K_{Priv}) \cdot secret^{-1} \mod n", PRIMARY_COLOR
        )

        scene.wait(2)
        self.r_box = EquationBox("R = (r, ?)")

        VGroup(self.signature, self.r_box).arrange(RIGHT, buff=1).next_to(
            self.code, DOWN, buff=0.5)

        scene.play(FadeIn(self.signature))
        scene.play(Indicate(self.signature[1],  color=SECONDARY_COLOR))
        scene.wait(4)
        scene.play(FadeIn(self.r_box))

        self.new_subsection(scene, "Why four values",
            sound="data/sound/episode1/s29-3.wav")
        scene.play(FadeOut(self.code), FadeOut(self.title_text))

        self.chart = DiscreteEllipticChart(include_details=False)
        self.chart.scale(0.8).next_to(self.signature, UP, buff=0.5)
        scene.play(FadeIn(self.chart))


        line = self.chart.create_vertical_line(5)
        scene.play(FadeIn(line), Wait())
        dots = self.chart.find_dots_by_x(5)
        label1 = Tex("0", color=PRIMARY_COLOR).scale(0.8).next_to(
            dots[0], RIGHT, buff=0.2)
        label2 = Tex("1", color=PRIMARY_COLOR).scale(0.8).next_to(
            dots[1], RIGHT, buff=0.2)
        label3 = Tex("27", color=PRIMARY_COLOR).scale(0.8).next_to(
            dots[0], RIGHT, buff=0.2)
        label4 = Tex("28", color=PRIMARY_COLOR).scale(0.8).next_to(
            dots[1], RIGHT, buff=0.2)
        scene.play(FadeIn(label1), FadeIn(label2))

        self.new_subsection(scene, "27 and 28",
            sound="data/sound/episode1/s29-4.wav")

        scene.play(TransformMatchingTex(label1, label3),
            TransformMatchingTex(label2, label4))

        self.new_subsection(scene, "Mystery solved",
            sound="data/sound/episode1/s29-5.wav")
        scene.play(FadeOut(line), FadeOut(label3), FadeOut(label4))
        scene.play(FadeOut(self.signature), FadeOut(self.r_box))
        scene.play(FadeOut(self.chart))

    def animate_out(self, scene):
        pass
