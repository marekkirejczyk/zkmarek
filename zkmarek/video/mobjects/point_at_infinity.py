from manim import (RIGHT, Axes, Dot, FadeOut, Indicate, MathTex,
                   TransformMatchingTex, VGroup, Write)

from zkmarek.video.constant import SECONDARY_COLOR


class PointAtInfinity(VGroup):
    dot: Dot
    label: MathTex
    ax: Axes
    x: float
    y: float
    color: str

    def __init__(self, ax: Axes, x: float, y: float, label="\mathcal{O}",
        color=SECONDARY_COLOR):
        super().__init__()
        self.ax = ax
        self.x = x
        self.y = y
        self.color = color
        self.dot = Dot(ax.c2p(x, y), color=color, radius=0.05)
        self.dot.set_z_index(1, family=True)
        self.label = MathTex(label, font_size=20, color=color)
        self.add(self.dot)
        self.add(self.label)

    def animate_in(self, scene):
        self.dot.move_to(self.ax.c2p(self.x, self.y))
        self.label.next_to(self.dot, RIGHT)
        scene.play(Indicate(self.dot), Write(self.label))


    def animate_out(self, scene):
        scene.play(FadeOut(self.label))
        scene.play(FadeOut(self.dot))

    def animate_update_label(self, scene, label):
        new_label = MathTex(label, font_size=20, color=self.color)
        new_label.next_to(self.dot, RIGHT)
        scene.play(TransformMatchingTex(self.label, new_label))
        self.remove(self.label)
        self.label = new_label
        self.add(self.label)

