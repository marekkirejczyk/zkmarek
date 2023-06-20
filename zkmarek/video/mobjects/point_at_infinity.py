from manim import (GREEN, RIGHT, Axes, Create, Dot, FadeOut, Flash, MathTex,
                   VGroup)


class PointAtInfinity(VGroup):
    dot: Dot
    label: MathTex
    ax: Axes
    x: float
    y: float

    def __init__(self, ax: Axes, x: float, y: float, label="\infty"):
        super().__init__()
        self.ax = ax
        self.x = x
        self.y = y
        self.dot = Dot(ax.c2p(x, y), color=GREEN, radius=0.05)
        self.dot.set_z_index(1, family=True)
        self.label = MathTex(label, font_size=20)
        self.add(self.dot)
        self.add(self.label)

    def animate_in(self, scene):
        self.dot.move_to(self.ax.c2p(self.x, self.y))
        self.label.next_to(self.dot, RIGHT)
        scene.play(Create(self.dot))
        scene.play(Create(self.label))
        scene.play(Flash(self.dot))

    def animate_out(self, scene):
        scene.play(FadeOut(self.label))
        scene.play(FadeOut(self.dot))
