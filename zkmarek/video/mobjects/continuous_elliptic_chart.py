from manim import (YELLOW, Axes, Create, Succession, Tex,
                   TexTemplate, VGroup, Write)

from manim.mobject.graphing.functions import ImplicitFunction

class ContinuousEllipticChart(VGroup):
    ax: Axes
    graph: ImplicitFunction

    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.ax = Axes(
            x_range=[-3, 7, 2],
            y_range=[-8, 8, 2],
            x_length=7,
            axis_config={"include_numbers": True}
        )
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{amsfonts}")
        self.labels = self.ax.get_axis_labels(
            Tex(r"$\mathbb{R}$", tex_template=template, font_size=26),
            Tex(r"$\mathbb{R}$", tex_template=template, font_size=26)
        )
        self.graph = self.ax.plot_implicit_curve(
            lambda x, y: y**2 - x**3 - 7,
            color=YELLOW
        )
        self.add(self.ax, self.labels, self.graph)

    def animate_appear(self):
        return Succession(Create(self.ax), Create(self.labels), Write(self.graph))
