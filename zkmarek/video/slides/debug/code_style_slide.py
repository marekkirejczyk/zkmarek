from manim import VGroup, FadeIn, FadeOut, Code
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.utils import chunks


class CodeStyleSlide(SlideBase):
    def __init__(self):
        super().__init__("Font slide")

    def animate_in(self, scene):
        for styles in chunks(Code.styles_list, 12):
            group = VGroup(*[Code(
                "data/debug/example.py",
                style=s,
                font_size=12,
                background="window") for s in styles])
            group.arrange_in_grid(cols=3)
            scene.play(FadeIn(group))
            scene.wait(1)
            scene.play(FadeOut(group))


