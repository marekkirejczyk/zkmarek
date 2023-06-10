from manim import YELLOW, Axes, Create, Tex, TexTemplate, VGroup, Write
from manim.mobject.graphing.functions import ImplicitFunction


class ContinuousEllipticChart(VGroup):
    ax: Axes
    graph: ImplicitFunction
    include_details: bool

    def __init__(self, include_details=True, **kwargs):
        super().__init__(**kwargs)
        self.include_details = include_details
        step = 2 if include_details else 20
        self.ax = Axes(
            x_range=[-3, 7, step],
            y_range=[-8, 8, step],
            x_length=7,
            axis_config={"include_numbers": include_details}
        )
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{amsfonts}")
        self.graph = self.ax.plot_implicit_curve(
            lambda x, y: y**2 - x**3 - 7,
            color=YELLOW
        )
        self.add(self.ax)
        if include_details:
            self.labels = self.ax.get_axis_labels(
                Tex(r"$\mathbb{R}$", tex_template=template, font_size=26),
                Tex(r"$\mathbb{R}$", tex_template=template, font_size=26)
            )
            self.add(self.labels)
        self.add(self.graph)

    def animate_in(self, scene):
        scene.play(Create(self.ax))
        if self.include_details:
            scene.play(Create(self.labels))
        scene.play(Write(self.graph))
