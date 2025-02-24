from manim import RoundedRectangle, Text, VGroup, Arrow, UP, DOWN, RIGHT, LEFT, StealthTip
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, HIGHLIGHT_COLOR, SECONDARY_COLOR

class MPTNode(VGroup):
    """Base class for nodes in the Merkle Patricia Trie."""
    def __init__(self, title, fields, width=2.8, height=0.9, font_size=15, color = PRIMARY_COLOR):
        super().__init__()
        self.title = title
        self.fields = fields
        self.color = color

        self.rect = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.05,
            color=self.color,
            fill_color=self.color,
            fill_opacity=0.18,
            stroke_width = 0.0,
        )

        self.title_text = Text(
            self.title, font_size=font_size + 3, color=self.color, font = PRIMARY_FONT
        ).move_to(self.rect.get_top() + 0.15 * DOWN)

        self.field_group = VGroup()
        for i, (key, value) in enumerate(self.fields.items()):
            field_rect = RoundedRectangle(
                width=width * 0.45, height=0.5, color=self.color, stroke_width=0.0, fill_opacity=0.25, corner_radius=0.05
            )
            field_text = Text(
                f"{key}: {value}",
                font_size=font_size,
                color=self.color,
                font = PRIMARY_FONT
            ).move_to(field_rect.get_center())

            field_rect.next_to(self.title_text, DOWN, buff=(0.2))
            if i == 0:
                field_rect.shift(LEFT*0.65)
            else:
                field_rect.shift(RIGHT*0.65)
            field_text.move_to(field_rect.get_center())

            self.field_group.add(VGroup(field_rect, field_text))

        self.add(self.rect, self.title_text, self.field_group)

def create_arrow(start, end, stroke_width=1.8):
    return Arrow(
        start=start.get_bottom(),
        end=end.get_top()+UP*0.1,
        color=PRIMARY_COLOR,
        buff=0,
        max_tip_length_to_length_ratio=0.1,
        stroke_width=stroke_width,
        tip_shape = StealthTip,
        tip_length=0.2,
    )

class BinaryMPT(VGroup):
    def __init__(self):
        super().__init__()
        
        self.root_branch = MPTNode("Branch node (root)", {"left child": "", "right child": ""}, color=HIGHLIGHT_COLOR)
        self.branch1 = MPTNode("Branch node", {"left child": "", "right child": ""}, color=HIGHLIGHT_COLOR)
        self.branch2 = MPTNode("Branch node", {"left child": "", "right child": ""}, color=HIGHLIGHT_COLOR)
        self.branch3 = MPTNode("Branch node", {"left child": "", "right child": ""}, color=HIGHLIGHT_COLOR)
        
        self.leaf1 = MPTNode("Leaf node", {"key": "b0100", "value": "0x5678"})
        self.leaf2 = MPTNode("Leaf node", {"key": "f1734", "value": "0x5678"})
        self.leaf3 = MPTNode("Leaf node", {"key": "d364d", "value": "0x5678"})
        
        self.empty_leaf1 = MPTNode("Empty leaf", {"": "", "": ""}, color = SECONDARY_COLOR)
        self.empty_leaf2 = MPTNode("Empty leaf", {"": "", "": ""}, color = SECONDARY_COLOR)
        
        self.root_branch.to_edge(UP).shift(DOWN*0.8)
        buff = 0.37
        self.branch1.next_to(self.root_branch, DOWN+LEFT, buff = buff).shift(RIGHT*1.5)
        self.empty_leaf1.next_to(self.root_branch, RIGHT+DOWN, buff = buff).shift(LEFT*1.5)
        self.branch2.next_to(self.branch1, DOWN+RIGHT, buff = buff).shift(LEFT*1.5)
        self.leaf1.next_to(self.branch1, DOWN+LEFT, buff = buff).shift(RIGHT*1.5)
        self.branch3.next_to(self.branch2, DOWN+LEFT, buff = buff).shift(RIGHT*1.5)
        self.empty_leaf2.next_to(self.branch2, DOWN+RIGHT, buff = buff).shift(LEFT*1.5)
        self.leaf2.next_to(self.branch3, DOWN+LEFT, buff = buff).shift(RIGHT*1.5)
        self.leaf3.next_to(self.branch3, DOWN+RIGHT, buff = buff).shift(LEFT*1.5)
        
        self.arrow1 = create_arrow(self.root_branch, self.branch1)
        self.arrow2 = create_arrow(self.root_branch, self.empty_leaf1)
        self.arrow3 = create_arrow(self.branch1, self.branch2)
        self.arrow4 = create_arrow(self.branch1, self.leaf1)
        self.arrow5 = create_arrow(self.branch2, self.branch3)
        self.arrow6 = create_arrow(self.branch2, self.empty_leaf2)
        self.arrow7 = create_arrow(self.branch3, self.leaf2)
        self.arrow8 = create_arrow(self.branch3, self.leaf3)
        
        shift = 0.3+DOWN*0.8
        
        one = Text("1", font_size=15, color=PRIMARY_COLOR, font = PRIMARY_FONT).move_to(self.arrow2.get_center()+LEFT*shift+DOWN*0.05)
        branch1_branch2 = one.copy().move_to(self.arrow3.get_center()+LEFT*shift+DOWN*0.05)
        branch2_empty = one.copy().move_to(self.arrow6.get_center()+LEFT*shift+DOWN*0.05)
        branch3_leaf3 = one.copy().move_to(self.arrow8.get_center()+LEFT*shift+DOWN*0.05)
        
        zero = Text("0", font_size=15, color=PRIMARY_COLOR, font = PRIMARY_FONT).move_to(self.arrow1.get_center()+RIGHT*shift+DOWN*0.05)
        branch1_leaf1 = zero.copy().move_to(self.arrow4.get_center()+RIGHT*shift+DOWN*0.05)
        branch2_branch3 = zero.copy().move_to(self.arrow5.get_center()+RIGHT*shift+DOWN*0.05)
        branch3_leaf2 = zero.copy().move_to(self.arrow7.get_center()+RIGHT*shift+DOWN*0.05)
        
        
        
        self.add(self.root_branch, self.branch1, self.branch2, self.branch3, self.leaf1, self.leaf2, self.leaf3, self.empty_leaf1, self.empty_leaf2)
        self.add(self.arrow1, self.arrow2, self.arrow3, self.arrow4, self.arrow5, self.arrow6, self.arrow7, self.arrow8)
        self.add(one, zero, branch1_branch2, branch2_empty, branch3_leaf3, branch1_leaf1, branch2_branch3, branch3_leaf2)
        