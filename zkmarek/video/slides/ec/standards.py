from manim import FadeIn, FadeOut, MathTex, MobjectTable, UP, VGroup, LEFT

from zkmarek.video.slides.common.slide_base import SlideBase


class Standards(SlideBase):
    secp256k1: MobjectTable

    def __init__(self):
        super().__init__("Standards")
        self.title = "Standards"

    def create_cell(self, caption, val):
        label = MathTex(caption, font_size=16)
        value = MathTex(val, font_size=26)
        label.next_to(value, UP, buff=0.1)
        label.align_to(value, LEFT)
        value.align_to(value, LEFT)
        return VGroup(label, value)

    def create_standard(self, name, equation, p, g, n, h):
        return MobjectTable(
            [
                [self.create_cell("Name", name)],
                [self.create_cell("Equation", equation)],
                [self.create_cell("Order\,p =", p)],
                [self.create_cell("Base\,point\,G =", g)],
                [self.create_cell("Order\,of\,G\,n=", n)],
                [self.create_cell("Cofactor", h)],
            ],
            include_outer_lines=True,
            v_buff=0.2,
            h_buff=0.2,
            arrange_in_grid_config={"col_alignments": "l"},
            line_config={"stroke_width": 1}
        )

    def construct(self):
        self.secp256k1 = self.create_standard(
            "Secp256k1",
            "y^2 = x^3 + 7",
            "p = 2^{256} - 2^{32} - 2^9 - 2^8 - 2^7 - 2^6 - 2^4 - 1",
            "02\enspace 79BE667E\enspace F9DCBBAC\enspace ... \enspace D0364141",
            "FFFFFFFF\enspace FFFFFFFF\enspace ...\enspace BFD25E8C",
            "h = 01",
        )
        self.secp256k1.align_on_border(UP + LEFT)


    def animate_in(self, scene):
        scene.play(FadeIn(self.secp256k1))

    def animate_out(self, scene):
        scene.play(FadeOut(self.secp256k1))
