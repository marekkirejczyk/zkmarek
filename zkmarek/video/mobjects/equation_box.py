from manim import LEFT, MathTex, SurroundingRectangle, Text, VGroup
from zkmarek.video.constant import PRIMARY_COLOR
from zkmarek.video.utils import chunks


class EquationBoxWithIcons(VGroup):
    rectangle: SurroundingRectangle

    def __init__(self, *mobjects, **kwargs):
        super().__init__(*mobjects, **kwargs)
        self.arrange_in_grid(cols=2, cell_alignment=LEFT)
        self.rectangle = SurroundingRectangle(self, buff=0.2,
            corner_radius=0.1, color=PRIMARY_COLOR)
        self.add(self.rectangle)
        self.rectangle.set_center(self.get_center())
        self.scale(0.65)

    @staticmethod
    def create(*arg_list):
        result = []
        for three in chunks(arg_list, 3):
            result.append(Text(three[0], color=three[2]))
            result.append(MathTex(three[1], color=three[2]))
        return EquationBoxWithIcons(*result)

class EquationBox(VGroup):
    rectangle: SurroundingRectangle

    def __init__(self, *eqs):
        super().__init__(*[MathTex(eq, color=PRIMARY_COLOR) for eq in eqs])
        self.arrange_in_grid(cols=1, cell_alignment=LEFT)
        self.rectangle = SurroundingRectangle(self, buff=0.2,
            corner_radius=0.1, color=PRIMARY_COLOR)
        self.add(self.rectangle)
        self.rectangle.set_center(self.get_center())
        self.scale(0.65)
