from random import randint

from manim import (LEFT, ORIGIN, RIGHT, Circle, FadeIn, RoundedRectangle, Text,
                   VGroup, Write, ReplacementTransform, Scene, DOWN, Animation)

from zkmarek.video.constant import (BACKGROUND_COLOR, HIGHLIGHT_COLOR,
                                    PRIMARY_COLOR, SECONDARY_COLOR, PRIMARY_FONT)


class Wallet(VGroup):
    border: RoundedRectangle
    clip: RoundedRectangle
    button: Circle
    secret_key: VGroup
    secret_key_label: Text
    secret_key_value: Text
    address: VGroup
    address_label: Text
    address_value: Text

    def __init__(self, secret_key="", address=""):
        super().__init__()
        self.secret_key_label = Text(secret_key, font_size=24, font=PRIMARY_FONT, color=SECONDARY_COLOR)
        self.secret_key_value = Text("", font_size=24, font=PRIMARY_FONT, color=SECONDARY_COLOR)
        self.secret_key_value.next_to(self.secret_key_label, RIGHT)
        self.secret_key = VGroup(self.secret_key_label, self.secret_key_value)
        self.secret_key.shift(1.7 * LEFT)

        self.address_label = Text(address, font_size=24, font=PRIMARY_FONT, color=HIGHLIGHT_COLOR)
        self.address_value = Text("", font_size=14, font=PRIMARY_FONT, color=HIGHLIGHT_COLOR)
        self.address_value.next_to(self.address_label, RIGHT)
        self.address = VGroup(self.address_label, self.address_value)
        self.address.shift(1.7 * LEFT)
        self.add(self.secret_key, self.address)
        self.arrange_in_grid(cols=1, cell_alignment=LEFT)

        width = self.get_width() + 4
        height = self.get_height() + 2
        self.border = RoundedRectangle(width=width, height=height, corner_radius=0.3, color=PRIMARY_COLOR)
        self.border.move_to(RIGHT * 0.3)
        self.clip = RoundedRectangle(width=0.6, height=0.5, corner_radius=0.1, color=PRIMARY_COLOR,
                                     fill_opacity=1, fill_color=BACKGROUND_COLOR)
        self.clip.next_to(self.border, RIGHT, buff=-0.5)
        self.button = Circle(radius=0.1, color=SECONDARY_COLOR, fill_opacity=1)
        self.button.next_to(self.clip, ORIGIN)
        self.add(self.border, self.clip, self.button)

    def animate_in(self, scene: Scene):
        scene.play(FadeIn(self.border), FadeIn(self.clip), FadeIn(self.button))
        scene.play(Write(self.secret_key))
        scene.play(Write(self.address))

    def animate_random_secret_key(self, scene: Scene, final_value: int, rand_max: int):
        rounds = 20
        for key in [str(randint(0, rand_max)) for i in range(rounds)] + [str(final_value), hex(final_value)]:
            new_secret_key_value: Text = Text(f"{key}", font_size=24, font=PRIMARY_FONT, color=SECONDARY_COLOR)
            new_secret_key_value.next_to(self.secret_key_label, RIGHT)
            last = key.startswith('0x')
            if last:
                scene.wait()
            scene.play(
                ReplacementTransform(self.secret_key_value, new_secret_key_value),
                run_time=1 if last else 0.1
            )
            self.secret_key_value = new_secret_key_value

    def animate_address_value(self, scene: Scene, address_value: str, with_animation: Animation):
        new_address_value = Text(address_value, font_size=14, font=PRIMARY_FONT, color=HIGHLIGHT_COLOR)
        new_address_value.next_to(self.address_label, RIGHT)
        new_address_value.shift(0.05 * DOWN)
        scene.play(ReplacementTransform(self.address_value, new_address_value), with_animation)
        self.address_value = new_address_value
