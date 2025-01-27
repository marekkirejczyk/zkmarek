from manim import VGroup, RIGHT, DOWN, RoundedRectangle, GREEN_E, TEAL_E, Arrow, Text
from zkmarek.video.constant import BACKGROUND_COLOR, PRIMARY_COLOR, PRIMARY_FONT

class Node(VGroup):
    def __init__(self, value=None, font_size=32):
        super().__init__()
        square = RoundedRectangle(
            color=PRIMARY_COLOR,
            fill_color=BACKGROUND_COLOR,
            fill_opacity=0.3,
            width=1.7,
            height=1.2,
        ).set_color_by_gradient([GREEN_E, TEAL_E])
        text = Text(str(value) if value is not None else "", z_index=1, font_size=font_size, font=PRIMARY_FONT)
        self.value = value
        self.text = text
        self.add(square, text)

    def set_value(self, value):
        """Update the value and the displayed text."""
        self.value = value
        self.text.text = str(value)


def create_arrow(start, end, stroke_width=1):
    return Arrow(
        start=start.get_bottom(),
        end=end.get_top(),
        color=PRIMARY_COLOR,
        buff=0,
        # max_tip_length_to_length_ratio=0.1,
        max_stroke_width_to_length_ratio=1,
        stroke_width=stroke_width,
    )


class SelectiveMerkleTree(VGroup):
    def __init__(self, num_children=16, num_levels=3, include_labels=True, focused_node_path=None):
        """
        Visualize a subset of a Merkle tree, displaying only one node's children per level.

        Parameters:
            num_children (int): Number of children per node.
            num_levels (int): Number of levels to visualize (including root).
            include_labels (bool): Whether to include labels on nodes.
            focused_node_path (list): A list specifying the path to the focused node.
                                      Example: [0, 1] means the root's first child, then its second child.
                                      Defaults to the first path [0, 0, ...].
        """
        super().__init__()

        if num_children < 2 or num_children > 16:
            raise ValueError("Number of children per node must be between 2 and 16.")
        if num_levels < 1 or num_levels > 5:
            raise ValueError("Number of levels must be between 1 and 4.")

        if focused_node_path is None:
            focused_node_path = [0] * (num_levels - 1)

        if len(focused_node_path) != num_levels - 1:
            raise ValueError("The focused_node_path length must be num_levels - 1.")

        self.num_children = num_children
        self.num_levels = num_levels
        self.include_labels = include_labels
        self.focused_node_path = focused_node_path

        self.nodes = []
        self.arrows = []

        self._create_selective_tree()

    def _create_selective_tree(self):
        """Generate the selective tree by focusing on the specified path."""
        root = Node("Root" if self.include_labels else None)
        root.move_to(0.5 * DOWN)
        self.nodes.append([root])
        self.add(root)

        current_node = root
        for level_idx in range(1, self.num_levels):
            child_index = self.focused_node_path[level_idx - 1]

            children = [
                Node(f"{level_idx}-{i}" if self.include_labels else None).scale(0.5)
                for i in range(self.num_children)
            ]

            focused_child = children[child_index]
            self.nodes.append(children)
            for child in children:
                self.add(child)

            spacing = 0.8
            for i, child in enumerate(children):
                child.next_to(current_node, DOWN, buff=1.4).shift(1.3*RIGHT * (i - (self.num_children - 1) / 2) * spacing)
            for i, child in enumerate(children):
                arrow = create_arrow(current_node, children[i])
                self.add(arrow)
                self.arrows.append(arrow)

            current_node = focused_child


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