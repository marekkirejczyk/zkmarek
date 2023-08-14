from manim import RIGHT, UP, Square, Tex, Text, TransformMatchingShapes, VGroup

from zkmarek.video.constant import (BACKGROUND_COLOR, PRIMARY_COLOR,
                                    PRIMARY_FONT, SECONDARY_COLOR)


class Cell(VGroup):
    def __init__(self, value, index=None):
        super().__init__()
        square = Square(
            color = PRIMARY_COLOR,
            fill_color = BACKGROUND_COLOR,
            fill_opacity = 1,
            side_length = 1,
        )
        text = Text(str(value), z_index=1, font=PRIMARY_FONT,
            color=SECONDARY_COLOR)
        self.add(square, text)
        if index is not None:
            index = Tex(str(index), z_index=1, font_size = 24,
                color=PRIMARY_COLOR)
            index.next_to(square, UP, buff=0.2)
            self.add(index)

class Array(VGroup):
    cells: list[Cell]
    def __init__(self, values, indexes=[]):
        super().__init__()
        self.cells = []
        for i, value in enumerate(values):
            index = indexes[i] if len(indexes) > i else None
            cell = Cell(value, index=index)
            self.cells.append(cell)
            self.add(cell)
        self.arrange(RIGHT, buff=0)

    def animate_morph_index(self, scene, i, value):
        cell = self.cells[i]
        tex2 = Tex(value, color=PRIMARY_COLOR, font_size = 24)
        tex2.next_to(cell[0], UP, buff=0.2)
        scene.play(TransformMatchingShapes(cell[2], tex2), run_time=0.4)
        scene.remove(cell[2])
        cell.remove(cell[2])
        cell.add(tex2)
