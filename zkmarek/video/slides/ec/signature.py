from re import S
from manim import (DOWN, GREEN, GREY, LEFT, RED, RIGHT, UP, Circumscribe,
                   Create, DashedLine, FadeIn, FadeOut, Indicate, Line, Text,
                   Transform, Write)
from zkmarek.video.mobjects.equation_box import (EquationBox,
                                                 EquationBoxWithIcons)
from zkmarek.video.mobjects.signature import Signature as SignatureBoxFront
from zkmarek.video.slides.common.slide_base import SlideBase


class Signature(SlideBase):
    sender_label: Text
    receiver_label: Text
    h_line: DashedLine

    def __init__(self):
        super().__init__("Signature")

    def construct(self):
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
            scene.camera.frame_height / 2 * UP, scene.camera.frame_height / 2 * DOWN
        )
        scene.play(Create(self.h_line))

    def animate_in(self, scene):
        self.fade_in_board(scene)
        key_box1 = EquationBoxWithIcons.create(
            "⚿", "Private\ key", RED,
            "⚿", "Public\ key", GREEN
        ).next_to(self.sender_label, DOWN, buff=0.5)

        key_box2 = EquationBoxWithIcons.create(
            "⚿", "K_{Priv} = k\ (random)", RED,
            "⚿", "K_{Pub} = k \cdot G", GREEN
        ).next_to(self.sender_label, DOWN, buff=0.5)

        msg_box1 =  EquationBoxWithIcons.create(
            "✉", "Lorem\ ipsum\ dolor\ sit\ amet...", GREEN
            ).next_to(key_box2, DOWN, buff=0.5)

        msg_box2 =  EquationBoxWithIcons.create(
            "✉", "hash(\"Lorem\ ipsum\ dolor\ sit\ amet...\")", GREEN
            ).next_to(key_box2, DOWN, buff=0.5)

        msg_box3 =  EquationBoxWithIcons.create(
            "✉", "msg =hash(\"...\")", GREEN
            ).next_to(key_box2, DOWN, buff=0.5)

        signature = SignatureBoxFront(height=1).next_to(
            msg_box3, DOWN, buff=0.5
        )

        signature2 = EquationBoxWithIcons.create(
            "⚂", "secret\ (random)", RED
        ).next_to(msg_box3, DOWN, buff=0.5)

        signature3 = EquationBoxWithIcons.create(
            "⚂", "secret\ (random)", RED,
            "⚂", "R = secret \cdot G", GREY
        ).next_to(msg_box3, DOWN, buff=0.5)

        signature4 = EquationBoxWithIcons.create(
            "⚂", "secret\ (random)", RED,
            "⚂", "R = secret \cdot G", GREY,
            "⎘", "r = R_x \mod n", GREEN
        ).next_to(msg_box3, DOWN, buff=0.5)

        signature5 = EquationBoxWithIcons.create(
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

        ver_key_box = EquationBoxWithIcons.create(
            "⚿", "K_{Pub} = k \cdot G", GREEN
        ).align_to(key_box2, DOWN)
        scene.play(ver_key_box.animate.next_to(
            self.receiver_label, DOWN, buff=0.5
        ))

        ver_msg_box = msg_box3.copy()
        scene.play(ver_msg_box.animate.next_to(
            ver_key_box, DOWN, buff=0.5
        ))

        ver_signature = EquationBoxWithIcons.create(
            "⎘", "r = R_x \mod n", GREEN,
            "⎘", "s = (msg + r * K_{Priv})*secret^{-1} \mod n", GREEN
        ).align_to(signature5, DOWN)
        scene.play(ver_signature.animate.next_to(
            ver_msg_box, DOWN, buff=0.5
        ))

        equation_box = EquationBox(
            "{{U}} = msg * s^{-1} \mod n",
            "{{V}} = r * s^{-1} \mod n",
        ).next_to(
            ver_signature, DOWN, buff=0.5
        )
        scene.play(FadeIn(equation_box))

        c_box = EquationBox(
            "C = {{U}} \cdot G + {{V}} \cdot K_{Pub}",
            "C_x \mod n \stackrel{?}{=} r"
        ).next_to(
            equation_box, DOWN, buff=0.5
        )
        scene.play(FadeIn(c_box))
        scene.play(Circumscribe(equation_box[0][0]))
        scene.play(Circumscribe(c_box[0][1]))
        scene.play(Circumscribe(equation_box[1][0]))
        scene.play(Circumscribe(c_box[0][3]))

        c_box2 = EquationBox(
            "C = msg * {{s^{-1}}}\cdot {{G}} + r * {{s^{-1}}} * K_{Priv} \cdot {{G}}",
            "C_x \mod n \stackrel{?}{=} r"
        ).next_to(
            equation_box, DOWN, buff=0.5
        )

        scene.play(Transform(c_box, c_box2))
        scene.play(Circumscribe(c_box2[0][1]))
        scene.play(Circumscribe(c_box2[0][5]))
        scene.play(Circumscribe(c_box2[0][3]))
        scene.play(Circumscribe(c_box2[0][7]))

        c_box3 = EquationBox(
            "C = {{s^{-1} \cdot G}} (msg + r * K_{Priv})",
            "C_x \mod n \stackrel{?}{=} r"
        ).next_to(
            equation_box, DOWN, buff=0.5
        )

        scene.remove(c_box)
        scene.play(Transform(c_box2, c_box3))
        scene.play(Circumscribe(c_box3[0][1]))

        scene.play(Indicate(ver_signature[3]))

        ver_signature2 = EquationBoxWithIcons.create(
            "⎘", "r = R_x \mod n", GREEN,
            "⎘", "s^{-1} = (msg + r * K_{Priv})^{-1} * secret", GREEN
        ).next_to(ver_msg_box, DOWN, buff=0.5)
        scene.play(Transform(ver_signature, ver_signature2))

        c_box4 = EquationBox(
            "C = G \cdot secret * {{(msg + r * K_{Priv})^{-1}}} * {{(msg + r * K_{Priv})}}",
            "C_x \mod n \stackrel{?}{=} r"
        ).next_to(
            equation_box, DOWN, buff=0.5
        ).align_on_border(RIGHT)

        h_line2 = DashedLine(
            scene.camera.frame_height / 2 * UP, scene.camera.frame_height / 3 * DOWN
        )
        scene.remove(c_box2)
        scene.play(Transform(c_box3, c_box4), Transform(self.h_line, h_line2))

        c1 = c_box4[0][1]
        strike1 = Line(start=c1.get_critical_point(DOWN + LEFT), end=c1.get_critical_point(UP + RIGHT))
        scene.play(Write(strike1))

        c2 = c_box4[0][3]
        strike2 = Line(start=c2.get_critical_point(DOWN + LEFT), end=c2.get_critical_point(UP + RIGHT))
        scene.play(Write(strike2))

        c_box5 = EquationBox(
            "C = G \cdot secret",
            "C_x \mod n \stackrel{?}{=} r"
        ).next_to(
            equation_box, DOWN, buff=0.5
        )
        h_line3 = DashedLine(
            scene.camera.frame_height / 2 * UP, scene.camera.frame_height / 2 * DOWN
        )

        scene.remove(c_box3)
        scene.remove(self.h_line)
        scene.play(
            Transform(c_box4, c_box5),
            Transform(h_line2, h_line3),
            FadeOut(strike1),
            FadeOut(strike2))

        scene.play(Indicate(c_box5[0]))
        scene.play(Indicate(signature5[3]))
        scene.play(Indicate(c_box5[1]))
        scene.play(Indicate(signature5[5]))
