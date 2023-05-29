from manim import DOWN, UP, Tex, Text, Unwrite, Write, TexTemplate

from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.utils import load


class TexSlide(SlideBase):
    title_text: Text
    tex: Tex

    def __init__(self, title: str, tex_path: str, **kwargs):
        super().__init__(title)
        self.title_text = Text(title)
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[normalem]{ulem}")
        self.tex = Tex(load(tex_path), tex_template=template, **kwargs)
        self.title_text.to_edge(UP)
        self.tex.next_to(self.title_text, DOWN)

    def animate_in(self, scene):
        scene.play(Write(self.title_text))
        scene.play(Write(self.tex))

    def animate_out(self, scene):
        scene.play(Unwrite(self.title_text))
        scene.play(Unwrite(self.tex))
