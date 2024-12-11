from manim import Axes, Create, SingleStringMathTex, TexTemplate, VGroup, Write
from manim.mobject.graphing.functions import ImplicitFunction

from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR


class ContinuousEllipticChart(VGroup):
    ax: Axes
    graph: ImplicitFunction
    include_details: bool

    def __init__(self, include_details=True, b=None, curve_color = SECONDARY_COLOR, **kwargs):
        super().__init__(**kwargs)
        self.include_details = include_details
        self.b = 7 if None else b
        step = 2 if include_details else 20
        self.ax = Axes(
            x_range=[-3, 7, step],
            y_range=[-8, 8, step],
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
            lambda x, y: y**2 - x**3 - self.b,
            color=curve_color
        )
        self.add(self.ax)
        if include_details:
            self.labels = self.ax.get_axis_labels(
                SingleStringMathTex(r"\mathbb{R}", tex_template=template,
                    font_size=26, color=PRIMARY_COLOR),
                SingleStringMathTex(r"\mathbb{R}", tex_template=template,
                    font_size=26, color=PRIMARY_COLOR)
            )
            self.add(self.labels)
        self.add(self.graph)

    def animate_in(self, scene):
        if self.include_details:
            scene.play(Create(self.ax), Create(self.labels))
        else:
            scene.play(Create(self.ax))
        scene.play(Write(self.graph))
