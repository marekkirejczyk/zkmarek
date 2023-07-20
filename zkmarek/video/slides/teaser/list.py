from manim import DOWN, UP, Tex, Text, Write

from zkmarek.video.constant import (HIGHLIGHT_COLOR, PRIMARY_COLOR,
                                    PRIMARY_FONT, SECONDARY_COLOR)
from zkmarek.video.slides.common.slide_base import SlideBase


class ListSlide(SlideBase):
    title_text: Text
    list: Tex

    def __init__(self):
        super().__init__("Episode 1")

    def construct(self):
        self.title_text = Text(
            self.title,
            should_center=True,
            font=PRIMARY_FONT,
            color=PRIMARY_COLOR)
        self.list = Tex(
            "· Elliptic curves\\\\",
            "· Digital Signature Algorithm\\\\",
            "· Usage in Ethereum\\\\",
            tex_environment=None,
            color=SECONDARY_COLOR
        )
        self.title_text.align_on_border(UP, buff=1)
        self.list.next_to(self.title_text, DOWN, buff=1)

    def animate_in(self, scene):
        self.play_sound(scene, "data/sound/teaser/s7.wav")
        scene.play(Write(self.title_text))
        scene.wait(2)
        scene.play(Write(self.list), run_time=2)
        self.list.set_color_by_tex("· Elliptic curves", HIGHLIGHT_COLOR)
        scene.wait(2)
        self.list.set_color_by_tex("· Digital Signature Algorithm", HIGHLIGHT_COLOR)
        scene.wait(4)
        self.list.set_color_by_tex("· Usage in Ethereum", HIGHLIGHT_COLOR)



