from manim import Write
from zkmarek.video.slides.common.title import TitleSlide


class ECCTitleSlide(TitleSlide):
    def __init__(self):
        super().__init__("Digital signatures",
            subtitle="Episode 1")

    def animate_in(self, scene):
        self.play_sound(scene, sound="data/sound/teaser/s4.wav")
        scene.play(Write(self.title_text), run_time=2)
        scene.wait(1)
        scene.play(Write(self.subtitle_text), run_time=2)
        scene.wait(3)
