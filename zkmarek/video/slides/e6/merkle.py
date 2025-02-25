from manim import (VGroup, Group, Rectangle, Text, ImageMobject, UP, LEFT, RIGHT, DOWN, Write, Create, FadeIn, MoveToTarget, Indicate, 
                   FadeOut, MathTex, RoundedRectangle, Transform, TransformMatchingShapes, Arrow, StealthTip, GrowArrow, Brace)
from manim import PURPLE_B, GREEN_D, YELLOW_D, GREEN_E, TEAL_E
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, HIGHLIGHT2_COLOR, SECONDARY_COLOR, HIGHLIGHT_COLOR
from zkmarek.video.slides.e6.tree import MerkleTree as Tree
from zkmarek.video.slides.e6.merkle_particia_trie import MerklePatriciaTrie as MPT
from zkmarek.video.slides.e6.worldstate import SimplifiedWorldState 
from zkmarek.video.slides.e6.bin_mpt import BinaryMPT as BinMPT
from zkmarek.video.slides.e6.table import TableKeyValue
from zkmarek.video.slides.e6.merkle16 import SelectiveMerkleTree as MT16 

class MerkleTree(SlideBase):
    def __init__(self) -> None:
        super().__init__("Merkle Trees")
        
    def construct(self):
        self.title_label = Text("Merkle Trees", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 40).to_edge(UP)
        
        self.finalized_blocks = [Rectangle(width=3, height=2, fill_opacity=0.0) for _ in range(3)]
        for i in range(3):
            self.finalized_blocks[i].set_color(HIGHLIGHT2_COLOR)
        self.finalized_group = VGroup(*self.finalized_blocks).arrange(RIGHT, buff=0.5)
        self.arrow_0_1 = Arrow(LEFT*0.4, RIGHT*0.5, color = PRIMARY_COLOR, tip_shape = StealthTip, stroke_width=2, 
                               max_tip_length_to_length_ratio=0.15).set_color(HIGHLIGHT2_COLOR).next_to(self.finalized_blocks[0], RIGHT, buff = 0.05)
        self.arrow_1_2 = Arrow(LEFT*0.4, RIGHT*0.5, color = PRIMARY_COLOR, tip_shape = StealthTip, stroke_width=2,
                               max_tip_length_to_length_ratio=0.15).set_color(HIGHLIGHT2_COLOR).next_to(self.finalized_group[1], RIGHT, buff = 0.05)
        
        self.ethereum = ImageMobject("data/images/ethereum_logo.png").scale(0.5)
        self.ethereum.move_to(self.finalized_blocks[1])
        self.ethereum2 = self.ethereum.copy()
        self.ethereum2.move_to(self.finalized_blocks[0])
        self.ethereum3 = self.ethereum.copy()
        self.ethereum3.move_to(self.finalized_blocks[2])
        self.eth_logos = Group(self.ethereum, self.ethereum2, self.ethereum3)
        
        self.account_data = Text("account data: [0x1298...1872: 0.1 ETH ", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 22)
        self.account_data_more = Text("0x9132...3817: 0.4 ETH \n 0x9712...1386: 2 ETH \n 0x2651...8137: 1 ETH \n ...]", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 22)
        self.transaction_data = Text("transaction data", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 24)
        
        self.transaction_data1 = Text("transaction data", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 24)
        self.transaction_data2 = Text("transaction data", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 24)
        
        self.account_data1 = Text("account data: [0x1234...1234: 0.5 ETH", color = PRIMARY_COLOR, font=PRIMARY_FONT, font_size = 22)
        self.account_data1_more = Text("0x3791...2468: 0.8 ETH \n 0x2651...8137: 3 ETH \n 0x9132...3817: 0.2 ETH \n ...]", color = PRIMARY_COLOR, font=PRIMARY_FONT, font_size = 22).next_to(self.account_data1[23], DOWN, buff = 0.2)
        self.account_data1 = VGroup(self.account_data1, self.account_data1_more)
        self.account_data2 = Text("account data: [0x8167...7316: 1 ETH", color = PRIMARY_COLOR, font=PRIMARY_FONT, font_size = 22)
        self.account_data2_more = Text("0x0124...1265: 0.9 ETH \n 0x3791...2468: 2 ETH \n 0x9712...1386: 1.1 ETH \n ...]", color = PRIMARY_COLOR, font=PRIMARY_FONT, font_size = 22).next_to(self.account_data2[23], DOWN, buff = 0.2)
        self.account_data2 = VGroup(self.account_data2, self.account_data2_more)
        
        self.computer = ImageMobject("data/images/computer.png").scale(0.5).shift(UP)
        
        self.markle_tree_2_3 = Tree(num_children=2, num_levels=3, include_labels=False).shift(RIGHT*3.5+UP*2.8).scale(0.3)
        self.markle_tree_2_3.stretch(2, dim=1)
        
        self.account_data_vector = Text("Account Data Vector", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=30).shift(LEFT*3.5+UP)
        self.arrow_acc_tree = Arrow(self.account_data_vector.get_right(), RIGHT*2+UP, color = PRIMARY_COLOR, tip_shape = StealthTip, stroke_width=2,
                               max_tip_length_to_length_ratio=0.15).set_color(SECONDARY_COLOR)

        self.account_vector_rectangles = [RoundedRectangle(width=1.8, height=1, fill_opacity=0.3, stroke_width = 0.0) for _ in range(4)]
        for i in range(4):
            self.account_vector_rectangles[i].set_color(PRIMARY_COLOR).scale(0.6)
        self.account_group = VGroup(*self.account_vector_rectangles).arrange(RIGHT, buff=0.5).next_to(self.account_data_vector, DOWN)
        self.vec0 = Text("1 ETH", font = PRIMARY_FONT, color = GREEN_D, font_size = 16).move_to(self.account_vector_rectangles[0])
        self.vec1 = Text("0.1 ETH", color = GREEN_D, font = PRIMARY_FONT, font_size = 16).move_to(self.account_vector_rectangles[1])
        self.dots_vec = MathTex(r"\boldsymbol{\cdots}", color = GREEN_D, font_size = 35).next_to(self.account_vector_rectangles[1], RIGHT, buff = 0.05).scale(0.8)
        self.vec2 = Text("0.8 ETH", color = GREEN_D, font = PRIMARY_FONT, font_size = 16).move_to(self.account_vector_rectangles[2])
        self.vec3 = Text("1.1 ETH", color = GREEN_D, font = PRIMARY_FONT, font_size = 16).move_to(self.account_vector_rectangles[3])
        self.vecs = VGroup(self.vec0, self.vec1, self.dots_vec, self.vec2, self.vec3)
        
        self.vector_8element = Text(r"46735083", color = GREEN_D, font_size = 24, font = PRIMARY_FONT).next_to(self.account_data_vector, DOWN)
        self.merkle_tree_2_4 = Tree(num_children=2, num_levels=4, include_labels=False).shift(UP*4).scale(0.6)
        self.account_vector_rectangles_8_elements = [RoundedRectangle(width=3, height=2, fill_opacity=0.3, stroke_width = 0.0) for _ in range(8)]
        for i in range(8):
            self.account_vector_rectangles_8_elements[i].set_color(PRIMARY_COLOR).scale(0.2)
        self.account_group_8_elements = VGroup(*self.account_vector_rectangles_8_elements).arrange(RIGHT, buff=0.2).next_to(self.account_data_vector, DOWN)
        
        for i in range(8):
            self.vector_8element[i].move_to(self.account_vector_rectangles_8_elements[i].get_center())
        
        self.seal_of_authenticity = ImageMobject("data/images/Badge.png").scale(0.3)
        
    def animate_in(self, scene):
        self.new_subsection(scene, "big amount of data", "data/sound/e6/slide2-0.mp3")
        scene.play(Write(self.title_label))
        scene.play(Create(self.finalized_group), GrowArrow(self.arrow_0_1), GrowArrow(self.arrow_1_2))
        for i in range(3):
            scene.play(FadeIn(self.eth_logos[i]))
        
        
        self.new_subsection(scene, "Full node 15 TB", "data/sound/e6/slide2-0a.mp3")
        side_block1 = Group(self.finalized_blocks[0], self.ethereum2.set_opacity(0.3))
        side_block2 = Group(self.finalized_blocks[2], self.ethereum3.set_opacity(0.3))
        main_block = Group(self.finalized_blocks[1], self.ethereum.set_opacity(0.3))
        side_block1.generate_target()
        side_block1.target.scale(0.4).shift(LEFT*2)
        side_block2.generate_target()
        side_block2.target.scale(0.4).shift(RIGHT*2)
        main_block.generate_target()
        main_block.target.scale(2)
        self.arrow_0_1.generate_target()
        self.arrow_0_1.target.scale(1.5).shift(LEFT*2.3)
        self.arrow_1_2.generate_target()
        self.arrow_1_2.target.scale(1.5).shift(RIGHT*2.3)
        scene.play(MoveToTarget(side_block1), MoveToTarget(side_block2), MoveToTarget(self.arrow_0_1), MoveToTarget(self.arrow_1_2)) 
        scene.play(MoveToTarget(main_block))
        self.account_data.move_to(self.finalized_blocks[1].get_top()+DOWN)
        self.account_data_more.next_to(self.account_data[23], DOWN, buff = 0.2)
        self.transaction_data.next_to(self.account_data, DOWN, buff = 1.5)  
        data_vecs = VGroup(self.transaction_data, self.account_data, self.account_data_more)
        self.data_size = Text("15 TB", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 24).shift(UP)
        scene.play(Write(self.account_data))
        scene.play(Create(self.account_data_more), Write(self.transaction_data), run_time=0.5)
        side_block1.generate_target()
        side_block1.target.scale(1/0.4).shift(RIGHT*1.5+DOWN)
        side_block2.generate_target()
        side_block2.target.scale(1/0.4).shift(LEFT*1.5+DOWN)
        main_block = Group(main_block, data_vecs)
        main_block.generate_target()
        main_block.target.scale(1/2).shift(DOWN)
        self.arrow_0_1.generate_target()
        self.arrow_0_1.target.shift(RIGHT*2.07+DOWN).scale(1/1.5)
        self.arrow_1_2.generate_target()
        self.arrow_1_2.target.shift(LEFT*2+DOWN).scale(1/1.5)
        scene.play(MoveToTarget(main_block), MoveToTarget(side_block1), MoveToTarget(side_block2), MoveToTarget(self.arrow_0_1), MoveToTarget(self.arrow_1_2)) 
        self.account_data1.scale(1/2).move_to(self.finalized_blocks[0].get_top()+DOWN*0.85)
        self.account_data2.scale(1/2).move_to(self.finalized_blocks[2].get_top()+DOWN*0.85)
        self.transaction_data1.scale(1/2).next_to(self.account_data1, DOWN, buff = 0.1)
        self.transaction_data2.scale(1/2).next_to(self.account_data2, DOWN, buff = 0.1)
        scene.play(Write(self.account_data1), Write(self.account_data2), Write(self.transaction_data1), Write(self.transaction_data2))
        scene.play(FadeIn(self.data_size))
        scene.wait(2.5)
        
        self.new_subsection(scene, "computer", "data/sound/e6/slide2-0b.mp3")
        scene.play(FadeIn(self.computer), FadeOut(self.data_size))
        scene.wait(2.5)
        all_vecs = VGroup(self.transaction_data1, self.transaction_data, self.transaction_data2)
        for i in range(len(all_vecs)):
            scene.play(Indicate(all_vecs[i], color = PURPLE_B, scale_factor=1.2), run_time=0.3)
        
        self.new_subsection(scene, "transaction included", "data/sound/e6/slide2-0c.mp3")
        scene.wait(3)
        account_indications = [self.account_data1_more[20:38], self.account_data[13:26], self.account_data2_more[20:38]]
        for acc in account_indications:
            scene.play(Indicate(acc, color = PURPLE_B), run_time=0.5)
        scene.wait(1)
        
        self.new_subsection(scene, "merkle trees", "data/sound/e6/slide2-1.mp3")
        scene.wait(2)
        scene.play(FadeOut(self.computer, main_block, side_block1, side_block2, self.finalized_group, self.eth_logos, self.transaction_data1, 
                           self.transaction_data2, self.account_data1, self.account_data2, self.arrow_0_1, self.arrow_1_2))
        
        self.new_subsection(scene, "data-> tree", "data/sound/e6/slide2-1a.mp3")
        node0_0 = self.markle_tree_2_3.get_node(0, 0)
        node2_1 = self.markle_tree_2_3.get_node(2, 1)
        node2_0 = self.markle_tree_2_3.get_node(2, 0)
        node2_2 = self.markle_tree_2_3.get_node(2, 2)
        node2_3 = self.markle_tree_2_3.get_node(2, 3)
        nodes_down = [node2_1, node2_0, node2_2, node2_3]
        for i in range(4):
            nodes_down[i].set_color(PRIMARY_COLOR)
        self.dots_vec_node = self.dots_vec.copy()
        self.dots_vec_node.next_to(node0_0, DOWN, buff = 1.0)
        self.dots_vec_node1 = self.dots_vec.copy()
        self.dots_vec_node1.next_to(node0_0, DOWN, buff = 1.0).shift(DOWN*1.2)
        scene.play(Create(self.account_data_vector))
        scene.play(Create(self.account_vector_rectangles[0]), Write(self.vec0), run_time=0.2)
        scene.play(Create(self.account_vector_rectangles[1]), Write(self.vec1), Write(self.dots_vec), run_time=0.2)
        scene.play(Create(self.account_vector_rectangles[2]), Write(self.vec2), run_time=0.2)
        scene.play(Create(self.account_vector_rectangles[3]), Write(self.vec3), run_time=0.2)
        scene.wait(2)
        scene.play(Create(self.markle_tree_2_3), Create(self.dots_vec_node1), Create(self.dots_vec_node))
        scene.wait(1)
        self.sel_node = self.markle_tree_2_3.get_node(2, 1)
        self.sel_node.set_color(SECONDARY_COLOR)
        scene.play(GrowArrow(self.arrow_acc_tree), run_time=0.5)
        scene.wait(1)
        self.other_nodes = [self.markle_tree_2_3.get_node(2, 0), self.markle_tree_2_3.get_node(2, 2), self.markle_tree_2_3.get_node(2, 3)]
        for node in self.other_nodes: 
            node.set_opacity(0.3)
        scene.wait(4)
        scene.play(FadeOut(self.account_group, self.vecs, self.markle_tree_2_3, self.dots_vec_node, self.dots_vec_node1, self.arrow_acc_tree, self.account_data_vector))
        
        
        self.new_subsection(scene, "8 element vector", "data/sound/e6/slide2-2.mp3")
        self.merkle24_nodes_level3 = [self.merkle_tree_2_4.get_node(3, 0), self.merkle_tree_2_4.get_node(3, 1), self.merkle_tree_2_4.get_node(3, 2), 
                                      self.merkle_tree_2_4.get_node(3, 3), self.merkle_tree_2_4.get_node(3, 4), self.merkle_tree_2_4.get_node(3, 5), 
                                      self.merkle_tree_2_4.get_node(3, 6), self.merkle_tree_2_4.get_node(3, 7)]
        for i in range(8):
            self.account_group_8_elements[i].next_to(self.merkle24_nodes_level3[i], DOWN, buff = 0.3)
            self.vector_8element[i].move_to(self.account_group_8_elements[i].get_center())
        for i in range(8):
            scene.play(Write(self.vector_8element[i]), Create(self.account_group_8_elements[i]), run_time=0.07)
        scene.wait(2)
        scene.play(Create(self.merkle_tree_2_4))
            

        
        self.new_subsection(scene, "leaf: value+hash", "data/sound/e6/slide2-2a.mp3")

        self.hashes_of_8_element(scene)

        
        self.new_subsection(scene, "root hash - immutable", "data/sound/e6/slide2-2c.mp3")
        scene.wait(1)
        self.seal_of_authenticity.next_to(self.merkle24_nodes_level0, LEFT, buff = 0.3)
        scene.play(FadeIn(self.seal_of_authenticity))
        scene.wait(1)
        scene.play(FadeOut(self.seal_of_authenticity))
        self.update_nodes(scene)
        
        self.new_subsection(scene, "merkle proofs", "data/sound/e6/slide2-3.mp3")
        level = [self.merkle24_nodes_level3[0], self.merkle24_nodes_level2[0], self.merkle24_nodes_level1[0], self.merkle24_nodes_level0]
        for i in range(4):
            levels = level[i]
            levels.set_color_by_gradient([GREEN_E, TEAL_E])

        self.account_group_8_elements[0].set_color(PRIMARY_COLOR)
        self.merkle_proof(scene)
        scene.wait(1)

        self.merkle_tree_all = Group(self.merkle_tree_2_4, self.vector_8element, self.account_group_8_elements, self.all_hashes)
        self.merkle_tree_all.generate_target()
        self.merkle_tree_all.target.scale(0.9).shift(LEFT)
        scene.play(MoveToTarget(self.merkle_tree_all))
        
        self.new_subsection(scene, "merkle proofs", "data/sound/e6/slide2-3b.mp3")
        self.calculate_merkle_proof(scene)
        
        self.new_subsection(scene, "key-value pairs", "data/sound/e6/slide2-4.mp3")
        self.key_value_pairs(scene)
        
        self.new_subsection(scene, "300m addresses - bin/hex", "data/sound/e6/slide2-5.mp3")
        self.brace_levels(scene)
        
        
    #     self.new_subsection(scene, "MPT -> ext, branches, leaves", "data/sound/e6/slide2-6.mp3")
    #     self.merkle_particia_trie(scene)
        
    #     self.new_subsection(scene, "4 deep level deep state", "data/sound/e6/slide2-6a.mp3")
    #     indications = [self.MPT.root, self.MPT.branch1, self.MPT.extension2, self.MPT.branch2]
    #     for i in indications:
    #         scene.play(Indicate(i, color = PURPLE_B, scale_factor=1.1), run_time=0.5)
            
    #     scene.wait(1)
    #     scene.play(Indicate(self.MPT.leaf1.field_group[0], color = PURPLE_B), Indicate(self.worldState.keys_table.get_rows()[0], color = PRIMARY_COLOR, scale_factor=1.5))
    #     scene.wait(1)
    #     scene.play(Indicate(self.MPT.leaf1.field_group[1], color = PURPLE_B), Indicate(self.worldState.values_table.get_rows()[0], color = PRIMARY_COLOR))
        
    #     self.new_subsection(scene, "8-10 levels", "data/sound/e6/slide2-7.mp3")
    #     self.brace_levels_16_children.next_to(self.MPT, RIGHT, buff = 0.1)
    #     self.brace_text_levels.next_to(self.brace_levels_16_children, RIGHT, buff = 0.1)
    #     scene.wait(1.5)
    #     self.worldState.remove_table(scene)
    #     scene.play(FadeIn(self.brace_levels_16_children, self.brace_text_levels))
        
    #     self.new_subsection(scene, "single merkle proof", "data/sound/e6/slide2-7a.mp3")
    #     scene.wait(0.5)
    #     self.proof_formula4 = MathTex(r"\mathrm{Proof size} = 15 \cdot \mathrm{depth} \cdot \mathrm{Hash size}", color = PRIMARY_COLOR, font_size = 30)
    #     self.proof_formula4.to_edge(LEFT+UP).shift(DOWN*0.8+RIGHT*0.7)
    #     scene.play(Indicate(self.proof_formula3, color = PURPLE_B))
    #     self.size_proof_mpt = MathTex(r"\sim 5 \  \mathrm{kB}", color = SECONDARY_COLOR, font_size = 30).next_to(self.proof_formula3, DOWN, buff = 0.2)
    #     scene.play(Create(self.size_proof_mpt))
        
    #     self.new_subsection(scene, "1000 account balances", "data/sound/e6/slide2-7b.mp3")
    #     scene.wait(2)
    #     self.proof_formula3.generate_target()
    #     self.proof_formula3.target.shift(RIGHT*0.7)
    #     scene.play(MoveToTarget(self.proof_formula3))
    #     self.thousand_proofs = MathTex(r"1000 \times", color = PRIMARY_COLOR, font_size = 30).next_to(self.proof_formula4, LEFT, buff = 0.1)
    #     self.thousand_size = MathTex(r"\sim 5 \ \mathrm{MB}", color = SECONDARY_COLOR, font_size = 30).next_to(self.proof_formula4, DOWN, buff = 0.1)
    #     scene.play(TransformMatchingShapes(self.size_proof_mpt, self.thousand_size), FadeIn(self.thousand_proofs))
        
    #     self.new_subsection(scene, "proofs smaller?", "data/sound/e6/slide2-7c.mp3")
    #     scene.wait(1.5)
    #     scene.play(FadeOut(self.MPT, self.brace_levels_16_children, self.brace_text_levels, self.proof_formula3, self.thousand_proofs, self.thousand_size))
    #     self.merkle_tree_text = Text("Merkle Tree", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 30).shift(LEFT*4)
    #     self.verkle_tree_text = Text("Verkle Tree", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 30).shift(RIGHT*4)
    #     self.arrow_merkle_verkle = Arrow(self.merkle_tree_text.get_right(), self.verkle_tree_text.get_left(), color = PRIMARY_COLOR, tip_shape = StealthTip, stroke_width=2, max_tip_length_to_length_ratio=0.15).set_color(PRIMARY_COLOR)
    #     self.vector_commitment = Text("+ Vector Commitment", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 30).next_to(self.arrow_merkle_verkle, DOWN, buff = 0.2)
    #     scene.play(Write(self.merkle_tree_text))
        
    #     self.new_subsection(scene, "merkle-> verkle", "data/sound/e6/slide2-7d.mp3")
    #     scene.play(GrowArrow(self.arrow_merkle_verkle), Create(self.vector_commitment))
    #     scene.play(Write(self.verkle_tree_text))
    #     scene.wait(2)
        
    # def animate_out(self, scene):
    #     scene.play(FadeOut(self.title_mpt, self.verkle_tree_text, self.merkle_tree_text, self.vector_commitment, self.arrow_merkle_verkle))
        
        
    def hashes_of_8_element(self, scene):
        self.level3_hashes_not_numerical = [Text("H(4)", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 16), Text("H(6)", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 16),
                                            Text("H(7)", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 16), Text("H(3)", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 16),
                                            Text("H(5)", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 16), Text("H(0)", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 16),
                                            Text("H(8)", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 16), Text("H(3)", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 16),]
        self.level_3_hashes = [Text("e2a1f...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 16), Text("f7c3b...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 16), 
                               Text("c1d04...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 16), Text("eccbc...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 16), 
                               Text("36279...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 16), Text("4b227...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 16), 
                               Text("cd573...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 16), Text("eccbc...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 16)]
        
        self.level_2_hashes = [Text("a6a68...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 16), Text("ae5a7...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 16), 
                               Text("e326b...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 16), Text("8dbb1...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 16)]
        
        self.level_1_hashes = [Text("56f15...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 16), Text("913a7...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 16)]
        
        self.level_0_hashes = Text("d7f0c...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 16)
        
        self.merkle24_nodes_level3 = [self.merkle_tree_2_4.get_node(3, 0), self.merkle_tree_2_4.get_node(3, 1), self.merkle_tree_2_4.get_node(3, 2), self.merkle_tree_2_4.get_node(3, 3), 
                                      self.merkle_tree_2_4.get_node(3, 4), self.merkle_tree_2_4.get_node(3, 5), self.merkle_tree_2_4.get_node(3, 6), self.merkle_tree_2_4.get_node(3, 7)]
        for i in range(8):
            level = self.merkle24_nodes_level3[i]
            self.level_3_hashes[i].move_to(level.get_center())
            not_numerical = self.level3_hashes_not_numerical[i]
            not_numerical.move_to(level.get_center())   
            
        self.merkle24_nodes_level2 = [self.merkle_tree_2_4.get_node(2, 0), self.merkle_tree_2_4.get_node(2, 1), self.merkle_tree_2_4.get_node(2, 2), self.merkle_tree_2_4.get_node(2, 3)]
        for i in range(4):
            level = self.merkle24_nodes_level2[i]
            self.level_2_hashes[i].move_to(level.get_center())
            
        self.merkle24_nodes_level1 = [self.merkle_tree_2_4.get_node(1, 0), self.merkle_tree_2_4.get_node(1, 1)]
        for i in range(2):
            level = self.merkle24_nodes_level1[i]
            self.level_1_hashes[i].move_to(level.get_center())
            
        self.merkle24_nodes_level0 = self.merkle_tree_2_4.get_node(0, 0)
        level = self.merkle24_nodes_level0
        self.level_0_hashes.move_to(level.get_center())
        
        for i in range(8):
            scene.play(Create(self.level3_hashes_not_numerical[i]), run_time=0.17)
        scene.play(Indicate(self.vector_8element, color = HIGHLIGHT_COLOR), Indicate(self.account_group_8_elements, color = HIGHLIGHT_COLOR), run_time=0.5)
        scene.wait(0.7)
        scene.play(TransformMatchingShapes(self.level3_hashes_not_numerical[0], self.level_3_hashes[0]), TransformMatchingShapes(self.level3_hashes_not_numerical[1], self.level_3_hashes[1]), 
                    TransformMatchingShapes(self.level3_hashes_not_numerical[2], self.level_3_hashes[2]), TransformMatchingShapes(self.level3_hashes_not_numerical[3], self.level_3_hashes[3]), 
                    TransformMatchingShapes(self.level3_hashes_not_numerical[4], self.level_3_hashes[4]), TransformMatchingShapes(self.level3_hashes_not_numerical[5], self.level_3_hashes[5]), 
                    TransformMatchingShapes(self.level3_hashes_not_numerical[6], self.level_3_hashes[6]), TransformMatchingShapes(self.level3_hashes_not_numerical[7], self.level_3_hashes[7]), 
                   run_time=0.5)
            
        scene.wait(1)
        
        self.new_subsection(scene, "children hashes", "data/sound/e6/slide2-2b.mp3")
        scene.play(
            *[Indicate(self.merkle24_nodes_level2[i], color = SECONDARY_COLOR) for i in range(4)],
            *[Indicate(self.merkle24_nodes_level1[i], color = SECONDARY_COLOR) for i in range(2)],
            run_time=0.8
        )
        for i in range(4):
            if i == 0:
                scene.play(Indicate(self.merkle24_nodes_level2[i]), Create(self.level_2_hashes[i]))
                scene.play(Indicate(self.merkle24_nodes_level3[0], color = SECONDARY_COLOR), run_time=0.5)
                scene.play(Indicate(self.merkle24_nodes_level3[1], color = SECONDARY_COLOR), run_time=0.5)
            else:
                scene.play(Create(self.level_2_hashes[i]), run_time=0.5)
        for i in range(2):
            scene.play(Create(self.level_1_hashes[i]), run_time=0.5)
        scene.play(Create(self.level_0_hashes), run_time=0.8)
        scene.wait(0.5)
        scene.play(Indicate(self.level_0_hashes, color = PURPLE_B), Indicate(self.merkle_tree_2_4.get_node(0,0)))
        
        
    def update_nodes(self, scene):
        index_of_the_node = 0
        new_value = 9
        new_numerical_value = Text(str(new_value), color = GREEN_D, font_size = 30, font=PRIMARY_FONT).move_to(self.account_group_8_elements[0].get_center())
        self.account_group_8_elements[0].set_color(YELLOW_D)
        scene.play(Transform(self.vector_8element[index_of_the_node], new_numerical_value))
        self.new_hashes = [Text("19581...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 16), Text("3c825...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 16), 
                      Text("9c493...", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size = 16), Text("d313e...", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size = 16)]
        level = [self.merkle24_nodes_level3[0], self.merkle24_nodes_level2[0], self.merkle24_nodes_level1[0], self.merkle24_nodes_level0]
        for i in range(4):
            levels = level[i]
            self.new_hashes[i].move_to(levels.get_center())
        
        prev_hashes = [self.level_3_hashes[0], self.level_2_hashes[0], self.level_1_hashes[0], self.level_0_hashes]
        for i in range(4):
            levels = level[i]
            prev_hash = prev_hashes[i]
            levels.set_color(YELLOW_D)
            scene.play(TransformMatchingShapes(prev_hash, self.new_hashes[i]), run_time=0.4)

        self.all_hashes = VGroup(
            *self.new_hashes, 
            *self.level_3_hashes[1:9], 
            *self.level_2_hashes[1:4], 
            *self.level_1_hashes[1:]
        )
        scene.wait(2.5)


    def merkle_proof(self, scene):     
        self.title_merkle_proof = Text("Merkle proof", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=40).to_edge(UP) 
        node_prove = self.merkle_tree_2_4.get_node(3, 3)
        scene.play(Indicate(node_prove, color = YELLOW_D), Indicate(self.account_group_8_elements[3], color = YELLOW_D), TransformMatchingShapes(self.title_label, self.title_merkle_proof))
        node_prove.set_color(YELLOW_D)
        self.account_group_8_elements[3].set_color(YELLOW_D)
        nodes_unused = [self.merkle_tree_2_4.get_node(3, 0), self.merkle_tree_2_4.get_node(3, 1), self.merkle_tree_2_4.get_node(3, 4), self.merkle_tree_2_4.get_node(3, 5), 
                        self.merkle_tree_2_4.get_node(3, 6), self.merkle_tree_2_4.get_node(3, 7), self.merkle_tree_2_4.get_node(2, 2), self.merkle_tree_2_4.get_node(2, 3)]
        self.hashes_unused = [self.new_hashes[0], self.level_3_hashes[1], self.level_3_hashes[4], self.level_3_hashes[5], self.level_3_hashes[6], 
                              self.level_3_hashes[7], self.level_2_hashes[2], self.level_2_hashes[3]]
        
        nodes_directly_used = [self.merkle_tree_2_4.get_node(2, 1), self.merkle_tree_2_4.get_node(1, 0), self.merkle_tree_2_4.get_node(0, 0)]
        for i in range(len(nodes_unused)):
            node = nodes_unused[i]
            hash = self.hashes_unused[i]
            node.generate_target()
            node.target.set_opacity(0.1)
            hash.generate_target()
            hash.target.set_opacity(0.1)
            scene.play(MoveToTarget(node), MoveToTarget(hash), run_time=0.2)
        scene.wait(1)
        for i in range(len(nodes_directly_used)):
            node = nodes_directly_used[i]
            node.generate_target()
            node.target.set_color(YELLOW_D)
            scene.play(MoveToTarget(node), run_time=0.35)
        scene.wait(1)
        nodes_needed_to_proof = [self.merkle_tree_2_4.get_node(3, 2), self.merkle_tree_2_4.get_node(2, 0), self.merkle_tree_2_4.get_node(1, 1)]
        for node in nodes_needed_to_proof:
            node.generate_target()
            node.target.set_color(HIGHLIGHT2_COLOR)
            scene.play(MoveToTarget(node), run_time=0.3)
        scene.wait(2)
            
        self.new_subsection(scene, "x3 belongs to set", "data/sound/e6/slide2-3a.mp3")
        scene.wait(1)
        scene.play(Indicate(node_prove, color = YELLOW_D))
        scene.wait(3)
        scene.play(Indicate(nodes_needed_to_proof[0], color = SECONDARY_COLOR), run_time=0.4)
        scene.play(Indicate(nodes_needed_to_proof[1], color = SECONDARY_COLOR), run_time=0.4)
        scene.play(Indicate(nodes_needed_to_proof[2], color = SECONDARY_COLOR), run_time=0.4)
        
    def calculate_merkle_proof(self, scene):
        sibling_formula = Text("c1d04...", color=PRIMARY_COLOR, font = PRIMARY_FONT, font_size=20).shift(RIGHT*4+UP*2.5)
        hash_sibling_leaf = Text("hash(c1d04..., eccbd...)", color=PRIMARY_COLOR, font = PRIMARY_FONT, font_size=20).shift(RIGHT*4+UP*2.5)
        parent_hash = Text("ae5a7... = hash(c1d04..., eccbd...)", color=PRIMARY_COLOR, font = PRIMARY_FONT, font_size=20).shift(RIGHT*4+UP*2.5)
        parent_sibling_hash = Text("hash(ae5a7..., 3c825...)", color=PRIMARY_COLOR, font = PRIMARY_FONT, font_size=20).shift(RIGHT*4+UP*2.5)
        grandparent_hash = Text("9c493... = hash(3c825..., ae5a7...)", color=PRIMARY_COLOR, font = PRIMARY_FONT, font_size=20).shift(RIGHT*4+UP*2.5)
        grandparent_sibling_hash = Text("hash(9c493..., 913a7...)", color=PRIMARY_COLOR, font = PRIMARY_FONT, font_size=20).shift(RIGHT*4+UP*2.5)
        root_hash = Text("d313e... = hash(9c493..., 913a7...)", color=PRIMARY_COLOR, font = PRIMARY_FONT, font_size=20).shift(RIGHT*4+UP*2.5)
        
        scene.wait(0.2)
        scene.play(TransformMatchingShapes(self.level_3_hashes[2].copy(), sibling_formula), Indicate(self.level_3_hashes[2], color = SECONDARY_COLOR), run_time=0.7)
        scene.wait(0.2)
        scene.play(TransformMatchingShapes(VGroup(sibling_formula, self.level_3_hashes[3].copy()), hash_sibling_leaf), Indicate(self.level_3_hashes[3], color = SECONDARY_COLOR), run_time=0.9)
        scene.wait(1)
        scene.play(TransformMatchingShapes(VGroup(hash_sibling_leaf, self.level_2_hashes[1].copy()), parent_hash), Indicate(self.level_2_hashes[1], color = SECONDARY_COLOR), run_time=0.9)
        scene.wait(0.4)
        parent_hash.generate_target()
        parent_hash.target.shift(DOWN*0.5)
        scene.play(TransformMatchingShapes(VGroup(parent_hash.copy(), self.new_hashes[1].copy()), parent_sibling_hash), Indicate(self.new_hashes[1], color = SECONDARY_COLOR), MoveToTarget(parent_hash), run_time=0.7)
        scene.wait(0.4)
        scene.play(TransformMatchingShapes(VGroup(parent_sibling_hash, self.new_hashes[2].copy()), grandparent_hash), Indicate(self.new_hashes[2], color = SECONDARY_COLOR), run_time=0.7)
        scene.wait(0.2)
        grandparent_hash.generate_target()
        grandparent_hash.target.shift(DOWN*0.5)
        parent_hash.generate_target()
        parent_hash.target.shift(DOWN*0.5)
        scene.play(TransformMatchingShapes(VGroup(grandparent_hash.copy(), self.level_1_hashes[1].copy()), grandparent_sibling_hash), Indicate(self.level_1_hashes[1], color = SECONDARY_COLOR), MoveToTarget(parent_hash), MoveToTarget(grandparent_hash), run_time=0.7)
        scene.wait(0.2)
        scene.play(TransformMatchingShapes(VGroup(grandparent_sibling_hash, self.new_hashes[3].copy()), root_hash), Indicate(self.new_hashes[3], color = SECONDARY_COLOR), run_time=0.7)
        
        scene.wait(1)
        scene.play(FadeOut(parent_hash, grandparent_hash, root_hash,
                           self.merkle_tree_all))
        
    def key_value_pairs(self, scene):
        node = RoundedRectangle(width=4, height=1.5, corner_radius=0.1, color=PRIMARY_COLOR, fill_opacity=0.2)
        key = RoundedRectangle(width=1.5, height=0.5, corner_radius=0.1, color=PRIMARY_COLOR, fill_opacity = 0.3).move_to(node.get_center()+UP*0.35)
        value = RoundedRectangle(width=1.5, height=0.5, corner_radius=0.1, color=PRIMARY_COLOR, fill_opacity = 0.3).move_to(node.get_center()+DOWN*0.35)
        key_text = Text("key", color=SECONDARY_COLOR, font=PRIMARY_FONT, font_size=20).move_to(key.get_center())
        value_text = Text("value", color=SECONDARY_COLOR, font=PRIMARY_FONT, font_size=20).move_to(value.get_center())
        
        key_explanation = Text("account address", color=HIGHLIGHT2_COLOR, font=PRIMARY_FONT, font_size=20).next_to(key, RIGHT, buff = 2.0)
        value_explanation = Text("account balance", color=HIGHLIGHT2_COLOR, font=PRIMARY_FONT, font_size=20).next_to(value, RIGHT, buff = 2.0)
        
        scene.play(Create(node))
        scene.play(Create(key), Write(key_text))
        scene.play(Create(value), Write(value_text))
        scene.wait(2)
        scene.play(Write(key_explanation))
        scene.wait(1)
        scene.play(Write(value_explanation))
        scene.wait(2)
        
        self.new_subsection(scene, "Table key-value", "data/sound/e6/slide2-4a.mp3")
        self.title_mpt = Text("Merkle Patricia Trie", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 40).to_edge(UP)
        scene.play(FadeOut(key_explanation, value_explanation, node, key, value, key_text, value_text))
        scene.play(TransformMatchingShapes(self.title_merkle_proof, self.title_mpt))

        table_key_value = TableKeyValue().scale(0.7).shift(DOWN*1)
        scene.play(Create(table_key_value))
        
        self.new_subsection(scene, "common prefixes", "data/sound/e6/slide2-4b.mp3")
        
        self.new_subsection(scene, "TABLE->MPT", "data/sound/e6/slide2-4c.mp3")
        self.bin_mpt = BinMPT().shift(LEFT*2.5).scale(0.7)
        table_key_value.generate_target()
        table_key_value.target.scale(0.75).shift(RIGHT*4.5)
        scene.wait(2)
        scene.play(MoveToTarget(table_key_value))
        scene.play(Create(self.bin_mpt), run_time=2)
        
        self.new_subsection(scene, "common prefixes", "data/sound/e6/slide2-4d.mp3")
        scene.play(FadeOut(table_key_value))
        self.bin_mpt.generate_target()
        self.bin_mpt.target.scale(1/0.75).shift(RIGHT*2.5)
        scene.play(MoveToTarget(self.bin_mpt))
        scene.wait(3)
        scene.play(FadeOut(self.bin_mpt))
        
        
    def brace_levels(self, scene):
        self.merkle_tree_binary = Tree(num_levels=4, include_labels=False).scale(0.5).shift(UP*3+LEFT*1)
        self.merkle_tree_hexary = MT16(num_levels=4, focused_node_path=[7,7,7], include_labels=False).scale(0.6).shift(UP*3+LEFT)
        scene.play(Create(self.merkle_tree_binary))
        self.brace_28_levels = Brace(self.merkle_tree_binary, direction=RIGHT, color=PRIMARY_COLOR)
        self.brace_text_levels28 = Text("28 levels", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=20).next_to(self.brace_28_levels, RIGHT, buff = 0.1)
        self.brace_7_levels = Brace(self.merkle_tree_hexary, direction=RIGHT, color=PRIMARY_COLOR)
        self.brace_text_levels7 = Text("7 levels", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=20).next_to(self.brace_7_levels, RIGHT, buff = 0.1)
        scene.wait(3)
        scene.play(Create(self.brace_28_levels), Write(self.brace_text_levels28))
        scene.wait(2)
        
        self.new_subsection(scene, "bin->hex", "data/sound/e6/slide2-5a.mp3")
        scene.wait(1)
        scene.play(FadeOut(self.merkle_tree_binary, self.brace_28_levels, self.brace_text_levels28))
        scene.play(Create(self.merkle_tree_hexary))
        
        self.new_subsection(scene, "300m ->7 lev", "data/sound/e6/slide2-5b.mp3")
        scene.wait(1)
        scene.play(Create(self.brace_7_levels), Write(self.brace_text_levels7))
        scene.wait(2)
        
        self.new_subsection(scene, "15 siblings", "data/sound/e6/slide2-5c.mp3")
        scene.wait(1)
        nodes = [self.merkle_tree_hexary.get_node(1, 0), self.merkle_tree_hexary.get_node(1, 1), self.merkle_tree_hexary.get_node(1, 2), self.merkle_tree_hexary.get_node(1, 3),
                 self.merkle_tree_hexary.get_node(1, 4), self.merkle_tree_hexary.get_node(1, 5), self.merkle_tree_hexary.get_node(1, 6), self.merkle_tree_hexary.get_node(1, 7),
                 self.merkle_tree_hexary.get_node(1, 8), self.merkle_tree_hexary.get_node(1, 9), self.merkle_tree_hexary.get_node(1, 10), self.merkle_tree_hexary.get_node(1, 11),
                 self.merkle_tree_hexary.get_node(1, 12), self.merkle_tree_hexary.get_node(1, 13), self.merkle_tree_hexary.get_node(1, 14), self.merkle_tree_hexary.get_node(1, 15)]
        for i in range(16):
            scene.play(Indicate(nodes[i], color = SECONDARY_COLOR), run_time=0.3)
            
        self.new_subsection(scene, "MPT->ETH MPT", "data/sound/e6/slide2-5d.mp3")
        scene.wait(1)
        self.title_ETH_MPT = Text("Ethereum MPT", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 40).to_edge(UP)
        scene.play(TransformMatchingShapes(self.title_mpt, self.title_ETH_MPT))
        scene.wait(2)        
        
    
    def merkle_particia_trie(self, scene):
        from manim import PURE_GREEN
        self.MPT = MPT().shift(UP*2.9+LEFT*1).scale(0.45)
        self.worldState = SimplifiedWorldState()
        self.worldState.construct()
        self.worldState.next_to(self.MPT, RIGHT+UP, buff = 0).shift(DOWN*2+LEFT*4)
        scene.play(Create(self.MPT))
        self.worldState.show_table(scene)
        scene.play(Indicate(self.worldState.keys_table.get_rows()[0], color = PRIMARY_COLOR, scale_factor=1.5), run_time=0.75)
        self.worldState.keys_table.get_rows()[0].set_color(PRIMARY_COLOR)
        path0 = [self.MPT.branch1.get_child_slot("1"), self.MPT.leaf1.field_group[0]]
        a7_label = None
        for field in self.MPT.root.field_group:
            _, text = field 
            if "a7" in text.text:
                a7_label = text[16:18]
                break
        if a7_label:
            scene.play(a7_label.animate.set_color(PURE_GREEN).scale(1.2)) 
        for item in path0:
            item.generate_target()
            item.target.set_color(PRIMARY_COLOR)
            scene.play(MoveToTarget(item), run_time=0.5)
            
        path1 = [self.MPT.branch2.get_child_slot("3"), self.MPT.leaf3.field_group[0]]
        d3_label = None
        for field in self.MPT.extension2.field_group:
            _, text = field 
            if "d3" in text.text:
                d3_label = text[16:18]
                break

        self.worldState.keys_table.get_rows()[1].set_color(SECONDARY_COLOR)
        scene.play(Indicate(self.worldState.keys_table.get_rows()[1], color = SECONDARY_COLOR, scale_factor=1.5), run_time=0.75)
        scene.play(Indicate(a7_label, color = SECONDARY_COLOR), run_time=0.5)
        scene.play(self.MPT.branch1.get_child_slot("7").animate.set_color(SECONDARY_COLOR), run_time=0.5)
        if d3_label:
            scene.play(d3_label.animate.set_color(SECONDARY_COLOR).scale(1.2)) 
        for item in path1:
            item.generate_target()
            item.target.set_color(SECONDARY_COLOR)
            scene.play(MoveToTarget(item), run_time=0.5)
    
        scene.wait(0.2)
        scene.play(Indicate(self.MPT.extension2, color = SECONDARY_COLOR, scale_factor=1.1))
        scene.play(Indicate(self.MPT.branch1, color = SECONDARY_COLOR, scale_factor=1.1))
        leaves = [self.MPT.leaf1, self.MPT.leaf2, self.MPT.leaf3, self.MPT.leaf4]
        for i in range(4):
            scene.play(Indicate(leaves[i], color = SECONDARY_COLOR, scale_factor=1.1), run_time=0.4)
            
        scene.wait(1)
        