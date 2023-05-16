from typing import Optional

from manim import DOWN, RIGHT, UP, Code, Tex, VGroup, Write
from utils import load


class Sidebar(VGroup):
    label: Tex
    math: Optional[Tex] = None
    code: Optional[Code] = None

    def __init__(self, title, code_path=None, tex_path=None):
        VGroup.__init__(self)
        self.label = Tex(title)
        self.add(self.label)
        bottom = self.label
        if tex_path:
            self.math = Tex(load(tex_path), font_size=32)
            self.math.next_to(bottom, DOWN, buff=0.5)
            self.add(self.math)
            bottom = self.math
        if code_path:
            self.code = Code(
                file_name=code_path,
                tab_width=2,
                background="rectangle",
                language="Python",
                font="Monospace",
                font_size=14,
            )
            self.code.next_to(bottom, DOWN, buff=0.5)
            self.add(self.code)
        self.align_on_border(UP)
        self.align_on_border(RIGHT)

    def animate_respectively(self, scene):
        scene.play(Write(self.label))
        if self.math is not None:
            scene.play(Write(self.math))
        if self.code is not None:
            scene.play(Write(self.code))
