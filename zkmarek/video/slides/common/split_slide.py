from manim import DOWN, LEFT, RIGHT, UP, Create, DashedLine, FadeIn, Text

from zkmarek.video.constant import PRIMARY_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase


class SplitSlide(SlideBase):
    left_label: Text
    right_label: Text
    h_line: DashedLine

    def __init__(self, title):
        super().__init__(title)

    def fade_in_board(self, scene):
        self.left_label.move_to(scene.camera.frame_width / 4 * LEFT)
        self.right_label.move_to(scene.camera.frame_width / 4 * RIGHT)
        self.left_label.to_edge(UP)
        self.right_label.to_edge(UP)
        scene.play(FadeIn(self.left_label), FadeIn(self.right_label))
        self.h_line = DashedLine(scene.camera.frame_height / 2 * UP,
            scene.camera.frame_height / 2 * DOWN,
            color=PRIMARY_COLOR)
        scene.play(Create(self.h_line))
