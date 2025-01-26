from manim import VGroup, Rectangle, Text, RIGHT, DOWN, LEFT, UP, Arrow
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT


class MPTNode(VGroup):
    """Base class for a generic node in a Merkle Patricia Trie."""
    def __init__(self, node_type, content, width=4, height=2, font_size=18):
        super().__init__()
        self.rect = Rectangle(width=width, height=height, color="#4C566A", fill_opacity=0.4).set_stroke(width=2)
        self.label = Text(node_type, font_size=font_size + 10, font = PRIMARY_FONT, color = PRIMARY_COLOR).move_to(self.rect.get_top() + 0.3 * DOWN)
        self.content = VGroup(
            *[
                Text(f"{key}: {value}", font_size=font_size, font=PRIMARY_FONT).next_to(self.rect.get_top() + (i + 1) * 0.2 * DOWN+LEFT*1.4, DOWN, aligned_edge=LEFT)
                for i, (key, value) in enumerate(content.items())
            ]
        )
        self.add(self.rect, self.label, self.content)

class MPTBranchNode(MPTNode):
    """Specialized class for a Branch Node with rectangular child slots."""
    def __init__(self, content, width=11, height=1.8, child_width=0.5, child_height=0.9, font_size=18):
        super().__init__("Branch Node", {}, width=width, height=height, font_size=font_size)
        
        self.child_slots = VGroup()
        for i, value in enumerate(content.keys()):
            slot = Rectangle(
                width=child_width, height=child_height, 
                color="#88C0D0", fill_opacity=0.4, stroke_width=1.5
            )
            label = Text(str(value), font_size=font_size, font = PRIMARY_FONT).move_to(slot.get_center())
            slot_group = VGroup(slot, label)
            self.child_slots.add(slot_group)

        self.child_slots.arrange(RIGHT, buff=0.2).move_to(self.rect.get_center())
        self.add(self.child_slots)


class MerklePatriciaTrie(VGroup):
    """Class to create and animate a Merkle Patricia Trie."""
    def __init__(self):
        super().__init__()
        
        self.root = MPTNode("ROOT: Extension Node", {"shared nibble(s)": "a7", "next node": ""})
        self.branch1 = MPTBranchNode({i: "" for i in range(16)})
        self.leaf1 = MPTNode("Leaf Node", {"key-end": "1355", "value": "45.0 ETH"})
        self.extension2 = MPTNode("Extension Node", {"shared nibble(s)": "d3", "next node": ""})
        self.leaf2 = MPTNode("Leaf Node", {"key-end": "9365", "value": "1.1 ETH"})
        self.branch2 = MPTBranchNode({i: "" for i in range(16)})
        self.leaf3 = MPTNode("Leaf Node", {"key-end": "7", "value": "0.12 ETH"})
        self.leaf4 = MPTNode("Leaf Node", {"key-end": "7", "value": "1.00 WEI"})

        self.root.move_to(2 * UP)
        self.branch1.next_to(self.root, DOWN, buff=0.7)
        self.leaf1.next_to(self.branch1, LEFT+DOWN, buff=0.7)
        self.extension2.next_to(self.branch1, DOWN, buff=0.7)
        self.leaf2.next_to(self.branch1, RIGHT+DOWN, buff=0.7)
        self.branch2.next_to(self.extension2, DOWN, buff=0.7)
        self.leaf3.next_to(self.branch2, DOWN, buff=0.7).shift(LEFT*3.5)
        self.leaf4.next_to(self.branch2, DOWN, buff=0.7).shift(RIGHT*3.5)
        
        arrow = create_arrow(self.root, self.branch1)
        arrow2 = create_arrow(self.branch1, self.leaf1)
        arrow3 = create_arrow(self.branch1, self.extension2)
        arrow4 = create_arrow(self.branch1, self.leaf2)
        arrow5 = create_arrow(self.extension2, self.branch2)
        arrow6 = create_arrow(self.branch2, self.leaf3)
        arrow7 = create_arrow(self.branch2, self.leaf4)
        

        self.add(
            arrow, arrow2, arrow3, arrow4, arrow5, arrow6, arrow7
        )

        self.add(self.root, self.branch1, self.leaf1, self.extension2, self.leaf2, self.branch2, self.leaf3, self.leaf4)

def create_arrow(start, end, stroke_width=1):
    return Arrow(
        start=start.get_bottom(),
        end=end.get_top(),
        color=PRIMARY_COLOR,
        buff=0,
        max_tip_length_to_length_ratio=0.1,
        max_stroke_width_to_length_ratio=1,
        stroke_width=stroke_width,
    )
