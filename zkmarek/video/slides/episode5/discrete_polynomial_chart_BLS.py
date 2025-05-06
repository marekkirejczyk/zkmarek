from manim import Axes, Dot, VGroup, TexTemplate, Tex, DashedLine, GrowFromPoint, Line, MathTex
from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.crypto.weierstrass_curve import BLS12381
from zkmarek.video.constant import SECONDARY_COLOR, PRIMARY_COLOR, HIGHLIGHT_COLOR
from zkmarek.crypto.field_element import FieldElement

class DotOnCurve(Dot):
    coords: ECAffine

    def __init__(self, ax: Axes, coords: ECAffine, color=SECONDARY_COLOR):
        super().__init__(
            ax.c2p(float(coords.x.value), float(coords.y.value)),
            color=color,
            radius=0.05
        )
        self.coords = coords
        
class PolynomialOnCurve(VGroup):
    def __init__(self, curve=BLS12381, dot_color=SECONDARY_COLOR, include_numbers = True, label = None):
        super().__init__()
        self.curve = curve
        self.dots = []
        self.label = curve.p if None else label
        self.dot_color = dot_color
        self.dots = []
        if self.curve.p>10:
            self.ax = Axes(
                x_range=[0, curve.p, 10],
                y_range=[0, curve.p, 10],
                x_length=7,
                axis_config={"include_numbers": include_numbers},
            )
        else:
            self.ax = Axes(
                x_range=[0, curve.p, 1],
                y_range=[0, curve.p, 1],
                x_length=7,
                axis_config={"include_numbers": include_numbers},
            )
        self.ax.color = PRIMARY_COLOR
        self.add(self.ax)

        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{amsfonts}")
        field_label = r"$\mathbb{F}_{" + str(self.label) + "}$"
        self.labels = self.ax.get_axis_labels(
            Tex(field_label, tex_template=template, font_size=42, color=PRIMARY_COLOR),
            Tex(field_label, tex_template=template, font_size=42, color=PRIMARY_COLOR),
        )
        self.add(self.labels)
        self.gen_points()

    def gen_points(self):
        points = ECAffine.generate_points(self.curve)
        for p in points:
            dot = DotOnCurve(self.ax, p, color=self.dot_color).scale(1.5)
            dot.set_z_index(10, family=True)
            self.dots.append(dot)
            self.add(dot)
                
    def get_point(self, x: FieldElement, sgn: int = 0):
        point = ECAffine.from_x(x.value, sgn, self.curve)

        if point is None:
            return None 

        dot = Dot(self.ax.c2p(float(point.x.value), float(point.y.value)), color=HIGHLIGHT_COLOR)
        dot.set_z_index(10, family=True)
        return dot



    def animate_create_vertical_line(self, scene, x, y_top, run_time=1):
        s = self.ax.c2p(x, -1)
        e = self.ax.c2p(x, y_top)
        line = Line(s, e, color=SECONDARY_COLOR, z_index=0)
        scene.play(GrowFromPoint(line, point=s), run_time=run_time)
        return line

    def animate_create_horizontal_line(self, scene, y, x_left, x_right, run_time=1):
        s = self.ax.c2p(x_left, y)
        e = self.ax.c2p(x_right, y)
        line = DashedLine(s, e, color=SECONDARY_COLOR, z_index=0)
        scene.play(GrowFromPoint(line, point=s), run_time=run_time)
        return line
    
    def add_xaxis_label(self, x, label):
        label = MathTex(label, color=PRIMARY_COLOR)
        label.move_to(self.ax.coords_to_point(x, -9))
        self.add(label)
        return label
    
    def add_yaxis_label(self, y, label):
        label = MathTex(label, color=PRIMARY_COLOR)
        label.move_to(self.ax.coords_to_point(-9, y))
        self.add(label)