from manim import Axes, Tex, TexTemplate, VGroup, Dot, Create, FadeOut, YELLOW
from zkmarek.crypto.ec_point_affine import ECPointAffine
from zkmarek.crypto.field import Field
from zkmarek.crypto.weierstrass_curve import Secp256k1_41, WeierstrassCurve


def secp256k1(x, y):
    return y**2 - x**3 - 7


class DiscreetEllipticChart(VGroup):
    curve: WeierstrassCurve

    def __init__(self, curve=Secp256k1_41):
        VGroup.__init__(self)
        self.curve = curve

        self.ax = Axes(
            x_range=[0, curve.p + 1, 5],
            y_range=[0, curve.p + 1, 5],
            x_length=7,
            axis_config={"include_numbers": True},
        )
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{amsfonts}")
        field_label = r"$\mathbb{F}_{" + str(curve.p) + "}$"
        self.labels = self.ax.get_axis_labels(
            Tex(field_label, tex_template=template, font_size=26),
            Tex(field_label, tex_template=template, font_size=26),
        )
        self.add(self.ax)
        self.add(self.labels)
        self.gen_points()

    def gen_points(self):
        points = ECPointAffine.generate_points(self.curve)
        for p in points:
            self.add(Dot(self.ax.c2p(p.x.value, p.y.value), color=YELLOW))

    def animate_appear(self):
        return Create(self)

    def animate_disappear(self):
        return FadeOut(self)
