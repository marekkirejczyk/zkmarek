from manim import (
    LEFT,
    ORIGIN,
    RIGHT,
    Group,
    ImageMobject,
    MoveToTarget,
    Text,
    rate_functions,
)

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT
from zkmarek.video.slides.common.slide_base import SlideBase


class Intro_ep2(SlideBase):
    marek: Text
    logo: ImageMobject
    sound: str

    def __init__(self, sound: str):
        super().__init__("Intro_ep2")
        self.sound = sound

    def construct(self):
        self.logo = ImageMobject("data/brand/logo.png").scale(1.5)
        self.marek = Text("Marek", font_size=60, font=PRIMARY_FONT, color=PRIMARY_COLOR)
        self.marek.next_to(self.logo, RIGHT, buff=0.25)
        self.group = Group(self.logo, self.marek)
        self.group.move_to(ORIGIN)

    def animate_in(self, scene):
        self.play_sound(scene, sound=self.sound)  # "data/sound/episode2/intro.mp3")
        self.logo.generate_target()
        self.marek.generate_target()
        self.logo.shift(8 * LEFT)
        self.marek.shift(8 * RIGHT)
        scene.play(
            MoveToTarget(
                self.marek, rate_func=rate_functions.ease_out_bounce, run_time=2.25
            ),
            MoveToTarget(self.logo, rate_func=rate_functions.ease_out_bounce),
            run_time=2.25,
        )
        scene.wait(4.5)

    def animate_out(self, scene):
        self.marek.generate_target()
        self.marek.target.shift(8 * RIGHT)
        self.logo.generate_target()
        self.logo.target.shift(8 * LEFT)
        scene.play(MoveToTarget(self.marek), MoveToTarget(self.logo))
