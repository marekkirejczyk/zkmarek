from typing import Optional

from manim import (DOWN, ApplyWave, FadeIn, FadeOut, Tex, TransformMatchingTex,
                   VGroup, Write)

from zkmarek.video.constant import PRIMARY_COLOR
from zkmarek.video.mobjects.array import Array
from zkmarek.video.slides.common.code_slide import CodeSlide

# TODO
# Scalar mi

class DoubleAndAdd(CodeSlide):
    array: Optional[Array]
    equation: Optional[Tex]

    def __init__(self):
        super().__init__("Double and add", "data/ec/double_and_add.py")

    def animate_in(self, scene):
        self.new_subsection(scene, "Double and add",
            sound="data/sound/episode/s19-1.wav")
        scene.play(Write(self.title_text), run_time=2)
        scene.wait(3)
        scene.play(ApplyWave(self.title_text))
        scene.play(FadeIn(self.code))


        self.array = Array([0,1,1,0,1,0,0,0],
            indexes=["128","64","32","16","8","4","2","1"])
        self.array.next_to(self.code, DOWN, buff=0.6)
        scene.play(FadeIn(self.array))

        self.new_subsection(scene, "Double and add",
            sound="data/sound/episode/s19-2.wav")

        scene.wait(1)
        for i in reversed(range(8)):
            self.array.animate_morph_index(scene, i, f"{{{str(2**(8-i-1))} $\cdot$ A}}")

        cells = []
        moves = []
        for i in [1, 2, 4]:
            cell = self.array.cells[i][2].copy()
            cells.append(cell)
            moves.append(cell.animate.next_to(self.array.cells[i][0],
                DOWN, buff=0.2))

        scene.play(*moves)
        scene.wait(1)
        text = "{{64 $\cdot$ A}} + {{32 $\cdot$ A}} + {{8 $\cdot$ A}} = 104 $\cdot$ A"
        self.equation = Tex(text, color=PRIMARY_COLOR, font_size = 24)
        self.equation.next_to(self.array.cells[3][0], DOWN, buff=0.2)

        scene.wait(1)
        scene.play(TransformMatchingTex(VGroup(*cells), self.equation))

        self.new_subsection(scene, "Double and add",
            sound="data/sound/episode/s19-3.wav")

        scene.wait(5)

    def animate_out(self, scene):
        scene.play(FadeOut(self.code))
        scene.play(FadeOut(self.title_text))
        scene.play(FadeOut(self.array), FadeOut(self.equation))
