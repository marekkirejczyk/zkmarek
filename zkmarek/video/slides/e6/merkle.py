from manim import (VGroup, Group, Rectangle, Text, ImageMobject, Brace, UP, LEFT, RIGHT, DOWN, Write, Create, FadeIn, MoveToTarget, Indicate, 
                   FadeOut, MathTex)
from manim import PURPLE_B, PURPLE, WHITE
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, HIGHLIGHT2_COLOR
from zkmarek.video.slides.e6.tree import MerkleTree as Tree
class MerkleTree(SlideBase):
    def __init__(self) -> None:
        super().__init__("Merkle Trees")
        
    def construct(self):
        self.title_label = Text("Merkle Trees", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 40).to_edge(UP)
        
        self.finalized_blocks = [Rectangle(width=3, height=2, fill_opacity=0.3) for _ in range(3)]
        for i in range(3):
            self.finalized_blocks[i].set_color_by_gradient([WHITE, PURPLE, HIGHLIGHT2_COLOR])
        self.finalized_group = VGroup(*self.finalized_blocks).arrange(RIGHT, buff=0.5)
        self.ethereum = ImageMobject("data/images/ethereum_logo.png").scale(0.5)
        self.ethereum.move_to(self.finalized_blocks[1])
        self.ethereum2 = self.ethereum.copy()
        self.ethereum2.move_to(self.finalized_blocks[0])
        self.ethereum3 = self.ethereum.copy()
        self.ethereum3.move_to(self.finalized_blocks[2])
        self.eth_logos = Group(self.ethereum, self.ethereum2, self.ethereum3)
        
        self.account_data = Text("account data: [3, 4, 5, ..., 4, 8, 3]", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 24)
        self.transaction_data = Text("transaction data: [1, 6, 2, ..., 7, 9, 4]\n .\n .\n .", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 24)
        
        self.transaction_data1 = Text("transaction data: [3, 2, 9, ..., 0, 2, 8]\n .\n .\n .", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 24)
        self.transaction_data2 = Text("transaction data: [7, 6, 0, ..., 8, 3, 4]\n .\n .\n .", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 24)
        
        self.account_data1 = Text("account data: [9, 8, 3, ..., 2, 7, 4]", color = PRIMARY_COLOR, font=PRIMARY_FONT, font_size = 24)
        self.account_data2 = Text("account data: [2, 1, 6, ..., 1, 0, 3]", color = PRIMARY_COLOR, font=PRIMARY_FONT, font_size = 24)
        
        self.computer = ImageMobject("data/images/computer.png").scale(0.5).shift(UP)
        
        self.markle_tree_2_3 = Tree(num_children=2, num_levels=3).shift(RIGHT*2.5+UP*2)
        
        self.account_data_vector = Text("Account Data Vector", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=30).shift(LEFT*2.5+UP)
        self.acc_vec = MathTex("[3, 4, 5, ..., 4, 8, 3]").next_to(self.account_data_vector, DOWN)
        
    def animate_in(self, scene):
        self.new_subsection(scene, "big amount of data", "data/sound/e6/slide2-0.mp3")
        scene.play(Write(self.title_label))
        scene.play(Create(self.finalized_group))
        for i in range(3):
            scene.play(FadeIn(self.eth_logos[i]))
        
        
        self.new_subsection(scene, "Full node 15 TB", "data/sound/e6/slide2-0a.mp3")
        side_block1 = Group(self.finalized_blocks[0], self.ethereum2)
        side_block2 = Group(self.finalized_blocks[3], self.ethereum3)
        main_block = Group(self.finalized_blocks[1], self.ethereum.set_opacity(0.3))
        side_block1.generate_target()
        side_block1.target.scale(0.4).shift(LEFT*2+DOWN)
        side_block2.generate_target()
        side_block2.target.scale(0.4).shift(RIGHT*2+DOWN)
        main_block.generate_target()
        main_block.target.scale(1.6)
        scene.play(MoveToTarget(side_block1), MoveToTarget(side_block2)) 
        scene.play(MoveToTarget(main_block))
        self.account_data.move_to(self.finalized_blocks[1].get_top()+DOWN)
        self.transaction_data.next_to(self.account_data, DOWN)  
        data_vecs = VGroup(self.transaction_data, self.account_data)
        self.brace_size_data = Brace(data_vecs, direction=LEFT)
        self.brace_text_size = Text("15 TB", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 24)
        self.brace_size_data.put_at_tip(self.brace_text_size)
        scene.play(Write(self.account_data))
        scene.play(Write(self.transaction_data))
        scene.wait(2)
        scene.play(FadeIn(self.brace_size_data, self.brace_text_size))
        scene.wait(2)
        
        self.new_subsection(scene, "computer", "data/sound/e6/slide2-0b.mp3")
        side_block1.generate_target()
        side_block1.target.scale(1/0.4).shift(RIGHT*2)
        side_block2.generate_target()
        side_block2.target.scale(1/0.4).shift(LEFT*2)
        main_block = Group(main_block, data_vecs, self.brace_size_data, self.brace_text_size)
        main_block.generate_target()
        main_block.target.scale(1/1.6).shift(DOWN)
        scene.play(MoveToTarget(main_block), MoveToTarget(side_block1), MoveToTarget(side_block2)) 
        self.account_data1.move_to(self.finalized_blocks[0].get_top()+DOWN)
        self.account_data2.move_to(self.finalized_blocks[2].get_top()+DOWN)
        self.transaction_data1.next_to(self.account_data1, DOWN)
        self.transaction_data2.next_to(self.account_data2, DOWN)
        scene.play(Write(self.account_data1), Write(self.account_data2), Write(self.transaction_data1), Write(self.transaction_data2))  
        scene.wait(1)
        scene.play(FadeIn(self.computer))
        scene.wait(1)
        all_vecs = VGroup(self.account_data1, self.account_data2, self.transaction_data1, self.transaction_data2, self.account_data, self.transaction_data)
        for i in range(len(all_vecs)):
            scene.play(Indicate(all_vecs[i], color = PURPLE_B), run_time=0.3)
        
        self.new_subsection(scene, "transaction included", "data/sound/e6/slide2-0c.mp3")
        scene.wait(3)
        self.account_data2.set_color(PURPLE)
        
        self.new_subsection(scene, "merkle trees", "data/sound/e6/slide2-1.mp3")
        scene.wait(1)
        scene.play(FadeOut(self.computer, main_block, side_block1, side_block2, self.finalized_group, self.eth_logos, self.transaction_data1, self.transaction_data2, self.account_data1, self.account_data2))
        
        self.new_subsection(scene, "data-> tree", "data/sound/e6/slide2-1a.mp3")
        scene.play(Create(self.account_data_vector), Create(self.acc_vec))
        scene.wait(2)
        scene.play(Create(self.markle_tree_2_3))
        
        
        # self.new_subsection(scene, "8 element vector", "data/sound/e6/slide2-2.mp3")
        
        # self.new_subsection(scene, "leaf: value+hash", "data/sound/e6/slide2-2a.mp3")
        
        # self.new_subsection(scene, "children hashes", "data/sound/e6/slide2-2b.mp3")
        
        # self.new_subsection(scene, "root hash - immutable", "data/sound/e6/slide2-2c.mp3")
        
        # self.new_subsection(scene, "merkle proofs", "data/sound/e6/slide2-3.mp3")
        
        # self.new_subsection(scene, "x3 belongs to set", "data/sound/e6/slide2-3a.mp3")
        
        # self.new_subsection(scene, "logarithmically", "data/sound/e6/slide2-4.mp3")
        
        # self.new_subsection(scene, "16 children 10 levels", "data/sound/e6/slide2-5.mp3")
        
        
        # self.new_subsection(scene, "32 bytes big -> formula for size", "data/sound/e6/slide2-5a.mp3")
        
        # self.new_subsection(scene, "MPT -> ext, branches, leaves", "data/sound/e6/slide2-6.mp3")
        
        # self.new_subsection(scene, "4 deep level deep state", "data/sound/e6/slide2-6a.mp3")
        
        # self.new_subsection(scene, "8-10 levels", "data/sound/e6/slide2-7.mp3")
        
        # self.new_subsection(scene, "single merkle proof", "data/sound/e6/slide2-7a.mp3")
        
        # self.new_subsection(scene, "1000 accounr balances", "data/sound/e6/slide2-7b.mp3")
        
        # self.new_subsection(scene, "proofs smaller?", "data/sound/e6/slide2-7c.mp3")
        
        # self.new_subsection(scene, "merkle-> verkle", "data/sound/e6/slide2-7d.mp3")
        