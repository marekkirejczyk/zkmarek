from manim import (DOWN, GREEN, LEFT, RED, RIGHT, UP, Create, DashedLine,
                   FadeIn, FadeOut, MathTex, Mobject, Rectangle, Scene,
                   SurroundingRectangle, Text, Transform, VGroup)

from zkmarek.video.slides.common.slide_base import SlideBase


class Box(VGroup):
    rectangle: Rectangle

    def __init__(self, *mobjects, **kwargs):
        super().__init__(*mobjects, **kwargs)
        self.arrange_in_grid(cols=2, cell_alignment=LEFT + UP)
        self.rectangle = SurroundingRectangle(self, buff=0.15, corner_radius=0.1)
        self.add(self.rectangle)
        self.rectangle.set_center(self.get_center())

    def morph_to(self, scene: Scene, index: int, new_mobject: Mobject):
        old = self[index]
        new_mobject.align_to(old, LEFT + UP)
        scene.play(Transform(old, new_mobject))
        self[index] = new_mobject


class KeyBox(Box):
    public_key: Text
    private_key: Text

    def __init__(self):
        self.private_key = Text("Private key", color=RED)
        self.public_key = Text("Public key", color=GREEN)
        super().__init__(
            Text("⚿", color=RED),
            self.private_key,
            Text("⚿", color=GREEN),
            self.public_key,
        )

    def animate_to_math(self, scene: Scene):
        self.morph_to(scene, 1, MathTex("k = rand()", color=RED))
        self.morph_to(scene, 1, MathTex("k", color=RED))
        self.morph_to(scene, 3, MathTex("k \cdot G", color=RED))


class Signature(SlideBase):
    key_box = KeyBox()
    sender_label: Text
    receiver_label: Text
    h_line: DashedLine

    def __init__(self):
        super().__init__("Signature")

    def construct(self):
        self.title = "Signature"
        self.sender_label = Text("Sender")
        self.receiver_label = Text("Receiver")

    def fade_in_labels(self, scene):
        self.sender_label.move_to(scene.camera.frame_width / 4 * LEFT)
        self.receiver_label.move_to(scene.camera.frame_width / 4 * RIGHT)
        self.sender_label.to_edge(UP)
        self.receiver_label.to_edge(UP)
        scene.play(FadeIn(self.sender_label), FadeIn(self.receiver_label))

        self.h_line = DashedLine(
            scene.camera.frame_height / 2 * DOWN, scene.camera.frame_height / 2 * UP
        )
        scene.play(Create(self.h_line))

    def animate_in(self, scene):
        scene.play(FadeIn(self.key_box))
        self.key_box.animate_to_math(scene)
        self.fade_in_labels(scene)
        scene.play(self.key_box.animate.next_to(self.sender_label, DOWN, buff=0.5))

    def animate_out(self, scene):
        scene.play(FadeOut(self.key_box))
