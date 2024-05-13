from manim import DOWN, UP, MoveToTarget, Text, VGroup, rate_functions

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase


class Credits(SlideBase):
    group: VGroup

    def __init__(self):
        super().__init__("Credits")

    def construct(self):
        self.group = VGroup()

    def add_title(self, text: Text):
        result = Text(text, font=PRIMARY_FONT, color=PRIMARY_COLOR)
        if len(self.group) > 0:
            result.next_to(self.group[-1], direction=DOWN, buff=1)
        self.group.add(result)

    def add_credit(self, text):
        result = Text(text, font=PRIMARY_FONT, color=SECONDARY_COLOR, font_size=30)
        result.next_to(self.group[-1], direction=DOWN, buff=0.2)
        self.group.add(result)

    def animate_in(self, scene):
        self.add_title("Idea and voice")
        self.add_credit("Marek Kirejczyk @zkmarek")
        self.add_title("Code and animation")
        self.add_credit("Marek Kirejczyk @zkmarek")
        self.add_credit("Arkadiusz Konior @ArkadiuszKonior")
        self.add_credit("Marta Wleklińska")
        self.add_title("Special thanks")
        self.group.generate_target()
        self.group.shift(5 * DOWN)
        self.group.target.shift(16 * UP)
        scene.play(
            MoveToTarget(self.group, run_time=32, rate_func=rate_functions.linear)
        )
