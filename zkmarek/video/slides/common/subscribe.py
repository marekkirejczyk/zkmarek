from manim import (DOWN, UP, AddTextLetterByLetter, FadeIn, FadeOut, Group,
                   ImageMobject, Text)
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT

from zkmarek.video.slides.common.slide_base import SlideBase


class Subscribe(SlideBase):
    button: ImageMobject
    button_clicked: ImageMobject
    title: Text
    group: Group

    def __init__(self) -> None:
        super().__init__("Subscribe")

    def construct(self):
        self.title = Text(
            "youtube.com/@zkmarek",
            font=PRIMARY_FONT,
            color=PRIMARY_COLOR,
            ).move_to(0.5*UP)
        self.button = ImageMobject(
            "data/subscribe/normal.png").scale(0.4)
        self.button_clicked = ImageMobject(
            "data/subscribe/clicked.png",
            z_index=1).scale(0.4)
        self.button.next_to(self.title, DOWN, buff=0.5)
        self.button_clicked.next_to(self.title, DOWN, buff=0.5)

    def animate_in(self, scene):
        scene.play(AddTextLetterByLetter(self.title))
        scene.play(FadeIn(self.button), run_time=0.5)
        scene.wait(0.5)

        # Source of sound under Creative Commons 0 License.
        # https://freesound.org/people/joebro10/sounds/219318/
        scene.add_sound("data/subscribe/click.wav", gain=10)
        scene.play(FadeIn(self.button_clicked), run_time=0.2)
        scene.play(FadeOut(self.button_clicked), run_time=0.2)
        scene.wait(1)

    def animate_out(self, scene):
        pass
