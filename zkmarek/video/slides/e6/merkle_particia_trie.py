from manim import VGroup, Rectangle, Text, RIGHT, DOWN, LEFT, UP, Arrow, RoundedRectangle, StealthTip
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT


class MPTNode(VGroup):
    """Base class for nodes in the Merkle Patricia Trie."""
    def __init__(self, title, fields, width=6, height=2.5, font_size=24):
        super().__init__()
        self.title = title
        self.fields = fields

        self.rect = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.15,
            color="#4C566A",
            fill_color="#2E3440",
            fill_opacity=0.8,
        )

        self.title_text = Text(
            self.title, font_size=font_size + 5, color=PRIMARY_COLOR, font = PRIMARY_FONT
        ).move_to(self.rect.get_top() + 0.3 * DOWN)

        self.field_group = VGroup()
        for i, (key, value) in enumerate(self.fields.items()):
            field_rect = Rectangle(
                width=width * 0.9, height=0.4, color="#88C0D0", stroke_width=1.5
            )
            field_text = Text(
                f"{key}: {value}",
                font_size=font_size,
                color="#ECEFF4",
                font = PRIMARY_FONT
            ).move_to(field_rect.get_center())

            field_rect.next_to(self.title_text, DOWN, buff=(0.4 + 0.5 * i))
            field_text.move_to(field_rect.get_center())

            self.field_group.add(VGroup(field_rect, field_text))

        self.add(self.rect, self.title_text, self.field_group)


class MPTBranchNode(MPTNode):
    """Specialized class for a Branch Node with rectangular child slots."""
    def __init__(self, content, width=11, height=1.8, child_width=0.5, child_height=0.9, font_size=24):
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

        self.child_slots.arrange(RIGHT, buff=0.2).move_to(self.rect.get_center()).shift(DOWN*0.1)
        self.add(self.child_slots)


class MerklePatriciaTrie(VGroup):
    """Class to create and animate a Merkle Patricia Trie."""
    def __init__(self):
        super().__init__()

        self.root = MPTNode(
            "ROOT: Extension Node", {"shared nibble(s)": "a7", "next node": ""}
        )
        values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        self.branch1 = MPTBranchNode({i: "" for i in values})
        self.leaf1 = MPTNode(
            "Leaf Node", {"key-end": "1355", "value": "45.0 ETH"}
        )
        self.extension2 = MPTNode(
            "Extension Node", {"shared nibble(s)": "d3", "next node": ""}
        )
        self.leaf2 = MPTNode(
            "Leaf Node", {"key-end": "9365", "value": "1.1 ETH"}
        )
        self.branch2 = MPTBranchNode({i: "" for i in values})
        self.leaf3 = MPTNode(
            "Leaf Node", {"key-end": "7", "value": "0.12 ETH"}
        )
        self.leaf4 = MPTNode(
            "Leaf Node", {"key-end": "7", "value": "1.00 WEI"}
        )

        self.root.move_to(2 * UP)
        self.branch1.next_to(self.root, DOWN, buff=0.7)
        self.leaf1.next_to(self.branch1, LEFT+DOWN, buff=0.7)
        self.extension2.next_to(self.branch1, DOWN, buff=0.7)
        self.leaf2.next_to(self.branch1, RIGHT+DOWN, buff=0.7)
        self.branch2.next_to(self.extension2, DOWN, buff=0.7)
        self.leaf3.next_to(self.branch2, DOWN, buff=0.7).shift(LEFT*5.5)
        self.leaf4.next_to(self.branch2, DOWN, buff=0.7).shift(RIGHT*5.5)
        
        self.arrow = create_arrow(self.root, self.branch1).scale(2).shift(RIGHT+UP*0.5)
        self.arrow2 = Arrow(self.branch1.get_left()+RIGHT+DOWN*0.5, self.leaf1.get_top(), color=PRIMARY_COLOR, buff=0.2, 
                            max_stroke_width_to_length_ratio=1, stroke_width=1.5, tip_shape=StealthTip, tip_length = 0.2)
        self.arrow3 = create_arrow(self.branch1, self.extension2).shift(UP*0.3+LEFT*0.3)
        self.arrow4 = Arrow(self.branch1.get_right()+LEFT*0.3+DOWN*0.5, self.leaf2.get_top(), color=PRIMARY_COLOR, buff=0.2, 
                            max_stroke_width_to_length_ratio=1.5, stroke_width=1.5, tip_shape=StealthTip, tip_length = 0.2)
        self.arrow5 = create_arrow(self.extension2, self.branch2).scale(2).shift(RIGHT+UP*0.5)
        self.arrow6 = Arrow(self.branch2.get_left()+RIGHT*1.7+DOWN*0.5, self.leaf3.get_top(), color=PRIMARY_COLOR, buff=0.2, 
                            max_stroke_width_to_length_ratio=1.5, stroke_width=2, tip_shape=StealthTip, tip_length = 0.2)
        self.arrow7 = Arrow(self.branch2.get_bottom()+RIGHT*0.2+UP*0.3, self.leaf4.get_top(), color=PRIMARY_COLOR, buff=0.2, 
                            max_stroke_width_to_length_ratio=1.5, stroke_width=2, tip_shape=StealthTip, tip_length = 0.2)
        


        self.add(self.root, self.branch1, self.leaf1, self.extension2, self.leaf2, self.branch2, self.leaf3, self.leaf4)
        self.add(
            self.arrow, self.arrow2, self.arrow3, self.arrow4, self.arrow5, self.arrow6, self.arrow7
        )

def create_arrow(start, end, stroke_width=1.8):
    return Arrow(
        start=start.get_bottom(),
        end=end.get_top()+UP*0.1,
        color=PRIMARY_COLOR,
        buff=0.5,
        # max_stroke_width_to_length_ratio=1.5,
        stroke_width=stroke_width,
        tip_shape = StealthTip,
        tip_length = 0.2,
    )
