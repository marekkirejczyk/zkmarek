from manim import Text, VGroup, FadeIn, FadeOut
from zkmarek.video.slides.common.slide_base import SlideBase
import manimpango
from zkmarek.video.utils import chunks

class FontSlide(SlideBase):
    def __init__(self):
        super().__init__("Font slide")

    def animate_in(self, scene):
        for sublist in chunks(manimpango.list_fonts(), 50):
            group = VGroup(*[Text(f, font=f, font_size=20) for f in sublist])
            group.arrange_in_grid(cols=4)
            scene.play(FadeIn(group))
            scene.wait(1)
            scene.play(FadeOut(group))
