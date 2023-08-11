from manim import MathTex, TexTemplate

from zkmarek.video.slides.common.slide_base import SlideBase


class TestSlide(SlideBase):
    def __init__(self):
        super().__init__("Test slide")

    def animate_in(self, scene):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{MnSymbol}")

        self.add(MathTex(r"order \approx 2^{256}", font_size=32, tex_template=template))



