from manim import Scene
from manim_editor import PresentationSectionType
from zkmarek.video.slides.slide_base import SlideBase


class Presentation:
    scene: Scene
    slides: list[SlideBase]
    all_slides: list[SlideBase]

    def __init__(
        self, scene: Scene, all_slides: list[SlideBase], slides: list[SlideBase]
    ):
        self.scene = scene
        self.slides = slides
        self.all_slides = all_slides

    def play(self):
        if len(self.slides) > 0:
            self.scene.next_section(
                self.slides[0].title, PresentationSectionType.NORMAL
            )
        for i, slide in enumerate(self.slides):
            next_slide = self.slides[i + 1] if i + 1 < len(self.slides) else None
            self.play_slide(slide, next_slide)

    def play_slide(self, slide, next_slide):
        slide.animate_in(self.scene)
        if next_slide is not None:
            self.scene.next_section(next_slide.title, PresentationSectionType.NORMAL)
        slide.animate_out(self.scene)

    def print_slides(self):
        def index_of(slide):
            try:
                return self.all_slides.index(slide)
            except ValueError:
                return 0
        print("Rendering slides: ")
        for slide in self.slides:
            print(f"{index_of(slide)}. {slide.title}")
