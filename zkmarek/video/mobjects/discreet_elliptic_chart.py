from manim import (LEFT, Axes, Create, Dot, FadeIn, FadeOut, Line, Tex,
                   TexTemplate, VGroup)
from numpy import ndarray

from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.crypto.weierstrass_curve import Secp256k1_41, WeierstrassCurve
from zkmarek.video.constant import (BACKGROUND_COLOR, PRIMARY_COLOR,
                                    SECONDARY_COLOR)
from zkmarek.video.mobjects.point_at_infinity import PointAtInfinity


class DotOnCurve(Dot):
    coords: ECAffine

    def __init__(self, ax: Axes, coords: ECAffine, color=SECONDARY_COLOR):
        super().__init__(
            ax.c2p(float(coords.x.value), float(coords.y.value)),
            color=color,
            radius=0.05
        )
        self.coords = coords

class DiscreteEllipticChart(VGroup):
    curve: WeierstrassCurve
    dots: list[Dot]
    ax: Axes
    point_at_infinity: PointAtInfinity
    dot_color: str

    def __init__(self, curve=Secp256k1_41, include_details=True,
        dot_color=SECONDARY_COLOR):
        super().__init__()
        self.dots = []
        self.curve = curve
        self.point_at_infinity = None
        self.dot_color = dot_color
        step = 5 if include_details else 500
        self.ax = Axes(
            x_range=[0, curve.p + 1, step],
            y_range=[0, curve.p + 1, step],
            x_length=7,
            axis_config={"include_numbers": True}
        )
        self.ax.color = PRIMARY_COLOR
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{amsfonts}")
        self.add(self.ax)
        if include_details:
            field_label = r"$\mathbb{F}_{" + str(curve.p) + "}$"
            self.labels = self.ax.get_axis_labels(
                Tex(field_label, tex_template=template,
                    font_size=26, color=dot_color),
                Tex(field_label, tex_template=template,
                    font_size=26, color=dot_color),
            )
            self.add(self.labels)
        self.set_z_index(1, family=True)
        self.gen_points()

    def create_point_at_infinity(self, x, y, label="\mathcal{O}", dot_color=None):
        color = dot_color if dot_color is not None else self.dot_color
        if self.point_at_infinity is None:
            self.point_at_infinity = PointAtInfinity(self.ax, x, y, label, color=color)
            self.add(self.point_at_infinity)
        else:
            self.point_at_infinity.move_to(self.ax.c2p(x, y))

    def gen_points(self):
        points = ECAffine.generate_points(self.curve)
        for p in points:
            dot = DotOnCurve(self.ax, p, color=self.dot_color)
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

    def animate_in(self, scene) -> None:
        scene.play(Create(self))

    def animate_out(self, scene) -> None:
        scene.play(FadeOut(self))

    def create_horizontal_line(self):
        mid_y = self.curve.p / 2
        s = self.ax.c2p(-1, mid_y)
        e = self.ax.c2p(self.curve.p, mid_y)
        return Line(s, e, color=BACKGROUND_COLOR, z_index=0)

    def create_vertical_line(self, x):
        s = self.ax.c2p(x, -1)
        e = self.ax.c2p(x, self.curve.p)
        return Line(s, e, color=BACKGROUND_COLOR, z_index=0)

    def animate_add(self, scene, *mobjects, animation_class=FadeIn,
        run_time=1):
        self.add(*mobjects)
        scene.play(animation_class(*mobjects), run_time=run_time)

    def animate_remove(self, scene, *mobject, animation_class=FadeOut):
        scene.play(animation_class(*mobject))
        self.remove(*mobject)

    def animate_align_left(self, scene, run_time=1):
        scene.play(self.animate.align_on_border(LEFT, buff=0.2), run_time=run_time)

    def animate_align_center(self, scene):
        scene.play(self.animate.center())
