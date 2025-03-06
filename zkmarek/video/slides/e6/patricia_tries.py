from manim import (Text, RoundedRectangle, DashedVMobject, Create, Write, FadeIn, FadeOut, ReplacementTransform, Indicate, Brace, MathTex, TransformMatchingShapes, 
                   VGroup, ImageMobject, Integer, MoveToTarget, Group, RIGHT, UP, LEFT, DOWN, ChangeDecimalToValue)
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, HIGHLIGHT2_COLOR, SECONDARY_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.e6.bin_mpt import BinaryMPT as BinMPT
from zkmarek.video.slides.e6.table import TableKeyValue
from zkmarek.video.slides.e6.merkle16 import SelectiveMerkleTree as MT16 
from zkmarek.video.slides.e6.tree import MerkleTree as Tree

class PatriciaTries(SlideBase):
    def __init__(self) -> None:
        super().__init__("Patricia Tries")
        
    def construct(self):
        self.title_pt = Text("Patricia Trie", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 40).to_edge(UP)
        
    def animate_in(self, scene):
        self.key_value_pairs(scene)
        
        
    def key_value_pairs(self, scene):
        node = RoundedRectangle(width=4, height=2.5, corner_radius=0.1, color=PRIMARY_COLOR, fill_opacity=0.27)
        node = DashedVMobject(node, num_dashes=60)
        key = RoundedRectangle(width=1.5, height=0.5, corner_radius=0.1, color=PRIMARY_COLOR, fill_opacity = 0.27, stroke_width = 0.0).move_to(node.get_center()+UP*0.35)
        value = RoundedRectangle(width=1.5, height=0.5, corner_radius=0.1, color=PRIMARY_COLOR, fill_opacity = 0.27, stroke_width = 0.0).move_to(node.get_center()+DOWN*0.35)
        key_text = Text("key", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=20).move_to(key.get_center())
        value_text = Text("value", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=20).move_to(value.get_center())
        
        # key_explanation = Text("account address", color=SECONDARY_COLOR, font=PRIMARY_FONT, font_size=20).next_to(key, RIGHT, buff = 2.0)
        # value_explanation = Text("account balance", color=SECONDARY_COLOR, font=PRIMARY_FONT, font_size=20).next_to(value, RIGHT, buff = 2.0)
        
        self.new_subsection(scene, "key-value", "data/sound/e6/slide2-4a.mp3")
        scene.play(FadeIn(self.title_pt), Create(node))
        scene.play(Create(key), Write(key_text))
        scene.play(Create(value), Write(value_text))
        scene.wait(2.5)
        
        scene.play(FadeOut(node, key, value, key_text, value_text))

        table_key_value = TableKeyValue().scale(0.85)
        scene.play(Create(table_key_value))
        
        self.new_subsection(scene, "common prefixes", "data/sound/e6/slide2-4b.mp3")
        prefixes1 = [table_key_value.key_cells[0][0], table_key_value.key_cells[1][0], table_key_value.key_cells[2][0],
                     table_key_value.key_cells[3][0]]
        for i in range(len(prefixes1)):
            pref = prefixes1[i]
            scene.play(Indicate(pref[0:3], color = HIGHLIGHT2_COLOR), run_time=0.3)

        self.bin_mpt = BinMPT(include_labels=False).shift(LEFT*2.5).scale(0.7)
        self.bin_mpt_labels = BinMPT(include_labels=True)
        table_key_value.generate_target()
        table_key_value.target.scale(0.75).shift(RIGHT*4.5)
        scene.wait(1)
        scene.play(MoveToTarget(table_key_value))
        scene.play(Create(self.bin_mpt), run_time=2)
            
        self.new_subsection(scene, "indexed along the path", "data/sound/e6/slide2-4c.mp3")
        scene.play(FadeOut(table_key_value))
        self.bin_mpt.generate_target()
        self.bin_mpt.target.scale(1/0.7).shift(RIGHT*2.5)
        scene.play(MoveToTarget(self.bin_mpt))
        scene.play(ReplacementTransform(self.bin_mpt, self.bin_mpt_labels))
        self.bin_mpt = self.bin_mpt_labels
        indeces_nodes = [self.bin_mpt.root_branch.title_text, self.bin_mpt.branch1.title_text, self.bin_mpt.branch3.title_text, self.bin_mpt.leaf1.title_text]
        for indeces in indeces_nodes:
            scene.play(Indicate(indeces, color = HIGHLIGHT2_COLOR), run_time=0.45)
        scene.wait(0.5)
        scene.play(Indicate(self.bin_mpt.leaf1.field_group[0], color = HIGHLIGHT2_COLOR), run_time=1)
        scene.play(Indicate(self.bin_mpt.leaf2.field_group[0], color = HIGHLIGHT2_COLOR), run_time=0.5)
        scene.play(Indicate(self.bin_mpt.leaf4.field_group[0], color = HIGHLIGHT2_COLOR), run_time=0.5)
        scene.play(Indicate(self.bin_mpt.leaf3.field_group[0], color = HIGHLIGHT2_COLOR), run_time=0.5)
        scene.play(Indicate(self.bin_mpt.leaf1.field_group[1], color = HIGHLIGHT2_COLOR), run_time=1)
        scene.play(Indicate(self.bin_mpt.leaf2.field_group[1], color = HIGHLIGHT2_COLOR), run_time=0.5)
        scene.play(Indicate(self.bin_mpt.leaf4.field_group[1], color = HIGHLIGHT2_COLOR), run_time=0.5)
        scene.play(Indicate(self.bin_mpt.leaf3.field_group[1], color = HIGHLIGHT2_COLOR), run_time=0.5)
        
        self.new_subsection(scene, "300 mln addresses", "data/sound/e6/slide2-5.mp3")
        self.brace_levels(scene)
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.bin_mpt, self.title_pt))
        
    def brace_levels(self, scene):
        self.block = RoundedRectangle(width=5.5, height=3, color=PRIMARY_COLOR, fill_opacity=0.17, stroke_width = 0.0)
        ethereum = ImageMobject("data/images/new_ethereum.png").scale(1).move_to(self.block.get_bottom()+LEFT*2+UP*0.8)
        self.block = Group(self.block, ethereum)
        number = Integer(100000000, color = PRIMARY_COLOR).move_to(self.block.get_center()).shift(RIGHT+UP*0.3)
        addresses = Text("addresses", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=25).next_to(number, LEFT, buff = 0.3).shift(UP*0.1)
        brace_addresses = Brace(self.block, RIGHT, color=PRIMARY_COLOR).next_to(addresses, RIGHT, buff = 0).scale(0.5)
        scene.play(FadeIn(self.block, addresses, brace_addresses))
        scene.play(ChangeDecimalToValue(number, 308105039), run_time=3)
        scene.play(FadeOut(self.block, number, addresses, brace_addresses))
        
        self.merkle_tree_binary = Tree(num_levels=4).scale(0.5).shift(UP*3.7+LEFT*1)
        self.dots_bin_merkle1 = MathTex(r"\boldsymbol{\cdots}", color = PRIMARY_COLOR, font_size = 40).next_to(self.merkle_tree_binary.get_node(2, 0), DOWN, buff = 1.0).shift(DOWN*0.2)
        self.dots_bin_merkle2 = MathTex(r"\boldsymbol{\cdots}", color = PRIMARY_COLOR, font_size = 40).next_to(self.merkle_tree_binary.get_node(2, 1), DOWN, buff = 1.0).shift(DOWN*0.2)
        self.dots_bin_merkle3 = MathTex(r"\boldsymbol{\cdots}", color = PRIMARY_COLOR, font_size = 40).next_to(self.merkle_tree_binary.get_node(2, 2), DOWN, buff = 1.0).shift(DOWN*0.2)
        self.dots_bin_merkle4 = MathTex(r"\boldsymbol{\cdots}", color = PRIMARY_COLOR, font_size = 40).next_to(self.merkle_tree_binary.get_node(2, 3), DOWN, buff = 1.0).shift(DOWN*0.2)
        self.merkle_tree_binary = VGroup(self.merkle_tree_binary, self.dots_bin_merkle1, self.dots_bin_merkle2, self.dots_bin_merkle3, self.dots_bin_merkle4)
        scene.play(Create(self.merkle_tree_binary))
        self.brace_28_levels = Brace(self.merkle_tree_binary, direction=RIGHT, color=PRIMARY_COLOR)
        
        self.merkle_tree_hexary = MT16(num_levels=4, focused_node_path=[7,8,7]).scale(0.6).shift(UP*4+LEFT)
        self.dots_hex_merkle = MathTex(r"\boldsymbol{\cdots}", color = PRIMARY_COLOR, font_size = 40).next_to(self.merkle_tree_hexary, DOWN, buff = 0.3)
        
        self.brace_text_levels28 = Text("28 levels", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=20).next_to(self.brace_28_levels, RIGHT, buff = 0.1)
        self.brace_7_levels = Brace(self.merkle_tree_hexary, direction=RIGHT, color=PRIMARY_COLOR).scale(1.2).shift(DOWN*0.3)
        self.brace_text_levels7 = Text("8 levels", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=20).next_to(self.brace_7_levels, RIGHT, buff = 0.1)
        scene.wait(1.5)
        scene.play(Create(self.brace_28_levels), Write(self.brace_text_levels28))
        scene.wait(1.5)
        
        self.new_subsection(scene, "bin->hex", "data/sound/e6/slide2-5a.mp3")
        nodes = [self.merkle_tree_hexary.get_node(1, 0), self.merkle_tree_hexary.get_node(1, 1), self.merkle_tree_hexary.get_node(1, 2), self.merkle_tree_hexary.get_node(1, 3),
                 self.merkle_tree_hexary.get_node(1, 4), self.merkle_tree_hexary.get_node(1, 5), self.merkle_tree_hexary.get_node(1, 6), self.merkle_tree_hexary.get_node(1, 7),
                 self.merkle_tree_hexary.get_node(1, 8), self.merkle_tree_hexary.get_node(1, 9), self.merkle_tree_hexary.get_node(1, 10), self.merkle_tree_hexary.get_node(1, 11),
                 self.merkle_tree_hexary.get_node(1, 12), self.merkle_tree_hexary.get_node(1, 13), self.merkle_tree_hexary.get_node(1, 14), self.merkle_tree_hexary.get_node(1, 15)]
        scene.wait(1)
        scene.play(FadeOut(self.merkle_tree_binary, self.brace_28_levels, self.brace_text_levels28))
        scene.play(Create(self.merkle_tree_hexary), Write(self.dots_hex_merkle))
        for i in range(16):
            scene.play(Indicate(nodes[i], color = SECONDARY_COLOR), run_time=0.15)
            
        
        self.new_subsection(scene, "300m ->8 levels", "data/sound/e6/slide2-5b.mp3")
        scene.wait(1)
        scene.play(Create(self.brace_7_levels), Write(self.brace_text_levels7))
        scene.wait(2)
        
        self.new_subsection(scene, "15 siblings", "data/sound/e6/slide2-5c.mp3")
        scene.wait(2)
        scene.play(
            *[Indicate(nodes[i], color = SECONDARY_COLOR) for i in range(16)],
            run_time=0.8
        )
        self.new_subsection(scene, "MPT->ETH MPT", "data/sound/e6/slide2-5d.mp3")
        scene.wait(1)
        self.title_ETH_MPT = Text("Ethereum MPT", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 40).to_edge(UP)
        scene.play(TransformMatchingShapes(self.title_pt, self.title_ETH_MPT))
        scene.wait(2)  
        
        scene.play(FadeOut(self.merkle_tree_hexary, self.brace_7_levels, self.brace_text_levels7, self.dots_hex_merkle))     
        