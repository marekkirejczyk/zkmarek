from manim import (DOWN, UP, FadeIn, FadeOut, ImageMobject, Scene, Text,
                   Unwrite, Write)

from zkmarek.video.slides.common.slide_base import SlideBase


class ImageSlide(SlideBase):
    title: Text
    image: ImageMobject

    def __init__(self, title: str, image_path: str):
        super().__init__(title)
        self.title = Text(title)
        self.image = ImageMobject(image_path)
        self.title.to_edge(UP)
        self.image.next_to(self.title, DOWN)

    def animate_in(self, scene: Scene):
        scene.play(Write(self.title))
        scene.play(FadeIn(self.image))

    def animate_out(self, scene: Scene):
        scene.play(Unwrite(self.title))
        scene.play(FadeOut(self.image))
