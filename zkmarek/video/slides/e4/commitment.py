from manim import Create, Rectangle, ImageMobject, RIGHT, LEFT, UP, FadeIn, MoveToTarget

from zkmarek.video.constant import PRIMARY_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase


class Commitment(SlideBase):

    def __init__(self):
        super().__init__("Commitment")

    def construct(self):
        self.verifier = ImageMobject("data/images/person.png").shift(RIGHT*3)
        self.commiter = ImageMobject("data/images/person_blue.png")
        self.rectangle = Rectangle(height=1.5, width=4, color = PRIMARY_COLOR).next_to(self.commiter, LEFT + UP, buff = 0)
        self.rectangle_copy = Rectangle(height=1.5, width=4, color = PRIMARY_COLOR).next_to(self.commiter, LEFT + UP, buff = 0)
        
    def animate_in(self, scene):
        self.new_subsection(scene, "envelope", "data/sound/e4/slide2-1.mp3")
        scene.play(FadeIn(self.commiter))
        scene.play(Create(self.rectangle))

        self.new_subsection(scene, "another party", "data/sound/e4/slide2-3.mp3")
        self.commiter.generate_target()
        self.commiter.target.shift(LEFT*3)
        scene.play(MoveToTarget(self.commiter))
        scene.play(FadeIn(self.verifier))
        scene.wait(1)

        self.rectangle_copy.generate_target()
        self.rectangle_copy.target.next_to(self.verifier, UP+RIGHT)
        scene.play(MoveToTarget(self.rectangle_copy), run_time=2)