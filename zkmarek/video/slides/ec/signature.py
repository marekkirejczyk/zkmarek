from manim import DOWN, GREEN, RED, FadeIn, FadeOut, Text, Transform, VGroup, Rectangle, SurroundingRectangle, LEFT, UP, Scene, UL

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
    def __init__(self):
        super().__init__("Signature")
        self.title = "Signature"

    def construct(self):
        pass

    def animate_in(self, scene):
        scene.play(FadeIn(self.key_box))
        self.key_box.animate_to_math(scene)
        scene.play(self.key_box.animate.to_corner(UL))

    def animate_out(self, scene):
        scene.play(FadeOut(self.key_box))
