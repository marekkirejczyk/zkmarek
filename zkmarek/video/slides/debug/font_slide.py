from manim import Text, VGroup, FadeIn, FadeOut
from zkmarek.video.slides.common.slide_base import SlideBase
import manimpango

class FontSlide(SlideBase):
    def __init__(self):
        super().__init__("Font slide")


    def animate_in(self, scene):
        list = manimpango.list_fonts()
        n = 50
        for i in range(len(list) // n+1):
            sublist = list[i*n:(i+1)*n]
            group = VGroup(*[Text(f, font=f, font_size=20) for f in sublist])
            group.arrange_in_grid(cols=4)
            scene.play(FadeIn(group))
            scene.wait(1)
            scene.play(FadeOut(group))
