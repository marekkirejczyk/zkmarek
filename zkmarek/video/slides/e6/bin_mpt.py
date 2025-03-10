from manim import RoundedRectangle, Text, VGroup, UP, DOWN, RIGHT, LEFT, StealthTip, DashedVMobject, Arrow
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, HIGHLIGHT_COLOR
class MPTNode(VGroup):
    """Base class for nodes in the Merkle Patricia Trie."""
    def __init__(self, title, fields, width=2, height=0.7, font_size=15, color=PRIMARY_COLOR, fillopacity=0.18, include_labels=True):
        super().__init__()
        self.title = title
        self.fields = fields if fields is not None else {} 
        self.color = color
        if fields is not None:
            width = width
        else:
            width = width*0.65
        self.rect = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.05,
            color=self.color,
            fill_color=self.color,
            fill_opacity=fillopacity,
            stroke_width = 0.0,
        )
        if include_labels:
            self.title_text = Text(
                self.title, font_size=font_size + 3, color=self.color, font = PRIMARY_FONT
            ).move_to(self.rect.get_top() + 0.15 * DOWN)
            if fields is None:
                self.title_text.move_to(self.rect.get_center())

            self.field_group = VGroup()
            for i, (key, value) in enumerate(self.fields.items()):
                field_rect = RoundedRectangle(
                    width=width * 0.46, height=0.35, color=self.color, stroke_width=0.0, fill_opacity=0.25, corner_radius=0.05
                )
                field_text = Text(
                    f"{key}: {value}",
                    font_size=font_size,
                    color=self.color,
                    font = PRIMARY_FONT
                ).move_to(field_rect.get_center())

                field_rect.next_to(self.title_text, DOWN, buff=(0.1))
                if i == 0:
                    field_rect.shift(LEFT*0.69)
                else:
                    field_rect.shift(RIGHT*0.69)
                field_text.move_to(field_rect.get_center())

                self.field_group.add(VGroup(field_rect, field_text))
            
            self.add(self.rect, self.title_text, self.field_group)
        else:
            self.add(self.rect)

def create_arrow(start, end, stroke_width=1.8, dash_density=3.5):
    arrow = Arrow(
        start=start.get_bottom(),
        end=end.get_top() + UP * 0.1,
        color=PRIMARY_COLOR,
        buff=0,
        # max_tip_length_to_length_ratio=0.1,
        stroke_width=stroke_width,
        tip_shape=StealthTip,
        tip_length=0.15,
    )

    arrow_length = arrow.get_length()

    num_dashes = max(2, int(arrow_length * dash_density)) 

    return DashedVMobject(arrow, num_dashes=num_dashes)


class BinaryMPT(VGroup):
    def __init__(self, include_labels = True):
        super().__init__()
        self.include_labels = include_labels
        
        self.root_branch = MPTNode("T", fields=None, color=HIGHLIGHT_COLOR, include_labels=self.include_labels)
        self.branch1 = MPTNode("R", fields=None, color=HIGHLIGHT_COLOR, include_labels=self.include_labels)
        self.branch2 = MPTNode("O", fields=None, color=HIGHLIGHT_COLOR, include_labels=self.include_labels)
        
        self.branch3 = MPTNode("I", fields=None, color=HIGHLIGHT_COLOR, fillopacity=0.12, include_labels=self.include_labels)
        self.branch4 = MPTNode("A", fields=None, color=HIGHLIGHT_COLOR, fillopacity=0.12, include_labels=self.include_labels)
        self.branch5 = MPTNode("K", fields=None, color=HIGHLIGHT_COLOR, fillopacity=0.12, include_labels=self.include_labels)
        
        self.leaf1 = MPTNode("E", fields=None, include_labels=self.include_labels)
        self.leaf2 = MPTNode("N", fields=None, include_labels=self.include_labels)
        self.leaf3 = MPTNode("EN", fields=None, include_labels=self.include_labels)
        self.leaf4 = MPTNode("W", fields=None, include_labels=self.include_labels)
        
        self.root_branch.to_edge(UP).shift(DOWN*0.8)
        buff = 0.5
        self.branch1.next_to(self.root_branch, LEFT+DOWN, buff=buff).shift(DOWN*0.2+LEFT*0.5)
        self.branch2.next_to(self.root_branch, RIGHT+DOWN, buff=buff).shift(DOWN*0.2+RIGHT*0.5)
        self.branch3.next_to(self.branch1, LEFT+DOWN, buff=buff).shift(RIGHT*0.7+DOWN*0.2)
        
        self.leaf1.next_to(self.branch3, DOWN, buff=buff).shift(DOWN*0.2)
        
        self.branch4.next_to(self.branch1, RIGHT+DOWN, buff=buff).shift(LEFT*0.7+DOWN*0.2)
        self.leaf2.next_to(self.branch4, DOWN, buff=buff).shift(DOWN*0.2)
        
        self.branch5.next_to(self.branch2, RIGHT+DOWN, buff=buff).shift(LEFT*0.7+DOWN*0.2)
        self.leaf4.next_to(self.branch2, DOWN+LEFT, buff=buff).shift(DOWN*0.2+RIGHT*1.2)
        self.leaf3.next_to(self.branch5, DOWN, buff=buff).shift(DOWN*0.2)
        
        self.arrow1 = create_arrow(self.root_branch, self.branch1)
        self.arrow2 = create_arrow(self.root_branch, self.branch2)
        self.arrow3 = create_arrow(self.branch1, self.branch3)
        self.arrow4 = create_arrow(self.branch1, self.branch4)
        self.arrow5 = create_arrow(self.branch4, self.leaf2)
        self.arrow6 = create_arrow(self.branch2, self.branch5)
        self.arrow7 = create_arrow(self.branch2, self.leaf4)
        self.arrow8 = create_arrow(self.branch5, self.leaf3)
        self.arrow9 = create_arrow(self.branch3, self.leaf1)
        
        # shift = 0.3+DOWN*0.8
        
        # one = Text("1", font_size=15, color=PRIMARY_COLOR, font = PRIMARY_FONT).move_to(self.arrow2.get_center()+LEFT*shift+DOWN*0.05)
        # branch1_branch2 = one.copy().move_to(self.arrow3.get_center()+LEFT*shift+DOWN*0.05)
        # branch2_empty = one.copy().move_to(self.arrow6.get_center()+LEFT*shift+DOWN*0.05)
        # branch3_leaf3 = one.copy().move_to(self.arrow8.get_center()+LEFT*shift+DOWN*0.05)
        
        # zero = Text("0", font_size=15, color=PRIMARY_COLOR, font = PRIMARY_FONT).move_to(self.arrow1.get_center()+RIGHT*shift+DOWN*0.05)
        # branch1_leaf1 = zero.copy().move_to(self.arrow4.get_center()+RIGHT*shift+DOWN*0.05)
        # branch2_branch3 = zero.copy().move_to(self.arrow5.get_center()+RIGHT*shift+DOWN*0.05)
        # branch3_leaf2 = zero.copy().move_to(self.arrow7.get_center()+RIGHT*shift+DOWN*0.05)
        
        
        
        self.add(self.root_branch, self.branch1, self.branch2, self.branch3, self.leaf1, self.leaf2, self.leaf3, self.leaf4, self.branch4, self.branch5)
        self.add(self.arrow1, self.arrow2, self.arrow3, self.arrow4, self.arrow5, self.arrow6, self.arrow7, self.arrow8, self.arrow9)
