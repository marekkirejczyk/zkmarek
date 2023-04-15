from manim import *

class ContinuousEllipticChart(VGroup):
    ax = None

    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.ax = Axes(
            x_range=[-5, 7, 2],
            y_range=[-8, 8, 2],
            x_length=7,
            axis_config={"include_numbers": True}
        )
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{amsfonts}")
        self.labels = self.ax.get_axis_labels(
            Tex(r"$\mathbb{R}$", tex_template=myTemplate, font_size=26),
            Tex(r"$\mathbb{R}$", tex_template=myTemplate, font_size=26)
        )
        self.graph = self.ax.plot_implicit_curve(
            lambda x, y: y**2 - x**3 - 7,
            color=YELLOW
        )
        self.add(self.ax, self.labels, self.graph)

    def animate_appear(self):
        return [Create(self.ax), Create(self.labels), Write(self.graph)]

