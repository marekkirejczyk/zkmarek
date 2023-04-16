import types

from manim import *
from manim_editor import PresentationSectionType

from .slides.slide_base import NewSection


class Presentation():
    def __init__(self, scene):
        self.scene = scene

    def play(self, slides):
        for (i, slide) in enumerate(slides):
            next_slide = slides[i+1] if i+1 < len(slides) else None
            self.play_slide(slide, next_slide)

    def play_slide(self, slide, next_slide):
        self.play_animation(slide.animate_in())
        if next_slide is not None:
            self.scene.next_section(next_slide.title, PresentationSectionType.NORMAL)
        self.play_animation(slide.animate_out())

    def play_animation(self, item):
        if isinstance(item, list):
            for a in item:
                self.play_animation(a)
        elif isinstance(item, types.LambdaType):
            item()
        elif isinstance(item, NewSection):
            self.scene.next_section(item.title, item.type)
        else:
            self.scene.play(item, Wait())
