from manim import VGroup, Text, RIGHT, LEFT, DOWN, RoundedRectangle
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT

class TableKeyValue(VGroup):
    def __init__(self):
        super().__init__()

        keys = ["TRIE", "TRAN", "TOW", "TOKEN"]
        values = ["7", "9", "1", "7"]

        cell_width = 2.2
        cell_height = 0.8
        corner_radius = 0.2
        spacing = 0.1 
        num_rows = len(keys)

        bg_width = (cell_width * 2) + 1.2
        bg_height = (cell_height + spacing) * num_rows + 1.2
        self.background = RoundedRectangle(
            width=bg_width,
            height=bg_height,
            corner_radius=0.3,
            color=PRIMARY_COLOR,
            fill_opacity=0.2,
            stroke_width = 0.0
        )

        self.key_header = Text("Keys", font=PRIMARY_FONT, font_size=36, color=PRIMARY_COLOR)
        self.value_header = Text("Values", font=PRIMARY_FONT, font_size=36, color=PRIMARY_COLOR)

        self.key_header.next_to(self.background.get_top(), DOWN).shift(LEFT * (cell_width / 2 + 0.2))
        self.value_header.next_to(self.background.get_top(), DOWN).shift(RIGHT * (cell_width / 2 + 0.2))

        self.key_cells = VGroup()
        self.value_cells = VGroup()

        for i, (key, value) in enumerate(zip(keys, values)):
            key_cell = RoundedRectangle(
                width=cell_width,
                height=cell_height,
                corner_radius=corner_radius,
                fill_opacity=0.3,
                color=PRIMARY_COLOR,
                stroke_width = 0.0
            ).move_to(self.background.get_top()).shift(DOWN * (i + 1.5) * (cell_height + spacing)+LEFT*1.25)

            value_cell = key_cell.copy().shift(RIGHT * (cell_width + 0.3))

            key_text = Text(key, font=PRIMARY_FONT, font_size=30, color=PRIMARY_COLOR).move_to(key_cell)
            value_text = Text(value, font=PRIMARY_FONT, font_size=30, color=PRIMARY_COLOR).move_to(value_cell)

            self.key_cells.add(VGroup(key_cell, key_text))
            self.value_cells.add(VGroup(value_cell, value_text))

        self.add(self.background, self.key_header, self.value_header, self.key_cells, self.value_cells)
