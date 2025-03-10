from manim import Table, Text, VGroup, LEFT, Write, Create, RIGHT, UP, FadeOut, Indicate, MoveToTarget
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, HIGHLIGHT_COLOR

class SimplifiedWorldState(VGroup):
    def __init__(self, keys_data=None, font_size=32):
        super().__init__()
        self.keys_data = keys_data
        self.font_size = font_size
        
    def construct(self):
        self.keys_data = [
            ["a", "7", "1", "1", "3", "5", "5"],  
            ["a", "7", "f", "9", "3", "6", "5"],  
            ["a", "7", "7", "d", "3", "3", "7"],  
            ["a", "7", "7", "d", "3", "8", "7"],  
        ]
        values_data = ["45.0 ETH", "1.00 WEI", "1.1 ETH", "0.12 ETH"] 

        self.keys_table = Table(
            self.keys_data,
            include_outer_lines=True,
        ).scale(0.5).set_color(HIGHLIGHT_COLOR)

        self.values_table = Table(
            [[value] for value in values_data],
            include_outer_lines=True,
        ).scale(0.5).set_color(HIGHLIGHT_COLOR)
            
        self.keys_table.shift(LEFT * 1.2)
        self.values_table.next_to(self.keys_table, RIGHT, buff=0.1)
        
        self.keys_header = Text("Keys", font = PRIMARY_FONT).scale(0.5).next_to(self.keys_table, UP)
        self.values_header = Text("Values", font = PRIMARY_FONT).scale(0.5).next_to(self.values_table, UP)

        self.title = Text("Simplified World State", font = PRIMARY_FONT, color = PRIMARY_COLOR).scale(0.75).next_to(self.keys_header, UP, buff = 0.0).shift(RIGHT*0.7)
        
        self.table = VGroup(self.keys_table, self.values_table, self.keys_header, self.values_header, self.title)
        
    def show_table(self, scene, runtime=1):
        scene.play(Write(self.title), Create(self.keys_table), Create(self.values_table), Write(self.keys_header), Write(self.values_header), run_time = runtime)


    def remove_table(self, scene):
        scene.play(FadeOut(*[self.title, self.keys_table, self.values_table, self.keys_header, self.values_header]))


    def appear_table(self, scene):
        scene.play(Create(self.title), Create(self.keys_table), Create(self.values_table), Create(self.keys_header), Create(self.values_header))
        scene.wait(0.5)
        scene.play(Indicate(self.keys_table, color = PRIMARY_COLOR))
        scene.play(Indicate(self.values_table, color = HIGHLIGHT_COLOR))
        scene.wait(1.5)
        self.table.generate_target()
        self.table.target.shift(RIGHT*4.7+UP*1).scale(0.6)
        scene.play(MoveToTarget(self.table))