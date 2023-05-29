from manim import (DOWN, UP, FadeIn, FadeOut, ImageMobject, Scene, Text,
                   Unwrite, Write)

from zkmarek.video.slides.common.slide_base import SlideBase


class ImageSlide(SlideBase):
    title_text: Text
    image: ImageMobject

    def __init__(self, title: str, image_path: str, image_scale=1.0):
        super().__init__(f"{title} (IMAGE)")
        self.title_text = Text(title)
        self.image = ImageMobject(image_path)
        self.title_text.to_edge(UP)
        self.image.scale(image_scale)
        self.image.next_to(self.title_text, DOWN)

    def animate_in(self, scene: Scene):
        scene.play(Write(self.title_text))
        scene.play(FadeIn(self.image))

    def animate_out(self, scene: Scene):
        scene.play(Unwrite(self.title_text))
        scene.play(FadeOut(self.image))
