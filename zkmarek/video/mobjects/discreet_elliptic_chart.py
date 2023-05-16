from manim import Axes, Tex, TexTemplate, VGroup, Dot, Create, FadeOut, YELLOW
from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.crypto.weierstrass_curve import Secp256k1_41, WeierstrassCurve


class DotOnCurve(Dot):
    point: ECAffine

    def __init__(self, ax: Axes, p: ECAffine):
        super(DotOnCurve, self).__init__(
            ax.c2p(float(p.x.value), float(p.y.value)), color=YELLOW
        )
        self.point = p


class DiscreetEllipticChart(VGroup):
    curve: WeierstrassCurve
    dots: list[Dot] = []
    ax: Axes

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
        points = ECAffine.generate_points(self.curve)
        for p in points:
            dot = DotOnCurve(self.ax, p)
            self.dots.append(dot)
            self.add(dot)

    def animate_appear(self):
        return Create(self)

    def animate_disappear(self):
        return FadeOut(self)
