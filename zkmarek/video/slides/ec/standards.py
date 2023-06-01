from manim import FadeIn, FadeOut, MathTex, MobjectTable, UP, VGroup, LEFT, Text, DOWN

from zkmarek.video.slides.common.slide_base import SlideBase


class Standard(MobjectTable):

    def __init__(self, name, equation, p, g, n, h):
        super().__init__(
            [
                [Standard.create_cell("Name", name)],
                [Standard.create_cell("Equation", equation)],
                [Standard.create_cell("Order\,p =", p)],
                [Standard.create_cell("Base\,point\,G_x =", g)],
                [Standard.create_cell("Order\,of\,G\,n=", n)],
                [Standard.create_cell("Cofactor", h)],
            ],
            include_outer_lines=True,
            v_buff=0.2,
            h_buff=0.2,
            arrange_in_grid_config={"col_alignments": "l"},
            line_config={"stroke_width": 1}
        )

    @staticmethod
    def create_cell(caption, val):
        label = MathTex(caption, font_size=16)
        value = MathTex(val, font_size=26)
        label.next_to(value, UP, buff=0.1)
        label.align_to(value, LEFT)
        value.align_to(value, LEFT)
        return VGroup(label, value)

class Standards(SlideBase):
    secp256k1: Standard
    curve25519: Standard
    alt_BN128: Standard
    label: Text
    group: VGroup

    def __init__(self):
        super().__init__("Standards")
        self.title = "Standards"

    def construct(self):
        self.secp256k1 = Standard(
            "Secp256k1",
            "y^2 = x^3 + 7",
            "p = 2^{256} - 2^{32} - 2^9 - 2^8 - 2^7 - 2^6 - 2^4 - 1",
            "02\enspace 79BE667E\enspace F9DCBBAC\enspace ... \enspace D0364141",
            "FFFFFFFF\enspace FFFFFFFF\enspace ...\enspace BFD25E8C",
            "h = 1",
        )
        self.curve25519 = Standard(
            "Curve25519",
            "y^2 = x^3 + 486662x^2 + x",
            "p = 2^{255}-19",
            "G_x = 9",
            " {2^{252}+27742317777372353535851937790883648493",
            "h = 8",
        )
        self.label = Text(self.title)
        self.label.to_edge(UP)
        self.group = VGroup(self.secp256k1, self.curve25519).arrange_in_grid(cols=2)
        self.group.next_to(self.label, DOWN)

    def animate_in(self, scene):
        scene.play(FadeIn(self.label))
        scene.play(FadeIn(self.secp256k1))
        scene.play(FadeIn(self.curve25519))

    def animate_out(self, scene):
        scene.play(FadeOut(self.secp256k1))
