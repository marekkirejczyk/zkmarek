from manim import VGroup, Text, RIGHT, LEFT, DOWN, UP, RoundedRectangle, Create
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, HIGHLIGHT_COLOR

class TableKZGIPA(VGroup):
    def __init__(self):
        super().__init__()

        vec_commitment_column = ["   vector\n elements", "proof", "commitment" ,
                                 "      trusted setup", " require\n pairings"]
        kzg_values = [ "   scalar\n     field \n element", "1 EC point","1 EC point", 
                      "Yes", "Yes"]
        
        ipa_values = ["   scalar\n     field \n element", "1 EC point", "  2log2(n)\n EC points", 
                      "No", "No"]
        
        sizes_kzg = ["<32 B", "<48 B", "<48 B"]
        sizes_ipa = ["<32 B", "<32 B", "each\n<32 B"]

        cell_width = 2.4
        cell_height = 0.8
        corner_radius = 0.2
        spacing = 0.1 
        num_rows = len(kzg_values)

        bg_width = (cell_width * 3) + 1.5
        bg_height = (cell_height + spacing) * num_rows + 1.2
        self.background = RoundedRectangle(
            width=bg_width,
            height=bg_height,
            corner_radius=0.3,
            color=PRIMARY_COLOR,
            fill_opacity=0.2,
            stroke_width = 0.0
        )

        self.key_header = Text("KZG (BLS12-381)", font=PRIMARY_FONT, font_size=23, color=PRIMARY_COLOR)
        self.value_header = Text("IPA (Bandersnatch)", font=PRIMARY_FONT, font_size=22, color=PRIMARY_COLOR)


        self.key_cells = VGroup()
        self.value_cells = VGroup()
        self.vec_column = VGroup()
        self.sizes_kzg = VGroup()
        self.sizes_ipa = VGroup()

        for i, (vec_column, key, value) in enumerate(zip(vec_commitment_column, kzg_values, ipa_values)):
            if i <3:
                size_kzg = sizes_kzg[i]
                size_ipa = sizes_ipa[i]
            
            key_cell = RoundedRectangle(
                width=cell_width,
                height=cell_height,
                corner_radius=corner_radius,
                fill_opacity=0.3,
                color=PRIMARY_COLOR,
                stroke_width = 0.0
            ).move_to(self.background.get_top()).shift(DOWN * (i + 1.5) * (cell_height + spacing))
            
            key_cell_ec_scalar = RoundedRectangle(
                width=cell_width*20/33,
                height=cell_height,
                corner_radius=corner_radius,
                fill_opacity=0.3,
                color=PRIMARY_COLOR,
                stroke_width = 0.0
            ).move_to(self.background.get_top()).shift(DOWN * (i + 1.5) * (cell_height + spacing)+LEFT*0.4)
            
            key_cell_size = RoundedRectangle(
                width=cell_width*10/33,
                height=cell_height,
                corner_radius=corner_radius,
                fill_opacity=0.3,
                color=PRIMARY_COLOR,
                stroke_width = 0.0
            ).move_to(self.background.get_top()).shift(DOWN * (i + 1.5) * (cell_height + spacing))

            if i < 3:
                key_cell_true = key_cell_ec_scalar
                size_kzg_cell = key_cell_size.copy().next_to(key_cell_true, RIGHT, buff = 0.1)
                value_cell_true = key_cell_ec_scalar.copy().next_to(size_kzg_cell, RIGHT, buff = 0.33).shift(RIGHT * 0.2)
                size_ipa_cell = key_cell_size.copy().next_to(value_cell_true, RIGHT, buff = 0.1)

            else:
                key_cell_true = key_cell
                value_cell_true = key_cell.copy().shift(RIGHT * (cell_width + 0.3)+RIGHT * 0.2)
                
            vec_cell = key_cell.copy().shift(LEFT * (cell_width + 0.3)).set_color(HIGHLIGHT_COLOR)
            vec_text = Text(vec_column, font=PRIMARY_FONT, font_size=23, color=HIGHLIGHT_COLOR).move_to(vec_cell)
            key_text = Text(key, font=PRIMARY_FONT, font_size=18, color=PRIMARY_COLOR).move_to(key_cell_true)
            value_text = Text(value, font=PRIMARY_FONT, font_size=18, color=PRIMARY_COLOR).move_to(value_cell_true)
            size_kzg_text = Text(size_kzg, font=PRIMARY_FONT, font_size=20, color=PRIMARY_COLOR).move_to(size_kzg_cell)
            size_ipa_text = Text(size_ipa, font=PRIMARY_FONT, font_size=20, color=PRIMARY_COLOR).move_to(size_ipa_cell)
            
            self.vec_column.add(VGroup(vec_cell, vec_text))
            self.key_cells.add(VGroup(key_cell_true, key_text))
            self.value_cells.add(VGroup(value_cell_true, value_text))
            self.sizes_kzg.add(VGroup(size_kzg_cell, size_kzg_text))
            self.sizes_ipa.add(VGroup(size_ipa_cell, size_ipa_text))

        self.key_header.next_to(self.key_cells.get_top(), UP)
        self.value_header.next_to(self.value_cells.get_top(), UP)
        self.add(self.background, self.key_header, self.value_header, self.key_cells, self.value_cells, 
                 self.vec_column, self.sizes_kzg, self.sizes_ipa)


    def get_table_without_stuff(self, scene):
        scene.play(Create(self.background), run_time=0.5)
        scene.play(Create(self.key_header), Create(self.value_header), run_time=0.5)