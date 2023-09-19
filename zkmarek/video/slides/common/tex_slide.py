from manim import (DOWN, UP, Tex, Text, TexTemplate, TransformMatchingShapes,
                   Unwrite, Write)
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT

from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.utils import load


class TexSlide(SlideBase):
    title_text: Text
    tex: Tex
    tex_below: Tex
    tex_path: str
    kwargs: dict
    template: TexTemplate

    def __str__(self):
        return f"{self.title} (MATH)"

    def __init__(self, title: str, tex_path: str, **kwargs):
        super().__init__(title)
        self.tex_path = tex_path
        self.kwargs = kwargs

    def construct(self):
        self.title_text = Text(self.title, color=PRIMARY_COLOR,
            font=PRIMARY_FONT)
        self.template = TexTemplate()
        self.template.add_to_preamble(r"\usepackage[normalem]{ulem}")
        self.tex = Tex(load(self.tex_path), tex_template=self.template,
            color=PRIMARY_COLOR)
        self.title_text.to_edge(UP)
        self.tex.next_to(self.title_text, DOWN, buff=1)

    def animate_replace_tex(self, scene, path):
        tex2 = Tex(load(path), tex_template=self.template,
            color=PRIMARY_COLOR)
        tex2.next_to(self.title_text, DOWN, buff=1)
        scene.play(TransformMatchingShapes(self.tex, tex2))
        scene.remove(self.tex)
        self.tex = tex2

    def animate_in(self, scene):
        scene.play(Write(self.title_text))
        scene.play(Write(self.tex))

    def animate_out(self, scene):
        scene.play(Unwrite(self.title_text))
        scene.play(Unwrite(self.tex))
