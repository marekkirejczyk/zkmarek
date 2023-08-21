from manim import Rectangle

from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.teaser.ecrecover import ECRecoverSlideTeaser
from zkmarek.video.slides.teaser.season_teaser import SeasonTeaser


class TeaserReference(SlideBase):
    def __init__(self):
        super().__init__("Teaser Reference")

    def animate_in(self, scene):
        self.new_subsection(scene, "Intro", sound="data/sound/episode/s2-2.m4a")
        scene.wait(1)
        slide1 = ECRecoverSlideTeaser()
        slide1.construct()
        slide1.animate_miniature(scene)

        slide2 = SeasonTeaser()
        slide2.construct()
        slide2.animate_miniature(scene)
