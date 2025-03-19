from manim import (Text, UP, VGroup, Rectangle, Group, FadeIn, MoveToTarget, LEFT, RIGHT, DOWN, Indicate, Write, Create,
                   RoundedRectangle, ReplacementTransform, FadeOut, Arrow, DashedVMobject, StealthTip)
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR, HIGHLIGHT_COLOR

class EthereumBlock(SlideBase):
    def __init__(self) -> None:
        super().__init__("Ethereum Block")
        
    def construct(self):
        self.title_label = Text("Ethereum Block", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 40).to_edge(UP)

        self.block = Rectangle(width=10.5, height=2.5, color=PRIMARY_COLOR, fill_opacity=0.17, stroke_width = 0.0)
        # self.block.next_to(self.title_label, DOWN, buff = 0.5)
        self.block_label = Text("Block N Header", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=30).next_to(self.block, UP, buff = 0.2).shift(LEFT*1.5)
        
        labels = ["Prev hash", "Nonce", "Timestamp", "Uncles hash", "Mix hash", "...", "...", "..."]
        self.labels = VGroup()
        rectangle = Rectangle(width=1.5, height=0.5, color=PRIMARY_COLOR, fill_opacity=0.25, stroke_width = 0.0)
        
        self.rectangles = Group()
        for i, label in enumerate(labels):
            rectangle = rectangle.copy().move_to(self.block.get_center()).shift(LEFT*4+RIGHT*(i % 5)*2+UP*0.6)
            if i > 4:
                rectangle.shift(DOWN*0.6)
            if i > 9:
                rectangle.shift(DOWN*0.6)

            label_text = Text(label, font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=20).move_to(rectangle.get_center())
            self.labels.add(label_text)
            self.rectangles.add(rectangle)
                    
        
        tries = ["State Trie", "Withdrawals Trie", "Receipts Trie", "Transaction Trie"]
        self.tries = VGroup()
        self.rectangles_tries = Group()
        rectangle = Rectangle(width=2, height=0.5, color=PRIMARY_COLOR, fill_opacity=0.25, stroke_width = 0.0)
        for i, trie in enumerate(tries):
            rectangle = rectangle.copy().move_to(self.block.get_center()).shift(LEFT*3.75+RIGHT*(i % 5)*2.5+UP*0.6).shift(DOWN*1.2)
            trie_text = Text(trie, font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=20).move_to(rectangle.get_center())
            self.tries.add(trie_text)
            self.rectangles_tries.add(rectangle)
        
        self.block_header_whole = Group(self.block, self.block_label, self.rectangles, self.labels, self.rectangles_tries, self.tries)
        
        

    def animate_in(self, scene):
        self.new_subsection(scene, "five seperate tries", "data/sound/e6/slide2-7.mp3")
        scene.play(FadeIn(self.block), Write(self.block_label), Write(self.title_label))
        scene.play(FadeIn(self.rectangles_tries), Write(self.tries))
        scene.wait(0.3)
        scene.play(FadeIn(self.rectangles), Write(self.labels))
        scene.wait(1)
        self.block_header_whole.generate_target()
        self.block_header_whole.target.next_to(self.title_label, DOWN, buff = 0.1).scale(0.6)
        scene.play(MoveToTarget(self.block_header_whole))
        
        self.new_subsection(scene, "state trie", "data/sound/e6/slide2-7a.mp3")
        scene.play(Indicate(self.tries[0], color = SECONDARY_COLOR, scale_factor=1.5))
        self.create_state_trie()
        
        scene.play(Create(self.state_trie), run_time=2)
        
        self.rectangle_state_trie = Rectangle(width=6, height=0.75, color=HIGHLIGHT_COLOR, fill_opacity=0.25, stroke_width = 0.0)
        self.rectangle_state_trie.move_to(self.nodes[5]).shift(DOWN*0.2+RIGHT*2.5)
        
        labels_state_trie = ["address", "...", "...", "...", "Storage root"]
        self.labels_state_trie = VGroup()
        self.rectangles_state_trie = Group()
        rectangle_all = Rectangle(width=0.5, height=0.5, color=PRIMARY_COLOR, fill_opacity=0.25, stroke_width = 0.0)
        rectangle_storage = Rectangle(width=1.5, height=0.5, color=PRIMARY_COLOR, fill_opacity=0.25, stroke_width = 0.0)
        
        for i, label in enumerate(labels_state_trie):
            if i == 0:
                rectangle = rectangle_storage.copy().move_to(self.rectangle_state_trie.get_center()).shift(LEFT*2)
            elif i ==4:
                rectangle = rectangle_storage.copy().next_to(self.rectangles_state_trie[i-1], RIGHT, buff = 0.25)
            else:
                rectangle = rectangle_all.copy().next_to(self.rectangles_state_trie[i-1], RIGHT, buff = 0.25)
            
            label_text = Text(label, font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=20).move_to(rectangle.get_center())
            self.rectangles_state_trie.add(rectangle)
            self.labels_state_trie.add(label_text)
        
        self.account_balance_node = RoundedRectangle(width = 3.5, height = 0.7, corner_radius=0.05, color = HIGHLIGHT_COLOR, fill_opacity = 0.25, stroke_width = 0.0)
        self.account_balance_node.move_to(self.nodes[5]).shift(RIGHT*1.5+DOWN*0.1)
        
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
        scene.play(ReplacementTransform(self.nodes[5], self.acc_balance_node))
        scene.wait(2)
        scene.play(FadeOut(self.acc_balance_node), FadeIn(self.array_4_item))
        
        scene.wait(1)
        scene.play(Indicate(self.labels_state_trie[4], color=SECONDARY_COLOR, scale_factor=1.5))
        
        self.new_subsection(scene, "three more tries", "data/sound/e6/slide2-7c.mp3")
        scene.play(Indicate(self.tries[1], color=SECONDARY_COLOR, scale_factor=1.5), run_time=0.8)
        scene.play(Indicate(self.tries[2], color=SECONDARY_COLOR, scale_factor=1.5), run_time=0.8)
        scene.play(Indicate(self.tries[3], color=SECONDARY_COLOR, scale_factor=1.5), run_time=0.8)
        scene.wait(1)
        scene.play(Indicate(self.tries[3], color = SECONDARY_COLOR, scale_factor=1.5), run_time=0.8)
        scene.wait(0.5)
        scene.play(Indicate(self.tries[2], color = SECONDARY_COLOR, scale_factor=1.5), run_time=0.8)
        scene.wait(0.5)
        scene.play(Indicate(self.tries[1], color = SECONDARY_COLOR, scale_factor=1.5), run_time=0.8)
        scene.wait(0.5)
        
        self.new_subsection(scene, "each trie has key value", "data/sound/e6/slide2-7d.mp3")
        
        
        
    def create_state_trie(self):
        node1_0 = RoundedRectangle(corner_radius=0.05, height = 0.5, width = 0.5, color = HIGHLIGHT_COLOR, fill_opacity = 0.25, stroke_width = 0.0)
        node1_0.next_to(self.tries[0], LEFT+DOWN, buff = 0.8)
        
        node1_1 = node1_0.copy()
        node1_1.next_to(self.tries[0], RIGHT+DOWN, buff = 0.8)
        
        node2_0 = node1_0.copy()
        node2_0.next_to(node1_0, DOWN+LEFT, buff = 0.8).shift(RIGHT*0.5)
        
        node2_1 = node1_0.copy()
        node2_1.next_to(node1_0, DOWN+RIGHT, buff = 0.8).shift(LEFT*0.5)
        
        node2_2 = node1_0.copy()
        node2_2.next_to(node1_1, DOWN+LEFT, buff = 0.8).shift(RIGHT*0.5)
        
        node2_3 = node1_0.copy()
        node2_3.next_to(node1_1, DOWN+RIGHT, buff = 0.8).shift(LEFT*0.5)
        
        self.nodes = VGroup(node1_0, node1_1, node2_0, node2_1, node2_2, node2_3)   
        
        arrow1 = create_arrow(self.tries[0], node1_0)
        arrow2 = create_arrow(self.tries[0], node1_1)
        
        arrow3 = create_arrow(node1_0, node2_0)
        arrow4 = create_arrow(node1_0, node2_1)
        
        arrow5 = create_arrow(node1_1, node2_2)
        arrow6 = create_arrow(node1_1, node2_3)
        
        self.arrows = VGroup(arrow1, arrow2, arrow3, arrow4, arrow5, arrow6)
        
        self.state_trie = VGroup(self.nodes, self.arrows)
        
        
def create_arrow(start, end, stroke_width=1.8, dash_density=2):
    arrow = Arrow(
            start=start.get_bottom()+DOWN*0.1,
            end=end.get_top(),
            color=PRIMARY_COLOR,
            buff=0,
            max_tip_length_to_length_ratio=0.1,
            stroke_width=stroke_width,
            tip_shape=StealthTip,
            tip_length=0.15,
    )

    arrow_length = arrow.get_length()

    num_dashes = max(2, int(arrow_length * dash_density)) 

    return DashedVMobject(arrow, num_dashes=num_dashes)
        
        