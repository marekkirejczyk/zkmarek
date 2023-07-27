from manim import RIGHT, Axes, Create, Dot, MathTex, VGroup, Write

from zkmarek.crypto.cec_affine import CECAffine
from zkmarek.video.constant import HIGHLIGHT_COLOR


class DotOnCurve(VGroup):
    label: MathTex
    ax: Axes
    dot: Dot
    lines: VGroup

    p: CECAffine
    include_lines: bool
    include_coords: bool
    label_direction: int

    def __init__(
        self,
        ax: Axes,
        label: str,
        p: CECAffine,
        include_lines: bool= False,
        include_coords: bool = False,
        label_direction=RIGHT,
    ):
        super().__init__()
        self.ax = ax
        self.include_lines = include_lines
        self.label_direction = label_direction

        text = (
            r"{}({:.4f}, {:.4f})".format(label, p.x, p.y) if include_coords else label
        )
        self.dot = Dot(ax.coords_to_point(p.x, p.y), color=HIGHLIGHT_COLOR)
        self.add(self.dot)

        if include_lines:
            self.lines = ax.get_lines_to_point(ax.c2p(p.x, p.y))
            self.add(self.lines)
        self.label = MathTex(text, font_size=30, color=HIGHLIGHT_COLOR)
        self.add(self.label)
        self.set_p(p)
        self.set_z_index(2, family=True)

    def set_p(self, p):
        self.p = p
        self.dot.move_to(self.ax.coords_to_point(p.x, p.y))
        self.label.next_to(self.dot, self.label_direction)

    def animate_in(self, scene):
        scene.play(Create(self.dot))
        if self.include_lines:
            scene.play(Create(self.lines))
        scene.play(Write(self.label))

    def to_coord(self):
        return self.ax.c2p(self.p.x, self.p.y)
