from manim import Create, Rectangle, ImageMobject, RIGHT, LEFT, UP, DOWN, FadeIn, MoveToTarget, Text, Write, Indicate, Tex

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.utils import load

class Commitment(SlideBase):

    def __init__(self):
        super().__init__("Commitment")

    def construct(self):
        self.title_text = Text("Commitment scheme", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size=100).to_edge(UP)
        self.verifier = ImageMobject("data/images/person.png")
        self.commiter = ImageMobject("data/images/person_blue.png")
        self.rectangle = Rectangle(height=1.5, width=4, color = PRIMARY_COLOR).next_to(self.commiter, LEFT + UP, buff = 0)
        self.rectangle_copy = Rectangle(height=1.5, width=4, color = PRIMARY_COLOR).next_to(self.commiter, LEFT + UP, buff = 0)

        self.verifier.shift(3*RIGHT)
        self.tex = Tex(load("zkmarek/video/slides/e4/properties.tex"), color=SECONDARY_COLOR)

    def animate_in(self, scene):
        self.new_subsection(scene, "envelope", "data/sound/e4/slide2-1.mp3")
        scene.play(FadeIn(self.commiter))
        scene.play(Create(self.rectangle))

        self.commiter.generate_target()
        self.commiter.target.shift(LEFT*3)
        scene.play(MoveToTarget(self.commiter))
        scene.play(FadeIn(self.verifier))
        scene.wait(1)

        self.rectangle_copy.generate_target()
        self.rectangle_copy.target.to_edge(UP+RIGHT)
        scene.play(MoveToTarget(self.rectangle_copy), run_time=2)

        self.new_subsection(scene, "properties of commitment", "data/sound/e4/slide2-2.mp3")
        self.tex.scale(0.8).to_edge(DOWN)
        scene.play(Write(self.tex))

        self.new_subsection(scene, "hiding", "data/sound/e4/slide2-3.mp3")
        scene.wait(2)
        scene.play(Indicate(self.tex[0][0:7]))
        scene.wait(2)

        self.new_subsection(scene, "binding", "data/sound/e4/slide2-3.mp3")
        scene.play(Indicate(self.tex[0][8:13]))