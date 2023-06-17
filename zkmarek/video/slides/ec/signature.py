from manim import (DOWN, GREEN, GREY, LEFT, RED, RIGHT, UP, Create, DashedLine,
                   FadeIn, FadeOut, MathTex, Rectangle, SurroundingRectangle,
                   Text, Transform, VGroup)
from zkmarek.video.mobjects.signature import Signature as SignatureBoxFront
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.utils import into_groups

class BoxWithIcons(VGroup):
    rectangle: Rectangle

    def __init__(self, *mobjects, **kwargs):
        super().__init__(*mobjects, **kwargs)
        self.arrange_in_grid(cols=2, cell_alignment=LEFT)
        self.rectangle = SurroundingRectangle(self, buff=0.2, corner_radius=0.1)
        self.add(self.rectangle)
        self.rectangle.set_center(self.get_center())
        self.scale(0.65)

    @staticmethod
    def create(*arg_list):
        result = []
        for three in into_groups(arg_list, 3):
            result.append(Text(three[0], color=three[2]))
            result.append(MathTex(three[1], color=three[2]))
        return BoxWithIcons(*result)

class VerifyBox(BoxWithIcons):
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


class ExpansionBox(BoxWithIcons):
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
        self.title = "Signature"
        self.verify_box = VerifyBox()
        self.expansion_box = ExpansionBox()
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
        key_box1 = BoxWithIcons.create(
            "⚿", "Private\ key", RED,
            "⚿", "Public\ key", GREEN
        ).next_to(self.sender_label, DOWN, buff=0.5)

        key_box2 = BoxWithIcons.create(
            "⚿", "K_{Priv} = k\ (random)", RED,
            "⚿", "K_{Pub} = k \cdot G", GREEN
        ).next_to(self.sender_label, DOWN, buff=0.5)

        msg_box1 =  BoxWithIcons.create(
            "✉", "Lorem\ ipsum\ dolor\ sit\ amet...", GREEN
            ).next_to(key_box2, DOWN, buff=0.5)

        msg_box2 =  BoxWithIcons.create(
            "✉", "hash(\"Lorem\ ipsum\ dolor\ sit\ amet...\")", GREEN
            ).next_to(key_box2, DOWN, buff=0.5)

        msg_box3 =  BoxWithIcons.create(
            "✉", "hash(\"...\")", GREEN
            ).next_to(key_box2, DOWN, buff=0.5)

        signature = SignatureBoxFront(height=1).next_to(
            msg_box3, DOWN, buff=0.5
        )

        signature2 = BoxWithIcons.create(
            "⚂", "secret\ (random)", RED
        ).next_to(msg_box3, DOWN, buff=0.5)

        signature3 = BoxWithIcons.create(
            "⚂", "secret\ (random)", RED,
            "⚂", "R = secret \cdot G", GREY
        ).next_to(msg_box3, DOWN, buff=0.5)

        signature4 = BoxWithIcons.create(
            "⚂", "secret\ (random)", RED,
            "⚂", "R = secret \cdot G", GREY,
            "⎘", "r = R_x \mod n", GREEN
        ).next_to(msg_box3, DOWN, buff=0.5)

        signature5 = BoxWithIcons.create(
            "⚂", "secret\ (random)", RED,
            "⚂", "R = secret \cdot G", GREY,
            "⎘", "r = R_x \mod n", GREEN,
            "⎘", "s = (msg + r * K_{Priv})*secret^{-1} \mod n", GREEN
        ).next_to(msg_box3, DOWN, buff=0.5)

        scene.play(FadeIn(key_box1))
        scene.play(FadeIn(msg_box1))
        signature.animate_in(scene)
        scene.play(Transform(msg_box1, msg_box2))
        scene.remove(msg_box1)
        scene.play(Transform(msg_box2, msg_box3))
        scene.play(Transform(key_box1, key_box2))
        scene.play(Transform(signature, signature2))
        scene.remove(signature)
        scene.play(Transform(signature2, signature3))
        scene.remove(signature2)
        scene.play(Transform(signature3, signature4))
        scene.remove(signature3)
        scene.play(Transform(signature4, signature5))


    def animate_in2(self, scene):
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

    def animate_out2(self, scene):
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
