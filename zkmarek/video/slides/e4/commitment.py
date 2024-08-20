from manim import Create, Rectangle, ImageMobject, RIGHT, LEFT, UP, DOWN, FadeIn, MoveToTarget, Text, Write, Indicate, Tex, FadeOut

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR, HIGHLIGHT_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.utils import load

class Commitment(SlideBase):

    def __init__(self):
        super().__init__("Commitment")

    def construct(self):
        self.title_text = Text("Commitment scheme", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size=40).to_edge(UP)
        self.commiter = ImageMobject("data/images/person_blue.png")
        self.rectangle = Rectangle(height=1.5, width=4, color = PRIMARY_COLOR).next_to(self.commiter, LEFT, buff = 0.5)
        self.commitment = Text("secret message", font = PRIMARY_FONT, color = PRIMARY_COLOR).scale(0.6).next_to(self.commiter, LEFT, buff = 0.6).shift(LEFT*0.8)

        self.lock = ImageMobject("data/images/Locked@2x.png").scale(0.25).next_to(self.commitment, RIGHT, buff = 0.1)
        self.tex = Tex(load("zkmarek/video/slides/e4/properties.tex"), color=SECONDARY_COLOR)

    def animate_in(self, scene):
        self.new_subsection(scene, "envelope", "data/sound/e4/slide2-1.mp3")
        scene.play(Write(self.title_text))
        scene.play(FadeIn(self.commiter))
        scene.play(Create(self.rectangle))

        scene.wait(2)
        scene.play(Write(self.commitment), run_time=1.2)
        scene.wait(2)
        scene.play(FadeIn(self.lock))


        scene.wait(4.5)
        scene.play(Indicate(self.lock, color = HIGHLIGHT_COLOR))

        self.new_subsection(scene, "properties of commitment", "data/sound/e4/slide2-2.mp3")

        self.tex.scale(0.8).next_to(self.commiter, RIGHT, buff = 1)
        scene.play(Write(self.tex))

        self.new_subsection(scene, "hiding", "data/sound/e4/slide2-3.mp3")
        scene.wait(0.2)
        scene.play(Indicate(self.tex[0][1:7], color = HIGHLIGHT_COLOR))
        scene.wait(2)

        self.new_subsection(scene, "binding", "data/sound/e4/slide2-4.mp3")
        scene.play(Indicate(self.tex[0][8:15], color = HIGHLIGHT_COLOR))   
        scene.wait(4)
        scene.play(Indicate(self.lock, color = HIGHLIGHT_COLOR))
        scene.wait(3)

    def animate_out(self, scene):
        scene.play(FadeOut(self.tex, self.rectangle, self.commitment, self.commiter, self.lock, self.title_text))