from manim import (
    UP,
    FadeOut,
    FadeIn,
    ImageMobject,
    Text,
    ReplacementTransform,
)
from zkmarek.video.constant import (
    PRIMARY_COLOR,
    PRIMARY_FONT,
)

from zkmarek.video.slides.common.tex_slide import SlideBase


class Sponsored(SlideBase):

    def __init__(self) -> None:
        super().__init__(title="This video is supported by: and sponsored by")

    def construct(self):
        self.vlayer = ImageMobject(
            "zkmarek/video/slides/episode2/sponsors/Logo_304_color_on_dark.png"
        ).scale(1.3)
        self.ecosystem = ImageMobject(
            "zkmarek/video/slides/episode2/sponsors/ecosystem_support_program.png"
        ).scale(0.3)
        self.title = Text(
            "This video is supported by",
            font=PRIMARY_FONT,
            color=PRIMARY_COLOR,
        ).to_edge(UP)
        self.title_replace = Text(
            "... and sponsored by", font=PRIMARY_FONT, color=PRIMARY_COLOR
        ).to_edge(UP)

    def animate_in(self, scene):
        self.new_subsection(scene, "thanks to", "data/sound/episode2/slide3-0.mp3")
        scene.play(FadeIn(self.title))
        scene.play(FadeIn(self.ecosystem))
        scene.wait(1.5)
        scene.play(
            ReplacementTransform(self.title, self.title_replace),
            FadeOut(self.ecosystem),
            FadeIn(self.vlayer),
        )
        scene.wait(3)

    def animate_out(self, scene):
        scene.play(FadeOut(self.vlayer), FadeOut(self.title_replace))
