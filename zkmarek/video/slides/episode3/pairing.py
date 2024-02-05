from manim import MathTex, Write, Unwrite, DOWN, UP
from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase

class Pairing(SlideBase):
    definition_label: MathTex
    definition: MathTex
    bilinearity_label: MathTex
    bilinearity: MathTex
    bilinearity_ext: MathTex
    non_degeneracy_label: MathTex
    non_degeneracy: MathTex

    def __init__(self):
        super().__init__("Pairing")

    def construct(self):
        self.definition_label = MathTex(r"Pairing", font_size=50, color=PRIMARY_COLOR)
        self.definition = MathTex(r"e: G_1  \times G_2 \rightarrow G_T", font_size=70, color=PRIMARY_COLOR)
        self.bilinearity_label = MathTex(r"Bilinearity", font_size=40, color=SECONDARY_COLOR)
        self.bilinearity = MathTex(r"e(P + P', Q) = e(P, Q) \cdot e(P', Q)", font_size=40, color=SECONDARY_COLOR)
        bilinearity_tex = r"e([a]P, [b]Q) = e(P, [b]Q)^a = e([a]P, Q)^b = e(P, Q)^{ab} = e([b]P, [a]Q)"
        self.bilinearity_ext = MathTex(bilinearity_tex, font_size=40, color=SECONDARY_COLOR)
        self.non_degeneracy_label = MathTex(r"Non-degeneracy", font_size=40, color=SECONDARY_COLOR)
        nd_text = r"\forall a \in G_1, \forall b \in G_2, \left( (a, b \neq \mathcal{O})"
        nd_text += "\Rightarrow e(a, b) \neq 1_{G_T} \right)"
        self.non_degeneracy = MathTex(nd_text, font_size=40, color=SECONDARY_COLOR)
        self.computability_label = MathTex(r"Computability", font_size=40, color=SECONDARY_COLOR)

        self.definition_label.to_edge(UP)
        self.definition.next_to(self.definition_label, DOWN)
        self.bilinearity_label.next_to(self.definition, DOWN, buff=0.8)
        self.bilinearity.next_to(self.bilinearity_label, DOWN)
        self.bilinearity_ext.next_to(self.bilinearity, DOWN)
        self.non_degeneracy_label.next_to(self.bilinearity, DOWN, buff=0.6)
        self.non_degeneracy.next_to(self.non_degeneracy_label, DOWN)
        self.computability_label.next_to(self.non_degeneracy, DOWN, buff=0.6)

    def animate_in(self, scene):
        scene.play(Write(self.definition_label))
        scene.play(Write(self.definition))
        scene.play(Write(self.bilinearity_label))
        scene.play(Write(self.bilinearity))
        scene.play(Write(self.bilinearity_ext))
        scene.play(Unwrite(self.bilinearity_ext))
        scene.play(Write(self.non_degeneracy_label))
        scene.play(Write(self.non_degeneracy))
        scene.play(Write(self.computability_label))
