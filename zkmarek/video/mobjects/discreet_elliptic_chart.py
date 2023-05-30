from manim import (DARK_GREY, LEFT, YELLOW, Axes, Create, Dot, FadeIn, FadeOut,
                   Line, Tex, TexTemplate, VGroup)
from numpy import ndarray

from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.crypto.weierstrass_curve import Secp256k1_41, WeierstrassCurve


class DotOnCurve(Dot):
    coords: ECAffine

    def __init__(self, ax: Axes, p: ECAffine):
        super().__init__(
            ax.c2p(float(p.x.value), float(p.y.value)), color=YELLOW, radius=0.05
        )
        self.coords = p


class DiscreteEllipticChart(VGroup):
    curve: WeierstrassCurve
    dots: list[Dot] = []
    ax: Axes

    def __init__(self, curve=Secp256k1_41):
        super().__init__()
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
        self.set_z_index(1, family=True)
        self.gen_points()

    def gen_points(self):
        points = ECAffine.generate_points(self.curve)
        for p in points:
            dot = DotOnCurve(self.ax, p)
            dot.set_z_index(10, family=True)
            self.dots.append(dot)
            self.add(dot)

    def find_dot_by_affine(self, p: ECAffine) -> DotOnCurve:
        return next(filter(lambda d: d.coords == p, self.dots))

    def find_dots_by_x(self, x) -> list[DotOnCurve]:
        return list(filter(lambda d: d.coords.x.value == x, self.dots))

    def find_affine_by_x(self, x: int, odd: int) -> list[ECAffine]:
        return list(map(lambda d: d.coords, self.find_dots_by_x(x)))[odd]

    def affine_to_point(self, p: ECAffine) -> ndarray:
        return self.ax.c2p(p.x.value, p.y.value)

    def animate_appear(self, scene) -> None:
        scene.play(Create(self))

    def animate_disappear(self, scene) -> None:
        scene.play(FadeOut(self))

    def create_horizontal_line(self):
        mid_y = self.curve.p / 2
        s = self.ax.c2p(-1, mid_y)
        e = self.ax.c2p(self.curve.p, mid_y)
        return Line(s, e, color=DARK_GREY, z_index=0)

    def create_vertical_line(self, x):
        s = self.ax.c2p(x, -1)
        e = self.ax.c2p(x, self.curve.p)
        return Line(s, e, color=DARK_GREY, z_index=0)

    def animate_add(self, scene, *mobjects, animation_class=FadeIn):
        self.add(*mobjects)
        scene.play(animation_class(*mobjects))

    def animate_remove(self, scene, *mobject, animation_class=FadeOut):
        scene.play(animation_class(*mobject))
        self.remove(*mobject)

    def animate_align_left(self, scene):
        scene.play(self.animate.align_on_border(LEFT, buff=0.2))

    def animate_align_center(self, scene):
        scene.play(self.animate.center())
