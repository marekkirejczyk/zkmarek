from manim import VGroup, FadeOut

class SlideBase(VGroup):
    title: str = ""

    def __init__(self, title:str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.title = title

    def new_subsection(self, scene, title):
        scene.next_section(f"{self.title}: {title}")

    def animate_in(self, scene):
        pass

    def animate_out(self, scene):
        scene.play(FadeOut(self))

    @staticmethod
    def print(slides, all_slides):
        for i, slide in enumerate(slides):
            print(f"{all_slides.index(slide)}. {slide.title}")
