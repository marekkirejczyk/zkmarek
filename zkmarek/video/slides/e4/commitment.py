from manim import LEFT, RIGHT, FadeIn, ImageMobject

# from zkmarek.video.constant import SECONDARY_COLOR, PRIMARY_FONT, PRIMARY_COLOR, HIGHLIGHT_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase

class Commitment(SlideBase):

    def __init__(self):
        super().__init__("Commitment")

    def construct(self):
        self.verifier = ImageMobject("data/images/person.png").shift(LEFT*3)
        self.commiter = ImageMobject("data/images/person_blue.png").shift(RIGHT*3)

    def animate_in(self, scene):
        self.new_subsection(scene, "intro", "data/sound/e4/slide2-0.mp3")
        scene.wait(4)
        scene.play(FadeIn(self.commiter))
        scene.play(FadeIn(self.verifier))

        self.new_subsection(scene, "committing", "data/sound/e4/slide2-1.mp3")

        self.new_subsection(scene, "validation", "data/sound/e4/slide2-2.mp3")

        self.new_subsection(scene, "opening", "data/sound/e4/slide2-3.mp3")

        self.new_subsection(scene, "quotient", "data/sound/e4/slide2-4.mp3")

