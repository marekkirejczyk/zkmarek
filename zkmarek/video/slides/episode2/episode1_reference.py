from manim import (LEFT, RIGHT, UP, ApplyWave, Arrow, FadeOut, MoveToTarget,
                   Text, VGroup, rate_functions)

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT
from zkmarek.video.slides.common.slide_base import SlideBase
from slides.equation import EquationSlide
from slides.ec.introduction import Introduction as ECIntroduction

class Episode1_Reference(SlideBase):
    slide1: EquationSlide
    slide2: ECIntroduction
    arrow: Arrow
    label: Text

    def __init__(self):
        super().__init__("Episode 1 reference")

    def create_arrow(self):
        self.arrow = Arrow(start=LEFT, end=RIGHT, color=PRIMARY_COLOR)
        self.arrow.align_on_border(UP, buff=0.1)
        self.arrow.shift(RIGHT * 1)
        self.arrow.generate_target()

        self.label = Text("Click here for episode 1", font_size=24, color=PRIMARY_COLOR, font=PRIMARY_FONT)
        self.label.next_to(self.arrow, LEFT)
        self.label.generate_target()

        self.arrow.shift(9 * LEFT)
        self.label.shift(9 * LEFT)
### CHANGE ECRECOVER FOR WEIERSTRASS AND SOMETHING SLIDES FROM EPISODE 1

    def animate_in(self, scene):
        self.new_subsection(scene, "Intro", sound="data/sound/episode1/s3.wav")
        self.create_arrow()
        scene.play(MoveToTarget(self.label, rate_func=rate_functions.ease_out_bounce, run_time=1),
            MoveToTarget(self.arrow, rate_func=rate_functions.ease_out_bounce, run_time=1))

        self.slide1 = ECRecoverSlideTeaser()
        self.slide1.construct()
        self.slide1.animate_miniature(scene)
        scene.wait(0.5)
        self.slide2 = SeasonTeaser()
        self.slide2.construct()
        self.slide2.animate_miniature(scene)
        scene.wait(1)
        scene.play(ApplyWave(VGroup(self.label, self.arrow)), run_time=2)


    def animate_out(self, scene):
        scene.play(FadeOut(self.slide1), FadeOut(self.slide2), FadeOut(self.label), FadeOut(self.arrow),
            FadeOut(*self.slide2.rest))
        self.wait_for_sound(scene)
