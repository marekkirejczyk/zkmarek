from manim import (FadeIn, FadeOut, ImageMobject, Text, LEFT, RIGHT, DOWN, UP, Write, Create, MoveToTarget, VGroup, Rectangle, WHITE, PURPLE, 
Indicate, Group, Circle, Brace, AddTextLetterByLetter, BLACK, GREY, Arrow, StealthTip, GrowArrow, SurroundingRectangle, ApplyWave,
BLUE_E, GREEN_E, TEAL_E, RoundedRectangle)
from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR, HIGHLIGHT_COLOR, PRIMARY_FONT, HIGHLIGHT2_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
SCROLL_COLOR_BACKGROUND = "#FCEFCC"
SCROLL_COLOR = "#E4C495"

class Layer2(SlideBase):
    def __init__(self) -> None:
        super().__init__(title="ZK rollups")
        
    def construct(self):
        self.title_text = Text("Layer 2: ZK rollups", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 40).to_edge(UP)
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
                               self.tx_label5, self.tx_label6, self.tx_label7, self.tx_label8).shift(UP * 2.2+RIGHT*1.06)

        self.layer2_blocks = [Rectangle(width=1.3, height=1, fill_opacity=0.3) for _ in range(4)]
        for i in range(4):
            self.layer2_blocks[i].set_color_by_gradient([WHITE, SCROLL_COLOR_BACKGROUND, SCROLL_COLOR])

        self.layer2_group = VGroup(*self.layer2_blocks).arrange(RIGHT, buff=0.5).shift(UP*0.67)
        self.brace_tx = Brace(self.tx_group, DOWN, color = PRIMARY_COLOR)
        self.brace_tx.put_at_tip(self.layer2_blocks[1])
        
        
        self.layer2_blocks[0].shift(0.03*LEFT)
        self.layer2_blocks[2].shift(LEFT*0.15)
        self.layer2_blocks[3].shift(LEFT*0.2)
        
        self.finalized_blocks = [Rectangle(width=1.3, height=1, fill_opacity=0.3) for _ in range(4)]
        for i in range(4):
            self.finalized_blocks[i].set_color_by_gradient([WHITE, PURPLE, HIGHLIGHT2_COLOR])
        self.finalized_group = VGroup(*self.finalized_blocks).arrange(RIGHT, buff=0.5).shift(DOWN *1.7+LEFT*0.07)
        self.ethereum = ImageMobject("data/images/ethereum_logo.png").scale(0.2)
        self.ethereum.move_to(self.finalized_blocks[1])
        self.ethereum2 = self.ethereum.copy()
        self.ethereum2.move_to(self.finalized_blocks[0])
        self.ethereum3 = self.ethereum.copy()
        self.ethereum3.move_to(self.finalized_blocks[2])
        self.ethereum4 = self.ethereum.copy()
        self.ethereum4.move_to(self.finalized_blocks[3])
        self.rollup_brace = Brace(self.layer2_blocks[1], DOWN, color = PRIMARY_COLOR)
        self.rollup_brace.put_at_tip(self.finalized_blocks[1])
        self.finalized_blocks[1].next_to(self.finalized_blocks[0], RIGHT, buff = 0.5)
        self.rollup_text = Text("rollup", color = PRIMARY_COLOR, font = PRIMARY_FONT, 
                                font_size = 22).next_to(self.rollup_brace, RIGHT).shift(DOWN*0.3+LEFT)
        self.rollup_batch_text = Text("transactions batch", color = PRIMARY_COLOR, font = PRIMARY_FONT, 
                                font_size = 22).next_to(self.rollup_brace, DOWN)
        self.pricey_dollars_rollup = Text("$$$", color = HIGHLIGHT_COLOR, font = PRIMARY_FONT, font_size = 22).next_to(self.rollup_batch_text, LEFT)
        self.proof_of_correctness = Text("ZK proof", color = HIGHLIGHT_COLOR, font= PRIMARY_FONT, font_size = 22)
        
        self.transactions = Text("transactions", color = WHITE, font = PRIMARY_FONT, 
                                 font_size = 22).next_to(self.tx_circle8, RIGHT).shift(RIGHT*2.5)
        self.layer2 = Text("L2: ZK rollup", color = WHITE, font=PRIMARY_FONT, 
                           font_size = 22).next_to(self.layer2_blocks[3], RIGHT).shift(RIGHT*1.5)
        self.layer1_ethereum = Text("L1: Ethereum", color = WHITE, font = PRIMARY_FONT, 
                                    font_size = 22).next_to(self.finalized_blocks[3], RIGHT).shift(RIGHT*1.5)
        
        self.arrow_txs = Arrow(self.tx_circle8.get_right(), self.transactions.get_left(), tip_shape=StealthTip, 
                               stroke_width=2, max_tip_length_to_length_ratio=0.15).scale(0.7).set_color_by_gradient([HIGHLIGHT2_COLOR, GREY])
        self.arrow_layer2 = Arrow(self.layer2_blocks[3].get_right(), self.layer2.get_left(), tip_shape=StealthTip, 
                                  stroke_width=2, max_tip_length_to_length_ratio=0.15).scale(0.7).set_color_by_gradient([HIGHLIGHT2_COLOR, GREY])
        self.arrow_layer1 = Arrow(self.finalized_blocks[3].get_right(), self.layer1_ethereum.get_left(), tip_shape=StealthTip, 
                                  stroke_width=2, max_tip_length_to_length_ratio=0.15).scale(0.7).set_color_by_gradient([HIGHLIGHT2_COLOR, GREY]).shift(LEFT*0.06)
        
        
        self.arrow_layer2_blocks = [Arrow(self.layer2_blocks[0].get_right(), self.layer2_blocks[1].get_left(), tip_shape=StealthTip, 
                                  stroke_width=2, max_tip_length_to_length_ratio=0.15).set_color_by_gradient([WHITE, SCROLL_COLOR_BACKGROUND, SCROLL_COLOR]) for _ in range(3)]
        for i in range(3):
            self.arrow_layer2_blocks[i].next_to(self.layer2_blocks[i], RIGHT, buff=0).scale(0.7)
        self.arrow_layer2_group = VGroup(*self.arrow_layer2_blocks)
        
        self.arrow_layer1_blocks = [Arrow(self.layer2_blocks[0].get_right(), self.layer2_blocks[1].get_left(), tip_shape=StealthTip, 
                                  stroke_width=2, max_tip_length_to_length_ratio=0.15).set_color_by_gradient([HIGHLIGHT2_COLOR, GREY]) for _ in range(3)]

        for i in range(3):
            self.arrow_layer1_blocks[i].next_to(self.finalized_blocks[i], RIGHT, buff=0).scale(0.7)
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
        self.arrow_proof_of_correctness = Arrow(self.layer2_blocks[1].get_bottom(), self.finalized_blocks[1].get_top(), tip_shape=StealthTip, 
                                  stroke_width=2, max_tip_length_to_length_ratio=0.15).scale(0.7).set_color_by_gradient([HIGHLIGHT2_COLOR, GREY]).shift(DOWN*0.1)
        self.proof_of_correctness.next_to(self.arrow_proof_of_correctness, LEFT)

        
    def animate_in(self, scene):
        self.new_subsection(scene, "rollup", "data/sound/e5/slide1-1.mp3")
        scene.play(FadeIn(self.tx_group, self.title_text), Create(self.transactions), GrowArrow(self.arrow_txs), run_time=0.8)

        scene.play(Create(self.layer2_group), FadeIn(self.arrow_layer2_group), Write(self.brace_tx), run_time=0.7)
        scene.play(Create(self.layer2), GrowArrow(self.arrow_layer2), run_time=0.7)
        
        scene.play(ApplyWave(self.tx_group), run_time=1)

        scene.play(FadeIn(self.rollup_brace))
        scene.play(FadeIn(self.ethereum4, self.ethereum3, self.ethereum2,self.ethereum))
        scene.play(FadeIn(self.arrow_layer1_group))
        scene.play(Create(self.finalized_group), 
                   Create(self.layer1_ethereum), GrowArrow(self.arrow_layer1))
        
        scene.wait(0.5)
        scene.play(Create(self.proof_of_correctness), GrowArrow(self.arrow_proof_of_correctness))
        self.proof_of_correctness.generate_target()
        self.proof_of_correctness.target.move_to(self.finalized_blocks[1].get_center()).set_opacity(0.2)
        
        scene.play(MoveToTarget(self.proof_of_correctness), FadeOut(self.arrow_proof_of_correctness))
        scene.wait(0.5)
        scene.play(Indicate(self.layer1_ethereum, color = PURPLE))
        scene.play(FadeOut(self.proof_of_correctness))
        scene.play(Indicate(self.layer2, color = PURPLE), Indicate(self.transactions, color = PURPLE))
        scene.wait(0.5)
        scene.play(FadeIn(self.rollup_batch_text))
        scene.wait(2)
        scene.play(Create(self.pricey_dollars_rollup))
        scene.wait(1.5)
        
        self.new_subsection(scene, "blobs provide space", "data/sound/e5/slide1-2.mp3")

        self.block_chain.generate_target()
        self.block_chain.target.scale(0.5).shift(RIGHT*2.5+UP)
        scene.play(MoveToTarget(self.block_chain))
        self.box = SurroundingRectangle(self.block_chain, buff = 0.2).set_color_by_gradient([PRIMARY_COLOR, GREY, WHITE])
        scene.wait()
        scene.play(AddTextLetterByLetter(self.blobs), Create(self.rounded_rectangle))
        for i in range(8):
            if i!=3:
                scene.play(Indicate(self.blobs[i], color = SECONDARY_COLOR), run_time=0.2)
        
        self.new_subsection(scene, "blobs are cheaper", "data/sound/e5/slide1-2a.mp3")

        scene.play(Write(self.cheap_storage))
        
        self.new_subsection(scene, "still can access specific data", "data/sound/e5/slide1-2b.mp3")
        scene.play(Write(self.smart_contracts))
        scene.wait(4)
        scene.play(Write(self.post_removal))
        scene.wait(4)
        
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.title_text, self.block_chain, self.blobs, self.cheap_storage, self.smart_contracts, self.post_removal, self.rounded_rectangle))