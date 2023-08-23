from manim import FadeOut
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.teaser.ecrecover import ECRecoverSlideTeaser
from zkmarek.video.slides.teaser.season_teaser import SeasonTeaser


class TeaserReference(SlideBase):
    slide1: ECRecoverSlideTeaser
    slide2: SeasonTeaser

    def __init__(self):
        super().__init__("Teaser Reference")

    def animate_in(self, scene):
        self.new_subsection(scene, "Intro", sound="data/sound/episode/s2-2.wav")
        self.slide1 = ECRecoverSlideTeaser()
        self.slide1.construct()
        self.slide1.animate_miniature(scene)

        self.slide2 = SeasonTeaser()
        self.slide2.construct()
        self.slide2.animate_miniature(scene)

    def animate_out(self, scene):
        scene.play(FadeOut(self.slide1), FadeOut(self.slide2),
            FadeOut(*self.slide2.rest))
        self.wait_for_sound(scene)
