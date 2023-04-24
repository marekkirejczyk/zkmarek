from manim import *
from crypto.field import Field

def secp256k1(x, y):
    return y**2 - x**3 - 7

class DiscreetEllipticChart(VGroup):
    def __init__(self, prime=19, equation=secp256k1):
        VGroup.__init__(self)
        self.equation = equation
        self.prime = prime

        self.ax = Axes(
            x_range=[0, prime+1, 5],
            y_range=[0, prime+1, 2],
            x_length=7,
            axis_config={"include_numbers": True},
        )
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{amsfonts}")
        field_label = r"$\mathbb{F}_{" + str(prime) + "}$"
        self.labels = self.ax.get_axis_labels(
            Tex(field_label, tex_template=template, font_size=26),
            Tex(field_label, tex_template=template, font_size=26)
        )
        self.add(self.ax)
        self.add(self.labels)
        self.gen_points()

    def gen_points(self):
        for (x, y) in [(x, y) for x in range(0, self.prime+1) for y in range(0, self.prime+1)]:
            if self.equation(Field(x, self.prime), Field(y, self.prime)) == Field(0, self.prime):
                self.add(Dot(self.ax.c2p(x, y), color=YELLOW))

    def animate_appear(self):
        return Create(self)

    def animate_disappear(self):
        return FadeOut(self)
