from manim import *

class PointOnCurve(VGroup):
    def __init__(self, ax, label, p, include_lines=False, include_coords=False, label_direction=RIGHT):
        VGroup.__init__(self)
        self.ax = ax
        self.p = p
        self.include_lines = include_lines

        text = r"{}({:.4f}, {:.4f})".format(label, p.x, p.y) if include_coords else label
        self.point = Dot(ax.coords_to_point(p.x, p.y), color=GREEN)
        self.add(self.point)
        if include_lines:
            self.lines = ax.get_lines_to_point(ax.c2p(p.x, p.y))
            self.add(self.lines)
        self.label = MathTex(text, font_size=30).next_to(self.point, label_direction)
        self.add(self.label)

    def animate_appear(self):
        result = [Create(self.point)]
        if self.include_lines:
            result.append(Create(self.lines))
        result.append(Write(self.label))
        return result

    def to_coord(self):
        return self.ax.c2p(self.p.x, self.p.y)
