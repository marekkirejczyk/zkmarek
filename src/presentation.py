from manim import *
import types


class Presentation():
    def __init__(self, scene):
        self.scene = scene

    def play(self, slides):
        for slide in slides:
            self.play_slide(slide)

    def play_slide(self, slide):
        self.play_animation(slide.animate_in())
        self.play_animation(slide.animate_out())

    def play_animation(self, item):
        if isinstance(item, list):
            for a in item:
                self.play_animation(a)
        elif isinstance(item, types.LambdaType):
            item()
        else:
            self.scene.play(item, Wait())
