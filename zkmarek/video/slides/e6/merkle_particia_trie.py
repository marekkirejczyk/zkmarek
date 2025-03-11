from manim import (VGroup, Rectangle, Text, RIGHT, DOWN, LEFT, UP, RoundedRectangle, StealthTip, Arrow, DashedVMobject,
                    TransformMatchingShapes)
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, HIGHLIGHT_COLOR

class MPTNode(VGroup):
    """Base class for nodes in the Merkle Patricia Trie."""
    def __init__(self, title, fields, width=6, height=2.5, font_size=26, color = HIGHLIGHT_COLOR):
        super().__init__()
        self.title = title
        self.fields = fields
        self.color = color
        self.rect = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.1,
            color=self.color,
            fill_opacity=0.15,
            stroke_width=0.0,
        )
        if self.title is not None:
            self.title_text = Text(
                self.title, font_size=font_size + 5, color=PRIMARY_COLOR, font = PRIMARY_FONT
            ).move_to(self.rect.get_top() + 0.3 * DOWN)

        self.field_group = VGroup()
        for i, (key, value) in enumerate(self.fields.items()):
            field_rect = RoundedRectangle(
                width=width * 0.9, height=0.7, color=self.color, stroke_width=0.0, fill_opacity=0.4, corner_radius=0.1
            )
            field_text = Text(
                f"{key}: {value}",
                font_size=font_size,
                # color="#ECEFF4",
                font = PRIMARY_FONT
            ).move_to(field_rect.get_center())

            
            if self.title is not None:
                field_rect.next_to(self.title_text, DOWN, buff=(0.2 + 0.8 * i))
                field_text.move_to(field_rect.get_center())
                self.add(self.title_text)
            else:
                shifts = [UP, DOWN]
                field_rect.move_to(self.rect.get_center()).shift(shifts[i] * 0.5)
                field_text.move_to(field_rect.get_center())
                

            self.field_group.add(VGroup(field_rect, field_text))

        self.add(self.rect, self.field_group)

class MPTBranchNode(MPTNode):
    """Specialized class for a Branch Node with rectangular child slots."""
    def __init__(self, content, width=12, height=1.8, child_width=0.5, child_height=0.9, font_size=24, color = HIGHLIGHT_COLOR):
        super().__init__("Branch Node", {}, width=width, height=height, font_size=font_size)

        self.child_slots = VGroup()
        self.child_slot_map = {} 
        self.color = color

        for i, value in enumerate(content.keys()):
            slot = Rectangle(
                width=child_width, height=child_height, 
                color=self.color, fill_opacity=0.6, stroke_width=0.0
            )
            label = Text(str(value), font_size=font_size, font=PRIMARY_FONT).move_to(slot.get_center())
            slot_group = VGroup(slot, label)
            
            self.child_slot_map[value] = slot_group
            self.child_slots.add(slot_group)

        self.child_slots.arrange(RIGHT, buff=0.2).move_to(self.rect.get_center()).shift(DOWN * 0.1)
        self.add(self.child_slots)

        if self.title is not None:
            self.add(self.title_text)

    def get_child_slot(self, value):
        """Retrieve a specific child slot by its label (e.g., '4')."""
        return self.child_slot_map.get(str(value), None)



class MerklePatriciaTrie(VGroup):
    """Class to create and animate a Merkle Patricia Trie."""
    def __init__(self):
        super().__init__()

        self.root = MPTNode(
            "Root: extension node", {"key": "a7", "next node": ""}
        )
        values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        self.branch1 = MPTBranchNode({i: "" for i in values})
        self.leaf_replace = MPTNode(
            title=None, fields = {"key": "a711355", "value": "45.0 ETH"}, color = PRIMARY_COLOR
        )
        self.extension2 = MPTNode(
            "Extension Node", {"shared nibble(s)": "d3", "next node": ""}
        )
        self.leaf2 = MPTNode(
            "Leaf Node", {"key": "9365", "value": "1.1 ETH"}, color = PRIMARY_COLOR
        )
        self.branch2 = MPTBranchNode({i: "" for i in values})
        self.leaf3 = MPTNode(
            "Leaf Node", {"key": "7", "value": "0.12 ETH"}, color = PRIMARY_COLOR
        )
        self.leaf4 = MPTNode(
            "Leaf Node", {"key": "7", "value": "1.00 WEI"}, color = PRIMARY_COLOR
        )
        
        self.leaf_replace2 = MPTNode(
            title=None, fields={"key": "11335", "value": "45.0 ETH"}, color = PRIMARY_COLOR)
        self.leaf1 = MPTNode(
            "Leaf", {"key": "1335", "value": "45.0 ETH"}, color = PRIMARY_COLOR)

        self.root.move_to(2 * UP)
        self.branch1.next_to(self.root, DOWN, buff=0.7)
        self.leaf1.next_to(self.branch1, LEFT+DOWN, buff=0.7)
        self.leaf_replace.next_to(self.branch1, LEFT+DOWN, buff=0.7)
        self.leaf_replace2.next_to(self.branch1, LEFT+DOWN, buff=0.7)
        self.extension2.next_to(self.branch1, DOWN, buff=0.7)
        self.leaf2.next_to(self.branch1, RIGHT+DOWN, buff=0.7)
        self.branch2.next_to(self.extension2, DOWN, buff=0.7)
        self.leaf3.next_to(self.branch2, DOWN, buff=0.7).shift(LEFT*5.5)
        self.leaf4.next_to(self.branch2, DOWN, buff=0.7).shift(RIGHT*5.5)
        
        self.arrow = create_arrow(end = self.root.get_bottom()+UP*0.8+RIGHT, start = self.branch1.get_top()+RIGHT)
        self.arrow2 = create_arrow(end = self.branch1.get_child_slot("1"), start = self.leaf1.get_top()).shift(RIGHT*0.4)
                      
        self.arrow3 = create_arrow(end = self.branch1.get_bottom()+UP*0.3+LEFT*0.33, start = self.extension2.get_top()+UP*0.3+LEFT*0.33)
        self.arrow4 = create_arrow(end = self.branch1.get_right()+LEFT*0.9+DOWN*0.5, start = self.leaf2.get_top())
                      
        self.arrow5 = create_arrow(end = self.extension2.get_bottom()+UP*0.8+RIGHT*1, start = self.branch2.get_top()+RIGHT*1)
        self.arrow6 = create_arrow(end = self.branch2.get_child_slot("3").get_bottom()+LEFT*0.2, start = self.leaf3.get_top()).shift(RIGHT*0.42+UP*0.01)
        self.arrow7 = create_arrow(end = self.branch2.get_bottom()+RIGHT*0.3+UP*0.3, start = self.leaf4.get_top()).shift(UP*0.01)
        


        self.add(self.root, self.branch1, self.leaf1, self.extension2, self.leaf2, self.branch2, self.leaf3, self.leaf4)
        self.add(
            self.arrow, self.arrow2, self.arrow3, self.arrow4, self.arrow5, self.arrow6, self.arrow7
        )
    def replace_leaf1(self, scene):
        self.leaf_replace2.move_to(self.leaf_replace.get_center())
        scene.play(TransformMatchingShapes(self.leaf_replace, self.leaf_replace2), run_time=1)
            
    def replace_leaf2(self, scene):
        self.leaf1.move_to(self.leaf_replace2.get_center())
        scene.play(TransformMatchingShapes(self.leaf_replace2, self.leaf1), run_time=1)

def create_arrow(start, end, stroke_width=1.8, dash_density=3):
    arrow = Arrow(
        start=end,
        end=start + UP * 0.1,
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

