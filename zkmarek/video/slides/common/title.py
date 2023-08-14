from typing import Optional

from manim import DOWN, Write, Text

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR

from .slide_base import SlideBase


class TitleSlide(SlideBase):
    title_text: Text
    subtitle_text: Optional[Text] = None
    subtitle: Optional[str]
    sound: Optional[str]
    pre_wait_time: int
    post_wait_time: int

    def __init__(self, title: str,
            subtitle: Optional[str] = None,
            sound: Optional[str] = None,
            pre_wait_time: Optional[int] = 0,
            post_wait_time: Optional[int] = 1) -> None:
        super().__init__(title)
        self.subtitle = subtitle
        self.sound = sound
        self.pre_wait_time = pre_wait_time
        self.post_wait_time = post_wait_time

    def __str__(self):
        return f"{self.title} (TITLE)"

    def construct(self):
        self.title_text = Text(
            self.title,
            should_center=True,
            font=PRIMARY_FONT,
            color=PRIMARY_COLOR)
        self.add(self.title_text)
        if self.subtitle is not None:
            self.subtitle_text = Text(
                self.subtitle,
                font_size=38,
                font=PRIMARY_FONT,
                color=SECONDARY_COLOR)
            self.subtitle_text.next_to(self.title_text, DOWN)
            self.add(self.subtitle_text)

    def animate_in(self, scene):
        if self.sound is not None:
            self.play_sound(scene, sound=self.sound)
        scene.wait(self.pre_wait_time)
        scene.play(Write(self.title_text))
        if self.subtitle_text is not None:
            scene.play(Write(self.subtitle_text))
        scene.wait(self.post_wait_time)

