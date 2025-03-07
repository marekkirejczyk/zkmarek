from manim import (Text, RoundedRectangle, DashedVMobject, Create, Write, FadeIn, FadeOut, ReplacementTransform, Indicate, Brace, MathTex, 
                   VGroup, ImageMobject, Integer, MoveToTarget, Group, RIGHT, UP, LEFT, DOWN, ChangeDecimalToValue)
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, HIGHLIGHT2_COLOR, SECONDARY_COLOR, HIGHLIGHT_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.e6.bin_mpt import BinaryMPT as BinMPT
from zkmarek.video.slides.e6.table import TableKeyValue
from zkmarek.video.slides.e6.merkle16 import SelectiveMerkleTree as MT16 
from zkmarek.video.slides.e6.tree import MerkleTree as Tree

class PatriciaTries(SlideBase):
    def __init__(self) -> None:
        super().__init__("Patricia Tries")
        
    def construct(self):
        self.title_pt = Text("Patricia Tries", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 40).to_edge(UP)
        self.bin_mpt = BinMPT(include_labels=False).shift(LEFT*2.5).scale(0.7)
        self.bin_mpt_labels = BinMPT(include_labels=True)
        texts = ["T", "R", "I", "A", "O", "K"]
        nodes = [self.bin_mpt.root_branch, self.bin_mpt.branch1, self.bin_mpt.branch3, 
                 self.bin_mpt.branch4, self.bin_mpt.branch2, self.bin_mpt.branch5]
        self.keys_on_nodes = []
        for i in range(len(texts)):
            text = texts[i]
            self.keys_on_nodes.append(Text(text, font=PRIMARY_FONT, color=HIGHLIGHT_COLOR, font_size = 20).move_to(nodes[i].get_center()))
        leaf_texts = ["E 7", "N 9", "W 1", "EN 7"]

        leaf_nodes = [self.bin_mpt.leaf1, self.bin_mpt.leaf2, self.bin_mpt.leaf4, self.bin_mpt.leaf3]
        
        self.leaf_keys = []
        for i in range(len(leaf_texts)):
            text = leaf_texts[i]
            self.leaf_keys.append(Text(text, font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 20).move_to(leaf_nodes[i].get_center()))
            
        self.addresses = Text("0x837416...934816", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=25)
        self.more_addresses = Text("0x123456...789012", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=25).next_to(self.addresses, DOWN, buff = 0.6)
        self.dots = Text("...\n...", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=30).next_to(self.more_addresses, DOWN, buff = 0.3)
        
    def animate_in(self, scene):
        self.key_value_pairs(scene)
        
        self.brace_levels(scene)
        
    def key_value_pairs(self, scene):
        node = RoundedRectangle(width=4, height=2.5, corner_radius=0.1, color=PRIMARY_COLOR, fill_opacity=0.27)
        node = DashedVMobject(node, num_dashes=60)
        key = RoundedRectangle(width=1.5, height=0.5, corner_radius=0.1, color=PRIMARY_COLOR, fill_opacity = 0.27, stroke_width = 0.0).move_to(node.get_center()+UP*0.35)
        value = RoundedRectangle(width=1.5, height=0.5, corner_radius=0.1, color=PRIMARY_COLOR, fill_opacity = 0.27, stroke_width = 0.0).move_to(node.get_center()+DOWN*0.35)
        key_text = Text("key", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=20).move_to(key.get_center())
        value_text = Text("value", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=20).move_to(value.get_center())
        
        self.new_subsection(scene, "key-value", "data/sound/e6/slide2-4a.mp3")
        scene.play(FadeIn(self.title_pt), Create(node), run_time=1)
        scene.wait(0.5)
        scene.play(Create(key), Write(key_text))
        scene.wait(1)
        scene.play(Create(value), Write(value_text))
        scene.wait(1)
        
        scene.play(FadeOut(node, key, value, key_text, value_text))

        table_key_value = TableKeyValue().scale(0.85)
        scene.play(Create(table_key_value))
        
        self.new_subsection(scene, "common prefixes", "data/sound/e6/slide2-4b.mp3")
        scene.wait(1)
        prefixes1 = [table_key_value.key_cells[0][0], table_key_value.key_cells[1][0], table_key_value.key_cells[2][0],
                     table_key_value.key_cells[3][0]]
        for i in range(len(prefixes1)):
            pref = prefixes1[i]
            scene.play(Indicate(pref[0:3], color = HIGHLIGHT2_COLOR), run_time=0.3)

        table_key_value.generate_target()
        table_key_value.target.scale(0.75).shift(RIGHT*4.5)
        scene.wait(1)
        scene.play(MoveToTarget(table_key_value))
        scene.play(Create(self.bin_mpt), run_time=2)
            
        self.new_subsection(scene, "indexed along the path", "data/sound/e6/slide2-4c.mp3")

        scene.play(Indicate(prefixes1[0], color = HIGHLIGHT2_COLOR), run_time=1)
        for j in range(3):
            scene.play(Write(self.keys_on_nodes[j]), run_time=0.5)
        scene.play(Write(self.leaf_keys[0]))
        scene.play(Indicate(prefixes1[1], color = HIGHLIGHT2_COLOR), run_time=1)
        scene.play(Write(self.keys_on_nodes[3]), Write(self.leaf_keys[1]), run_time=0.5)
        
        scene.play(Indicate(prefixes1[2], color = SECONDARY_COLOR), run_time=1)
        scene.play(Write(self.keys_on_nodes[4]), Write(self.leaf_keys[2]), run_time=0.5)
        
        scene.play(Indicate(prefixes1[3], color = SECONDARY_COLOR), run_time=1)
        scene.play(Write(self.keys_on_nodes[5]), Write(self.leaf_keys[3]), run_time=0.5)
                
        self.new_subsection(scene, "300 mln addresses", "data/sound/e6/slide2-5.mp3")
        scene.play(FadeOut(self.bin_mpt, table_key_value, *self.keys_on_nodes, *self.leaf_keys))
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.title_pt))
        
    def brace_levels(self, scene):
        self.block = RoundedRectangle(width=8.5, height=3, color=PRIMARY_COLOR, fill_opacity=0.17, stroke_width = 0.0)
        ethereum = ImageMobject("data/images/new_ethereum.png").scale(1).move_to(self.block.get_bottom()+LEFT*3+UP*0.8)
        self.block = Group(self.block, ethereum)
        number = Integer(0, color = PRIMARY_COLOR).move_to(self.block.get_center()).shift(RIGHT*3+UP*0.3)
        addresses = VGroup(self.addresses, self.more_addresses, self.dots).next_to(number, LEFT, buff = 0.8)
        brace_addresses = Brace(addresses, RIGHT, color=PRIMARY_COLOR).next_to(addresses, RIGHT, buff = 0.3)
        
        scene.play(FadeIn(self.block, addresses, brace_addresses))
        scene.play(ChangeDecimalToValue(number, 308105039), run_time=2)
        self.addresses.generate_target()
        self.addresses.target.move_to(self.block.get_center())
        scene.play(FadeOut(self.dots, self.more_addresses, number, brace_addresses), run_time=0.5)
        scene.play(MoveToTarget(self.addresses), run_time=0.5)
        
        length_brace = Brace(self.addresses, DOWN, color = PRIMARY_COLOR)
        length_text = Text("40 nibbles", color = PRIMARY_COLOR, font=PRIMARY_FONT, font_size=20).next_to(length_brace, DOWN, buff = 0.1)
        length_text_bytes = Text("20 bytes", color = PRIMARY_COLOR, font=PRIMARY_FONT, font_size=20).next_to(length_brace, DOWN, buff = 0.1)
        scene.play(Create(length_brace), Write(length_text))
        scene.wait(2)
        scene.play(ReplacementTransform(length_text, length_text_bytes))
        scene.wait(0.8)
        scene.play(FadeOut(self.addresses, length_brace, length_text_bytes, self.block))
        
        
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
        
        self.brace_text_levels28 = Text("160 levels", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=20).next_to(self.brace_28_levels, RIGHT, buff = 0.1)
        self.brace_7_levels = Brace(self.merkle_tree_hexary, direction=RIGHT, color=PRIMARY_COLOR).scale(1.2).shift(DOWN*0.3)
        self.brace_text_levels7 = Text("40 levels", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=20).next_to(self.brace_7_levels, RIGHT, buff = 0.1)
        scene.wait(1)
        scene.play(Create(self.brace_28_levels), Write(self.brace_text_levels28))
        scene.wait(3)
        
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
        
        self.new_subsection(scene, "nice optimization but still a lot of calc", "data/sound/e6/slide2-5c.mp3")
        scene.wait(2)
        scene.play(
            *[Indicate(nodes[i], color = SECONDARY_COLOR) for i in range(16)],
            run_time=0.8
        )
        scene.wait(6)
        
        self.play_sound(scene, "data/sound/e6/slide2-5d.mp3")
        scene.wait(2)  
        
        scene.play(FadeOut(self.merkle_tree_hexary, self.brace_7_levels, self.brace_text_levels7, self.dots_hex_merkle))     
        