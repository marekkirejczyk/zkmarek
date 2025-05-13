from manim import VGroup, Text, RIGHT, LEFT, DOWN, UP, RoundedRectangle, Create
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, HIGHLIGHT_COLOR

class TableKZGIPA(VGroup):
    def __init__(self):
        super().__init__()

        vec_commitment_column = ["commitment", "proof", "commitment\n   opening" ,
                                 "     use of\n trusted setup", "pairing-based\n verification"]
        kzg_values = ["1 EC point <48 B", "1 EC point <48 B", "   1 scalar field \n element <32 B", 
                      "Yes", "Yes"]
        
        ipa_values = ["1 EC point <32 B", "log2(n) EC points", "   1 scalar field\n element <32 B", 
                      "No", "No"]

        cell_width = 2.9
        cell_height = 0.8
        corner_radius = 0.2
        spacing = 0.1 
        num_rows = len(kzg_values)

        bg_width = (cell_width * 3) + 1.2
        bg_height = (cell_height + spacing) * num_rows + 1.2
        self.background = RoundedRectangle(
            width=bg_width,
            height=bg_height,
            corner_radius=0.3,
            color=PRIMARY_COLOR,
            fill_opacity=0.2,
            stroke_width = 0.0
        )

        self.key_header = Text("KZG on BLS12-381", font=PRIMARY_FONT, font_size=23, color=PRIMARY_COLOR)
        self.value_header = Text("IPA on Bandersnatch", font=PRIMARY_FONT, font_size=22, color=PRIMARY_COLOR)


        self.key_cells = VGroup()
        self.value_cells = VGroup()
        self.vec_column = VGroup()

        for i, (vec_column, key, value) in enumerate(zip(vec_commitment_column, kzg_values, ipa_values)):
            key_cell = RoundedRectangle(
                width=cell_width,
                height=cell_height,
                corner_radius=corner_radius,
                fill_opacity=0.3,
                color=PRIMARY_COLOR,
                stroke_width = 0.0
            ).move_to(self.background.get_top()).shift(DOWN * (i + 1.5) * (cell_height + spacing))

            value_cell = key_cell.copy().shift(RIGHT * (cell_width + 0.3))
            vec_cell = key_cell.copy().shift(LEFT * (cell_width + 0.3)).set_color(HIGHLIGHT_COLOR)

            vec_text = Text(vec_column, font=PRIMARY_FONT, font_size=23, color=HIGHLIGHT_COLOR).move_to(vec_cell)
            key_text = Text(key, font=PRIMARY_FONT, font_size=23, color=PRIMARY_COLOR).move_to(key_cell)
            value_text = Text(value, font=PRIMARY_FONT, font_size=23, color=PRIMARY_COLOR).move_to(value_cell)

            self.vec_column.add(VGroup(vec_cell, vec_text))
            self.key_cells.add(VGroup(key_cell, key_text))
            self.value_cells.add(VGroup(value_cell, value_text))

        self.key_header.next_to(self.key_cells.get_top(), UP)
        self.value_header.next_to(self.value_cells.get_top(), UP)
        self.add(self.background, self.key_header, self.value_header, self.key_cells, self.value_cells, self.vec_column)


    def get_table_without_stuff(self, scene):
        scene.play(Create(self.background), run_time=0.5)
        scene.play(Create(self.key_header), Create(self.value_header), run_time=0.5)