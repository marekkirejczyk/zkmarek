from typing import Optional

from manim import (DOWN, RIGHT, UP, Code, ReplacementTransform, Tex, VGroup,
                   VMobject, Write)
from utils import load


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
        VGroup.__init__(self)
        self.label = Tex(title)
        self.add(self.label)
        self.bottom = self.label
        if tex_path:
            self.math = self.create_math(tex_path)
            self.add(self.math)
            self.bottom = self.math
        if code_path:
            self.code = self.create_sidebar(code_path)
            self.add(self.code)
        self.align_on_border(UP)
        self.align_on_border(RIGHT)

    def create_math(self, tex_path):
        math = Tex(load(tex_path), font_size=32)
        math.next_to(self.label, DOWN, buff=0.5)
        return math

    def create_sidebar(self, code_path):
        code = Code(
            file_name=code_path,
            tab_width=2,
            background="rectangle",
            language="Python",
            font="Monospace",
            font_size=14,
        )
        code.next_to(self.bottom, DOWN, buff=0.5)
        return code

    def animate_respectively(self, scene):
        scene.play(Write(self.label))
        if self.math is not None:
            scene.play(Write(self.math))
        if self.code is not None:
            scene.play(Write(self.code))

    def animate_replace_code(self, scene, code_path: str):
        new_code = self.create_sidebar(code_path)
        scene.play(ReplacementTransform(self.code, new_code))
        self.remove(self.code)
        self.code = new_code
        self.add(self.code)
