from manim import Create, Rectangle, ImageMobject, RIGHT, LEFT, UP, DOWN, FadeIn, MoveToTarget, Text, Write, Indicate, Tex, FadeOut

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR, HIGHLIGHT_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.utils import load

class Commitment(SlideBase):

    def __init__(self):
        super().__init__("Commitment")

    def construct(self):
        self.title_text = Text("Commitment scheme", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size=40).to_edge(UP)
        self.verifier = ImageMobject("data/images/person.png")
        self.commiter = ImageMobject("data/images/person_blue.png")
        self.rectangle = Rectangle(height=1.5, width=4, color = PRIMARY_COLOR).to_edge(LEFT + UP, buff = 0).shift(DOWN)
        self.rectangle_copy = Rectangle(height=1.5, width=4, color = PRIMARY_COLOR).next_to(self.commiter, LEFT + UP, buff = 0).shift(DOWN)
        self.commitment = Text("secret message", font = PRIMARY_FONT, color = PRIMARY_COLOR).scale(0.6).next_to(self.commiter, UP+LEFT, buff = 0.3)
        self.commitment_copy = Text("secret message", font = PRIMARY_FONT, color = PRIMARY_COLOR).scale(0.6).next_to(self.commiter, UP+LEFT, buff = 0.3)
        self.verifier.shift(3*RIGHT)
        self.lock = ImageMobject("data/images/Locked@2x.png").scale(0.25).next_to(self.commitment, RIGHT, buff = 0.1)
        self.lock_copy = ImageMobject("data/images/Locked@2x.png").scale(0.25).next_to(self.commitment, RIGHT, buff = 0.1)
        self.tex = Tex(load("zkmarek/video/slides/e4/properties.tex"), color=SECONDARY_COLOR)

    def animate_in(self, scene):
        self.new_subsection(scene, "envelope", "data/sound/e4/slide2-1.mp3")
        scene.play(Write(self.title_text))
        scene.play(FadeIn(self.commiter))
        scene.play(Create(self.rectangle))

        self.commiter.generate_target()
        self.commiter.target.shift(LEFT*3)
        scene.play(MoveToTarget(self.commiter))
        scene.play(FadeIn(self.verifier))
        scene.wait(1)
        scene.play(Write(self.commitment))
        scene.wait(2)
        scene.play(FadeIn(self.lock))

        self.commitment_copy.generate_target()
        self.commitment_copy.target.next_to(self.verifier, UP+RIGHT, buff = 0.3).shift(0.5*LEFT)
        self.lock_copy.generate_target()
        self.lock_copy.target.next_to(self.commitment_copy, RIGHT, buff = 0.1)
        self.rectangle_copy.generate_target()
        self.rectangle_copy.target.to_edge(UP+RIGHT).shift(DOWN)
        scene.play(MoveToTarget(self.rectangle_copy), MoveToTarget(self.commitment_copy), run_time=2)

        self.new_subsection(scene, "properties of commitment", "data/sound/e4/slide2-2.mp3")
        self.tex.scale(0.8).to_edge(DOWN)
        scene.play(Write(self.tex))

        self.new_subsection(scene, "hiding", "data/sound/e4/slide2-3.mp3")
        scene.wait(2)
        scene.play(Indicate(self.tex[0][1:8], color = HIGHLIGHT_COLOR))
        scene.wait(2)

        self.new_subsection(scene, "binding", "data/sound/e4/slide2-3.mp3")
        scene.play(Indicate(self.tex[0][9:15], color = HIGHLIGHT_COLOR))   
        scene.wait(4)

    def animate_out(self, scene):
        scene.play(FadeOut(self.tex, self.rectangle, self.rectangle_copy, self.verifier, self.commitment, self.commiter, self.lock, self.lock_copy, self.title_text))