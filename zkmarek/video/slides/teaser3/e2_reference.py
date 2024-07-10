from typing import Optional

from manim import DOWN, Write, Text, Arrow, LEFT, RIGHT, UP, MoveToTarget, rate_functions, VGroup, ApplyWave

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR

from zkmarek.video.slides.common.slide_base import SlideBase


class TitleSlide(SlideBase):
    title_text: Text
    subtitle_text: Optional[Text] = None
    subtitle: Optional[str]
    sound: Optional[str]
    pre_wait_time: int
    wait_time: int

    def __init__(
        self,
        title: str,
        subtitle: Optional[str] = None,
        sound: Optional[str] = None,
        pre_wait_time: Optional[int] = 0,
        wait_time: Optional[int] = 0,
    ) -> None:
        super().__init__(title)
        self.subtitle = subtitle
        self.sound = sound
        self.pre_wait_time = pre_wait_time
        self.wait_time = wait_time

    def __str__(self):
        return f"{self.title} (TITLE)"
    
    def create_arrow(self):
        self.arrow = Arrow(start=LEFT, end=RIGHT, color=PRIMARY_COLOR)
        self.arrow.align_on_border(UP, buff=0.1)
        self.arrow.shift(RIGHT * 3)
        self.arrow.generate_target()

        self.label = Text("Click here for teaser", font_size=24, color=PRIMARY_COLOR, font=PRIMARY_FONT)
        self.label.next_to(self.arrow, LEFT)
        self.label.generate_target()

        self.arrow.shift(9 * LEFT)
        self.label.shift(9 * LEFT)

    def construct(self):
        self.title_text = Text(
            self.title, should_center=True, font=PRIMARY_FONT, color=PRIMARY_COLOR
        )
        self.add(self.title_text)
        if self.subtitle is not None:
            self.subtitle_text = Text(
                self.subtitle, font_size=38, font=PRIMARY_FONT, color=SECONDARY_COLOR
            )
            self.subtitle_text.next_to(self.title_text, DOWN)
            self.add(self.subtitle_text)

    def animate_in(self, scene):
        self.new_subsection(scene, self.title, sound=self.sound)
        self.create_arrow()

        if self.pre_wait_time > 0:
            scene.wait(self.pre_wait_time)
        scene.play(Write(self.title_text))
        scene.play(MoveToTarget(self.label, rate_func=rate_functions.ease_out_bounce, run_time=1),
            MoveToTarget(self.arrow, rate_func=rate_functions.ease_out_bounce, run_time=1))

        scene.play(ApplyWave(VGroup(self.label, self.arrow)), run_time=2)

        if self.subtitle_text is not None:
            scene.play(Write(self.subtitle_text))
        if self.wait_time > 0:
            scene.wait(self.wait_time)
