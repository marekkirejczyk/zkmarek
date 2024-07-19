from manim import DOWN, UP, RIGHT, Brace, FadeIn, FadeOut, MathTex, Text, Unwrite, Write, VGroup, TransformMatchingShapes, Indicate

from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR, PRIMARY_FONT, HIGHLIGHT_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.episode3.morphin_math_text import MorphinMathText
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
    bilinearity_label: MathTex
    bilinearity: MathTex
    bilinearity_morph: MorphinMathText
    non_degeneracy_label: MathTex
    non_degeneracy: MathTex

    def __init__(self):
        super().__init__("Pairing")

    def construct(self):
        self.definition_label = Text("Pairing", font_size=50, color=PRIMARY_COLOR, font = PRIMARY_FONT)
        self.definition = MathTex(r"{{e}}: {{G_1}}  \times {{G_2}} \rightarrow {{G_T}}", font_size=70, color=PRIMARY_COLOR)
        self.brace1 = Brace(self.definition[2], DOWN, color=PRIMARY_COLOR)
        self.brace2 = Brace(self.definition[4], DOWN, color=PRIMARY_COLOR)
        self.brace3 = Brace(self.definition[6], DOWN, color=PRIMARY_COLOR)
        self.brace1.shift(UP * 2.5)
        self.brace2.shift(UP * 2.5)
        self.brace3.shift(UP * 2.5)
        self.brace1_label = Text(r"Subgroups of points on elliptic curve", font_size=30, color=PRIMARY_COLOR, font = PRIMARY_FONT)
        self.brace1.put_at_tip(self.brace1_label)
        self.brace3_label = Text(r"Prime field", font_size=30, color=PRIMARY_COLOR, font = PRIMARY_FONT)
        self.brace3.put_at_tip(self.brace3_label)
        self.chart = DiscreetePolynomialChart(41, poly).scale(0.55)
        self.bilinearity_label = Text("Bilinearity", font_size=40, color=SECONDARY_COLOR, font = PRIMARY_FONT)
        self.bilinearity1 = MathTex(r"e({{P}} \oplus {{P'}}, Q)", font_size = 40, color = SECONDARY_COLOR)
        self.bilinearity = MathTex(r"e({{P}} {{\oplus}} {{P'}}, Q) = e({{P}}, Q) {{\oplus}} e({{P'}}, Q)", font_size=40, color=SECONDARY_COLOR)
        self.bilinearity2 = MathTex(r"e(P + P', Q) = e({{P}}, Q) \oplus e({{P'}}, Q)", font_size=40, color=SECONDARY_COLOR)
        self.bilinearity3 = MathTex(r"e(P + P', Q) = e({{P}}, Q) \cdot e({{P'}}, Q)", font_size=40, color=SECONDARY_COLOR)

        self.bilinearity1[1].set_color(PRIMARY_COLOR)
        self.bilinearity1[3].set_color(PRIMARY_COLOR)
        self.bilinearity[1].set_color(PRIMARY_COLOR)
        self.bilinearity[5].set_color(PRIMARY_COLOR)
        self.bilinearity[7].set_color(PRIMARY_COLOR)
        self.bilinearity[11].set_color(PRIMARY_COLOR)
        self.bilinearity2[1].set_color(PRIMARY_COLOR)
        self.bilinearity2[3].set_color(PRIMARY_COLOR)
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
        ]).shift(DOWN)
        self.multiplying = MathTex(r"a\cdot P = {{P+P+P \cdots}}", color = HIGHLIGHT_COLOR, font_size =40).next_to(self.bilinearity, DOWN).shift(DOWN)
        self.multiplying_brace = Brace(self.multiplying[1], DOWN, color = PRIMARY_COLOR)
        self.multiplying_brace_label = Text(r"a times", font_size=30, color=PRIMARY_COLOR, font = PRIMARY_FONT)
        self.multiplying_brace.put_at_tip(self.multiplying_brace_label)
        self.non_degeneracy_label = Text("Non-degeneracy", font_size=40, color=SECONDARY_COLOR, font = PRIMARY_FONT)
        nd_text = r"\forall{a \in G_1}, \forall{b \in G_2} ({{a, b \neq \mathcal{O}}}"
        nd_text += r" \Rightarrow e(a, b) \neq {{1_{G_T}}}) "
        self.non_degeneracy = MathTex(nd_text, font_size=40, color=SECONDARY_COLOR)
        self.computability_label = Text("Computability", font_size=40, color=SECONDARY_COLOR, font = PRIMARY_FONT)

        self.definition_label.to_edge(UP)
        self.definition.next_to(self.definition_label, DOWN)
        self.bilinearity_label.next_to(self.definition, DOWN, buff=0.8)
        self.bilinearity.next_to(self.bilinearity_label, DOWN)
        self.bilinearity2.next_to(self.bilinearity_label, DOWN)
        self.bilinearity3.next_to(self.bilinearity_label, DOWN)
        self.non_degeneracy_label.next_to(self.bilinearity, DOWN, buff=1)
        self.non_degeneracy.next_to(self.non_degeneracy_label, DOWN)
        self.computability_label.next_to(self.non_degeneracy, DOWN, buff=0.6)
        self.brace1_label.shift(RIGHT)

    def animate_in(self, scene):
        self.new_subsection(scene, "what is a pairing", "data/sound/episode3/slide2-0.mp3")
        scene.play(Write(self.definition_label))
        scene.play(Write(self.definition))

        scene.play(FadeIn(self.brace1, self.brace2))
        scene.play(FadeIn(self.brace1_label))
        scene.wait(0.6)
        scene.play(Indicate(self.definition[2], color = HIGHLIGHT_COLOR), run_time=0.7)
        scene.play(Indicate(self.definition[4], color = HIGHLIGHT_COLOR), run_time=0.7)
        scene.play(FadeOut(self.brace1, self.brace2), FadeOut(self.brace1_label))

        scene.play(FadeIn(self.brace3))
        scene.play(FadeIn(self.brace3_label), Indicate(self.definition[6], color = HIGHLIGHT_COLOR))
        scene.play(FadeOut(self.brace3), FadeOut(self.brace3_label))
        scene.wait(3.3)
        scene.play(Indicate(self.definition[0], color = HIGHLIGHT_COLOR, scale_factor=2))

        self.new_subsection(scene, "bilinear definition", "data/sound/episode3/slide2-1.mp3")
        scene.play(Write(self.bilinearity_label))
        scene.play(Write(self.bilinearity1))
        scene.wait(4.3)
        scene.play(Indicate(self.bilinearity1[1], color = PRIMARY_COLOR))
        scene.play(Indicate(self.bilinearity1[3], color = PRIMARY_COLOR))
        scene.wait(1)
        scene.play(TransformMatchingShapes(VGroup(self.bilinearity1[1].copy(), self.bilinearity1[3].copy(), self.bilinearity1), self.bilinearity))
        scene.wait(3)
        scene.play(Indicate(self.bilinearity[1], color = HIGHLIGHT_COLOR), Indicate(self.bilinearity[7], color = HIGHLIGHT_COLOR))
        scene.play(Indicate(self.bilinearity[11], color = HIGHLIGHT_COLOR), Indicate(self.bilinearity[5], color = HIGHLIGHT_COLOR))

        self.new_subsection(scene, "operations on ec and pairings", "data/sound/episode3/slide2-2.mp3")
        scene.wait(2)
        scene.play(Indicate(self.bilinearity[3], color = HIGHLIGHT_COLOR))
        scene.wait(0.5)
        scene.play(Indicate(self.bilinearity[9], color = HIGHLIGHT_COLOR))
        scene.wait(4)
        scene.play(FadeOut(self.bilinearity), FadeIn(self.bilinearity2))
        
        scene.wait(4)
        scene.play(FadeOut(self.bilinearity2), FadeIn(self.bilinearity3))
        scene.wait(1)

        self.new_subsection(scene, "multiplying", "data/sound/episode3/slide2-3.mp3")
        self.bilinearity_morph.animate_in(scene)
        self.play_sound(scene, "data/sound/episode3/slide2-3_1.mp3")

        self.new_subsection(scene, "explaining the multiplying", "data/sound/episode3/slide2-4.mp3")
        scene.play(self.bilinearity_morph.texs[-1].animate.next_to(self.bilinearity, DOWN))
        
        scene.play(Write(self.multiplying), Write(self.multiplying_brace), Write(self.multiplying_brace_label))
        scene.wait(4)
        scene.play(Unwrite(self.multiplying), Unwrite(self.multiplying_brace), Unwrite(self.multiplying_brace_label))
        scene.wait(1)
        scene.play(Indicate(self.bilinearity3, color = PRIMARY_COLOR))
        scene.wait(3)

        self.new_subsection(scene, "non degeneracy", "data/sound/episode3/slide2-5.mp3")
        scene.play(Write(self.non_degeneracy_label))
        scene.play(Write(self.non_degeneracy))
        scene.wait(2.4)
        scene.play(Indicate(self.non_degeneracy[1], color = PRIMARY_COLOR))
        scene.wait(2)
        scene.play(Indicate(self.non_degeneracy[3], color = PRIMARY_COLOR))
        scene.wait(1.5)

        self.new_subsection(scene, "computability", "data/sound/episode3/slide2-6.mp3")
        scene.play(Write(self.computability_label))
        scene.wait(3.5)