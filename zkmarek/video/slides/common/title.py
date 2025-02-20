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
    wait_time: int
    font_size = Optional[int] 
    background_sound = Optional[str]

    def __init__(
        self,
        title: str,
        subtitle: Optional[str] = None,
        sound: Optional[str] = None,
        pre_wait_time: Optional[int] = 0,
        wait_time: Optional[int] = 0,
        font_size: Optional[int] = 48,
        background_sound: Optional[str] = None,
    ) -> None:
        super().__init__(title)
        self.subtitle = subtitle
        self.sound = sound
        self.pre_wait_time = pre_wait_time
        self.wait_time = wait_time
        self.font_size = font_size 
        self.background_sound = background_sound

    def __str__(self):
        return f"{self.title} (TITLE)"

    def construct(self):
        self.title_text = Text(
            self.title, should_center=True, font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=self.font_size
        )
        self.add(self.title_text)
        if self.subtitle is not None:
            self.subtitle_text = Text(
                self.subtitle, font_size=38, font=PRIMARY_FONT, color=SECONDARY_COLOR
            )
            self.subtitle_text.next_to(self.title_text, DOWN)
            self.add(self.subtitle_text)

    def animate_in(self, scene):
        if self.background_sound is not None:
           self.play_music(scene, self.background_sound)
        self.new_subsection(scene, self.title, sound=self.sound)

        if self.pre_wait_time > 0:
            scene.wait(self.pre_wait_time)
        scene.play(Write(self.title_text))
        if self.subtitle_text is not None:
            scene.play(Write(self.subtitle_text))
        if self.wait_time > 0:
            scene.wait(self.wait_time)
