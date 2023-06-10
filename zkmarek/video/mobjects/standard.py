from manim import LEFT, RIGHT, UP, Create, MathTex, MobjectTable, VGroup


class Standard(MobjectTable):

    def __init__(self, name, equation, p, g, n, h):
        super().__init__(
            [
                [Standard.create_row_with_pair("Name", name, "Equation", equation)],
                [Standard.create_row("Order\,p =", p)],
                [Standard.create_row("Base\,point\,G_x =", g)],
                [Standard.create_row("Order\,of\,G\,n=", n)],
                [Standard.create_row("Cofactor", h)],
            ],
            include_outer_lines=True,
            v_buff=0.2,
            h_buff=0.2,
            arrange_in_grid_config={"col_alignments": "l"},
            line_config={"stroke_width": 1}
        )

    def animate_in(self, scene):
        scene.play(Create(self))

    @staticmethod
    def create_row_with_pair(caption1, val1, caption2, val2):
        left = Standard.create_row(caption1, val1)
        right = Standard.create_row(caption2, val2)
        right.next_to(left, RIGHT)
        return VGroup(left, right)

    @staticmethod
    def create_row(caption, val):
        label = MathTex(caption, font_size=16)
        value = MathTex(val, font_size=26)
        label.next_to(value, UP, buff=0.1)
        label.align_to(value, LEFT)
        value.align_to(value, LEFT)
        return VGroup(label, value)


def secp256k1_standard():
    return Standard(
        "Secp256k1",
        "y^2 = x^3 + 7",
        "p = 2^{256} - 2^{32} - 2^9 - 2^8 - 2^7 - 2^6 - 2^4 - 1",
        "02\enspace 79BE667E\enspace F9DCBBAC\enspace ... \enspace D0364141",
        "FFFFFFFF\enspace FFFFFFFF\enspace ...\enspace BFD25E8C",
        "h = 1",
    )

def curve25519_standard():
    return Standard(
        "Curve25519",
        "y^2 = x^3 + 486662x^2 + x",
        "p = 2^{255}-19",
        "G_x = 9",
        " {2^{252}+27742317777372353535851937790883648493",
        "h = 8",
    )
