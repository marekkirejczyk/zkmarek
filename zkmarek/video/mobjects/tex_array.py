from manim import RIGHT, MathTex, Rectangle, TransformMatchingShapes, VGroup

from zkmarek.video.constant import (BACKGROUND_COLOR, PRIMARY_COLOR,
                                    SECONDARY_COLOR)


class TexCell(VGroup):
    def __init__(self, value, width=2):
        super().__init__()
        text = MathTex(str(value), z_index=1,
            color=SECONDARY_COLOR)
        rectangle = Rectangle(
            color = PRIMARY_COLOR,
            fill_color = BACKGROUND_COLOR,
            fill_opacity = 1,
            width = width,
            height = 1
        )
        self.add(rectangle, text)

    def animate_transform_matching_shapes(self, scene, value):
        tex2 = MathTex(str(value), z_index=1,
            color=SECONDARY_COLOR)
        tex2.move_to(self[0])
        scene.play(TransformMatchingShapes(self[1], tex2), run_time=0.4)
        scene.remove(self[1])
        self.remove(self[1])
        self.add(tex2)

class TexArray(VGroup):
    cells: list[TexCell]
    def __init__(self, values, widths=None):
        super().__init__()
        self.cells = []
        default_width=2
        widths = widths or [default_width] * len(values)
        for i, (value, width) in enumerate(zip(values, widths)):
            cell = TexCell(value, width)
            self.cells.append(cell)
            self.add(cell)
        self.arrange(RIGHT, buff=0) 


    def arrange_cells(self):
        self.arrange(RIGHT, buff=0)

    def animate_transform_matching_shapes(self, scene, values):
        for index, cell in enumerate(self.cells):
            cell.animate_transform_matching_shapes(scene, values[index])
