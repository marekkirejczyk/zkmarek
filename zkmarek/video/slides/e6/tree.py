from manim import VGroup, RIGHT, DOWN, Arrow, Square, Text, AnimationGroup, Transform
from zkmarek.video.constant import BACKGROUND_COLOR, PRIMARY_COLOR, PRIMARY_FONT

class Node(VGroup):
    def __init__(self, value=None, font_size=32):
        super().__init__()
        square = Square(
            color=PRIMARY_COLOR,
            fill_color=BACKGROUND_COLOR,
            fill_opacity=1,
            side_length=1,
        )
        text = Text(str(value) if value is not None else "", z_index=1, font_size=font_size, font=PRIMARY_FONT)
        self.value = value 
        self.text = text 
        self.add(square, text)

    def set_value(self, value):
        """Update the value and the displayed text."""
        self.value = value
        self.text.text = str(value)

def create_arrow(start, end):
    return Arrow(
        start=start.get_bottom(),
        end=end.get_top(),
        color=PRIMARY_COLOR,
        buff=0,
        max_tip_length_to_length_ratio=0.1,
        max_stroke_width_to_length_ratio=1,
    )

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
        self.levels = [] 
        self.arrows = []

        base_font_size = max(12, 28 - 2 * (num_children - 2))

        for level in range(num_levels):
            num_nodes = num_children ** level
            nodes = VGroup(
                *[Node(None if not include_labels else f"0x{level}{i:03X}", font_size=base_font_size) for i in range(num_nodes)]
            )
            nodes.arrange(RIGHT, buff=1 if level == 0 else 0.5)
            self.levels.append(nodes)

        for i, level in enumerate(self.levels):
            if i == 0:
                level.move_to(0.5 * DOWN)
            else:
                level.next_to(self.levels[i - 1], DOWN, buff=1)

        for i in range(1, num_levels):
            parent_level = self.levels[i - 1]
            child_level = self.levels[i]
            for parent_idx, parent_node in enumerate(parent_level):
                for child_offset in range(num_children):
                    child_idx = parent_idx * num_children + child_offset
                    if child_idx < len(child_level):
                        self.arrows.append(create_arrow(parent_node, child_level[child_idx]))

        for level in self.levels:
            self.add(level)
        self.add(*self.arrows)

    def add_labels(self):
        for level_idx, level in enumerate(self.levels):
            for node_idx, node in enumerate(level):
                node.set_value(f"0x{level_idx}{node_idx:03X}")

    def update_hash(self, level_idx, node_idx, new_value):
        if level_idx >= self.num_levels or node_idx >= len(self.levels[level_idx]):
            raise IndexError("Invalid level or node index.")
        self.levels[level_idx][node_idx].set_value(new_value)

        for i in range(level_idx, 0, -1):
            parent_idx = node_idx // self.num_children
            parent = self.levels[i - 1][parent_idx]
            child_hashes = [self.levels[i][child_idx].value for child_idx in range(parent_idx * self.num_children, (parent_idx + 1) * self.num_children)]
            parent.set_value(f"Hash({','.join(map(str, child_hashes))})")
            node_idx = parent_idx

    def indicate_node(self, scene, level_idx, node_idx, color=PRIMARY_COLOR, scale_factor=1.2, duration=1):
        """
        Highlight a node at the specified level and index.
        
        Parameters:
            level_idx (int): The level of the node (0 for root, and so on).
            node_idx (int): The index of the node at the given level (0 for leftmost node).
            color (str): The color to highlight the node.
            scale_factor (float): Factor to scale the node for the highlight effect.
            duration (float): Duration of the indication animation.
        """
        if level_idx >= self.num_levels or node_idx >= len(self.levels[level_idx]):
            raise IndexError("Invalid level or node index.")
        
        node = self.levels[level_idx][node_idx]

        node.generate_target()
        for submob in node.target:
            if isinstance(submob, Square): 
                submob.set_color(color)
            submob.scale(scale_factor)

        scene.play(
            AnimationGroup(
                Transform(node, node.target, run_time=duration),
                Transform(node, node.copy(), run_time=duration),
            ),
            lag_ratio=0.5,
        )