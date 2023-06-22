from manim import DOWN, UP, FadeIn, FadeOut, Text, VGroup
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
        self.label = Text(self.title)
        self.label.to_edge(UP)
        self.group = VGroup(self.secp256k1, self.curve25519).arrange_in_grid(cols=2)
        self.group.next_to(self.label, DOWN)

    def animate_in(self, scene):
        scene.play(FadeIn(self.label))
        scene.play(FadeIn(self.secp256k1))
        self.new_subsection(scene, "Curve25519")
        scene.play(FadeIn(self.curve25519))

    def animate_out(self, scene):
        scene.play(FadeOut(self.secp256k1))
