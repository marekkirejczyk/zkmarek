from curses.textpad import rectangle
from manim import (BLACK, DOWN, UP, WHITE, FadeIn, FadeOut, ImageMobject,
                   Scene, Text, Unwrite, Write, Rectangle)

from zkmarek.video.slides.common.slide_base import SlideBase


class ImageSlide(SlideBase):
    title_text: Text
    image: ImageMobject
    background_rect: rectangle

    def __init__(self, title: str, image_path: str, image_scale=1.0):
        super().__init__(f"{title} (IMAGE)")
        self.title_text = Text(title)
        self.image = ImageMobject(image_path)
        self.title_text.to_edge(UP)
        self.title_text.set_color(BLACK)
        self.image.scale(image_scale)
        self.image.next_to(self.title_text, DOWN)

    def animate_in(self, scene: Scene):
        self.background_rect = Rectangle(
            width=scene.camera.frame_width,
            height=scene.camera.frame_height,
            fill_opacity=1,
            stroke_width=0,
            fill_color=BLACK
        )
        scene.add(self.background_rect)
        scene.play(self.background_rect.animate.set_fill(color=WHITE), run_time=1)
        scene.play(Write(self.title_text))
        scene.play(FadeIn(self.image))

    def animate_out(self, scene: Scene):
        scene.play(Unwrite(self.title_text))
        scene.play(FadeOut(self.image))
        scene.play(FadeOut(self.background_rect))

