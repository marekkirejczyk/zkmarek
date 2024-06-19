# from manim import ThreeDScene
from manim_editor import PresentationSectionType
from zkmarek.video.slides.common.slide_base import SlideBase


class Presentation:
    # scene: ThreeDScene
    slides: list[SlideBase]
    all_slides: list[SlideBase]

    def __init__(self, scene, all_slides: list[SlideBase], slides: list[SlideBase]):
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
        slide.construct()
        slide.animate_in(self.scene)
        if next_slide is not None:
            self.scene.next_section(next_slide.title, PresentationSectionType.NORMAL)
        else:
            self.scene.next_section("End", PresentationSectionType.NORMAL)
        slide.animate_out(self.scene)
        self.scene.clear()

    def print_slides(self, name: str):
        def index_of(slide, slides):
            try:
                return slides.index(slide)
            except ValueError:
                return -1

        print(f"Rendering '{name}': ")
        for slide in self.all_slides:
            prefix = "-> " if index_of(slide, self.slides) >= 0 else "   "
            index = index_of(slide, self.all_slides) + 1
            print(f"{prefix}{index:2}. {slide}")
