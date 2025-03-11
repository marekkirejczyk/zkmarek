from manim import VGroup, Text, RIGHT, LEFT, DOWN, UP, Create, FadeOut, Indicate, MoveToTarget, RoundedRectangle, Write
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT

class SimplifiedWorldState(VGroup):
    def __init__(self):
        super().__init__()

        keys_data = [
            ["a", "7", "1", "1", "3", "5", "5"],  
            ["a", "7", "f", "9", "3", "6", "5"],  
            ["a", "7", "7", "d", "3", "3", "7"],  
            ["a", "7", "7", "d", "3", "8", "7"],  
        ]
        values_data = ["45.0 ETH", "1.00 WEI", "1.1 ETH", "0.12 ETH"] 

        cell_width = 0.45
        cell_height = 0.45
        corner_radius = 0.1
        spacing = 0.07
        num_rows = len(keys_data)
        num_cols = len(keys_data[0])

        bg_width = (cell_width * (num_cols + 1)) + 2.6
        bg_height = (cell_height + spacing) * num_rows + 1.2
        self.background = RoundedRectangle(
            width=bg_width,
            height=bg_height,
            corner_radius=0.3,
            color=PRIMARY_COLOR,
            fill_opacity=0.2,
            stroke_width=0.0
        )

        key_header = Text("Keys", font=PRIMARY_FONT, font_size=32, color=PRIMARY_COLOR)
        value_header = Text("Values", font=PRIMARY_FONT, font_size=32, color=PRIMARY_COLOR)
        title = Text("Simplified World State", font=PRIMARY_FONT, font_size=36, color=PRIMARY_COLOR)

        key_header.next_to(self.background.get_top(), DOWN).shift(LEFT * 1)
        value_header.next_to(self.background.get_top(), DOWN).shift(RIGHT * 1.9)
        title.next_to(self.background.get_top(), UP)

        self.key_cells = VGroup()
        self.value_cells = VGroup()

        for row_idx, (key_row, value) in enumerate(zip(keys_data, values_data)):
            for col_idx, key in enumerate(key_row):
                key_cell = RoundedRectangle(
                    width=cell_width,
                    height=cell_height,
                    corner_radius=corner_radius,
                    fill_opacity=0.3,
                    color=PRIMARY_COLOR,
                    stroke_width=0.0
                ).move_to(self.background.get_top()).shift(DOWN * (row_idx + 2) * (cell_height + spacing) + LEFT * (num_cols - col_idx - 1.2) * (cell_width + 0.1)+RIGHT*0.6)

                key_text = Text(key, font=PRIMARY_FONT, font_size=28, color=PRIMARY_COLOR).move_to(key_cell)

                self.key_cells.add(VGroup(key_cell, key_text))

            value_cell = RoundedRectangle(
                width=cell_width*3.6,
                height=cell_height,
                corner_radius=corner_radius,
                fill_opacity=0.35,
                color=PRIMARY_COLOR,
                stroke_width=0.0
            ).move_to(self.background.get_top()).shift(DOWN * (row_idx + 2) * (cell_height + spacing) + RIGHT * 2)

            value_text = Text(value, font=PRIMARY_FONT, font_size=28, color=PRIMARY_COLOR).move_to(value_cell)

            self.value_cells.add(VGroup(value_cell, value_text))
        self.title = title
        self.value_header = value_header
        self.key_header = key_header
        self.add(self.background, key_header, value_header, self.key_cells, self.value_cells, self.title)

    def show_table(self, scene, runtime=1):
        scene.play(
            Create(self.background),
            Write(self.key_cells),
            Write(self.value_cells),
            run_time=runtime
        )

    def remove_table(self, scene):
        scene.play(FadeOut(*self.submobjects))

    def appear_table(self, scene):
        scene.play(Create(self.background), Create(self.key_cells), Create(self.value_cells), Create(self.key_header), Create(self.value_header), Create(self.title), run_time=1)
        scene.wait(0.5)
        scene.play(Indicate(self.key_cells, color=PRIMARY_COLOR))
        scene.play(Indicate(self.value_cells, color=PRIMARY_COLOR))
        scene.wait(1.5)
        self.generate_target()
        self.target.shift(RIGHT * 4.7 + UP * 1).scale(0.6)
        scene.play(MoveToTarget(self))
