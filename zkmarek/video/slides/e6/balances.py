from manim import (Text, RoundedRectangle, Arrow, StealthTip, DashedVMobject, Group, ImageMobject, VGroup, ORIGIN, UP, RIGHT, LEFT, DOWN, Create, 
                   FadeIn, FadeOut, MoveToTarget, Indicate, Write)
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR

class EthBalances(SlideBase):
    def __init__(self) -> None:
        super().__init__("Ethereum Balances")
        
    def construct(self):
        self.title_label = Text("Ethereum Balances", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 40).to_edge(UP)
        
        self.finalized_blocks = [RoundedRectangle(width=3.9, height=1.9, fill_opacity=0.2, corner_radius=0.15, stroke_width=0.0) for _ in range(3)]
        for i in range(3):
            self.finalized_blocks[i].set_color(PRIMARY_COLOR)
        self.finalized_group = VGroup(*self.finalized_blocks).arrange(RIGHT, buff=0.5)
        self.arrow_0_1 = Arrow(LEFT*0.4, RIGHT*0.5, color = PRIMARY_COLOR, tip_shape = StealthTip, stroke_width=2, 
                               max_tip_length_to_length_ratio=0.15).set_color(PRIMARY_COLOR).next_to(self.finalized_blocks[0], RIGHT, buff = 0.05)
        self.arrow_0_1 = DashedVMobject(self.arrow_0_1, num_dashes=3)
        self.arrow_1_2 = Arrow(LEFT*0.4, RIGHT*0.5, color = PRIMARY_COLOR, tip_shape = StealthTip, stroke_width=2,
                               max_tip_length_to_length_ratio=0.15).set_color(PRIMARY_COLOR).next_to(self.finalized_group[1], RIGHT, buff = 0.05)
        self.arrow_1_2 = DashedVMobject(self.arrow_1_2, num_dashes=3)
        
        self.ethereum = ImageMobject("data/images/new_ethereum.png").scale(0.75)
        self.ethereum.move_to(self.finalized_blocks[1])
        self.ethereum2 = self.ethereum.copy()
        self.ethereum2.move_to(self.finalized_blocks[0])
        self.ethereum3 = self.ethereum.copy()
        self.ethereum3.move_to(self.finalized_blocks[2])
        self.eth_logos = Group(self.ethereum, self.ethereum2, self.ethereum3)
        
        self.account_data = Text("account data: \n\n 0x1293...1877: 0.1 ETH ", font = PRIMARY_FONT, font_size = 28)
        self.account_data_more = Text(" 0x9132...3817: 0.4 ETH \n 0x9712...1386: 2.0 ETH \n 0x2651...8137: 1.0 ETH \n ...", font = PRIMARY_FONT, font_size = 28)
        self.transaction_data = Text("transaction data \n ... \n receipt data \n ...", font = PRIMARY_FONT, font_size = 28)
        
        self.transaction_data1 = Text("transaction data \n ... \n receipt data \n ...",  font = PRIMARY_FONT, font_size = 28)
        self.transaction_data2 = Text("transaction data \n ... \n receipt data \n ...", font = PRIMARY_FONT, font_size = 28)
        
        self.account_data1 = Text("account data: \n\n 0x1234...1234: 0.5 ETH", font=PRIMARY_FONT, font_size = 28)
        self.account_data1_more = Text(" 0x3791...2468: 0.8 ETH \n 0x2651...8137: 3.0 ETH \n 0x9132...3817: 0.2 ETH \n ...", font=PRIMARY_FONT, font_size = 28).next_to(self.account_data1[22], DOWN, buff = 0.2).shift(0.1*RIGHT)
        self.account_data1 = VGroup(self.account_data1, self.account_data1_more)
        self.account_data2 = Text("account data: \n\n 0x8173...7318: 1.0 ETH", font=PRIMARY_FONT, font_size = 28)
        self.account_data2_more = Text(" 0x0124...1265: 0.9 ETH \n 0x3791...2468: 2.0 ETH \n 0x9712...1386: 1.1 ETH \n ...", font=PRIMARY_FONT, font_size = 28).next_to(self.account_data2[22], DOWN, buff = 0.2).shift(0.1*RIGHT)
        self.account_data2 = VGroup(self.account_data2, self.account_data2_more)
        
        self.computer = ImageMobject("data/images/Laptop2x.png").scale(0.75).shift(UP)
        
        self.question_mark = Text("?", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size = 28)
        
    def animate_in(self, scene):
        self.new_subsection(scene, "big amount of data", "data/sound/e6/slide2-0.mp3")
        scene.play(Write(self.title_label))
        scene.play(Create(self.finalized_group[1]))

        scene.play(FadeIn(self.eth_logos[0]))
        
        self.new_subsection(scene, "Full node 15 TB", "data/sound/e6/slide2-0a.mp3")
        side_block1 = Group(self.finalized_blocks[0], self.ethereum2)
        side_block2 = Group(self.finalized_blocks[2], self.ethereum3)
        main_block = Group(self.finalized_blocks[1], self.ethereum)
        
        self.finalized_blocks[1].generate_target()
        self.finalized_blocks[1].target.scale(2)
        self.ethereum.generate_target()
        self.ethereum.target.scale(2).move_to(self.finalized_blocks[1].target.get_bottom()+RIGHT*3+UP)
        
        scene.play(MoveToTarget(self.finalized_blocks[1]), MoveToTarget(self.ethereum))
        
        self.account_data.move_to(self.finalized_blocks[1].get_top()+DOWN*0.98+LEFT*1.5)
        self.account_data_more.next_to(self.account_data[22], DOWN, buff = 0.2).shift(0.1*RIGHT)
        self.transaction_data.next_to(self.account_data[11], RIGHT, buff = 1.0).shift(RIGHT*0.6+DOWN*0.4)
        data_vecs = VGroup(self.transaction_data, self.account_data, self.account_data_more)
        self.data_size = Text("15 TB", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 24).shift(UP)
        
        scene.play(Write(self.account_data), run_time=1)
        scene.play(Create(self.account_data_more), Write(self.transaction_data), run_time=1)
        
        side_block1.shift(LEFT*0.5+DOWN)
        side_block2.shift(RIGHT*0.5+DOWN)
        
        main_block = Group(main_block, data_vecs)
        main_block.generate_target()
        main_block.target.scale(1/2).move_to(side_block2.get_center())
        side_block2.move_to(ORIGIN).shift(DOWN)
        
        self.arrow_0_1.shift(DOWN+LEFT*0.27)
        
        self.arrow_1_2.shift(DOWN+RIGHT*0.27)
        
        scene.wait(2)
        
        scene.play(MoveToTarget(main_block))
        scene.play(FadeIn(side_block1), FadeIn(side_block2), Write(self.arrow_0_1), Write(self.arrow_1_2)) 
        
        self.account_data1.scale(1/2).move_to(self.finalized_blocks[0].get_top()+DOWN*0.9+LEFT*0.8)
        self.account_data2.scale(1/2).move_to(self.finalized_blocks[2].get_top()+DOWN*0.9+LEFT*0.8)
        self.transaction_data1.scale(1/2).next_to(self.account_data1[0], RIGHT, buff = 0.1).shift(DOWN*0.12)
        self.transaction_data2.scale(1/2).next_to(self.account_data2[0], RIGHT, buff = 0.1).shift(DOWN*0.12)
        
        self.ethereum3.generate_target()
        self.ethereum3.target.move_to(self.finalized_group[2].get_bottom()+RIGHT*1.5+UP*0.5)
        self.ethereum2.generate_target()
        self.ethereum2.target.move_to(self.finalized_blocks[0].get_bottom()+RIGHT*1.5+UP*0.5)
        
        scene.play(Write(self.account_data1), Write(self.account_data2), Write(self.transaction_data1), Write(self.transaction_data2), MoveToTarget(self.ethereum3), MoveToTarget(self.ethereum2))
        scene.play(FadeIn(self.data_size))
        scene.wait(2.5)
        
        self.new_subsection(scene, "computer", "data/sound/e6/slide2-0b.mp3")
        scene.play(FadeIn(self.computer), FadeOut(self.data_size))
        scene.play(Write(self.question_mark.next_to(self.computer, RIGHT, buff = 0.1)), run_time=0.8)
        scene.wait(1.7)
        all_vecs = VGroup(self.transaction_data1, self.transaction_data, self.transaction_data2)
        for i in range(len(all_vecs)):
            scene.play(Indicate(all_vecs[i], color = SECONDARY_COLOR, scale_factor=1.2), run_time=0.3)
        scene.wait(1)
        scene.play(Indicate(self.question_mark, color = SECONDARY_COLOR))
        
        self.new_subsection(scene, "transaction included", "data/sound/e6/slide2-0c.mp3")
        scene.wait(3)
        account_indications = [self.account_data1_more[20:40], self.account_data[13:28], self.account_data2_more[20:40]]
        # for acc in account_indications:
        #     scene.play(Indicate(acc, color = SECONDARY_COLOR), run_time=0.5)
        scene.play(Indicate(account_indications[1], color = SECONDARY_COLOR), run_time=0.8)
        scene.wait(0.5)
        scene.play(Indicate(main_block, color = SECONDARY_COLOR), run_time=0.8)
        scene.wait(2)
        
        self.main_block = main_block
        self.side_block1 = side_block1
        self.side_block2 = side_block2
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.computer, self.main_block, self.side_block1, self.side_block2, self.finalized_group, self.eth_logos, self.transaction_data1, 
                           self.transaction_data2, self.account_data1, self.account_data2, self.arrow_0_1, self.arrow_1_2, self.question_mark, self.title_label))