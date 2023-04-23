from manim import *

from .slide_base import SlideBase


class EquationSlide(SlideBase):
    def __init__(self) -> None:
        SlideBase.__init__(self, title="Elliptic Curve equation")

        self.weierstrass_form = Text(r"Weierstrass form")
        self.weierstrass_equation = MathTex(r"y^2 = x^3 + ax + b")
        self.secp256k1_label = Text(r"Secp256k1 equation")
        self.secp_equation1 = self.weierstrass_equation.copy()
        self.secp_equation2 = MathTex(r"y^2 = x^3 + 0x + 7")
        self.secp_equation3 = MathTex(r"y^2 = x^3 + 7")
        self.a = MathTex(r"a = 0", color=YELLOW)
        self.b = MathTex(r"b = 7", color=YELLOW)
        self.ab = VGroup(self.a, self.b).arrange_submobjects()

        self.secp_equation1[0][6:7].set_color(YELLOW)
        self.secp_equation1[0][9:10].set_color(YELLOW)
        self.secp_equation2[0][6:7].set_color(YELLOW)
        self.secp_equation2[0][9:10].set_color(YELLOW)

        # positions
        self.weierstrass_form.next_to(self.weierstrass_equation, UP)
        self.secp256k1_label.next_to(self.weierstrass_equation, DOWN, buff=1)
        self.secp_equation1.generate_target()
        self.secp_equation1.target.next_to(self.secp256k1_label, DOWN)
        self.secp_equation2.next_to(self.secp256k1_label, DOWN)
        self.secp_equation3.next_to(self.secp256k1_label, DOWN)
        self.ab.next_to(self.secp_equation2, DOWN)

    def animate_in(self, scene):
        scene.play(Write(self.weierstrass_form))
        scene.play(Write(self.weierstrass_equation))

        scene.next_section("Secp256k1")
        scene.play(Write(self.secp256k1_label))
        scene.play(Write(self.secp_equation1))
        scene.play(MoveToTarget(self.secp_equation1))
        scene.play(FadeIn(self.ab))
        scene.play(AnimationGroup(
                    ReplacementTransform(self.secp_equation1, self.secp_equation2),
                    FadeOut(self.ab),
                ))
        scene.play(ReplacementTransform(self.secp_equation2, self.secp_equation3))


    def animate_out(self, scene):
        scene.play(
            Succession(
                FadeOut(self.weierstrass_form),
                FadeOut(self.weierstrass_equation),
                FadeOut(self.secp256k1_label),
                FadeOut(self.secp_equation3),
            )
        )
