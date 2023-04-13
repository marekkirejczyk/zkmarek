from manim import *
from src.utils import load

class Sidebar(VGroup):
    def __init__(self, ax, title, code_filename=None, tex_filename=None):
        VGroup.__init__(self)
        label = Tex(title)
        self.add(label)
        bottom = label
        if code_filename:
            code = Code(file_name=code_filename, tab_width=2, background="rectangle",
                language="Python", font="Monospace", font_size=15)
            code.next_to(bottom, DOWN, buff=0.5)
            bottom = code
            self.add(code)
        if tex_filename:
            tex = Tex(load(tex_filename))
            tex.next_to(bottom, DOWN, buff=0.5)
            self.add(tex)
        self.next_to(ax, RIGHT, buff=0.5)
        self.align_on_border(UP)
