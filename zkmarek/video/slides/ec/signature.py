from manim import (DOWN, GREEN, GREY, LEFT, RED, RIGHT, UP, Create, DashedLine,
                   FadeIn, FadeOut, MathTex, Mobject, Rectangle, Scene,
                   SurroundingRectangle, Text, Transform, VGroup)

from zkmarek.video.slides.common.slide_base import SlideBase


class Box(VGroup):
    rectangle: Rectangle

    def __init__(self, *mobjects, **kwargs):
        super().__init__(*mobjects, **kwargs)
        self.arrange_in_grid(cols=2, cell_alignment=LEFT + UP)
        self.rectangle = SurroundingRectangle(self, buff=0.2, corner_radius=0.1)
        self.add(self.rectangle)
        self.rectangle.set_center(self.get_center())
        self.scale(0.65)

    def morph_to(self, scene: Scene, index: int, new_mobject: Mobject):
        old = self[index]
        new_mobject.align_to(old, LEFT + UP)
        scene.play(Transform(old, new_mobject))
        self[index] = new_mobject
        new_rect = SurroundingRectangle(self, buff=0.2, corner_radius=0.1)
        scene.play(Transform(self.rectangle, new_rect))
        scene.remove(new_rect)
        scene.remove(self.rectangle)
        self.rectangle = new_rect


class KeyBox(Box):
    def __init__(self):
        super().__init__(
            Text("⚿", color=RED),
            MathTex("K_{Priv} = k (random)", color=RED),
            Text("⚿", color=GREEN),
            MathTex("K_{Pub} = k \cdot G", color=GREEN),
        )


class MsgBox(Box):
    def __init__(self):
        super().__init__(
            Text("✉", color=GREEN),
            MathTex('msg = hash("...")', color=GREEN),
        )


class SignatureBox(Box):
    def __init__(self):
        super().__init__(
            Text("⚂", color=RED),
            MathTex("secret = rand()", color=RED),
            Text("⚂", color=GREEN),
            MathTex("R = secret \cdot G", color=GREY),
            Text("⚂", color=GREEN),
            MathTex("r = R_x \mod n", color=GREEN),
            Text("⚂", color=GREEN),
            MathTex("s = (msg + r * K_{Priv})*secret^{-1} \mod n", color=GREEN),
        )


class VerifyBox(Box):
    def __init__(self, *mobjects, **kwargs):
        super().__init__(
            Text(""),
            MathTex("U = msg * s^{-1} \mod n"),
            Text(""),
            MathTex("V = r * s^{-1} \mod n"),
            Text(""),
            MathTex("C = U \cdot G + V \cdot K_{Pub}"),
            Text(""),
            MathTex("C_x \mod n \stackrel{?}{=} r"),
        )


class ExpansionBox(Box):
    def __init__(self, *mobjects, **kwargs):
        super().__init__(
            Text(""),
            MathTex("C = msg * s^{-1}\cdot G + r * s^{-1} * K_{Priv} \cdot G"),
            Text(""),
            MathTex("C = s^{-1} \cdot G (msg + r * K_{Priv})"),
            Text(""),
            MathTex("Note: s^{-1} = (msg + r * K_{Priv})^{-1} * secret"),
            Text(""),
            MathTex(
                "C = G \cdot secret * (msg + r * K_{Priv})^{-1} * (msg + r * K_{Priv})"
            ),
            Text(""),
            MathTex("C = G \cdot secret = R"),
            Text(""),
            MathTex("C_x \mod n \stackrel{?}{=} R_x \mod n"),
        )
        self.scale(0.8)


class Signature(SlideBase):

    def __init__(self):
        super().__init__("Signature")

    def construct(self):
        self.key_box = KeyBox()
        self.signature_box = SignatureBox()
        self.msg_box = MsgBox()
        self.verify_box = VerifyBox()
        self.expansion_box = ExpansionBox()
        self.title = "Signature"
        self.sender_label = Text("Sender")
        self.receiver_label = Text("Receiver")

    def fade_in_board(self, scene):
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
        self.fade_in_board(scene)
        self.key_box.next_to(self.sender_label, DOWN, buff=1)
        scene.play(FadeIn(self.key_box))
        self.msg_box.next_to(self.key_box, DOWN, buff=0.5)
        scene.play(FadeIn(self.msg_box))
        self.new_subsection(scene, "Introduce r, s")
        self.signature_box.next_to(self.msg_box, DOWN, buff=0.5)
        scene.play(FadeIn(self.signature_box))
        self.new_subsection(scene, "Introduce s, v")
        self.verify_box.next_to(self.receiver_label, DOWN, buff=1)
        scene.play(FadeIn(self.verify_box))
        self.new_subsection(scene, "Expand")
        self.expansion_box.next_to(self.verify_box, DOWN, buff=0.5)
        scene.play(FadeIn(self.expansion_box))

    def animate_out(self, scene):
        scene.play(
            FadeOut(self.expansion_box),
            FadeOut(self.verify_box),
            FadeOut(self.signature_box),
            FadeOut(self.msg_box),
            FadeOut(self.key_box),
            FadeOut(self.sender_label),
            FadeOut(self.receiver_label),
            FadeOut(self.h_line),
        )
