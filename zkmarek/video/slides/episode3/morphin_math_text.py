from typing import List

from manim import MathTex, Scene, TransformMatchingTex, Unwrite, VGroup, Write

from zkmarek.video.constant import SECONDARY_COLOR


class MorphinMathText(VGroup):
    texts: List[str]
    texs: List[MathTex]

    def __init__(self, texts: List[str]):
        super().__init__()
        self.texts = texts

        self.texs = []
        for tex in texts:
            math_tex = MathTex(tex, font_size=40, color=SECONDARY_COLOR)
            self.texs.append(math_tex)
            self.add(math_tex)

    def animate_in(self, scene: Scene):
        self.animate_first(scene)
        self.animate_rest(scene)

    def animate_out(self, scene: Scene):
        scene.play(Unwrite(self.texs[-1]))

    def animate_first(self, scene: Scene):
        scene.play(Write(self.texs[0]))

    def animate_rest(self, scene: Scene):
        for i in range(0, len(self.texs) - 1):
            scene.play(TransformMatchingTex(self.texs[i], self.texs[i+1]))

    def animate_next(self, scene: Scene, i):
        scene.play(TransformMatchingTex(self.texs[i], self.texs[i+1]))
