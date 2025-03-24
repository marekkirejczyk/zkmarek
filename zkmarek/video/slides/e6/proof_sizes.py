from manim import (Text, Create, Write, Arrow, StealthTip, GrowArrow, RIGHT, LEFT, UP, DOWN, Brace, 
                   FadeIn, MathTex, Indicate, TransformMatchingShapes, FadeOut, VGroup, MoveToTarget)
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.e6.merkle16 import SelectiveMerkleTree
from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR, PRIMARY_FONT

class ProofSize(SlideBase):
    def __init__(self)-> None:
        super().__init__("Proof Size")
        
    def construct(self):
        self.title_label = Text("Proof Sizes", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size = 40).to_edge(UP)
        self.merkle_tree = SelectiveMerkleTree(num_levels=5, include_labels=False, focused_node_path=[7, 8, 7, 8]).scale(0.4).shift(UP*5.5)
        
        self.dots = Text("...\n...", color = PRIMARY_COLOR, font=PRIMARY_FONT, font_size = 40).next_to(self.merkle_tree, DOWN, buff = 0.15)
        
        self.brace_levels = Brace(self.merkle_tree, direction = RIGHT, color = PRIMARY_COLOR).scale(1.2).shift(DOWN*0.3)
        self.levels_text = Text("8--10 levels", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 30).next_to(self.brace_levels, RIGHT, buff = 0.2)
        
        self.formula = Text("depth x 15 siblings x hash size", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 30)
        self.formula1 = Text("depth x 15 siblings x 32 B", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 30)
        
        self.formula2 = Text("9 x 15 x 32 B      4 kB", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 35).scale(0.8)
        self.formula3 = Text("1000 x 9 x 15 x 32 B     4 MB", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 35).scale(0.8)
        
        approx = MathTex(r"\approx", color = PRIMARY_COLOR)
        approx_formula2 = approx.copy().move_to(self.formula2[8].get_center()).shift(LEFT*0.35)
        approx_formula3 = approx.copy().move_to(self.formula2[10].get_center()).shift(LEFT*0.24)
        self.formula2 = VGroup(self.formula2, approx_formula2)
        self.formula3 = VGroup(self.formula3, approx_formula3)
        
        self.stay_tuned = Text("Stay tuned!", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 40).to_edge(UP)
        
    def animate_in(self, scene):        
        self.new_subsection(scene, "depends on trie depth", "data/sound/e6/slide2-8a.mp3")
        scene.play(Write(self.title_label), run_time=0.7)
        scene.play(Create(self.merkle_tree), Write(self.dots))
        
        self.new_subsection(scene, "8--10 levels", "data/sound/e6/slide2-8b.mp3")
        scene.play(FadeIn(self.brace_levels), Write(self.levels_text))
        scene.play(*[Indicate(self.merkle_tree.get_node(1, i), color = SECONDARY_COLOR) for i in range(0,16)], run_time=0.5)
        scene.play(*[Indicate(self.merkle_tree.get_node(2, i), color = SECONDARY_COLOR) for i in range(0,16)], run_time=0.5)
        scene.play(*[Indicate(self.merkle_tree.get_node(3, i), color = SECONDARY_COLOR) for i in range(0,16)], run_time=0.5)
        scene.play(*[Indicate(self.merkle_tree.get_node(4, i), color = SECONDARY_COLOR) for i in range(0,16)], run_time=0.5)
        scene.play(Indicate(self.dots, color = SECONDARY_COLOR), run_time=0.5)
        
        self.new_subsection(scene, "formula: depth*diblings*hash size", "data/sound/e6/slide2-8c.mp3")
        merkle_dots = VGroup(self.merkle_tree, self.dots)
        merkle_dots.generate_target()
        merkle_dots.target.shift(LEFT*2)
        scene.play(FadeOut(self.levels_text), FadeOut(self.brace_levels), MoveToTarget(merkle_dots), run_time=1)
        
        self.formula.next_to(self.merkle_tree, RIGHT).shift(LEFT*0.2)
        self.formula1.next_to(self.merkle_tree, RIGHT)
        self.formula2.next_to(self.merkle_tree, RIGHT).shift(RIGHT*0.5)
        self.formula3.next_to(self.merkle_tree, RIGHT)
        
        scene.play(Write(self.formula), run_time=1.2)
        scene.play(Indicate(self.formula[0:5], color = SECONDARY_COLOR), run_time=0.8)
        scene.wait(1)
        scene.play(Indicate(self.formula[6:16], color = SECONDARY_COLOR), run_time=0.8)
        scene.wait(1.7)
        scene.play(Indicate(self.formula[17:], color = SECONDARY_COLOR), run_time=0.8)
        scene.wait(1)
        scene.play(TransformMatchingShapes(self.formula, self.formula1))
        
        self.new_subsection(scene, "it weighs", "data/sound/e6/slide2-8d.mp3")
        scene.wait(1)
        scene.play(*[Indicate(self.merkle_tree.get_node(1, i), color = SECONDARY_COLOR) for i in range(0,16)], run_time=0.3)
        scene.play(*[Indicate(self.merkle_tree.get_node(2, i), color = SECONDARY_COLOR) for i in range(0,16)], run_time=0.3)
        scene.play(*[Indicate(self.merkle_tree.get_node(3, i), color = SECONDARY_COLOR) for i in range(0,16)], run_time=0.3)
        scene.play(*[Indicate(self.merkle_tree.get_node(4, i), color = SECONDARY_COLOR) for i in range(0,16)], run_time=0.3)
        scene.play(Indicate(self.dots, color = SECONDARY_COLOR), run_time=0.3)
        
        scene.play(TransformMatchingShapes(self.formula1, self.formula2))
        
        self.new_subsection(scene, "multiple values", "data/sound/e6/slide2-8e.mp3")
        nodes = [self.merkle_tree.get_node(4,0), self.merkle_tree.get_node(4,4), self.merkle_tree.get_node(4,8),
                 self.merkle_tree.get_node(4,12), self.merkle_tree.get_node(4,14)]
        for node in nodes:
            scene.play(Indicate(node, color = SECONDARY_COLOR, scale_factor=1.5), run_time=0.5)
            
        scene.play(TransformMatchingShapes(self.formula2, self.formula3))
        
        self.new_subsection(scene, "proofs smaller", "data/sound/e6/slide2-8f.mp3")
        scene.wait(3)
        scene.play(FadeOut(self.formula3, self.merkle_tree, self.dots))
        self.new_subsection(scene, "merkle verkle", "data/sound/e6/slide2-8g.mp3")
        self.merkle_tree_text = Text("Merkle Tree", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 30).shift(LEFT*4)
        self.verkle_tree_text = Text("Verkle Tree", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 30).shift(RIGHT*4)
        self.arrow_merkle_verkle = Arrow(self.merkle_tree_text.get_right(), self.verkle_tree_text.get_left(), color = PRIMARY_COLOR, tip_shape = StealthTip, stroke_width=2, max_tip_length_to_length_ratio=0.15).set_color(PRIMARY_COLOR)
        self.vector_commitment = Text("+ Vector Commitment", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 30).next_to(self.arrow_merkle_verkle, DOWN, buff = 0.2)
        scene.play(Write(self.merkle_tree_text))
        
        scene.play(GrowArrow(self.arrow_merkle_verkle), Create(self.vector_commitment))
        scene.play(Write(self.verkle_tree_text))
        scene.wait(1)
        
        self.new_subsection(scene, "teaser", "data/sound/e6/slide2-8h.mp3")
        scene.play(TransformMatchingShapes(self.title_label, self.stay_tuned))
        scene.wait(3)
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.stay_tuned, self.arrow_merkle_verkle, self.vector_commitment, self.merkle_tree_text, self.verkle_tree_text))