from manim import Table, VGroup, Text, UP, RIGHT, LEFT, DOWN
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, HIGHLIGHT_COLOR

class TableKeyValue(VGroup):
    def __init__(self):
        super().__init__()
        
        self.keys_values_data = [
            ["'TRIE'",  "7"],  
            ["'TRAN'",  "9"],  
            ["'TOW'",   "1"],  
            ["'TOKEN'", "7"],  
        ]

        self.keys_table = Table(
            self.keys_values_data,
            include_outer_lines=True,
            element_to_mobject=lambda text: Text(text, font=PRIMARY_FONT) 
        ).set_color(HIGHLIGHT_COLOR).scale(0.7)
        
        self.keys_header = Text("Keys", font = PRIMARY_FONT, font_size = 30, color=PRIMARY_COLOR).next_to(self.keys_table, UP).shift(LEFT*1.2+DOWN*0.05)
        self.values_header = Text("Values", font = PRIMARY_FONT, font_size = 30, color=PRIMARY_COLOR).next_to(self.keys_table, UP).shift(RIGHT*1.2)
        
        self.add(self.keys_table, self.keys_header, self.values_header)
