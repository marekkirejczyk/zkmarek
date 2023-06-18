from manim import LEFT, MathTex, SurroundingRectangle, Text, VGroup
from zkmarek.video.utils import into_groups


class EquationBoxWithIcons(VGroup):
    rectangle: SurroundingRectangle

    def __init__(self, *mobjects, **kwargs):
        super().__init__(*mobjects, **kwargs)
        self.arrange_in_grid(cols=2, cell_alignment=LEFT)
        self.rectangle = SurroundingRectangle(self, buff=0.2, corner_radius=0.1)
        self.add(self.rectangle)
        self.rectangle.set_center(self.get_center())
        self.scale(0.65)

    @staticmethod
    def create(*arg_list):
        result = []
        for three in into_groups(arg_list, 3):
            result.append(Text(three[0], color=three[2]))
            result.append(MathTex(three[1], color=three[2]))
        return EquationBoxWithIcons(*result)

class EquationBox(VGroup):
    rectangle: SurroundingRectangle

    def __init__(self, *equations):
        super().__init__(*[MathTex(eq) for eq in equations])
        self.arrange_in_grid(cols=1, cell_alignment=LEFT)
        self.rectangle = SurroundingRectangle(self, buff=0.2, corner_radius=0.1)
        self.add(self.rectangle)
        self.rectangle.set_center(self.get_center())
        self.scale(0.65)
