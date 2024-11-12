from manim import (FadeIn, FadeOut, ImageMobject, Text, LEFT, RIGHT, DOWN, UP, Write, Create, MoveToTarget, VGroup, Rectangle, WHITE, 
Indicate, Group, Square, Circle, Brace, AddTextLetterByLetter, BLACK, GREY, Arrow, StealthTip, GrowArrow, SurroundingRectangle, BulletedList)
from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR, HIGHLIGHT_COLOR, PRIMARY_FONT, HIGHLIGHT2_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase

class Layer2(SlideBase):
    def __init__(self) -> None:
        super().__init__(title="Layer 2")
        
    def construct(self):
        self.title_text = Text("Layer 2", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 40).to_edge(UP)
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

        self.layer2_blocks = [Rectangle(width=1, height=1.4) for _ in range(4)]
        for i in range(4):
            self.layer2_blocks[i].set_color_by_gradient([WHITE, HIGHLIGHT_COLOR, PRIMARY_COLOR])

        self.layer2_group = VGroup(*self.layer2_blocks).arrange(RIGHT, buff=0.5).shift(UP*0.47)
        self.brace_tx = Brace(self.tx_group, DOWN, color = PRIMARY_COLOR)
        self.brace_tx.put_at_tip(self.layer2_blocks[1])
        
        self.ethereum = ImageMobject("data/images/ethereum_logo.png").scale(0.4)
        self.layer2_blocks[0].shift(LEFT*0.2)
        self.layer2_blocks[2].shift(LEFT*0.2)
        self.layer2_blocks[3].shift(LEFT*0.2)
        self.ethereum.move_to(self.layer2_blocks[1])
        self.ethereum2 = self.ethereum.copy()
        self.ethereum2.move_to(self.layer2_blocks[0])
        self.ethereum3 = self.ethereum.copy()
        self.ethereum3.move_to(self.layer2_blocks[2])
        self.ethereum4 = self.ethereum.copy()
        self.ethereum4.move_to(self.layer2_blocks[3])
        
        
        self.finalized_blocks = [Square(side_length=1, fill_opacity=0.3) for _ in range(4)]
        for i in range(4):
            self.finalized_blocks[i].set_color_by_gradient([WHITE, SECONDARY_COLOR, GREY])
        self.finalized_group = VGroup(*self.finalized_blocks).arrange(RIGHT, buff=0.5).shift(DOWN *1.7+LEFT*0.2)
        self.rollup_brace = Brace(self.layer2_blocks[1], DOWN, color = PRIMARY_COLOR)
        self.rollup_brace.put_at_tip(self.finalized_blocks[1])
        self.finalized_blocks[1].next_to(self.finalized_blocks[0], RIGHT, buff = 0.5)
        self.rollup_text = Text("rollup", color = PRIMARY_COLOR, font = PRIMARY_FONT, 
                                font_size = 22).next_to(self.rollup_brace, RIGHT).shift(DOWN*0.3)
        
        
        self.transactions = Text("transactions", color = WHITE, font = PRIMARY_FONT, 
                                 font_size = 22).next_to(self.tx_circle8, RIGHT).shift(RIGHT*1.8)
        self.layer2 = Text("Layer 2", color = WHITE, font=PRIMARY_FONT, 
                           font_size = 22).next_to(self.layer2_blocks[3], RIGHT).shift(RIGHT*2)
        self.layer1_ethereum = Text("Layer1: Ethereum", color = WHITE, font = PRIMARY_FONT, 
                                    font_size = 22).next_to(self.finalized_blocks[3], RIGHT).shift(RIGHT*1.5)
        
        self.arrow_txs = Arrow(self.tx_circle8.get_right(), self.transactions.get_left(), tip_shape=StealthTip, 
                               stroke_width=2, max_tip_length_to_length_ratio=0.15).scale(0.7).set_color_by_gradient([HIGHLIGHT2_COLOR, GREY])
        self.arrow_layer2 = Arrow(self.layer2_blocks[3].get_right(), self.layer2.get_left(), tip_shape=StealthTip, 
                                  stroke_width=2, max_tip_length_to_length_ratio=0.15).scale(0.7).set_color_by_gradient([GREY, HIGHLIGHT2_COLOR])
        self.arrow_layer1 = Arrow(self.finalized_blocks[3].get_right(), self.layer1_ethereum.get_left(), tip_shape=StealthTip, 
                                  stroke_width=2, max_tip_length_to_length_ratio=0.15).scale(0.7).set_color_by_gradient([HIGHLIGHT2_COLOR, GREY])
        
        self.blobs = Text("EIP-4844 blobs", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 30).shift(LEFT*2.5+UP*1.5)
        self.blist = BulletedList("Cheap temporary storage;", "Smart contracts accessible data...", "...even post removal", 
                                  height=5, width=5).next_to(self.blobs, DOWN).shift(DOWN)
        self.blist.set_color_by_tex("Cheap temporary storage;", SECONDARY_COLOR)
        self.blist.set_color_by_tex("Smart contracts accessible data...", HIGHLIGHT_COLOR)
        self.blist.set_color_by_tex("...even post removal", PRIMARY_COLOR)
        
    def animate_in(self, scene):
        self.new_subsection(scene, "How ETH works", "data/sound/e5/slide1-0.mp3")
        scene.play(FadeIn(self.tx_group, self.title_text))
        scene.play(Create(self.transactions), GrowArrow(self.arrow_txs))
        scene.play(Create(self.layer2_group), Write(self.brace_tx))
        scene.play(Create(self.layer2), GrowArrow(self.arrow_layer2))
        scene.play(FadeIn(self.ethereum4, self.ethereum3, self.ethereum2,self.ethereum))
        
        self.new_subsection(scene, "rollup", "data/sound/e5/slide1-1.mp3")
        scene.play(Indicate(self.tx_label, color = [SECONDARY_COLOR, PRIMARY_COLOR]),
                   Indicate(self.tx_label2, color = [SECONDARY_COLOR, PRIMARY_COLOR]),
                   Indicate(self.tx_label3, color = [SECONDARY_COLOR, PRIMARY_COLOR]),
                   Indicate(self.tx_label4, color = [SECONDARY_COLOR, PRIMARY_COLOR]),
                   Indicate(self.tx_label5, color = [SECONDARY_COLOR, PRIMARY_COLOR]),
                   Indicate(self.tx_label6, color = [SECONDARY_COLOR, PRIMARY_COLOR]),
                   Indicate(self.tx_label7, color = [SECONDARY_COLOR, PRIMARY_COLOR]),
                   Indicate(self.tx_label8, color = [SECONDARY_COLOR, PRIMARY_COLOR]))

        scene.play(FadeIn(self.rollup_brace, self.rollup_text))
        scene.play(Create(self.finalized_group))
        scene.play(Create(self.layer1_ethereum), GrowArrow(self.arrow_layer1))
        
        self.new_subsection(scene, "blobs provide space", "data/sound/e5/slide1-2.mp3")
        self.block_chain = Group(self.tx_group, self.layer1_ethereum, self.layer2, self.ethereum, 
                                 self.ethereum2, self.ethereum3, self.ethereum4, self.transactions,
                                 self.layer2_group, self.finalized_group, self.rollup_brace, self.rollup_text, 
                                 self.arrow_layer1, self.arrow_layer2, self.arrow_txs, self.brace_tx)
        self.block_chain.generate_target()
        self.block_chain.target.scale(0.5).shift(RIGHT*2.5+UP)
        scene.play(MoveToTarget(self.block_chain))
        self.box = SurroundingRectangle(self.block_chain, buff = 0.2).set_color_by_gradient([PRIMARY_COLOR, GREY, WHITE])
        scene.wait()
        scene.play(AddTextLetterByLetter(self.blobs))#, Create(self.box))
        
        self.new_subsection(scene, "blobs are cheaper", "data/sound/e5/slide1-2a.mp3")

        scene.play(Write(self.blist[0]))
        
        self.new_subsection(scene, "still can access specific data", "data/sound/e5/slide1-2b.mp3")
        scene.play(Write(self.blist[1]))
        scene.wait(4)
        scene.play(Write(self.blist[2]))
        scene.wait(4)
        
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.title_text, self.block_chain, self.blobs, self.blist))