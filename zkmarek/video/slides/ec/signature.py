from manim import (DOWN, GREEN, GREY, LEFT, RED, RIGHT, UP, Circumscribe,
                   Create, DashedLine, FadeIn, FadeOut, Indicate, MathTex,
                   ReplacementTransform, Text, TransformMatchingTex, VGroup,
                   Write)

from zkmarek.video.mobjects.equation_box import (EquationBox,
                                                 EquationBoxWithIcons)
from zkmarek.video.mobjects.signature import Signature as SignatureBoxFront
from zkmarek.video.mobjects.strike_line import StrikeLine
from zkmarek.video.slides.common.slide_base import SlideBase


class Signature(SlideBase):
    sender_label: Text
    receiver_label: Text
    h_line: DashedLine

    def __init__(self):
        super().__init__("Signature")

    def construct(self):
        self.title = "Signature"
        self.sender_label = Text("Signatory")
        self.receiver_label = Text("Verifier")

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
            "⚿", "K_{Priv} = random()", RED,
            "⚿", "K_{Pub} = {{K_{Priv} \cdot G}}", GREEN
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
            "⚂", "secret = random()", RED
        ).next_to(msg_box3, DOWN, buff=0.5)

        signature3 = EquationBoxWithIcons.create(
            "⚂", "secret = random()", RED,
            "⚂", "R = secret \cdot G", GREY
        ).next_to(msg_box3, DOWN, buff=0.5)

        signature4 = EquationBoxWithIcons.create(
            "⚂", "secret = random()", RED,
            "⚂", "R = secret \cdot G", GREY,
            "⎘", "r = R_x \mod n", GREEN
        ).next_to(msg_box3, DOWN, buff=0.5)

        signature5 = EquationBoxWithIcons.create(
            "⚂", "secret = random()", RED,
            "⚂", "R = {{secret \cdot G}}", GREY,
            "⎘", "r = R_x \mod n", GREEN,
            "⎘", "s = {{ (msg + r \cdot K_{Priv}) \cdot secret^{-1} }} \mod n", GREEN
        ).next_to(msg_box3, DOWN, buff=0.5)

        self.new_subsection(scene, "Introduce keys")
        scene.play(FadeIn(key_box1))
        self.new_subsection(scene, "Introduce message")
        scene.play(FadeIn(msg_box1))
        self.new_subsection(scene, "Introduce signature")
        signature.animate_in(scene)
        self.new_subsection(scene, "Message is hash")
        scene.play(ReplacementTransform(msg_box1, msg_box2))
        self.new_subsection(scene, "Message is msg")
        scene.play(ReplacementTransform(msg_box2, msg_box3))
        self.new_subsection(scene, "What are keys")
        scene.play(ReplacementTransform(key_box1, key_box2))
        self.new_subsection(scene, "What is signature")
        scene.play(ReplacementTransform(signature, signature2))
        self.new_subsection(scene, "Introduce R")
        scene.play(ReplacementTransform(signature2, signature3))
        self.new_subsection(scene, "Introduce r")
        scene.play(ReplacementTransform(signature3, signature4))
        self.new_subsection(scene, "Introduce s")
        scene.play(ReplacementTransform(signature4, signature5))

        self.new_subsection(scene, "From sender to receiver")

        ver_msg_box = msg_box3.copy()
        scene.play(ver_msg_box.animate.next_to(
            self.receiver_label, DOWN, buff=0.5
        ))

        ver_signature = EquationBoxWithIcons.create(
            "⎘", "r = R_x \mod n", GREEN,
            "⎘", "s = (msg + r \cdot K_{Priv}) \cdot secret^{-1} \mod n", GREEN
        ).align_to(signature5, DOWN)
        scene.play(ver_signature.animate.next_to(
            ver_msg_box, DOWN, buff=0.5
        ))

        self.new_subsection(scene, "Recover R")
        r_box = EquationBox("R = (r, ?)").next_to(
            ver_signature, DOWN, buff=0.5)
        scene.play(FadeIn(r_box))

        self.new_subsection(scene, "Introduce U1 and U2")
        variable_box = EquationBox(
            "{{R}} = (r, {{?}})",
            "u_1 = {{-msg \cdot r^{-1} }}",
            "u_2 = {{s \cdot r^{-1} }}",
        ).next_to(ver_signature, DOWN, buff=0.5)
        scene.play(ReplacementTransform(r_box, variable_box))

        self.new_subsection(scene, "Introduce Q")
        q_box = EquationBox(
            "Q = u_1 \cdot G + u_2 \cdot {{R}}"
        ).next_to(variable_box, DOWN, buff=0.5)
        scene.play(FadeIn(q_box))

        self.new_subsection(scene, "Equal to public key")
        q_box2 = EquationBox(
            "Q = u_1 \cdot G + u_2 \cdot {{R}} \stackrel{?}{=} K_{Pub}"
        ).next_to(variable_box, DOWN, buff=0.5)
        scene.play(ReplacementTransform(q_box, q_box2))


        self.new_subsection(scene, "Proof")
        equation = MathTex(
            "Q = u_1 \cdot G + u_2 {{\cdot R}}"
            ).scale(0.65).align_to(q_box2[0], LEFT + DOWN)
        scene.play(equation.animate.next_to(q_box, DOWN, buff=0.5))

        self.new_subsection(scene, "Expand R")
        scene.play(Circumscribe(equation[1]))
        scene.play(Circumscribe(signature5[3][1]))

        equation2 = MathTex(
            "Q = u_1 \cdot G + u_2 \cdot {{secret \cdot G}}"
            ).scale(0.65).next_to(q_box, DOWN, buff=0.5)
        scene.play(TransformMatchingTex(
            VGroup(equation, signature5[3].copy()), equation2))

        equation2b = MathTex(
            "Q = {{u_1}} {{\cdot G}} + {{u_2}} {{\cdot secret}} {{\cdot G}}"
            ).scale(0.65).next_to(q_box, DOWN, buff=0.5)
        scene.play(TransformMatchingTex(equation2, equation2b))

        self.new_subsection(scene, "Extract common factor")
        equation3 = MathTex(
            "Q = ({{u_1}} + {{u_2}} {{\cdot secret}}) {{\cdot  G}}"
            ).scale(0.65).next_to(q_box, DOWN, buff=0.5)
        scene.play(TransformMatchingTex(equation2b, equation3))

        self.new_subsection(scene, "Substitute u1 and u2")
        scene.play(Circumscribe(equation3[1]))
        scene.play(Circumscribe(variable_box[1][1]))

        scene.play(Circumscribe(equation3[3]))
        scene.play(Circumscribe(variable_box[2][1]))

        equation4 = MathTex(
            "Q = ({{-msg \cdot r^{-1} }} + {{s \cdot r^{-1}}} {{secret}}) {{\cdot  G}}"
            ).scale(0.65).next_to(q_box, DOWN, buff=0.5)
        scene.play(TransformMatchingTex(
            VGroup(variable_box[1].copy(), variable_box[2].copy(), equation3),
            equation4))

        equation4b = MathTex(
            "Q = (-msg \cdot r^{-1} + {{s}} {{\cdot r^{-1} secret) \cdot  G}}"
            ).scale(0.65).next_to(q_box, DOWN, buff=0.5)
        scene.play(TransformMatchingTex(equation4, equation4b))

        self.new_subsection(scene, "Substitute s")
        equation5 = MathTex(
            "Q = (-msg \cdot r^{-1} + {{ (msg + r \cdot K_{Priv}) \cdot secret^{-1} }} {{\cdot r^{-1} secret) \cdot  G}}" # noqa: E501 # pyright: ignore
            ).scale(0.65).next_to(q_box, DOWN, buff=0.5).align_on_border(RIGHT)

        h_line2 = DashedLine(
            scene.camera.frame_height / 2 * UP, scene.camera.frame_height / 3 * DOWN
        )

        scene.play(
            TransformMatchingTex(
                VGroup(equation4b, signature5[7].copy()),
                equation5),
            ReplacementTransform(self.h_line, h_line2))

        equation5b = MathTex(
            "Q = (-msg \cdot r^{-1} + (msg + r \cdot K_{Priv}) {{\cdot secret^{-1}}}  \cdot r^{-1} {{secret}}) \cdot  G}}" # noqa: E501 # pyright: ignore
            ).scale(0.65).next_to(q_box, DOWN, buff=0.5).align_on_border(RIGHT)

        scene.add(equation5b)
        scene.remove(equation5)

        self.new_subsection(scene, "Cancel secrete with inverse")

        scene.play(Indicate(equation5b[1]))
        scene.play(Indicate(equation5b[3]))
        strike1 = StrikeLine(equation5b[1])
        scene.play(Write(strike1))

        strike2 = StrikeLine(equation5b[3])
        scene.play(Write(strike2))

        equation6 = MathTex(
            "Q = (-msg \cdot r^{-1} + (msg + r \cdot K_{Priv}) {{}}  \cdot r^{-1} {{}}) \cdot G}}" # noqa: E501 # pyright: ignore
            ).scale(0.65).next_to(q_box, DOWN, buff=0.5).align_on_border(RIGHT)
        scene.play(TransformMatchingTex(equation5b, equation6),
            FadeOut(strike1),
            FadeOut(strike2))


        self.new_subsection(scene, "Multiply inverse of r")
        equation6b = MathTex(
            "Q = (-msg \cdot r^{-1} + ({{msg}} {{ }} + {{r \cdot}} K_{Priv}) {{\cdot r^{-1})}} \cdot G}}" # noqa: E501 # pyright: ignore
            ).scale(0.65).next_to(q_box, DOWN, buff=0.5).align_on_border(RIGHT)

        scene.add(equation6b)
        scene.remove(equation6)
        scene.play(Indicate(equation6b[7]))
        scene.play(Indicate(equation6b[1]))
        scene.play(Indicate(equation6b[5]))

        equation7 = MathTex(
            "Q = (-msg \cdot r^{-1} + ({{msg}} {{\cdot r^{-1} }} + {{ }} K_{Priv}) ) {{ }} \cdot G}}" # noqa: E501 # pyright: ignore
            ).scale(0.65).next_to(q_box, DOWN, buff=0.5).align_on_border(RIGHT)

        scene.play(TransformMatchingTex(equation6b, equation7))

        self.new_subsection(scene, "Remove brackets")
        equation7b = MathTex(
            "Q = (-msg \cdot r^{-1} + (msg \cdot r^{-1} + K_{Priv}) ) \cdot G}}"
            ).scale(0.65).next_to(q_box, DOWN, buff=0.5).align_on_border(RIGHT)
        scene.add(equation7b)
        scene.remove(equation7)

        equation8 = MathTex(
            "Q = {{(-msg \cdot r^{-1} + }} {{(}}{{msg \cdot r^{-1} + }} K_{Priv} {{)}} {{ ) }} \cdot G}}" # noqa: E501 # pyright: ignore
            ).scale(0.65).next_to(q_box, DOWN, buff=0.5).align_on_border(RIGHT)

        scene.play(TransformMatchingTex(equation7b, equation8))

        equation9 = MathTex(
            "Q = {{(-msg \cdot r^{-1} + }} {{ }}{{msg \cdot r^{-1} + }}  K_{Priv} {{ }} {{ ) }} \cdot G}}" # noqa: E501 # pyright: ignore
            ).scale(0.65).next_to(q_box, DOWN, buff=0.5).align_on_border(RIGHT)

        scene.play(TransformMatchingTex(equation8, equation9))

        self.new_subsection(scene, "Cancel msg*r^-1 with inverse")
        strike1 = StrikeLine(equation9[1])
        scene.play(Write(strike1))

        strike2 = StrikeLine(equation9[4])
        scene.play(Write(strike2))


        equation10 = MathTex(
            "Q = {{}} {{ }}{{ }} K_{Priv} {{ }} {{ }} \cdot G}}"
            ).scale(0.65).next_to(q_box, DOWN, buff=0.5)

        scene.play(TransformMatchingTex(equation9, equation10),
            FadeOut(strike1),
            FadeOut(strike2))

        self.new_subsection(scene, "Summary")
        scene.play(Indicate(equation10))
        scene.play(Indicate(key_box2[3]))

        self.new_subsection(scene, "Note v")
        scene.play(Indicate(variable_box[0][2]))
