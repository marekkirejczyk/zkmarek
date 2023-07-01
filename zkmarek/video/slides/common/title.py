from typing import Optional
from manim import FadeOut, Text, Write, DOWN
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR

from .slide_base import SlideBase


class TitleSlide(SlideBase):
    title_text: Text
    subtitle_text: Optional[Text] = None
    subtitle: Optional[str]

    def __init__(self, title: str, subtitle: Optional[str] = None) -> None:
        super().__init__(title)
        self.subtitle = subtitle

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

    def animate_in(self, scene):
        scene.play(Write(self.title_text))
        if self.subtitle_text is not None:
            scene.play(Write(self.subtitle_text))

    def animate_out(self, scene):
        scene.play(FadeOut(self.title_text))
        scene.play(FadeOut(self.subtitle_text))
