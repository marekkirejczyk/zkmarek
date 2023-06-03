from manim import DOWN, GREEN, RED, FadeIn, FadeOut, MathTex, Text, Transform, VGroup
from manimpango import list_fonts

from zkmarek.video.slides.common.slide_base import SlideBase


class Signature(SlideBase):
    public_key: Text
    private_key: Text

    def __init__(self):
        super().__init__("Signature")
        self.title = "Signature"

    def construct(self):
        self.private_key = Text("⚿ Private key", color=RED)
        self.public_key = Text("⚿ Public key", color=GREEN)
        self.public_key.next_to(self.private_key, DOWN)
        print(list_fonts())

    def animate_in(self, scene):
        scene.play(FadeIn(self.public_key), FadeIn(self.private_key))
        new_private_key = Text("⚿ k = rand()", color=RED, font="Noto Sans")
        new_public_key = Text("⚿ k * G", color=GREEN)
        new_public_key.next_to(new_private_key, DOWN)
        scene.play(Transform(self.private_key, new_private_key))
        scene.play(Transform(self.public_key, new_public_key))

        self.public_key = new_public_key
        self.private_key = new_private_key

    def animate_out(self, scene):
        scene.play(FadeOut(self.public_key))

