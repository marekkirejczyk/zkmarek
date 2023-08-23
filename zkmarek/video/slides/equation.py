from manim import (DOWN, UP, FadeIn, FadeOut, MathTex, MoveToTarget,
                   ReplacementTransform, Text, TransformMatchingShapes, VGroup,
                   Write)
from zkmarek.video.constant import SECONDARY_COLOR, PRIMARY_COLOR
from .common.slide_base import SlideBase


class EquationSlide(SlideBase):
    def __init__(self) -> None:
        super().__init__(title="Elliptic Curve Equation")

        self.weierstrass_form = Text(r"Weierstrass form", color=PRIMARY_COLOR)
        self.weierstrass_equation = MathTex(r"y^2 = x^3 + ax + b", color=PRIMARY_COLOR)
        self.secp256k1_label = Text(r"Secp256k1 equation", color=PRIMARY_COLOR)
        self.secp_equation1 = self.weierstrass_equation.copy()
        self.secp_equation2 = MathTex(r"y^2 = x^3 + 0x + 7", color=PRIMARY_COLOR)
        self.secp_equation3 = MathTex(r"y^2 = x^3 + 7", color=PRIMARY_COLOR)
        self.a = MathTex(r"a = 0", color=SECONDARY_COLOR)
        self.b = MathTex(r"b = 7", color=SECONDARY_COLOR)
        self.ab = VGroup(self.a, self.b).arrange_submobjects()

        self.secp_equation1[0][6:7].set_color(SECONDARY_COLOR)
        self.secp_equation1[0][9:10].set_color(SECONDARY_COLOR)
        self.secp_equation2[0][6:7].set_color(SECONDARY_COLOR)
        self.secp_equation2[0][9:10].set_color(SECONDARY_COLOR)

        # positions
        self.weierstrass_form.next_to(self.weierstrass_equation, UP)
        self.secp256k1_label.next_to(self.weierstrass_equation, DOWN, buff=1)
        self.secp_equation1.generate_target()
        self.secp_equation1.target.next_to(self.secp256k1_label, DOWN)
        self.secp_equation2.next_to(self.secp256k1_label, DOWN)
        self.secp_equation3.next_to(self.secp256k1_label, DOWN)
        self.ab.next_to(self.secp_equation2, DOWN)

    def animate_in(self, scene):
        self.play_sound(scene, "data/sound/episode/s5-1.wav")
        scene.wait(1)
        scene.play(Write(self.weierstrass_form), run_time=2)

        self.new_subsection(scene,
            "equation",
            sound="data/sound/episode/s5-2.wav")

        scene.play(Write(self.weierstrass_equation), run_time=9)

        self.new_subsection(scene,
            "Secp256k1",
            sound="data/sound/episode/s5-3.wav")

        scene.play(Write(self.secp256k1_label))
        scene.play(Write(self.secp_equation1))
        scene.play(MoveToTarget(self.secp_equation1))
        scene.play(FadeIn(self.ab))
        scene.play(
            ReplacementTransform(self.secp_equation1, self.secp_equation2),
            FadeOut(self.ab))
        scene.play(TransformMatchingShapes(self.secp_equation2, self.secp_equation3))
        self.new_subsection(scene,
            "Ethereum curve",
            sound="data/sound/episode/s5-4.wav")
        scene.wait(4)


    def animate_out(self, scene):
        scene.play(FadeOut(self.weierstrass_form), FadeOut(self.weierstrass_equation))
        scene.play(FadeOut(self.secp256k1_label), FadeOut(self.secp_equation3))

