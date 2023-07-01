from manim import VGroup, Square, Text, RIGHT, BLUE_B, BLUE_D

class Cell(VGroup):
    def __init__(self, value, text_config={}):
        super().__init__()
        square = Square(
            color = BLUE_B,
            fill_color = BLUE_D,
            fill_opacity = 1,
            side_length = 1,
        )
        text = Text(str(value), z_index=1, **text_config)
        self.add(square, text)

class Array(VGroup):
    def __init__(self, values, text_config={}):
        super().__init__()
        for value in values:
            self.add(Cell(value, text_config))
        self.arrange(RIGHT, buff=0)
