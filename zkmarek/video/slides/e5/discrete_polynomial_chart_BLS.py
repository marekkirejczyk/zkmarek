from manim import Axes, Dot, VGroup, TexTemplate, Tex
from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.crypto.weierstrass_curve import BLS12381
from zkmarek.video.constant import SECONDARY_COLOR, PRIMARY_COLOR


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
    def __init__(self, curve=BLS12381, polynomial=None, dot_color=SECONDARY_COLOR):
        """
        Initialize the PolynomialOnCurve visualization.
        :param curve: WeierstrassCurve instance (e.g., BLS12381)
        :param polynomial: A callable representing the polynomial (e.g., lambda x: x**2 + x + 1)
        :param dot_color: The color of the dots representing points
        """
        super().__init__()
        self.curve = curve
        self.polynomial = polynomial
        self.dots = []
        self.dot_color = dot_color
        self.dots = []
        if self.curve.p>10:
            self.ax = Axes(
                x_range=[0, curve.p, 10],
                y_range=[0, curve.p, 10],
                x_length=7,
                axis_config={"include_numbers": True},
            )
        else:
            self.ax = Axes(
                x_range=[0, curve.p, 1],
                y_range=[0, curve.p, 1],
                x_length=7,
                axis_config={"include_numbers": True},
            )
        self.ax.color = PRIMARY_COLOR
        self.add(self.ax)

        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{amsfonts}")
        field_label = r"$\mathbb{F}_{" + str(curve.p) + "}$"
        self.labels = self.ax.get_axis_labels(
            Tex(field_label, tex_template=template, font_size=32, color=PRIMARY_COLOR),
            Tex(field_label, tex_template=template, font_size=32, color=PRIMARY_COLOR),
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


