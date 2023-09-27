from random import randint

from manim import (LEFT, ORIGIN, RIGHT, Circle, FadeIn, RoundedRectangle, Text,
                   VGroup, Write, ReplacementTransform)

from zkmarek.video.constant import (BACKGROUND_COLOR, HIGHLIGHT_COLOR,
                                    PRIMARY_COLOR, SECONDARY_COLOR)


class Wallet(VGroup):
    border: RoundedRectangle
    clip: RoundedRectangle
    button: Circle
    secret_key: VGroup
    secret_key_label: Text
    secret_key_value: Text
    address: Text

    def __init__(self, secret_key="", address=""):
        super().__init__()
        self.secret_key_label = Text(secret_key, font_size=24, font="Monaco", color=SECONDARY_COLOR)
        self.secret_key_value = Text("", font_size=24, font="Monaco", color=SECONDARY_COLOR)
        self.secret_key_value.next_to(self.secret_key_label, RIGHT)
        self.secret_key = VGroup(self.secret_key_label, self.secret_key_value)

        self.address = Text(address, font_size=24, font="Monaco", color=HIGHLIGHT_COLOR)
        self.add(self.secret_key, self.address)
        self.arrange_in_grid(cols=1, cell_alignment=LEFT)

        width = self.get_width() + 3
        height = self.get_height() + 1
        self.border = RoundedRectangle(width=width, height=height, corner_radius=0.3, color=PRIMARY_COLOR)
        self.border.move_to(RIGHT*0.3)
        self.clip = RoundedRectangle(width=0.6, height=0.5, corner_radius=0.1, color=PRIMARY_COLOR,
                                     fill_opacity=1, fill_color=BACKGROUND_COLOR)
        self.clip.next_to(self.border, RIGHT, buff=-0.5)
        self.button = Circle(radius=0.1, color=SECONDARY_COLOR, fill_opacity=1)
        self.button.next_to(self.clip, ORIGIN)
        self.add(self.border, self.clip, self.button)

    def animate_in(self, scene):
        scene.play(FadeIn(self.border), FadeIn(self.clip), FadeIn(self.button))
        scene.play(Write(self.secret_key))
        scene.play(Write(self.address))

    def generate_random_secret_key(self, scene, final_value: int):
        rounds = 20
        for i in range(rounds + 1):
            random_key = randint(1, 40) if i < rounds else final_value
            new_secret_key_value: Text = Text(f"= {random_key}", font_size=24, font="Monaco", color=SECONDARY_COLOR)
            new_secret_key_value.next_to(self.secret_key_label, RIGHT)
            scene.play(
                ReplacementTransform(self.secret_key_value, new_secret_key_value),
                run_time=0.1
            )
            self.secret_key_value = new_secret_key_value
