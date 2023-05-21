from manim import VGroup, FadeOut

class SlideBase(VGroup):
    title: str = ""

    def __init__(self, title:str = "", **kwargs) -> None:
        VGroup.__init__(self, **kwargs)
        self.title = title

    def new_subsection(self, scene, title):
        scene.next_section(f"{self.title}: {title}")

    def animate_in(self, scene):
        pass

    def animate_out(self, scene):
        scene.play(FadeOut(self))
