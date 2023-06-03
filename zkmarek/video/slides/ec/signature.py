from manim import (DOWN, GREEN, LEFT, RED, RIGHT, UL, UP, Create, DashedLine,
                   FadeIn, FadeOut, Rectangle, Scene, SurroundingRectangle,
                   Text, Transform, VGroup)

from zkmarek.video.slides.common.slide_base import SlideBase


class Box(VGroup):
    rectangle: Rectangle

    def __init__(self, *mobjects, **kwargs):
        super().__init__(*mobjects, **kwargs)
        self.arrange(DOWN, aligned_edge=LEFT)
        self.rectangle = SurroundingRectangle(self, buff=0.15, corner_radius=0.1)
        self.add(self.rectangle)
        self.rectangle.set_center(self.get_center())


class KeyBox(Box):
    public_key: Text
    private_key: Text

    def __init__(self):
        self.private_key = Text("⚿ Private key", color=RED)
        self.public_key = Text("⚿ Public key", color=GREEN)
        super().__init__(self.private_key, self.public_key)

    def animate_to_math(self, scene: Scene):
        new_private_key = Text("⚿ k = rand()", color=RED)
        new_public_key = Text("⚿ k * G", color=GREEN)
        new_private_key.align_to(self.private_key, LEFT + UP)
        new_public_key.align_to(self.public_key, LEFT + UP)

        new_public_key.next_to(new_private_key, DOWN)
        scene.play(Transform(self.private_key, new_private_key))
        scene.play(Transform(self.public_key, new_public_key))

        self.public_key = new_public_key
        self.private_key = new_private_key


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
        scene.play(self.key_box.animate.to_corner(UL))
        self.fade_in_labels(scene)

    def animate_out(self, scene):
        scene.play(FadeOut(self.key_box))
