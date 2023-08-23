from typing import Optional

from manim import (DOWN, RIGHT, UP, AddTextLetterByLetter, Code, FadeIn,
                   FadeOut, Indicate, RemoveTextLetterByLetter,
                   ReplacementTransform, Scene, Tex, Text,
                   TransformMatchingShapes, VGroup, VMobject)
from utils import load

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.utils import find_in_code


class Sidebar(VGroup):
    label: Tex
    math: Optional[Tex] = None
    code: Optional[Code] = None
    bottom: VMobject = None

    def __init__(
        self,
        title: str,
        code_path: Optional[str] = None,
        tex_path: Optional[str] = None,
    ):
        super().__init__()
        self.label = Text(title, font=PRIMARY_FONT, color=PRIMARY_COLOR)
        self.add(self.label)

        if tex_path:
            self.math = self.create_math(tex_path)
            self.add(self.math)

        if code_path:
            self.code = self.create_code(code_path)
            self.add(self.code)
        self.align_on_border(UP)
        self.align_on_border(RIGHT)

    def create_math(self, tex_path: str):
        math = Tex(load(tex_path), font_size=28, color=PRIMARY_COLOR)
        math.next_to(self.label, DOWN, buff=0.5)
        return math

    def create_code(self, code_path: str):
        code = Code(
            file_name=code_path,
            tab_width=2,
            background="rectangle",
            language="Python",
            font="Monospace",
            font_size=14,
            margin=0.2,
            style="fruity",
            line_no_buff=0.2
        )
        self.position_code(code)
        return code

    def position_code(self, code: Code):
        if self.math is not None and self.math in self.submobjects:
            code.next_to(self.math, DOWN, buff=0.5)
        else:
            code.next_to(self.label, DOWN, buff=0.5)

    def animate_hide_code(self, scene):
        scene.play(FadeOut(self.code))
        self.remove(self.code)

    def animate_hide_math(self, scene):
        scene.play(FadeOut(self.math))
        self.remove(self.math)

    def animate_show_code(self, scene):
        self.position_code(self.code)
        scene.play(FadeIn(self.code))
        self.add(self.code)

    def animate_show_math(self, scene):
        scene.play(FadeIn(self.math))
        self.add(self.math)

    def animate_show_label(self, scene):
        scene.play(FadeIn(self.label))
        self.add(self.label)

    def animate_fast_show_math(self, scene):
        scene.play(FadeIn(self.math), FadeIn(self.label))
        self.add(self.math)
        self.add(self.label)

    def animate_in(self, scene, slide: Optional[SlideBase] = None):
        scene.play(AddTextLetterByLetter(self.label))
        if self.math is not None:
            if slide is not None:
                slide.new_subsection(scene, "Math")
            scene.play(AddTextLetterByLetter(self.math))
        if self.code is not None:
            if slide is not None:
                slide.new_subsection(scene, "Code")
            scene.play(AddTextLetterByLetter(self.code))

    def animate_out(self, scene):
        if self.code is not None and self.code in self.submobjects:
            scene.play(FadeOut(self.code))
        if self.math is not None and self.math in self.submobjects:
            scene.play(RemoveTextLetterByLetter(self.math))
        scene.play(RemoveTextLetterByLetter(self.label))

    def animate_replace_math(self, scene, tex_path: str):
        new_math = self.create_math(tex_path)
        scene.play(TransformMatchingShapes(self.math, new_math))
        self.remove(self.math)
        self.math = new_math
        self.add(self.math)

    def animate_replace_code(self, scene, code_path: str):
        new_code = self.create_code(code_path)
        scene.play(ReplacementTransform(self.code, new_code))
        self.remove(self.code)
        self.code = new_code
        self.add(self.code)

    def indicate_code(self, scene: Scene, fragment: str, index=0, run_time=0.5):
            chars = find_in_code(self.code, fragment)
            scene.play(Indicate(chars[index]), color=SECONDARY_COLOR,
                run_time=run_time)

    def math_set_color(self, start: int, end: int, color=SECONDARY_COLOR):
        self.math[0][start:end].set_color(color)


