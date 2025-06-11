from manim import (FadeIn, FadeOut, ImageMobject, Text, LEFT, RIGHT, DOWN, UP, Write, Create, MoveToTarget, VGroup, Rectangle, WHITE, PURPLE, 
Indicate, Group, Circle, Brace, AddTextLetterByLetter, BLACK, GREY, Arrow, StealthTip, GrowArrow, SurroundingRectangle, ApplyWave,
BLUE_E, GREEN_E, TEAL_E, RoundedRectangle, Transform, MathTex, rate_functions)
from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR, HIGHLIGHT_COLOR, PRIMARY_FONT, HIGHLIGHT2_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.e6.tree import MerkleTree
SCROLL_COLOR_BACKGROUND = "#FCEFCC"
SCROLL_COLOR = "#E4C495"

class Layer2(SlideBase):
    def __init__(self) -> None:
        super().__init__(title="rollups")
        
    def construct(self):
        self.title_text = Text("Layer 2: rollups", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 40).to_edge(UP)
        self.tx_circle = Circle(radius=0.3, color = BLACK).set_fill([WHITE, HIGHLIGHT_COLOR], opacity=0.2).shift(LEFT*5)
        self.tx_label = Text("tx", font_size=18, font = PRIMARY_FONT, color = PRIMARY_COLOR)
        self.tx_label.move_to(self.tx_circle.get_center())
        self.tx_circle2 = Circle(radius=0.3, color = BLACK).set_fill([WHITE, HIGHLIGHT_COLOR], opacity=0.2).next_to(self.tx_circle, RIGHT)
        self.tx_label2 = Text("tx", font_size=18, font = PRIMARY_FONT, color = PRIMARY_COLOR)
        self.tx_label2.move_to(self.tx_circle2.get_center())
        self.tx_circle3 = Circle(radius=0.3, color = BLACK).set_fill([WHITE, HIGHLIGHT_COLOR], opacity=0.2).next_to(self.tx_circle2, RIGHT)
        self.tx_label3 = Text("tx", font_size=18, font = PRIMARY_FONT, color = PRIMARY_COLOR).move_to(self.tx_circle3.get_center())
        self.tx_circle4 = Circle(radius=0.3, color = BLACK).set_fill([WHITE, HIGHLIGHT_COLOR], opacity=0.2).next_to(self.tx_circle3, RIGHT)
        self.tx_label4 = Text("tx", font_size=18, font = PRIMARY_FONT, color = PRIMARY_COLOR).move_to(self.tx_circle4.get_center())
        self.tx_circle5 = Circle(radius=0.3, color = BLACK).set_fill([WHITE, HIGHLIGHT_COLOR], opacity=0.2).next_to(self.tx_circle4, RIGHT)
        self.tx_label5 = Text("tx", font_size=18, font = PRIMARY_FONT, color = PRIMARY_COLOR).move_to(self.tx_circle5.get_center())
        self.tx_circle6 = Circle(radius=0.3, color = BLACK).set_fill([WHITE, HIGHLIGHT_COLOR], opacity=0.2).next_to(self.tx_circle5, RIGHT)
        self.tx_label6 = Text("tx", font_size=18, font = PRIMARY_FONT, color = PRIMARY_COLOR).move_to(self.tx_circle6.get_center())
        self.tx_circle7 = Circle(radius=0.3, color = BLACK).set_fill([WHITE, HIGHLIGHT_COLOR], opacity=0.2).next_to(self.tx_circle6, RIGHT)
        self.tx_label7 = Text("tx", font_size=18, font = PRIMARY_FONT, color = PRIMARY_COLOR).move_to(self.tx_circle7.get_center())
        self.tx_circle8 = Circle(radius=0.3, color = BLACK).set_fill([WHITE, HIGHLIGHT_COLOR], opacity=0.2).next_to(self.tx_circle7, RIGHT)
        self.tx_label8 = Text("tx", font_size=18, font = PRIMARY_FONT, color = PRIMARY_COLOR).move_to(self.tx_circle8.get_center())

        self.tx_group = VGroup(self.tx_circle8, self.tx_circle6, self.tx_circle7, self.tx_circle5, self.tx_circle4, self.tx_circle3, 
                               self.tx_circle2, self.tx_circle, self.tx_label, self.tx_label2, self.tx_label3, self.tx_label4, 
                               self.tx_label5, self.tx_label6, self.tx_label7, self.tx_label8).shift(DOWN * 1.9+RIGHT*1.06)

        self.layer2_blocks = [Rectangle(width=1.3, height=1, fill_opacity=0.3, stroke_width = 0.0) for _ in range(4)]
        for i in range(4):
            self.layer2_blocks[i].set_color_by_gradient([WHITE, SCROLL_COLOR_BACKGROUND, SCROLL_COLOR])

        self.layer2_group = VGroup(*self.layer2_blocks).arrange(RIGHT, buff=0.5).next_to(self.tx_group, UP)
        self.brace_tx = Brace(self.tx_group, UP, color = PRIMARY_COLOR)
        self.brace_tx.put_at_tip(self.layer2_blocks[1])
        
        
        self.layer2_blocks[0].shift(RIGHT*0.93+0.5*UP*0.85)
        self.layer2_blocks[2].shift(RIGHT+0.5*UP*0.9)
        self.layer2_blocks[3].shift(RIGHT+0.5*UP*0.9)
        
        self.finalized_blocks = [Rectangle(width=1.3, height=1, fill_opacity=0.3, stroke_width = 0.0) for _ in range(4)]
        for i in range(4):
            self.finalized_blocks[i].set_color_by_gradient([WHITE, PURPLE, HIGHLIGHT2_COLOR])
        self.finalized_group = VGroup(*self.finalized_blocks).arrange(RIGHT, buff=0.5).next_to(self.layer2_group, UP).shift(UP)
        self.ethereum = ImageMobject("data/images/ethereum_logo.png").scale(0.2)
        self.ethereum.move_to(self.finalized_blocks[1])
        self.ethereum2 = self.ethereum.copy()
        self.ethereum2.move_to(self.finalized_blocks[0])
        self.ethereum3 = self.ethereum.copy()
        self.ethereum3.move_to(self.finalized_blocks[2])
        self.ethereum4 = self.ethereum.copy()
        self.ethereum4.move_to(self.finalized_blocks[3])
        self.rollup_brace = Brace(self.layer2_blocks[1], UP, color = PRIMARY_COLOR)
        self.rollup_brace.put_at_tip(self.finalized_blocks[1])
        self.finalized_blocks[1].next_to(self.finalized_blocks[0], RIGHT, buff = 0.5)
        self.rollup_text = Text("rollup", color = PRIMARY_COLOR, font = PRIMARY_FONT, 
                                font_size = 22).next_to(self.rollup_brace, RIGHT).shift(DOWN*0.3+LEFT)
        self.rollup_batch_text = Text("transactions batch", color = PRIMARY_COLOR, font = PRIMARY_FONT, 
                                font_size = 22).next_to(self.rollup_brace, UP)
        self.pricey_dollars_rollup = Text("???", color = HIGHLIGHT_COLOR, font = PRIMARY_FONT, font_size = 22).next_to(self.rollup_batch_text, LEFT)

        self.transactions = Text("transactions", color = WHITE, font = PRIMARY_FONT, 
                                 font_size = 22).next_to(self.tx_circle8, RIGHT).shift(RIGHT*2.5)
        self.layer2 = Text("L2: rollup", color = WHITE, font=PRIMARY_FONT, 
                           font_size = 22).next_to(self.layer2_blocks[3], RIGHT).shift(RIGHT*1.5)
        self.layer1_ethereum = Text("L1: Ethereum", color = WHITE, font = PRIMARY_FONT, 
                                    font_size = 22).next_to(self.finalized_blocks[3], RIGHT).shift(RIGHT*1.5)
        
        self.arrow_txs = Arrow(self.tx_circle8.get_right(), self.transactions.get_left(), tip_shape=StealthTip, 
                               stroke_width=2, max_tip_length_to_length_ratio=0.15).scale(0.7).set_color_by_gradient([HIGHLIGHT2_COLOR, GREY])
        self.arrow_layer2 = Arrow(self.layer2_blocks[3].get_right(), self.layer2.get_left(), tip_shape=StealthTip, 
                                  stroke_width=2, max_tip_length_to_length_ratio=0.15).scale(0.7).set_color_by_gradient([HIGHLIGHT2_COLOR, GREY])
        self.arrow_layer1 = Arrow(self.finalized_blocks[3].get_right(), self.layer1_ethereum.get_left(), tip_shape=StealthTip, 
                                  stroke_width=2, max_tip_length_to_length_ratio=0.15).scale(0.7).set_color_by_gradient([HIGHLIGHT2_COLOR, GREY]).shift(LEFT*0.08)
        
        
        self.arrow_layer2_blocks = [Arrow(self.layer2_blocks[0].get_right(), self.layer2_blocks[1].get_left()+DOWN*0.05, tip_shape=StealthTip, 
                                  stroke_width=2, max_tip_length_to_length_ratio=0.15).set_color_by_gradient([WHITE, SCROLL_COLOR_BACKGROUND, SCROLL_COLOR]) for _ in range(3)]
        for i in range(3):
            self.arrow_layer2_blocks[i].next_to(self.layer2_blocks[i], RIGHT, buff=0).scale(0.67).shift(RIGHT*0.02)
        self.arrow_layer2_group = VGroup(*self.arrow_layer2_blocks)
        
        self.arrow_layer1_blocks = [Arrow(self.layer2_blocks[0].get_right(), self.layer2_blocks[1].get_left()+DOWN*0.05, tip_shape=StealthTip, 
                                  stroke_width=2, max_tip_length_to_length_ratio=0.15).set_color_by_gradient([HIGHLIGHT2_COLOR, GREY]) for _ in range(3)]

        for i in range(3):
            self.arrow_layer1_blocks[i].next_to(self.finalized_blocks[i], RIGHT, buff=0).scale(0.7).shift(RIGHT*0.02)
        self.arrow_layer1_group = VGroup(*self.arrow_layer1_blocks)
        
        self.blobs = Text("EIP-4844 blobs", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 30).shift(LEFT*3.3+UP*1.5)

        self.cheap_storage = Text("Cheap temporary storage", color = BLUE_E, font = PRIMARY_FONT, font_size = 28).next_to(self.blobs, DOWN).shift(DOWN*0.5)
        self.smart_contracts = Text("Smart contracts accessible...", font = PRIMARY_FONT, color = GREEN_E, font_size = 28).next_to(self.cheap_storage, DOWN)
        self.post_removal = Text("...even post removal", font = PRIMARY_FONT, color = TEAL_E, font_size = 28).next_to(self.smart_contracts, DOWN)   
        self.rounded_rectangle = RoundedRectangle(corner_radius=0.5, width=self.smart_contracts.width + 0.5, height=self.smart_contracts.height + 3.5).set_color_by_gradient([PRIMARY_COLOR, GREEN_E, HIGHLIGHT2_COLOR])
        self.rounded_rectangle.move_to(self.smart_contracts.get_center())
        self.block_chain = Group(self.tx_group, self.layer1_ethereum, self.layer2, self.ethereum, 
                                 self.ethereum2, self.ethereum3, self.ethereum4, self.transactions,
                                 self.layer2_group, self.finalized_group, self.rollup_brace, self.rollup_batch_text, 
                                 self.arrow_layer1, self.arrow_layer2, self.arrow_txs, self.brace_tx, self.pricey_dollars_rollup, 
                                 self.arrow_layer1_group, 
                                 self.arrow_layer2_group)
        self.block_chain.shift(LEFT)
        self.layer2_blocks[1].shift(DOWN*0.05+RIGHT*0.04)

        self.blob_image = ImageMobject("data/images/blob.png").scale(0.5).to_edge(DOWN+RIGHT).shift(LEFT*2.5)
        self.blob_image_1 = self.blob_image.copy()
        self.blob_image_1.scale(0.5).next_to(self.blob_image, RIGHT, buff = 0)
        self.blob_image_2 = self.blob_image.copy()
        self.blob_image_2.scale(0.5).next_to(self.blob_image, LEFT, buff = 0)
        self.arrow_layer2_blocks[1].shift(0.08*RIGHT+0.05*DOWN)
        
    def animate_in(self, scene):
        self.new_subsection(scene, "rollup", "data/sound/e5/slide1-0a.mp3")
        scene.play(FadeIn(self.title_text), run_time=0.8)

        scene.play(Create(self.layer2_group), run_time=0.7)
        scene.play(FadeIn(self.arrow_layer2_group), run_time=0.7)
        scene.play(Create(self.layer2), GrowArrow(self.arrow_layer2), run_time=0.7)
        scene.play(Write(self.brace_tx), FadeIn(self.tx_group))
        scene.play(Create(self.transactions), GrowArrow(self.arrow_txs))
        scene.wait(1.4)
        
        self.new_subsection(scene, "L2 rollups correctness", "data/sound/e5/slide1-1.mp3")
        scene.wait(2)
        scene.play(FadeIn(self.ethereum4, self.ethereum3, self.ethereum2,self.ethereum), FadeIn(self.arrow_layer1_group), 
                   Create(self.finalized_group), Create(self.layer1_ethereum), GrowArrow(self.arrow_layer1))
        scene.wait(1.5)
        scene.play(Indicate(self.layer2, color = PURPLE), Indicate(self.transactions, color = PURPLE), ApplyWave(self.tx_group), run_time=1)
        scene.wait(0.6)
        scene.play(ApplyWave(self.finalized_group))
        
        self.new_subsection(scene, "rollup", "data/sound/e5/slide1-1a.mp3")
        scene.wait(1.5)
        scene.play(FadeIn(self.rollup_brace))

        scene.play(FadeIn(self.rollup_batch_text))
        scene.wait(1)
        scene.play(Create(self.pricey_dollars_rollup))
        scene.wait(2)
        
        self.new_subsection(scene, "blobs provide space", "data/sound/e5/slide1-2.mp3")

        self.block_chain.generate_target()
        self.block_chain.target.scale(0.5).to_edge(UP+RIGHT).shift(DOWN*1.5+LEFT)
        scene.play(MoveToTarget(self.block_chain))
        self.box = SurroundingRectangle(self.block_chain, buff = 0.2).set_color_by_gradient([PRIMARY_COLOR, GREY, WHITE])
        scene.play(FadeIn(self.blob_image), run_time=0.35)
        scene.play(FadeIn(self.blob_image_1), run_time=0.35)
        scene.play(FadeIn(self.blob_image_2), run_time=0.35)
        scene.play(AddTextLetterByLetter(self.blobs), Create(self.rounded_rectangle))
        for i in range(8):
            if i!=3:
                scene.play(Indicate(self.blobs[i], color = SECONDARY_COLOR), run_time=0.2)
        
        scene.wait(1.2)

        scene.play(Write(self.cheap_storage))
        
        self.new_subsection(scene, "still can access specific data", "data/sound/e5/slide1-2b.mp3")
        scene.play(Write(self.smart_contracts))
        scene.wait(4)
        scene.play(Write(self.post_removal))
        scene.wait(2)
         
    def animate_out(self, scene):
        scene.play(FadeOut(self.title_text, self.block_chain, self.blobs, self.cheap_storage, self.smart_contracts, self.post_removal, 
                           self.rounded_rectangle, self.blob_image, self.blob_image_1, self.blob_image_2))
        
    def miniature(self, scene):
        self.blob = ImageMobject("data/images/blob.png").scale(0.9).shift(UP*3.5)
        self.blob_1 = self.blob.copy().scale(0.5).next_to(self.blob, LEFT, buff = 0.0)
        self.blob_2 = self.blob.copy().scale(0.5).next_to(self.blob, RIGHT, buff = 0.0)
        scene.play(FadeIn(self.blob), run_time=0.3)
        scene.play(FadeIn(self.blob_1), run_time=0.3)
        scene.play(FadeIn(self.blob_2), run_time=0.3)
        self.block_chain = VGroup(
            self.tx_group, self.layer1_ethereum, self.layer2, self.transactions,
            self.layer2_group, self.finalized_group, self.arrow_layer1, self.arrow_layer2,
            self.arrow_txs, self.brace_tx,
            self.arrow_layer1_group, self.arrow_layer2_group
        )

        scene.add(self.ethereum, self.ethereum2, self.ethereum3, self.ethereum4)
        self.block_chain.scale(0.75).shift(DOWN*2.5)
        self.ethereum.scale(0.5).move_to(self.finalized_blocks[0])
        self.ethereum2.scale(0.5).move_to(self.finalized_blocks[1])
        self.ethereum3.scale(0.5).move_to(self.finalized_blocks[2])
        self.ethereum4.scale(0.5).move_to(self.finalized_blocks[3])

        scene.play(FadeIn(self.block_chain))  
        scene.wait(0.3)
        
        self.new_subsection(scene, "verkle trees", "data/sound/e6/slide1-3a.mp3")
        scene.play(FadeOut(self.blob, self.blob_1, self.blob_2), run_time=0.5)
        
        import random
        rows, cols = 10, 16 
        self.binary_matrix = VGroup(*[
            VGroup(*[
                Text(str(random.choice([0, 1])), font_size=24)
                for _ in range(cols)
            ]).arrange(RIGHT, buff=0.1)
            for _ in range(rows)
        ]).arrange(DOWN, buff=0.2)

        self.binary_matrix.move_to(UP*3.5)
        scene.add(self.binary_matrix)
        self.tree = MerkleTree(num_children=2, num_levels=3, include_labels=False).shift(UP*5).scale(0.4)
        self.tree.stretch(2, dim=1)
        node1_0 = self.tree.get_node(1, 0)
        node2_1 = self.tree.get_node(2, 1)
        self.dots_vec_node = MathTex(r"\cdots", color = PRIMARY_COLOR)
        self.dots_vec_node.move_to(node1_0.get_right()).shift(RIGHT*1.2)
        self.dots_vec_node1 = self.dots_vec_node.copy()
        self.dots_vec_node1.move_to(node2_1.get_right()).shift(RIGHT*0.53)
        for _ in range(30):  
            new_rows = VGroup(*[
                VGroup(*[
                    Text(str(random.choice([0, 1])), font_size=24)
                    for _ in range(cols)
                ]).arrange(RIGHT, buff=0.1)
                for _ in range(rows)
            ]).arrange(DOWN, buff=0.2).move_to(LEFT*3)

            scene.play(*[
                Transform(self.binary_matrix[i], new_rows[i])
                for i in range(rows)
            ], run_time=0.1)
        scene.play(FadeOut(self.binary_matrix), run_time=0.3)
        scene.play(Create(self.tree), FadeIn(self.dots_vec_node, self.dots_vec_node1), run_time=1)
        scene.wait(2.2)
            
        scene.play(FadeOut(self.block_chain), FadeOut(self.ethereum), 
                FadeOut(self.ethereum2), FadeOut(self.ethereum3), 
                FadeOut(self.ethereum4, self.tree, self.dots_vec_node, self.dots_vec_node1))
        

    def animate_miniature_final_season(self, scene):
        rectangle = RoundedRectangle(corner_radius=0.3, width = 4, height = 2, color = PRIMARY_COLOR, stroke_width=0.3).shift(LEFT * 3 + DOWN * 2)
        self.blob = ImageMobject("data/images/blob.png").scale(0.4).move_to(rectangle.get_center()).shift(UP * 6.5)
        self.blob_0 = self.blob.copy().scale(0.25)
        self.blob_0.generate_target()
        self.blob_0.target.shift(DOWN * 5.5)
        self.blob_1 = self.blob.copy().scale(0.25)
        self.blob_1.generate_target()
        self.blob_1.target.next_to(self.blob_0.target, LEFT, buff = 0.0)
        self.blob_2 = self.blob.copy().scale(0.25)
        self.blob_2.generate_target()
        self.blob_2.target.next_to(self.blob_0.target, RIGHT, buff = 0.0)
        
        scene.play(MoveToTarget(self.blob_0, rate_func=rate_functions.ease_out_bounce), run_time=0.3)
        scene.play(MoveToTarget(self.blob_1, rate_func=rate_functions.ease_out_bounce), run_time=0.3)
        scene.play(MoveToTarget(self.blob_2, rate_func=rate_functions.ease_out_bounce), run_time=0.3)
        self.block_chain = VGroup(
            self.tx_group, self.layer1_ethereum, self.layer2, self.transactions,
            self.layer2_group, self.finalized_group, self.arrow_layer1, self.arrow_layer2,
            self.arrow_txs, self.brace_tx,
            self.arrow_layer1_group, self.arrow_layer2_group
        ).move_to(rectangle.get_center()).shift(DOWN * 1.5)

        scene.add(self.ethereum, self.ethereum2, self.ethereum3, self.ethereum4)
        self.block_chain.scale(0.4).next_to(self.blob_0, DOWN, buff = 0.3)
        self.ethereum.scale(0.5).move_to(self.finalized_blocks[0])
        self.ethereum2.scale(0.5).move_to(self.finalized_blocks[1])
        self.ethereum3.scale(0.5).move_to(self.finalized_blocks[2])
        self.ethereum4.scale(0.5).move_to(self.finalized_blocks[3])

        scene.play(FadeIn(self.block_chain, rectangle))  
        scene.wait(0.3)
        scene.play(self.ethereum.animate.set_color(PURPLE))