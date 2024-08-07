from manim import (LEFT, UP, FadeOut, Text, Arrow, RIGHT, MoveToTarget, rate_functions, ApplyWave, VGroup)

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.episode3.ceremony import Ceremony


class Episode3Reference(SlideBase):
    slide: Ceremony

    def __init__(self):
        super().__init__("E3 Reference")

    def create_arrow(self):
        self.arrow = Arrow(start=LEFT, end=RIGHT, color=PRIMARY_COLOR)
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
        self.create_arrow()
        scene.play(MoveToTarget(self.label, rate_func=rate_functions.ease_out_bounce, run_time=1),
            MoveToTarget(self.arrow, rate_func=rate_functions.ease_out_bounce, run_time=1))
        scene.play(ApplyWave(VGroup(self.label, self.arrow)), run_time=2)
        self.slide = Ceremony()
        self.slide.construct()
        scene.wait(0.5)

        self.new_subsection(scene, "to recap", "data/sound/e4/slide0-2.mp3")
        self.slide.animate_miniature(scene)

        self.new_subsection(scene, "powers of tau", "data/sound/e4/slide0-3.mp3")
        self.slide.animate_miniature2(scene)

        self.new_subsection(scene, "this episode", "data/sound/e4/slide0-4.mp3")
        

    def animate_out(self, scene):
        scene.play(FadeOut(self.slide), FadeOut(self.label), FadeOut(self.arrow))
        self.wait_for_sound(scene)
