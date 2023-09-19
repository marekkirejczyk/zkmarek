from typing import Optional

from manim import (DOWN, LEFT, UP, ApplyWave, Brace, FadeIn, FadeOut, Tex,
                   Text, TransformMatchingTex, VGroup, Write)

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT
from zkmarek.video.mobjects.array import Array
from zkmarek.video.slides.common.code_slide import CodeSlide


class DoubleAndAdd(CodeSlide):
    array: Optional[Array]
    equation1: Optional[Tex]
    equation2: Optional[Tex]
    label1: Optional[Tex]
    label2: Optional[Tex]
    label3: Optional[Tex]
    brace_label1: Optional[Tex]
    brace_label2: Optional[Tex]
    brace1: Brace
    brace2: Brace

    def __init__(self):
        super().__init__("Double and add", "data/ec/double_and_add.py")

    def construct(self):
        super().construct()
        self.array = Array([0,1,1,0,1,0,0,0],
            indexes=["","","","","","","",""])
        self.array.next_to(self.title_text, DOWN, buff=1)
        self.code.next_to(self.array, DOWN, buff=1)

        text = "{{64 $\cdot$ A}} + {{32 $\cdot$ A}} + {{8 $\cdot$ A}}"
        self.equation1 = Tex(text, color=PRIMARY_COLOR, font_size = 24)
        self.equation1.next_to(self.array.cells[2][0], DOWN, buff=0.2)

        text2 = "{{64 $\cdot$ A}} + {{32 $\cdot$ A}} + {{8 $\cdot$ A}} = 104 $\cdot$ A"
        self.equation2 = Tex(text2, color=PRIMARY_COLOR, font_size = 24)
        self.equation2.next_to(self.array.cells[2][0], DOWN, buff=0.2)

        self.label1 = Tex("tmp", color=PRIMARY_COLOR, font_size = 24)
        self.label2 = Tex("bit", color=PRIMARY_COLOR, font_size = 24)
        self.label3 = Tex("result", color=PRIMARY_COLOR, font_size = 24)
        self.label1.next_to(self.array.cells[0][0], LEFT + UP, buff=0.2)
        self.label2.next_to(self.array.cells[0][0], LEFT, buff=0.2)
        self.label3.next_to(self.array.cells[0][0], LEFT + DOWN, buff=0.2)

        cells = [self.array.cells[0][0], self.array.cells[7][0]]
        self.brace1 = Brace(VGroup(*cells), DOWN, buff=0, color=PRIMARY_COLOR)
        self.brace1.shift(UP)
        self.brace_label1 = Text("8 doublings", color=PRIMARY_COLOR,
            font=PRIMARY_FONT, font_size=28)
        self.brace1.put_at_tip(self.brace_label1)
        self.brace2 = Brace(self.equation2, DOWN, buff=0.2, color=PRIMARY_COLOR)
        self.brace_label2 = Text("3 additions", color=PRIMARY_COLOR,
            font=PRIMARY_FONT, font_size=28)
        self.brace2.put_at_tip(self.brace_label2)


    def animate_in(self, scene):
        self.new_subsection(scene, "Double and add",
            sound="data/sound/episode/s20-1.wav")
        scene.play(Write(self.title_text), run_time=2)
        scene.wait(3)
        scene.play(ApplyWave(self.title_text))
        scene.play(FadeIn(self.code), FadeIn(self.array),
            FadeIn(self.label2))

        self.new_subsection(scene, "Double and add",
            sound="data/sound/episode/s20-2.wav")
        scene.wait(1)
        scene.play(FadeIn(self.label1))
        for i in reversed(range(8)):
            value = f"{{{{{str(2**(8-i-1))} $\cdot$ A}}}}"
            self.array.animate_morph_index(scene, i, value)

        cells = []
        moves = []
        for i in [1, 2, 4]:
            cell = self.array.cells[i][2].copy()
            cells.append(cell)
            moves.append(cell.animate.next_to(self.array.cells[i][0],
                DOWN, buff=0.2))

        scene.play(FadeIn(self.label3), *moves)
        scene.wait(3)
        scene.play(TransformMatchingTex(VGroup(*cells), self.equation1))


        self.new_subsection(scene, "Double and add",
            sound="data/sound/episode/s20-3.wav")
        scene.wait(3)
        scene.play(TransformMatchingTex(self.equation1, self.equation2))

        fadeouts1 = [FadeOut(cell[0]) for cell in self.array.cells]
        fadeouts2 = [FadeOut(cell[1]) for cell in self.array.cells]
        scene.play(FadeOut(self.label1), FadeOut(self.label2),
            FadeOut(self.label3), FadeOut(self.code), *fadeouts1, *fadeouts2)

        scene.play(FadeIn(self.brace1), FadeIn(self.brace_label1))
        scene.play(FadeIn(self.brace2), FadeIn(self.brace_label2))

    def animate_out(self, scene):
        fadeouts = [FadeOut(cell[2]) for cell in self.array.cells]
        scene.play(FadeOut(self.equation2), FadeOut(self.title_text),
            FadeOut(self.brace1), FadeOut(self.brace2),
            FadeOut(self.brace_label1), FadeOut(self.brace_label2),
            *fadeouts)

