
from manim_editor import PresentationSectionType


class Presentation:
    def __init__(self, scene):
        self.scene = scene

    def play(self, slides):
        if len(slides) > 0:
            self.scene.next_section(slides[0].title, PresentationSectionType.NORMAL)
        for i, slide in enumerate(slides):
            next_slide = slides[i + 1] if i + 1 < len(slides) else None
            self.play_slide(slide, next_slide)

    def play_slide(self, slide, next_slide):
        slide.animate_in(self.scene)
        if next_slide is not None:
            self.scene.next_section(next_slide.title, PresentationSectionType.NORMAL)
        slide.animate_out(self.scene)
