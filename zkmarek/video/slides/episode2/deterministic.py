from manim import (
    DOWN,
    UP,
    Tex,
    Text,
    TexTemplate,
    TransformMatchingShapes,
    Unwrite,
    Write,
    Indicate,
    FadeIn,
)
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, HIGHLIGHT_COLOR

from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.utils import load


class Deterministic(SlideBase):
    title_text: Text
    tex: Tex
    tex_below: Tex
    tex_path: str
    kwargs: dict
    template: TexTemplate

    def __str__(self):
        return f"{self.title} (MATH)"

    def __init__(self):
        super().__init__("Deterministic signature")
        self.tex_path = "data/ec/deterministic_signature.tex"

    def construct(self):
        self.title_text = Text(self.title, color=PRIMARY_COLOR, font=PRIMARY_FONT)
        self.template = TexTemplate()
        self.template.add_to_preamble(r"\usepackage[normalem]{ulem}")
        self.tex = Tex(
            load(self.tex_path), tex_template=self.template, color=PRIMARY_COLOR
        )
        self.title_text.to_edge(UP)
        self.tex.next_to(self.title_text, DOWN, buff=1)

    def animate_replace_tex(self, scene, path):
        tex2 = Tex(load(path), tex_template=self.template, color=PRIMARY_COLOR)
        tex2.next_to(self.title_text, DOWN, buff=1)
        scene.play(TransformMatchingShapes(self.tex, tex2))
        scene.remove(self.tex)
        self.tex = tex2

    def animate_in(self, scene):
        self.new_subsection(
            scene, "deterministic signature", "data/sound/episode2/slide8-0.mp3"
        )
        scene.play(FadeIn(self.title_text))
        scene.play(Write(self.tex[0][0:17]))
        self.play_sound(scene, "data/sound/episode2/slide8-1.mp3")
        self.play_sound(scene, "data/sound/episode2/slide8-2.mp3")
        scene.play(Write(self.tex[0][17:57]))
        self.play_sound(scene, "data/sound/episode2/slide8-3.mp3")
        scene.play(Write(self.tex[0][57:101]))
        scene.play(Indicate(self.tex[0][71:75]), color=HIGHLIGHT_COLOR)

    def animate_out(self, scene):
        scene.play(Unwrite(self.title_text))
        scene.play(Unwrite(self.tex))
