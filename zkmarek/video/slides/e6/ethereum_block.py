from manim import (Text, UP, VGroup, Rectangle, Group, FadeIn, MoveToTarget, LEFT, RIGHT, DOWN, Indicate, Write, Create,
                   RoundedRectangle, ReplacementTransform, FadeOut)
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR, HIGHLIGHT_COLOR

from zkmarek.video.slides.e6.tree import MerkleTree

class EthereumBlock(SlideBase):
    def __init__(self) -> None:
        super().__init__("Ethereum Block")
        
    def construct(self):
        self.title_label = Text("Ethereum Block", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 40).to_edge(UP)

        self.block = Rectangle(width=10.5, height=3, color=PRIMARY_COLOR, fill_opacity=0.17, stroke_width = 0.0)
        # self.block.next_to(self.title_label, DOWN, buff = 0.5)
        self.block_label = Text("Block N Header", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=30).next_to(self.block, UP, buff = 0.2).shift(LEFT*1.5)
        
        labels = ["Prev hash", "Nonce", "Timestamp", "Uncles hash", "Mix hash", "Beneficiary", "Logs bloom", "Prev randao",
                  "Extra data", "Block num", "Gas limit", "Gas used", "Base fee per gas"]
        self.labels = VGroup()
        rectangle = Rectangle(width=1.5, height=0.5, color=PRIMARY_COLOR, fill_opacity=0.25, stroke_width = 0.0)
        
        self.rectangles = Group()
        for i, label in enumerate(labels):
            rectangle = rectangle.copy().move_to(self.block.get_center()).shift(LEFT*4+RIGHT*(i % 5)*2+UP*1)
            if i > 4:
                rectangle.shift(DOWN*0.6)
            if i > 9:
                rectangle.shift(DOWN*0.6)

            label_text = Text(label, font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=20).move_to(rectangle.get_center())
            self.labels.add(label_text)
            self.rectangles.add(rectangle)
                    
        
        tries = ["State Trie", "Storage Trie", "Receipts Trie", "Transaction Trie"]
        self.tries = VGroup()
        self.rectangles_tries = Group()
        rectangle = Rectangle(width=2, height=0.5, color=PRIMARY_COLOR, fill_opacity=0.25, stroke_width = 0.0)
        for i, trie in enumerate(tries):
            rectangle = rectangle.copy().move_to(self.block.get_center()).shift(LEFT*4+RIGHT*(i % 5)*2.5+UP*1.5).shift(DOWN*2.4)
            trie_text = Text(trie, font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=20).move_to(rectangle.get_center())
            self.tries.add(trie_text)
            self.rectangles_tries.add(rectangle)
        
        self.block_header_whole = Group(self.block, self.block_label, self.rectangles, self.labels, self.rectangles_tries, self.tries)
        
        # state trie
        self.state_trie = MerkleTree(num_children=2, num_levels=3, include_labels=False)
        self.state_trie.scale(0.2).stretch(2, 1)
        
        
        

    def animate_in(self, scene):
        self.new_subsection(scene, "five seperate tries", "data/sound/e6/slide2-7.mp3")
        scene.play(FadeIn(self.block), Write(self.block_label), Write(self.title_label))
        scene.wait(1)
        scene.play(FadeIn(self.rectangles), Write(self.labels))
        scene.wait(2)
        scene.play(FadeIn(self.rectangles_tries), Write(self.tries))
        self.block_header_whole.generate_target()
        self.block_header_whole.target.next_to(self.title_label, DOWN, buff = 0.1).scale(0.6)
        scene.play(MoveToTarget(self.block_header_whole))
        
        self.new_subsection(scene, "state trie", "data/sound/e6/slide2-7a.mp3")
        scene.play(Indicate(self.tries[0], color = SECONDARY_COLOR, scale_factor=1.5))
        self.state_trie.next_to(self.block, DOWN, buff = 0.2).shift(LEFT*2)
        scene.play(Create(self.state_trie), run_time=2)
        
        self.rectangle_state_trie = Rectangle(width=7, height=1, color=HIGHLIGHT_COLOR, fill_opacity=0.25, stroke_width = 0.0)
        self.rectangle_state_trie.move_to(self.state_trie.get_node(2, 3).get_center()).shift(DOWN*0.2+RIGHT*3.2)
        
        labels_state_trie = ["Nonce", "Balance", "Code hash", "Storage root"]
        self.labels_state_trie = VGroup()
        self.rectangles_state_trie = Group()
        rectangle = Rectangle(width=1.5, height=0.5, color=PRIMARY_COLOR, fill_opacity=0.25, stroke_width = 0.0)
        
        for i, label in enumerate(labels_state_trie):
            rectangle = rectangle.copy().move_to(self.rectangle_state_trie.get_center()).shift(LEFT*2.5+RIGHT*(i % 5)*1.7)
            label_text = Text(label, font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=20).move_to(rectangle.get_center())
            self.labels_state_trie.add(label_text)
            self.rectangles_state_trie.add(rectangle)
        
        self.account_balance_node = RoundedRectangle(width = 3.5, height = 0.7, corner_radius=0.05, color = HIGHLIGHT_COLOR, fill_opacity = 0.25, stroke_width = 0.0)
        self.account_balance_node.move_to(self.state_trie.get_node(2, 3).get_center()).shift(RIGHT*1.5+DOWN*0.1)
        
        address_rectangle = RoundedRectangle(width = 1.5, height = 0.5, corner_radius=0.05, color = PRIMARY_COLOR, fill_opacity = 0.25, stroke_width = 0.0)
        address_rectangle.move_to(self.account_balance_node.get_center()).shift(LEFT*0.82)
        address_text = Text("address", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=20).move_to(address_rectangle.get_center())
        self.address = VGroup(address_rectangle, address_text)
        
        balance_rectangle = RoundedRectangle(width = 1.5, height = 0.5, corner_radius=0.05, color = PRIMARY_COLOR, fill_opacity = 0.25, stroke_width = 0.0)
        balance_rectangle.move_to(self.account_balance_node.get_center()).shift(RIGHT*0.82)
        balance_text = Text("balance", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=20).move_to(balance_rectangle.get_center())
        self.balance = VGroup(balance_rectangle, balance_text)
        
        self.acc_balance_node = VGroup(self.balance, self.address, self.account_balance_node)
        
        self.array_4_item = Group(self.rectangles_state_trie, self.labels_state_trie, self.rectangle_state_trie)
        
        scene.wait(2)
        scene.play(ReplacementTransform(self.state_trie.get_node(2, 3), self.acc_balance_node))
        scene.wait(2)
        scene.play(FadeOut(self.acc_balance_node), FadeIn(self.array_4_item))
        
        self.new_subsection(scene, "storage trie", "data/sound/e6/slide2-7b.mp3")
        # scene.play(Indicate(self.tries[1], color=SECONDARY_COLOR, scale_factor=1.5))
        scene.wait(1)
        scene.play(Indicate(self.labels_state_trie[3], color=SECONDARY_COLOR, scale_factor=1.5))
        
        self.new_subsection(scene, "three more tries", "data/sound/e6/slide2-7c.mp3")
        scene.play(Indicate(self.tries[1], color=SECONDARY_COLOR, scale_factor=1.5))
        scene.wait(0.5)
        scene.play(Indicate(self.tries[2], color=SECONDARY_COLOR, scale_factor=1.5))
        scene.wait(0.5)
        scene.play(Indicate(self.tries[3], color=SECONDARY_COLOR, scale_factor=1.5))
        
        self.new_subsection(scene, "each trie has key value", "data/sound/e6/slide2-7d.mp3")
        
        