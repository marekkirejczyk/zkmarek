from manim import MathTex, TexTemplate
from zkmarek.video.constant import PRIMARY_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase

class TestSlide(SlideBase):
    def __init__(self):
        super().__init__("Test slide")

    def animate_in(self, scene):
        template = TexTemplate()

        template.add_to_preamble(r"\usepackage{MnSymbol,bm}")
        tex = MathTex(r"{{Order}} \approx 2^{256}",
            color=PRIMARY_COLOR,
            tex_template=template)

        self.add(tex)


