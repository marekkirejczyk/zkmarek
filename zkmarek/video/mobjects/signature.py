from manim import DOWN, LEFT, Create, Line, Rectangle, Text, VGroup, Write

from zkmarek.video.constant import SECONDARY_COLOR


class Signature(VGroup):
    def __init__(self, height=3, color=SECONDARY_COLOR):
        super().__init__()
        width=height*3
        self.rect = Rectangle(width=width, height=height, color=color)
        start = 0.45 * width * LEFT + 0.25 * height * DOWN
        end = -0.45 * width * LEFT + 0.25 * height * DOWN
        self.line = Line(start, end, color=color)
        self.text = Text("Signature", font="Zapfino", color=color).shift(
            DOWN * height * 0.2)
        self.text.scale(height*2/3)
        self.add(self.rect, self.line, self.text)

    def animate_in(self, scene):
        scene.play(Create(self.rect))
        scene.play(Create(self.line))
        scene.play(Write(self.text))
