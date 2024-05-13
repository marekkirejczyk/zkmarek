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
        scene.wait(3)
        scene.play(Indicate(self.tex[0][71:75]), color=HIGHLIGHT_COLOR, run_time=1)
        scene.play(Indicate(self.tex[0][76:86]), color=HIGHLIGHT_COLOR, run_time=1)
        scene.play(Indicate(self.tex[0][92:99]), color=HIGHLIGHT_COLOR, run_time=1)
        scene.wait(8.5)
        self.play_sound(scene, "data/sound/episode2/slide8-4.mp3")
        scene.play(Write(self.tex[0][101:128]), run_time=0.5)
        scene.wait(2.5)
        scene.play(Indicate(self.tex[0][102:103]), color=HIGHLIGHT_COLOR, run_time=0.5)
        scene.play(Indicate(self.tex[0][106:109]), color=HIGHLIGHT_COLOR, run_time=0.5)
        scene.wait(2)
        self.play_sound(scene, "data/sound/episode2/slide8-5.mp3")
        scene.wait(4)
        scene.play(Write(self.tex[0][128:]))
        scene.wait(3)

    def animate_out(self, scene):
        scene.play(Unwrite(self.title_text))
        scene.play(Unwrite(self.tex))
