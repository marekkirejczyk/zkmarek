from manim import VGroup, RIGHT, DOWN, Arrow, Square, Text
from zkmarek.video.constant import BACKGROUND_COLOR, PRIMARY_COLOR, PRIMARY_FONT

class Node(VGroup):
    def __init__(self, value, font_size=32):
        super().__init__()
        square = Square(
            color=PRIMARY_COLOR,
            fill_color=BACKGROUND_COLOR,
            fill_opacity=1,
            side_length=1,
        )
        text = Text(str(value), z_index=1, font_size=font_size, font=PRIMARY_FONT)
        self.add(square, text)

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
    def __init__(self, num_children=2, num_levels=3):
        super().__init__()

        if num_children < 2 or num_children > 16:
            raise ValueError("Number of children per node must be between 2 and 16.")
        if num_levels < 1 or num_levels > 4:
            raise ValueError("Number of levels must be between 1 and 4.")

        base_font_size = max(12, 32 - 2 * (num_children - 2))

        levels = []
        for level in range(num_levels):
            num_nodes = num_children ** level
            nodes = VGroup(
                *[Node(f"0x{level}{i:03X}", font_size=base_font_size) for i in range(num_nodes)]
            )
            nodes.arrange(RIGHT, buff=1 if level == 0 else 0.5)
            levels.append(nodes)

        for i, level in enumerate(levels):
            if i == 0:
                level.move_to(0.5 * DOWN)
            else:
                level.next_to(levels[i - 1], DOWN, buff=1)

        arrows = []
        for i in range(1, num_levels):
            parent_level = levels[i - 1]
            child_level = levels[i]
            for parent_idx, parent_node in enumerate(parent_level):
                for child_offset in range(num_children):
                    child_idx = parent_idx * num_children + child_offset
                    if child_idx < len(child_level):
                        arrows.append(create_arrow(parent_node, child_level[child_idx]))

        for level in levels:
            self.add(level)
        self.add(*arrows)
