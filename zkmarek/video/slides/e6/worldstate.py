from manim import Table, Text, VGroup, LEFT, Write, Create, RIGHT, UP, FadeOut, GREEN_D
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT

class SimplifiedWorldState(VGroup):
    def __init__(self, keys_data=None, font_size=32):
        super().__init__()
        self.keys_data = keys_data
        self.font_size = font_size
        
    def construct(self):
        self.keys_data = [
            ["a", "7", "1", "1", "3", "5", "5"],  
            ["a", "7", "7", "d", "3", "3", "7"],  
            ["a", "7", "f", "9", "3", "6", "5"],  
            ["a", "7", "7", "d", "3", "9", "7"],  
        ]
        values_data = ["45.0 ETH", "1.00 WEI", "1.1 ETH", "0.12 ETH"] 

        self.keys_table = Table(
            self.keys_data,
            include_outer_lines=True,
        ).scale(0.5).scale(0.5).set_color(GREEN_D)

        self.values_table = Table(
            [[value] for value in values_data],
            include_outer_lines=True,
        ).scale(0.5).scale(0.5).set_color(GREEN_D)
            
        self.keys_table.shift(LEFT * 3).shift(RIGHT*7+UP*1)
        self.values_table.next_to(self.keys_table, RIGHT, buff=0.1)
        
        self.keys_header = Text("Keys", font = PRIMARY_FONT).scale(0.5).next_to(self.keys_table, UP).scale(0.5)
        self.values_header = Text("Values", font = PRIMARY_FONT).scale(0.5).next_to(self.values_table, UP).scale(0.5)

        self.title = Text("Simplified World State", font = PRIMARY_FONT, color = PRIMARY_COLOR).scale(0.7).next_to(self.keys_header, UP, buff = 0.0).scale(0.5).shift(RIGHT*0.4)
        
        
    def show_table(self, scene, runtime=1):
        scene.play(Write(self.title), Create(self.keys_table), Create(self.values_table), Write(self.keys_header), Write(self.values_header), run_time = runtime)

        # scene.wait()

    def remove_table(self, scene):
        scene.play(FadeOut(*[self.title, self.keys_table, self.values_table, self.keys_header, self.values_header]))
