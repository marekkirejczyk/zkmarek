from manim import FadeIn, ImageMobject, Text, FadeOut, UP, config
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT
from zkmarek.video.slides.common.slide_base import SlideBase

config.frame_height = 1920
config.frame_width = 1080
config.pixel_height = 1920
config.pixel_width = 1080


class Challange(SlideBase):
    def __init__(self):
        super().__init__("Challange acceppted!")

    def construct(self):
        self.title = Text(
            "Challenge accepted!", color=PRIMARY_COLOR, font=PRIMARY_FONT
        ).to_edge(UP)

        self.image = ImageMobject("data/shorts/warpcast.png").scale(2.3)

    def animate_in(self, scene):
        self.new_subsection(scene, "challange", "data/sound/short1/slide1-0.mp3")
        scene.play(FadeIn(self.title), FadeIn(self.image), run_time=0.7)
        scene.wait(6)

    def animate_out(self, scene):
        scene.play(FadeOut(self.title), FadeOut(self.image), run_time=0.5)
