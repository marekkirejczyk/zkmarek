from manim import VGroup, DOWN, Text, RoundedRectangle, RIGHT, StealthTip
from zkmarek.video.constant import BACKGROUND_COLOR, PRIMARY_COLOR, PRIMARY_FONT, HIGHLIGHT_COLOR
from zkmarek.video.mobjects.dotted_line import DottedLine
class Node(VGroup):
    def __init__(self, value=None, font_size=32):
        super().__init__()
        square = RoundedRectangle(
            color=PRIMARY_COLOR,
            fill_color=BACKGROUND_COLOR,
            fill_opacity=0.3,
            width=2.3,
            height=1,
            stroke_width = 0.0,
            corner_radius=0.1
        ).set_color(HIGHLIGHT_COLOR)
        text = Text(str(value) if value is not None else "", z_index=1, font_size=font_size, font=PRIMARY_FONT)
        self.value = value
        self.text = text
        self.add(square, text)

    def set_value(self, value):
        """Update the value and the displayed text."""
        self.value = value
        self.text.text = str(value)


def create_arrow(start, end, stroke_width=1.8):
    return DottedLine(start = end.get_top(), 
                      end = start.get_bottom(), 
                      dot_spacing=0.1, 
                      dot_kwargs={"radius": 0.03, "color": PRIMARY_COLOR}, 
                      stroke_width=stroke_width).add_tip(tip_shape = StealthTip, tip_length=0.2, at_start=True).set_color(PRIMARY_COLOR)



class MerkleTree(VGroup):
    def __init__(self, num_children=2, num_levels=3, include_labels=True):
        super().__init__()

        if num_children < 2 or num_children > 16:
            raise ValueError("Number of children per node must be between 2 and 16.")
        if num_levels < 1 or num_levels > 4:
            raise ValueError("Number of levels must be between 1 and 4.")

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
                level_group.move_to(0.5 * DOWN)
            elif i == 1:
                level_group.arrange(RIGHT, buff=8.6)
                level_group.next_to(self.nodes[0][0], DOWN, buff=1)
            elif i == 2:
                level_group.arrange(RIGHT, buff=3.45)
                level_group.next_to(self.nodes[0][0], DOWN, buff=1).shift(DOWN*2)
            elif i == 3:
                level_group.next_to(self.nodes[0][0], DOWN, buff=1).shift(DOWN*4)
            elif i == 4:
                level_group.next_to(self.nodes[0][0], DOWN, buff=1).shift(DOWN*6)
            self.add(level_group)

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
        """
        Retrieve a node at a specific level and index.

        Parameters:
            level_idx (int): The level of the node (0 for root, and so on).
            node_idx (int): The index of the node at the given level (0 for leftmost node).

        Returns:
            Node: The specified node.
        """
        if level_idx >= self.num_levels or node_idx >= len(self.nodes[level_idx]):
            raise IndexError("Invalid level or node index.")
        return self.nodes[level_idx][node_idx]
