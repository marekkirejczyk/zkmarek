from manim import VGroup, RIGHT, DOWN, Arrow, Square, Text
from zkmarek.video.constant import BACKGROUND_COLOR, PRIMARY_COLOR, PRIMARY_FONT

class Node(VGroup):
    def __init__(self, value):
        super().__init__()
        square = Square(
            color = PRIMARY_COLOR,
            fill_color = BACKGROUND_COLOR,
            fill_opacity = 1,
            side_length = 1,
        )
        text = Text(str(value), z_index=1, font_size=32, font=PRIMARY_FONT)
        self.add(square, text)

class MerkleTree(VGroup):
    def __init__(self):
        super().__init__()
        l0 = Node("root")
        l1 = VGroup(Node("hash()"), Node("hash()"))
        l2a = VGroup(Node("TX0"), Node("TX1"), Node("TX2"))
        l2b = VGroup(Node("TX3"), Node("TX4"), Node("TX5"))
        l1.arrange(RIGHT, buff=4)
        l2a.arrange(RIGHT, buff=0.5)
        l2b.arrange(RIGHT, buff=0.5)
        l1.next_to(l0, DOWN, buff=1)
        l2a.next_to(l1[0], DOWN, buff=1)
        l2b.next_to(l1[1], DOWN, buff=1)
        a = []
        a.append(create_arrow(l0, l1[0]))
        a.append(create_arrow(l0, l1[1]))
        for i in range(3):
            a.append(create_arrow(l1[0], l2a[i]))
            a.append(create_arrow(l1[1], l2b[i]))
        self.add(l0, l1, l2a, l2b, *a)


def create_arrow(start, end):
    return Arrow(
        start=start.get_bottom(),
        end=end[0].get_top(),
        color=PRIMARY_COLOR,
        buff=0,
        max_tip_length_to_length_ratio=0.1,
        max_stroke_width_to_length_ratio=1)
