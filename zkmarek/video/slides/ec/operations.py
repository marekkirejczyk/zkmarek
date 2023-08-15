from manim import DOWN, FadeIn, Tex, TransformMatchingTex, Write

from zkmarek.video.constant import SECONDARY_COLOR
from zkmarek.video.slides.common.tex_slide import TexSlide
from zkmarek.video.utils import load


class Operations(TexSlide):
    def __init__(self):
        super().__init__("Discrete Elliptic Curves operations",
            "data/ec/operations1.tex")


    def animate_replace_tex(self, scene, path):
        tex2 = Tex(load(path), tex_template=self.template,
            color=SECONDARY_COLOR)
        tex2.next_to(self.title_text, DOWN, buff=1)
        scene.play(TransformMatchingTex(self.tex, tex2))
        scene.remove(self.tex)
        self.tex = tex2


    def animate_in(self, scene):
        self.new_subsection(scene, "Operations",
            sound="data/sound/episode/s22-1.wav")
        scene.play(Write(self.title_text))
        scene.play(FadeIn(self.tex))
        scene.wait(0.8)
        self.tex[0][0:12].set_color(SECONDARY_COLOR)
        scene.wait(0.5)
        self.tex[0][12:25].set_color(SECONDARY_COLOR)
        scene.wait(0.5)
        self.tex[0][25:38].set_color(SECONDARY_COLOR)
        scene.wait(3)
        self.tex[0][38:54].set_color(SECONDARY_COLOR)

        self.new_subsection(scene, "Operations",
            sound="data/sound/episode/s22-2.wav")
        self.new_subsection(scene, "Operations",
            sound="data/sound/episode/s22-3.wav")
        self.animate_replace_tex(scene, "data/ec/operations2.tex")
        self.new_subsection(scene, "Operations",
            sound="data/sound/episode/s22-4.wav")
        scene.wait(5)
        self.animate_replace_tex(scene, "data/ec/operations3.tex")
        self.new_subsection(scene, "Operations",
            sound="data/sound/episode/s22-5.wav")
        scene.wait(4)

