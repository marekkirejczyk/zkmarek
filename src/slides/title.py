from manim import *

class TitleSlide(VGroup):
    def __init__(self) -> None:
        VGroup.__init__(self)
        self.title = Text("Elliptic Curves")
        pass

    def animate_in(self):
        return [Write(self.title)]

    def animate_out(self):
        return [FadeOut(self.title)]




