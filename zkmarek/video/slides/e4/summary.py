from manim import FadeIn, Create, Brace, Text, DOWN, LEFT, RIGHT, UP, Write, MathTex, FadeOut, Indicate, AddTextLetterByLetter, MoveToTarget

from zkmarek.video.constant import SECONDARY_COLOR, PRIMARY_FONT, PRIMARY_COLOR, HIGHLIGHT2_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.mobjects.merkle_tree import MerkleTree

class SummaryE4(SlideBase):
    def __init__(self):
        super().__init__("Summary")
    
    def construct(self):
        self.title_label = Text("Summary", color = PRIMARY_COLOR, font_size = 40, font = PRIMARY_FONT).to_edge(UP)
        self.big_poly = MathTex(r"{{p(x)}} = {{a_{2^{28}}}} \cdot x^{2^{28}} + {{a_{2^{28}-1}}}\cdot x^{2^{28}-1} + \dots + {{a_1}}\cdot  x + {{a_0}}", color = SECONDARY_COLOR)
        self.commitment = MathTex(r"{{C}} = {{p(\tau)}} \cdot {{G_1}}", color = PRIMARY_COLOR)

        self.kzg = Text("KZG", color = PRIMARY_COLOR, font = PRIMARY_FONT).to_edge(UP+LEFT).shift(DOWN+RIGHT)
        self.merkle_tree = Text("Merkle tree", color = PRIMARY_COLOR, font = PRIMARY_FONT).to_edge(UP+RIGHT).shift(DOWN+LEFT)
        self.commitment.next_to(self.big_poly, DOWN, buff = 0.5)
        self.brace =  Brace(self.commitment, color=PRIMARY_COLOR, direction=DOWN)
        self.brace_label = Text("48 bytes", font_size=20, color=PRIMARY_COLOR, font = PRIMARY_FONT)
        self.brace.put_at_tip(self.brace_label)

    def animate_in(self, scene):
        self.new_subsection(scene, "what have we accomplished?", "data/sound/e4/slide5-0.mp3")
        scene.play(Write(self.title_label), run_time=1.5)

        self.new_subsection(scene, "we have big polynomial?", "data/sound/e4/slide5-1.mp3")
        scene.wait(2)
        scene.play(AddTextLetterByLetter(self.big_poly), run_time=2.5)
        scene.wait(2.5)
        scene.play(Write(self.commitment))
        scene.wait(1.5)
        scene.play(Indicate(self.commitment, color = HIGHLIGHT2_COLOR), run_time=1)

        self.new_subsection(scene, "48 bytes", "data/sound/e4/slide5-2.mp3")
        scene.wait(1)
        scene.play(Indicate(self.big_poly[2], color = HIGHLIGHT2_COLOR), run_time=0.2)
        scene.play(Indicate(self.big_poly[4], color = HIGHLIGHT2_COLOR), run_time=0.2)
        scene.play(Indicate(self.big_poly[6], color = HIGHLIGHT2_COLOR), run_time=0.2)
        scene.play(Indicate(self.big_poly[8], color = HIGHLIGHT2_COLOR), run_time=0.2)
        scene.wait(2)
        scene.play(FadeIn(self.brace))
        scene.play(FadeIn(self.brace_label))

        self.new_subsection(scene, "Kzg> Merkle?", "data/sound/e4/slide5-3.mp3")
        scene.play(FadeOut(self.brace, self.brace_label))
        self.big_poly.generate_target()
        self.big_poly.target.next_to(self.kzg, DOWN, buff = 0.1).shift(RIGHT).scale(0.6)
        self.commitment.generate_target()
        self.commitment.target.next_to(self.kzg, DOWN, buff = 1.4)
        scene.play(Write(self.kzg))
        scene.play(MoveToTarget(self.commitment), MoveToTarget(self.big_poly), run_time=1.5)
        scene.play(Write(self.merkle_tree))
        
        self.new_subsection(scene, "efficiency", "data/sound/e4/slide5-4.mp3")
        self.animate_tree(scene)
        scene.wait(4)

    def animate_out(self, scene):
        scene.play(FadeOut(self.merkle_tree, self.commitment, self.kzg, self.title_label, self.big_poly))

    def animate_tree(self, scene):
        tree = MerkleTree().scale(0.4).next_to(self.merkle_tree, DOWN, buff = 0.8)
        # self.merkle = Text("Merkle tree", color = PRIMARY_COLOR, font=PRIMARY_FONT)
        # scene.play(AddTextLetterByLetter(self.merkle), run_time=1.5)
        scene.wait(1.4)

        scene.play(Create(tree))
        scene.wait(6.5)
        scene.play(FadeOut(tree))