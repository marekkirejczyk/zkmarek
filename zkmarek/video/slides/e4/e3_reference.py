from manim import (LEFT, UP, DOWN, MathTex, FadeIn, Write, FadeOut, Text, Arrow, RIGHT, MoveToTarget, rate_functions, ApplyWave, VGroup, ImageMobject)

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.episode3.ceremony import Ceremony
from zkmarek.video.slides.episode3.polynomial import Polynomial


class Episode3Reference(SlideBase):
    slide: Ceremony
    slide2: Polynomial

    def __init__(self):
        super().__init__("E3 Reference")

    def create_arrow(self):
        self.arrow = Arrow(start=LEFT, end=RIGHT, color=PRIMARY_COLOR)
        self.group = ImageMobject("data/images/group.png")
        self.tau0 = MathTex(r"\tau_0", color = SECONDARY_COLOR, font_size=70).next_to(self.group, DOWN, buff=0)
        self.tau1 = MathTex(r"\tau_1", color = SECONDARY_COLOR, font_size=70).next_to(self.group, LEFT, buff=0.1)
        self.tau2 = MathTex(r"\tau_2", color = SECONDARY_COLOR, font_size=70).next_to(self.group, RIGHT, buff=0.1)

        self.title = Text("Previously on zkMarek", color = PRIMARY_COLOR, font = PRIMARY_FONT).to_edge(UP)
        self.arrow.align_on_border(UP, buff=0.1)
        self.arrow.shift(RIGHT * 1)
        self.arrow.generate_target()

        self.label = Text("Click here for episode 3", font_size=24, color=PRIMARY_COLOR, font=PRIMARY_FONT)
        self.label.next_to(self.arrow, LEFT)
        self.label.generate_target()

        self.arrow.shift(9 * LEFT)
        self.label.shift(9 * LEFT)


    def animate_in(self, scene):
        self.new_subsection(scene, "Intro", sound="data/sound/e4/slide0-1.mp3")
        scene.play(Write(self.title), run_time=2)
        scene.play(FadeIn(self.group))
        scene.play(Write(self.tau0))
        scene.play(Write(self.tau1))
        scene.play(Write(self.tau2))
        self.create_arrow()
        self.slide = Ceremony()
        self.slide.construct()
        self.slide2 = Polynomial()
        self.slide2.construct()

        scene.play(MoveToTarget(self.label, rate_func=rate_functions.ease_out_bounce, run_time=1),
            MoveToTarget(self.arrow, rate_func=rate_functions.ease_out_bounce, run_time=1))
        scene.play(ApplyWave(VGroup(self.label, self.arrow)), run_time=2)

        self.new_subsection(scene, "to recap", "data/sound/e4/slide0-2.mp3")
        scene.play(FadeOut(self.arrow, self.label, self.tau0, self.tau1, self.tau2, self.group))
        self.slide.animate_miniature(scene)

        self.new_subsection(scene, "polynomial", "data/sound/e4/slide0-3.mp3")
        scene.wait(0.5)
        self.slide2.animate_miniature(scene)
        

    def animate_out(self, scene):
        # scene.play(FadeOut(self.slide2))
        self.wait_for_sound(scene)
