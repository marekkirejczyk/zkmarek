from manim import UP, RIGHT, DOWN, VGroup, Tex, Code
from utils import load

class Sidebar(VGroup):
    def __init__(self, title, code_filename=None, tex_filename=None):
        VGroup.__init__(self)
        label = Tex(title)
        self.add(label)
        bottom = label
        if tex_filename:
            tex = Tex(load(tex_filename), font_size=32)
            tex.next_to(bottom, DOWN, buff=0.5)
            self.add(tex)
            bottom = tex
        if code_filename:
            code = Code(file_name=code_filename, tab_width=2, background="rectangle",
                language="Python", font="Monospace", font_size=14)
            code.next_to(bottom, DOWN, buff=0.5)
            self.add(code)
        self.align_on_border(UP)
        self.align_on_border(RIGHT)
