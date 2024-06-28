from manim import (
    DOWN,
    UP,
    RIGHT,
    Brace,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    Unwrite,
    Write,
    VGroup,
    MoveToTarget,
)

from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.episode3.morphin_math_text import MorphinMathText


class Pairing(SlideBase):
    definition_label: MathTex
    definition: MathTex
    brace1: Brace
    brace2: Brace
    brace3: Brace
    brace1_label: Text
    brace2_label: Text
    brace3_label: Text
    bilinearity_label: MathTex
    bilinearity: MathTex
    bilinearity_morph: MorphinMathText
    non_degeneracy_label: MathTex
    non_degeneracy: MathTex

    def __init__(self):
        super().__init__("Pairing")

    def construct(self):
        self.definition_label = MathTex(r"Pairing", font_size=50, color=PRIMARY_COLOR)
        self.definition = MathTex(
            r"e: {{G_1}}  \times {{G_2}} \rightarrow {{G_T}}",
            font_size=70,
            color=PRIMARY_COLOR,
        )
        self.brace1 = Brace(self.definition[1], DOWN, color=PRIMARY_COLOR)
        self.brace2 = Brace(self.definition[3], DOWN, color=PRIMARY_COLOR)
        self.brace3 = Brace(self.definition[5], DOWN, color=PRIMARY_COLOR)
        self.brace1.shift(UP * 2.5)
        self.brace2.shift(UP * 2.5)
        self.brace3.shift(UP * 2.5)
        self.brace1_label = Text(
            r"Subgroup of points on elliptic curve", font_size=30, color=PRIMARY_COLOR
        )
        self.brace1.put_at_tip(self.brace1_label)
        self.brace2_label = Text(
            r"Subgroup of points on elliptic curve", font_size=30, color=PRIMARY_COLOR
        )
        self.brace2.put_at_tip(self.brace2_label)
        self.brace3_label = Text(r"Prime field", font_size=30, color=PRIMARY_COLOR)
        self.brace3.put_at_tip(self.brace3_label)

        self.bilinearity_label = MathTex(
            r"Bilinearity", font_size=40, color=SECONDARY_COLOR
        )
        self.bilinearity = MathTex(
            r"e(P + P', Q) = e(P, Q) \cdot e(P', Q)",
            font_size=40,
            color=SECONDARY_COLOR,
        )
        self.bilinearity_morph = MorphinMathText(
            [
                r"{{e(aP, bQ)}}",
                r"{{e(aP, bQ)}} = e({{a}}P, bQ){{ }}",
                r"{{e(aP, bQ)}} = e({{ }}P, bQ){{^a}}",
                r"{{e(aP, bQ)}} = e({{ }}P, bQ){{^a}} = e(aP, {{b}}Q){{ }}",
                r"{{e(aP, bQ)}} = e({{ }}P, bQ){{^a}} = e(aP, {{ }}Q){{^b}}",
                r"{{e(aP, bQ)}} = e({{ }}P, bQ){{^a}} = e(aP, {{ }}Q){{^b}} = e({{a}}P, {{b}}Q){{^{}}}",
                r"{{e(aP, bQ)}} = e({{ }}P, bQ){{^a}} = e(aP, {{ }}Q){{^b}} = e({{ }}P, {{ }}Q){{^{ab}}}",
                r"{{e(aP, bQ)}} = e({{ }}P, bQ){{^a}} = e(aP, {{ }}Q){{^b}} = e({{ }}P, {{ }}Q){{^{ab}}}"
                " = e({{ }}P, {{ }}Q){{^{ab}}}",
                r"{{e(aP, bQ)}} = e({{ }}P, bQ){{^a}} = e(aP, {{ }}Q){{^b}} = e({{ }}P, {{ }}Q){{^{ab}}}"
                " = e({{b}}P, {{a}}Q){{ }}",
                r"{{e(aP, bQ)}} = e({{ }}P, {{ }}Q){{^{ab}}} = e({{b}}P, {{a}}Q){{ }}",
            ]
        )

        self.non_degeneracy_label = MathTex(
            r"Non-degeneracy", font_size=40, color=SECONDARY_COLOR
        )
        nd_text = r"\forall{a \in G_1}, \forall{b \in G_2} (a, b \neq \mathcal{O}"
        nd_text += r" \Rightarrow e(a, b) \neq 1_{G_T}) "
        self.non_degeneracy = MathTex(nd_text, font_size=40, color=SECONDARY_COLOR)
        self.computability_label = MathTex(
            r"Computability", font_size=40, color=SECONDARY_COLOR
        )

        self.definition_label.to_edge(UP)
        self.definition.next_to(self.definition_label, DOWN)
        self.bilinearity_label.next_to(self.definition, DOWN, buff=0.8)
        self.bilinearity.next_to(self.bilinearity_label, DOWN)
        self.non_degeneracy_label.next_to(self.bilinearity, DOWN, buff=0.6)
        self.non_degeneracy.next_to(self.non_degeneracy_label, DOWN)
        self.computability_label.next_to(self.non_degeneracy, DOWN, buff=0.6)

    def animate_in(self, scene):
        scene.play(Write(self.definition_label))
        scene.play(Write(self.definition))

        scene.play(FadeIn(self.brace1))
        scene.play(FadeIn(self.brace1_label))
        scene.play(FadeOut(self.brace1), FadeOut(self.brace1_label))

        scene.play(FadeIn(self.brace2))
        scene.play(FadeIn(self.brace2_label))
        scene.play(FadeOut(self.brace2), FadeOut(self.brace2_label))

        scene.play(FadeIn(self.brace3))
        scene.play(FadeIn(self.brace3_label))
        scene.play(FadeOut(self.brace3), FadeOut(self.brace3_label))

        scene.play(Write(self.bilinearity_label))
        scene.play(Write(self.bilinearity))
        self.bilinearity_morph.animate_in(scene)
        scene.play(Unwrite(self.bilinearity))
        scene.play(
            self.bilinearity_morph.texs[-1].animate.next_to(
                self.bilinearity_label, DOWN
            )
        )

        self.bilin_def = VGroup(
            self.definition,
            self.definition_label,
            self.bilinearity_label,
            self.bilinearity_morph,
        )

        self.bilin_def.generate_target()
        self.bilin_def.target.scale(0.3).to_edge(UP + RIGHT)

        scene.play(MoveToTarget(self.bilin_def))

        scene.play(Write(self.non_degeneracy_label))
        scene.play(Write(self.non_degeneracy))
        scene.play(Write(self.computability_label))
