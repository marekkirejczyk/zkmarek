from manim import (
    DOWN,
    UP,
    LEFT,
    Brace,
    FadeIn,
    FadeOut,
    MathTex,
    Text,
    Unwrite,
    Write,
    VGroup,
    MoveToTarget,
    ReplacementTransform,
    Indicate,
)

from zkmarek.video.constant import (
    PRIMARY_COLOR,
    SECONDARY_COLOR,
    PRIMARY_FONT,
    HIGHLIGHT_COLOR,
)
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.episode3.morphin_math_text import MorphinMathText
from zkmarek.video.mobjects.equation_box import EquationBoxWithIcons
from zkmarek.video.slides.episode3.discreete_polynomial_chart import DiscreetePolynomialChart
def poly(x):
    return x * x * x - x * x * 2 + x * 3 + 4

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
        self.definition_label = Text("Pairing", font_size=50, color=PRIMARY_COLOR, font = PRIMARY_FONT)
        self.definition = MathTex(r"{{e}}: G_1  \times G_2 \rightarrow G_T", font_size=70, color=PRIMARY_COLOR)
        self.brace1 = Brace(self.definition[1], DOWN, color=PRIMARY_COLOR)
        self.brace2 = Brace(self.definition[3], DOWN, color=PRIMARY_COLOR)
        self.brace3 = Brace(self.definition[5], DOWN, color=PRIMARY_COLOR)
        self.brace1.shift(UP * 2.5)
        self.brace2.shift(UP * 2.5)
        self.brace3.shift(UP * 2.5)
        self.brace1_label = Text(r"Subgroup of points on elliptic curve", font_size=30, color=PRIMARY_COLOR, font = PRIMARY_FONT)
        self.brace1.put_at_tip(self.brace1_label)
        self.brace2_label = Text(r"Subgroup of points on elliptic curve", font_size=30, color=PRIMARY_COLOR, font = PRIMARY_FONT)
        self.brace2.put_at_tip(self.brace2_label)
        self.brace3_label = Text(r"Prime field", font_size=30, color=PRIMARY_COLOR, font = PRIMARY_FONT)
        self.brace3.put_at_tip(self.brace3_label)
        self.chart = DiscreetePolynomialChart(41, poly).scale(0.85)
        self.chart.to_edge(DOWN).scale(0.45)
        self.bilinearity_label = Text("Bilinearity", font_size=40, color=SECONDARY_COLOR, font = PRIMARY_FONT)
        self.bilinearity = MathTex(r"e({{P}} + {{P'}}, Q) = {{e(P, Q)}} \cdot {{e(P', Q)}}", font_size=40, color=SECONDARY_COLOR)
        self.bilinearity_morph = MorphinMathText([
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
            r"{{e(aP, bQ)}} = e({{ }}P, {{ }}Q){{^{ab}}} = e({{b}}P, {{a}}Q){{ }}"
        ])

        self.non_degeneracy_label = Text("Non-degeneracy", font_size=40, color=SECONDARY_COLOR, font = PRIMARY_FONT)
        nd_text = r"\forall{a \in G_1}, \forall{b \in G_2} (a, b \neq \mathcal{O}"
        nd_text += r" \Rightarrow e(a, b) \neq 1_{G_T}) "
        self.non_degeneracy = MathTex(nd_text, font_size=40, color=SECONDARY_COLOR)
        self.computability_label = Text("Computability", font_size=40, color=SECONDARY_COLOR, font = PRIMARY_FONT)

        self.definition_label.to_edge(UP)
        self.definition.next_to(self.definition_label, DOWN)
        self.bilinearity_label.next_to(self.definition, DOWN, buff=0.8)
        self.bilinearity.next_to(self.bilinearity_label, DOWN)
        self.non_degeneracy_label.next_to(self.bilinearity, DOWN, buff=0.6)
        self.non_degeneracy.next_to(self.non_degeneracy_label, DOWN)
        self.computability_label.next_to(self.non_degeneracy, DOWN, buff=0.6)

    def animate_in(self, scene):
        self.new_subsection(
            scene, "what is a pairing", "data/sound/episode3/slide2-0.mp3"
        )
        scene.play(Write(self.definition_label))
        scene.play(Write(self.definition))

        scene.play(FadeIn(self.brace1))
        scene.play(FadeIn(self.brace1_label))
        scene.play(FadeOut(self.brace1), FadeOut(self.brace1_label))

        scene.play(FadeIn(self.brace2))
        scene.play(FadeIn(self.brace2_label))
        scene.play(FadeOut(self.brace2), FadeOut(self.brace2_label))

        scene.play(FadeIn(self.brace3))#, Indicate(self.definition[1], color = HIGHLIGHT_COLOR))
        scene.play(FadeIn(self.brace3_label))#, Indicate(self.definition[1], color = HIGHLIGHT_COLOR))
        scene.play(FadeOut(self.brace3), FadeOut(self.brace3_label))#, Indicate(self.definition[3], color = HIGHLIGHT_COLOR))
        scene.wait(2.7)
        scene.play(Indicate(self.definition[0], color = HIGHLIGHT_COLOR))

        self.new_subsection(scene, "bilinear definition", "data/sound/episode3/slide2-1.mp3")
        scene.play(Write(self.bilinearity_label))
        scene.play(Write(self.bilinearity))
        scene.wait(2)
        scene.play(Indicate(self.bilinearity[0], color = PRIMARY_COLOR))
        scene.play(Indicate(self.bilinearity[1], color = PRIMARY_COLOR))
        scene.wait(2.5)
        scene.play(Indicate(self.bilinearity[2], color = PRIMARY_COLOR))
        scene.play(Indicate(self.bilinearity[3], color = PRIMARY_COLOR))
        scene.wait(5.3)
        scene.play(FadeIn(self.chart))
        scene.wait(2)
        scene.play(FadeOut(self.chart))
        self.new_subsection(
            scene, "bilinearity example", "data/sound/episode3/slide2-2.mp3"
        )
        self.example_bilinearity(scene)
        self.new_subsection(
            scene, "finishing example", "data/sound/episode3/slide2-3.mp3"
        )
        self.example_bilinearity2(scene)
        self.new_subsection(scene, "multiplying", "data/sound/episode3/slide2-4.mp3")
        self.bilinearity_morph.animate_in(scene)
        scene.play(Unwrite(self.bilinearity))
        self.new_subsection(
            scene, "explaining the multiplying", "data/sound/episode3/slide2-5.mp3"
        )
        scene.play(
            self.bilinearity_morph.texs[-1].animate.next_to(
                self.bilinearity_label, DOWN
            )
        )

        self.new_subsection(scene, "non degeneracy", "data/sound/episode3/slide2-6.mp3")
        scene.play(Write(self.non_degeneracy_label))
        scene.play(Write(self.non_degeneracy))
        self.new_subsection(scene, "computability", "data/sound/episode3/slide2-7.mp3")
        scene.play(Write(self.computability_label))

    def example_bilinearity(self, scene):
        self.other_things = VGroup(self.bilinearity, self.bilinearity_label, self.definition)
        self.other_things.generate_target()
        self.other_things.target.to_edge(LEFT).scale(0.4)
        scene.play(MoveToTarget(self.other_things))

        self.example_operaton = (
            MathTex(r"e(x,y)=2^xy", color=HIGHLIGHT_COLOR)
            .next_to(self.definition_label, DOWN)
        )
        self.x = MathTex(r"x=4", color=HIGHLIGHT_COLOR).next_to(
            self.example_operaton, DOWN
        )
        y1 = MathTex(r"y=5", color=HIGHLIGHT_COLOR).next_to(self.x, DOWN)
        self.y = MathTex(r"y=2+3", color=HIGHLIGHT_COLOR).next_to(self.x, DOWN)
        scene.play(Write(self.example_operaton), run_time=0.7)
        scene.wait(2)
        scene.play(Write(self.x), Write(y1), run_time=0.7)
        scene.wait(5)
        scene.play(ReplacementTransform(y1, self.y))
        scene.wait(2)
        pairing_bilin = EquationBoxWithIcons.create(
            "⎘",
            "{{e(4,2+3)}}",
            SECONDARY_COLOR,
            "⎘",
            "{{e(4, 2)\cdot e(4,3)}}",
            SECONDARY_COLOR,
            "⎘",
            "{{2^{4\cdot 2}\cdot2^{4\cdot 3}}}",
            SECONDARY_COLOR,
            "⎘",
            "{{2^{20}}}",
            SECONDARY_COLOR,
        ).next_to(self.y, DOWN, buff=1)
        scene.play(Write(pairing_bilin[:3]), run_time=0.7)
        scene.play(
            ReplacementTransform(pairing_bilin[:3], pairing_bilin[3:6]), run_time=0.7
        )
        scene.play(
            ReplacementTransform(pairing_bilin[3:7], pairing_bilin[6:]), run_time=0.7
        )

        scene.play(
            Unwrite(pairing_bilin[7:11]),
            Unwrite(self.example_operaton),
        )

    def example_bilinearity2(self, scene):
        pairing_bilin2 = EquationBoxWithIcons.create(
            "⎘",
            "{{e(4,5)}}",
            SECONDARY_COLOR,
            "⎘",
            "{{2^{4\cdot 5}}}",
            SECONDARY_COLOR,
            "⎘",
            "{{2^{20}}}",
            SECONDARY_COLOR,
        ).next_to(self.y, DOWN, buff=1)
        scene.wait(2)
        scene.play(Write(pairing_bilin2[:3]), run_time=0.7)
        scene.wait(2)
        scene.play(
            ReplacementTransform(pairing_bilin2[:3], pairing_bilin2[3:7]), run_time=0.7
        )
        scene.wait(2)
        scene.play(
            ReplacementTransform(pairing_bilin2[3:7], pairing_bilin2[7:11]),
            run_time=0.7,
        )
        scene.wait(2)
        scene.play(Unwrite(pairing_bilin2), Unwrite(self.x), Unwrite(self.y))
        self.other_things.generate_target()
        self.other_things.target.get_center().scale(1)
        scene.play(MoveToTarget(self.other_things))



