from manim import VGroup, FadeOut

class SlideBase(VGroup):
    title = ""

    def __init__(self, title="", **kwargs) -> None:
        VGroup.__init__(self, **kwargs)
        self.title=title

    def animate_in(self, scene):
        pass

    def animate_out(self, scene):
        scene.play(FadeOut(self))
