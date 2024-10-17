from manim import Axes, Dot, GrowFromPoint, Line, MathTex, Tex, TexTemplate, VGroup, Indicate, DashedLine, FadeOut

from zkmarek.crypto.field_element import FieldElement
from zkmarek.video.constant import HIGHLIGHT_COLOR, PRIMARY_COLOR, SECONDARY_COLOR


class DiscreetePolynomialChart(VGroup):
    dots: list[Dot]
    ax: Axes
    p: int

    def __init__(self, p, f):
        super().__init__()
        self.f = f
        self.p = p
        self.dots = []
        if self.p>10:
            self.ax = Axes(
                x_range=[0, p, 10],
                y_range=[0, p, 10],
                x_length=7,
                axis_config={"include_numbers": True},
            )
        else:
            self.ax = Axes(
                x_range=[0, p, 1],
                y_range=[0, p, 1],
                x_length=7,
                axis_config={"include_numbers": True},
            )
        self.ax.color = PRIMARY_COLOR
        self.add(self.ax)

        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{amsfonts}")
        field_label = r"$\mathbb{F}_{" + str(self.p) + "}$"
        self.labels = self.ax.get_axis_labels(
            Tex(field_label, tex_template=template, font_size=26, color=PRIMARY_COLOR),
            Tex(field_label, tex_template=template, font_size=26, color=PRIMARY_COLOR),
        )
        self.add(self.labels)

    def gen_points(self):
        for i in range(0, self.p):
            x = FieldElement(i, self.p)
            y = self.f(x)
            dot = Dot(self.ax.coords_to_point(x.value, y.value), color=HIGHLIGHT_COLOR)
            dot.set_z_index(10, family=True)
            self.dots.append(dot)
            self.add(dot)

    def indicate_point(self, scene, value_at_x):
        for i in range(0, self.p):
            x = FieldElement(i, self.p)
            y = self.f(x)
            dot = Dot(self.ax.coords_to_point(x.value, y.value), color=HIGHLIGHT_COLOR)
            dot.set_z_index(10, family=True)

            if x == value_at_x:
                scene.play(Indicate(dot, scale_factor=3))
                scene.play(FadeOut(dot))


    def gen_points2(self):
        for i in range(0, self.p):
            x = FieldElement(i, self.p)
            y = self.f(x)
            dot = Dot(self.ax.coords_to_point(x.value, y.value), color=SECONDARY_COLOR)
            dot.set_z_index(10, family=True)
            self.dots.append(dot)
            self.add(dot)

    def add_xaxis_label(self, x, label):
        label = MathTex(label, color=PRIMARY_COLOR)
        label.move_to(self.ax.coords_to_point(x, -3))
        self.add(label)
        return label
    
    def indicate_xaxis_label(self, scene, label):
        scene.play(Indicate(label, scale_factor=1.7, color=HIGHLIGHT_COLOR))

    def add_yaxis_label(self, y, label):
        label = MathTex(label, color=PRIMARY_COLOR)
        label.move_to(self.ax.coords_to_point(-5.5, y))
        self.add(label)

    def animate_create_vertical_line(self, scene, x, y_top):
        s = self.ax.c2p(x, -1)
        e = self.ax.c2p(x, y_top)
        line = Line(s, e, color=SECONDARY_COLOR, z_index=0)
        scene.play(GrowFromPoint(line, point=s))
        return line

    def animate_create_horizontal_line(self, scene, y, x_left, x_right):
        s = self.ax.c2p(x_left, y)
        e = self.ax.c2p(x_right, y)
        line = DashedLine(s, e, color=SECONDARY_COLOR, z_index=0)
        scene.play(GrowFromPoint(line, point=s))
        scene.wait(1)
        return line
    
    def animate_shift_dots(self, scene, y_shift):
        animations = []
        for i, d in enumerate(self.dots):
            x = FieldElement(i, self.p)
            y = self.f(x)
            yy = y.value - y_shift
            if yy >= 0:
                a = d.animate.move_to(self.ax.c2p(x.value, yy))
                animations.append(a)
        scene.play(*animations)

    def animate_shift_dots_wrap_fix(self, scene, y_shift):
        animations = []
        for i, d in enumerate(self.dots):
            x = FieldElement(i, self.p)
            y = self.f(x)
            yy = y.value - y_shift
            if yy < 0:
                animations.append(d.animate.move_to(self.ax.c2p(x.value, yy % self.p)))
        scene.play(*animations)
        for d in self.dots:
            if d.get_fill_opacity() < 1:
                d.set_fill(opacity=1)
                
    def animate_shift_dots_with_fade(self, scene, y_shift):
        animations = []
        for i, d in enumerate(self.dots):
            x = FieldElement(i, self.p)
            y = self.f(x)
            yy = y.value - y_shift
            if yy >= 0:
                animations.append(d.animate.move_to(self.ax.c2p(x.value, yy)))
            else:
                animations.append(d.animate.move_to(self.ax.c2p(x.value, yy)).set_opacity(0.4))

    
        scene.play(*animations)

