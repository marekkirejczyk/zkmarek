from manim import Text, RIGHT, FadeIn, Rectangle, WHITE, BLACK
from zkmarek.video.slides.common.slide_base import SlideBase

class Intro(SlideBase):
    zk: Text
    marek: Text
    rectangle: Rectangle

    def __init__(self):
        super().__init__("Intro")

    def construct(self):
        self.rectangle = Rectangle(width=0.6, height=0.6,
            fill_color=WHITE, fill_opacity=1, color=WHITE)
        self.zk = Text("zk", color=BLACK)
        self.marek = Text("Marek")
        self.marek.next_to(self.zk, RIGHT, buff=0.05)

    def animate_in(self, scene):
        # scene.play(self.zk.animate.shift(2 * RIGHT))
        scene.play(FadeIn(self.rectangle))
        scene.play(FadeIn(self.zk))
        scene.play(FadeIn(self.marek))
