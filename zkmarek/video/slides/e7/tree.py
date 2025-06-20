from manim import VGroup, DOWN, Text, RoundedRectangle, RIGHT, StealthTip, Arrow, DashedVMobject, UP
from zkmarek.video.constant import BACKGROUND_COLOR, PRIMARY_COLOR, PRIMARY_FONT, HIGHLIGHT_COLOR

class Node(VGroup):
    def __init__(self, value=None, font_size=32):
        super().__init__()
        square = RoundedRectangle(
            color=PRIMARY_COLOR,
            fill_color=BACKGROUND_COLOR,
            fill_opacity=0.3,
            width=.7,
            height=0.4,
            stroke_width = 0.0,
            corner_radius=0.1
        ).set_color(HIGHLIGHT_COLOR)
        text = Text(str(value) if value is not None else "", z_index=1, font_size=font_size, font=PRIMARY_FONT, color = PRIMARY_COLOR)
        self.value = value
        self.text = text
        self.add(square, text)

    def set_value(self, value):
        """Update the value and the displayed text."""
        self.value = value
        self.text.text = str(value)


def create_arrow(start, end, stroke_width=1.8, dash_density=2):
    arrow = Arrow(
        start=start.get_bottom(),
        end=end.get_top() + UP * 0.1,
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


class MerkleTree(VGroup):
    def __init__(self, num_children=2, num_levels=5, include_labels=True):
        super().__init__()

        if num_children < 2 or num_children > 16:
            raise ValueError("Number of children per node must be between 2 and 16.")
        if num_levels < 1 or num_levels > 7:
            raise ValueError("Number of levels must be between 1 and 7.")

        self.num_children = num_children
        self.num_levels = num_levels
        self.include_labels = include_labels
        self.nodes = []

        base_font_size = max(12, 28 - 2 * (num_children - 2))

        for level in range(num_levels):
            num_nodes = num_children ** level
            level_nodes = [
                Node(None if not include_labels else f"0x{level}{i:03X}", font_size=base_font_size)
                for i in range(num_nodes)
            ]
            self.nodes.append(level_nodes)

        for i, level_nodes in enumerate(self.nodes):
            level_group = VGroup(*level_nodes)
            level_group.arrange(RIGHT, buff=3 if i == 0 else 0.75)
            if i == 0:
                level_group.move_to(2. * UP)
            elif i == 1:
                level_group.arrange(RIGHT, buff=9.5)
                level_group.next_to(self.nodes[0][0], DOWN, buff=1).shift(DOWN*2)
            elif i == 2:
                level_group.arrange(RIGHT, buff=4.1)
                level_group.next_to(self.nodes[0][0], DOWN, buff=1).shift(DOWN*(i+3))
            elif i == 3:
                level_group.arrange(RIGHT, buff=1.65)
                level_group.next_to(self.nodes[0][0], DOWN, buff=1).shift(DOWN * (i+5))
            elif i == 4:
                level_group.arrange(RIGHT, buff=0.5)
                level_group.next_to(self.nodes[0][0], DOWN, buff=1).shift(DOWN* (i+7))
            elif i == 5:
                level_group.arrange(RIGHT, buff=0.2)
                level_group.next_to(self.nodes[0][0], DOWN, buff=1).shift(DOWN * (i+9))
            elif i == 6:
                level_group.arrange(RIGHT, buff=0.2)
                level_group.next_to(self.nodes[0][0], DOWN, buff=1).shift(DOWN * (i+11))
            
            self.add(level_group)

            for left, right in zip(level_nodes[:-1], level_nodes[1:]):
                midpoint = (left.get_right() + right.get_left()) / 2
                dots = Text(
                    "...",
                    font=PRIMARY_FONT,
                    color=PRIMARY_COLOR,
                    font_size=35
                ).move_to(midpoint)
                self.add(dots)

            

        for i in range(1, num_levels):
            parent_level = self.nodes[i - 1]
            child_level = self.nodes[i]
            for parent_idx, parent_node in enumerate(parent_level):
                for child_offset in range(num_children):
                    child_idx = parent_idx * num_children + child_offset
                    if child_idx < len(child_level):
                        arrow = create_arrow(parent_node, child_level[child_idx])
                        self.add(arrow)


    def get_node(self, level_idx, node_idx):
        if level_idx >= self.num_levels or node_idx >= len(self.nodes[level_idx]):
            raise IndexError("Invalid level or node index.")
        return self.nodes[level_idx][node_idx]
