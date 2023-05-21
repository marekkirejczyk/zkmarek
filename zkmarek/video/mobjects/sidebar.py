from typing import Optional

from manim import (DOWN, RIGHT, UP, Code, FadeIn, FadeOut, Unwrite,
                   ReplacementTransform, Tex, VGroup, VMobject, Write)
from utils import load
from zkmarek.video.slides.slide_base import SlideBase


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
        self.label = Tex(title)
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
        math = Tex(load(tex_path), font_size=28)
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
            style="github-dark",
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

    def animate_appear(self, scene, slide: Optional[SlideBase] = None):
        scene.play(Write(self.label))
        if self.math is not None:
            if slide is not None:
                slide.new_subsection(scene, "Math")
            scene.play(Write(self.math))
        if self.code is not None:
            if slide is not None:
                slide.new_subsection(scene, "Code")
            scene.play(Write(self.code))

    def animate_disappear(self, scene):
        if self.code is not None and self.code in self.submobjects:
            scene.play(Unwrite(self.code))
        if self.math is not None and self.math in self.submobjects:
            scene.play(Unwrite(self.math))
        scene.play(Unwrite(self.label))

    def animate_replace_math(self, scene, tex_path: str):
        new_math = self.create_math(tex_path)
        scene.play(ReplacementTransform(self.math, new_math))
        self.remove(self.math)
        self.math = new_math
        self.add(self.math)

    def animate_replace_code(self, scene, code_path: str):
        new_code = self.create_code(code_path)
        scene.play(ReplacementTransform(self.code, new_code))
        self.remove(self.code)
        self.code = new_code
        self.add(self.code)
