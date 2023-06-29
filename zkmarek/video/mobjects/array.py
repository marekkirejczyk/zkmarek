from manim import VGroup, Square, Text, RIGHT, BLUE_B, BLUE_D

class Array(VGroup):
    def __init__(self, values):
        super().__init__()
        for value in values:
            square = Square(
                color = BLUE_B,
                fill_color = BLUE_D,
                fill_opacity = 1,
                side_length = 1,
            )
            text = Text(str(value), z_index=1)
            group = VGroup(square, text)
            self.add(group)
        self.arrange(RIGHT, buff=0)
