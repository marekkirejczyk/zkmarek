from manim import Axes, Create, SingleStringMathTex, TexTemplate, VGroup, Write
from manim.mobject.graphing.functions import ImplicitFunction

from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR, HIGHLIGHT_COLOR


class Chart(VGroup):
    ax: Axes
    graph: ImplicitFunction
    include_details: bool

    def __init__(self, include_details=True, **kwargs):
        super().__init__(**kwargs)
        self.include_details = include_details
        step = 10 if include_details else 20
        self.ax = Axes(
            x_range=[-4.7, 5, step],
            y_range=[-5.5, 42, step],
            x_length=7,
            axis_config={
                "include_numbers": include_details,
                "color": PRIMARY_COLOR,
                "decimal_number_config": {
                    "color": PRIMARY_COLOR,
                    "num_decimal_places": 0
                }
            }
        )
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{amsfonts}")
        self.graph = self.ax.plot_implicit_curve(
            lambda x, y: 4*x**3 - 8*x**2 - 17*x +30 - y,
            color=SECONDARY_COLOR
        )
        self.graph2 = self.ax.plot_implicit_curve(
            lambda x, y: x**3 +x**2 - 2*x + 8 - y,
            color=HIGHLIGHT_COLOR
        )
        self.graph3 = self.ax.plot_implicit_curve(
            lambda x, y: 3*x**3 - 9*x**2 - 15*x + 22 - y,
            color=PRIMARY_COLOR
        )
        self.add(self.ax)
        if include_details:
            self.labels = self.ax.get_axis_labels(
                SingleStringMathTex(r"x", tex_template=template,
                    font_size=56, color=PRIMARY_COLOR),
                SingleStringMathTex(r"y", tex_template=template,
                    font_size=56, color=PRIMARY_COLOR)
            )
            self.add(self.labels)
        self.add(self.graph)
        self.add(self.graph2)
        self.add(self.graph3)

    def animate_in(self, scene):
        if self.include_details:
            scene.play(Create(self.ax), Create(self.labels))
        else:
            scene.play(Create(self.ax))
        scene.play(Write(self.graph))
        scene.play(Write(self.graph2))
        scene.play(Write(self.graph3))
