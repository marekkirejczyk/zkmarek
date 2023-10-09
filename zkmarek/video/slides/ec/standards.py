from manim import (DOWN, UP, FadeIn, FadeOut, Indicate, ReplacementTransform,
                   Text, VGroup)

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT
from zkmarek.video.mobjects.standard import (Standard, curve25519_standard,
                                             secp256k1_standard)
from zkmarek.video.slides.common.slide_base import SlideBase


class Standards(SlideBase):
    secp256k1: Standard
    curve25519: Standard
    alt_BN128: Standard
    label: Text
    group: VGroup

    def __init__(self):
        super().__init__("Standards")
        self.title = "Standards"

    def construct(self):
        self.secp256k1 = secp256k1_standard()
        self.curve25519 = curve25519_standard()
        self.label = Text(self.title, font=PRIMARY_FONT, color=PRIMARY_COLOR)
        self.label.to_edge(UP)
        self.group = VGroup(self.secp256k1, self.curve25519
            ).arrange_in_grid(cols=2)
        self.group.next_to(self.label, DOWN)

    def animate_in(self, scene):
        self.new_subsection(scene, "Operations",
            sound="data/sound/episode1/s25-1.m4a")

        secp = []
        for i in range(0, 4):
            secp.append(self.secp256k1.copy_with_rows(i+1))
        scene.play(FadeIn(self.label), FadeIn(secp[0]))
        scene.wait(6.5)
        scene.play(ReplacementTransform(secp[0], secp[2]))
        scene.play(Indicate(secp[2].rows[0][0][1] ))
        scene.play(Indicate(secp[2].rows[1][0]))
        scene.play(Indicate(secp[2].rows[2][0]))
        self.new_subsection(scene, "Operations",
            sound="data/sound/episode1/s25-2.wav")
        scene.wait(1.5)
        scene.play(Indicate(secp[2].rows[1][0][1]))

        self.new_subsection(scene, "Operations",
            sound="data/sound/episode1/s25-3.wav")
        scene.play(ReplacementTransform(secp[2], secp[3]))
        scene.wait(2)
        scene.play(Indicate(secp[3].rows[3][0]))
        self.new_subsection(scene, "Operations",
            sound="data/sound/episode1/s25-4.wav")
        scene.play(ReplacementTransform(secp[3], self.secp256k1))
        scene.play(Indicate(self.secp256k1.rows[4][0]))
        scene.wait(8)
        scene.play(Indicate(self.secp256k1.rows[4][0][1]))
        self.new_subsection(scene, "Curve25519",
            sound="data/sound/episode1/s25-5.wav")

        scene.wait(5)
        scene.play(FadeIn(self.curve25519))
        scene.wait(3)
        scene.play(Indicate(self.curve25519.rows[0][0][1]))
        scene.play(Indicate(self.curve25519.rows[1][0]))
        scene.wait(1)
        scene.play(Indicate(self.curve25519.rows[2][0]))
        scene.wait(2)
        scene.play(Indicate(self.curve25519.rows[4][0]))
        self.new_subsection(scene, "Curve25519",
            sound="data/sound/episode1/s25-6.wav")
        scene.wait(13)

    def animate_out(self, scene):
        scene.play(FadeOut(self.secp256k1), FadeOut(self.curve25519))
