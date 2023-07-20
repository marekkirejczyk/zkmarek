from manim import Write, FadeOut, Text, ReplacementTransform, Indicate
from zkmarek.video.constant import PRIMARY_FONT, PRIMARY_COLOR, HIGHLIGHT_COLOR
from zkmarek.video.slides.common.title import TitleSlide

class ZKPSTitle(TitleSlide):
    def __init__(self):
        super().__init__("Zero Knowledge Proofs",
            subtitle="Season 1")

    def animate_in(self, scene):
        self.play_sound(scene, sound="data/sound/teaser/s2.wav")
        scene.wait(1)
        scene.play(Write(self.subtitle_text), run_time=2)
        scene.wait(0.5)
        scene.play(Write(self.title_text))

    def animate_out(self, scene):
        scene.play(FadeOut(self.subtitle_text))
        question_mark = Text(
            "?",
            should_center=True,
            font=PRIMARY_FONT,
            color=PRIMARY_COLOR)
        scene.play(ReplacementTransform(self.title_text, question_mark))
        scene.play(Indicate(question_mark, color=HIGHLIGHT_COLOR,
            scale_factor=3,
            run_time=1.5))
        scene.play(FadeOut(question_mark))
