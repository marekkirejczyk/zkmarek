from typing import Optional

from manim import DOWN, FadeOut, Indicate, ReplacementTransform, Text, Write

from zkmarek.video.constant import (HIGHLIGHT_COLOR, PRIMARY_FONT,
                                    SECONDARY_COLOR)
from zkmarek.video.slides.common.title import TitleSlide


class ECCTitleSlide(TitleSlide):
    question_mark: Optional[Text]
    def __init__(self):
        super().__init__("Elliptic curves",
            subtitle="Digital signatures")

    def animate_in(self, scene):
        self.play_sound(scene, sound="data/sound/teaser/s4.wav")
        scene.wait(1)
        scene.play(Write(self.title_text), run_time=2)
        scene.wait(1)
        scene.play(Indicate(self.title_text, color=HIGHLIGHT_COLOR))
        scene.wait(2)
        scene.play(Write(self.subtitle_text), run_time=2)
        scene.wait(1)
        scene.play(Indicate(self.subtitle_text, color=HIGHLIGHT_COLOR))
        scene.wait(2)

        self.question_mark = Text("?",
                font_size=38,
                font=PRIMARY_FONT,
                color=SECONDARY_COLOR)
        self.question_mark.next_to(self.title_text, DOWN)
        scene.wait(3)

        scene.play(ReplacementTransform(self.subtitle_text, self.question_mark),
            run_time=1)
        scene.play(Indicate(self.question_mark, color=HIGHLIGHT_COLOR))

    def animate_out(self, scene):
        scene.play(FadeOut(self.title_text, self.question_mark), run_time=0.5)
