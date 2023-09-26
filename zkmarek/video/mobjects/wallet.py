from manim import (LEFT, ORIGIN, RIGHT, Circle, FadeIn, RoundedRectangle, Text,
                   VGroup, Write)

from zkmarek.video.constant import (BACKGROUND_COLOR, HIGHLIGHT_COLOR,
                                    PRIMARY_COLOR, SECONDARY_COLOR)


class Wallet(VGroup):
    border: RoundedRectangle
    clip: RoundedRectangle
    button: Circle
    secretKey: Text
    address: Text

    def __init__(self, secret_key = "", address = ""):
        super().__init__()
        self.secret_key = Text(secret_key, font_size=24, font="Monaco", color=SECONDARY_COLOR)
        self.address = Text(address, font_size=24, font="Monaco", color=HIGHLIGHT_COLOR)
        self.add(self.secret_key, self.address)
        self.arrange_in_grid(cols=1, cell_alignment=LEFT)

        width = self.get_width() + 1
        height = self.get_height() + 0.6
        self.border = RoundedRectangle(width=width, height=height, corner_radius=0.3, color=PRIMARY_COLOR)
        self.border.move_to(RIGHT*0.3)
        self.clip = RoundedRectangle(width=0.6, height=0.5, corner_radius=0.1, color=PRIMARY_COLOR,
            fill_opacity=1, fill_color = BACKGROUND_COLOR)
        self.clip.next_to(self.border, RIGHT, buff=-0.5)
        self.button = Circle(radius=0.1, color=SECONDARY_COLOR, fill_opacity=1)
        self.button.next_to(self.clip, ORIGIN)
        self.add(self.border, self.clip, self.button)

    def animate_in(self, scene):
        scene.play(FadeIn(self.border), FadeIn(self.clip), FadeIn(self.button))
        scene.play(Write(self.secret_key))
        scene.play(Write(self.address))
