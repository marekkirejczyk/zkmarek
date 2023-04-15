from manim import *

class Presentation():
    def __init__(self, scene):
        self.scene = scene

    def play(self, slides):
        for slide in slides:
            self.play_slide(slide)

    def play_slide(self, slide):
        for a in slide.animate_in():
            self.scene.play(a, Wait())
        for a in slide.animate_out():
            self.scene.play(a, Wait())
