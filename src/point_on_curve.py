from manim import *

class PointOnCurve(VGroup):
    def __init__(self, ax, label, p, color=GREEN):
        VGroup.__init__(self)
        text = r"{}({:.4f}, {:.4f})".format(label, p.x, p.y)
        self.point = Dot(ax.coords_to_point(p.x, p.y), color=GREEN)
        self.lines = ax.get_lines_to_point(ax.c2p(p.x, p.y))
        self.label = MathTex(text, font_size=30).next_to(self.point, RIGHT)
        self.add(self.point, self.lines, self.label)

    def animate_appear(self):
        return [Write(self.lines), Create(self.point), Write(self.label)]
