from manim import ImageMobject, FadeIn, DOWN, FadeOut, RIGHT, LEFT, Text, UP
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR, PRIMARY_FONT

class SubscribeSponsors(SlideBase):
    def __init__(self) -> None:
        super().__init__("Subscribe and sponsors")
        
    def construct(self):
        self.title_text = Text(
            "youtube.com/@zkmarek",
            font=PRIMARY_FONT,
            color=PRIMARY_COLOR,
            t2c={"[:12]": PRIMARY_COLOR, "[12:]": SECONDARY_COLOR},
        ).move_to(1.5 * UP)
        self.button = ImageMobject("data/subscribe/normal.png").scale(0.4)
        self.button_clicked = ImageMobject(
            "data/subscribe/clicked.png", z_index=1
        ).scale(0.4)
        self.logo = ImageMobject("data/brand/logo.png").scale(1.5)
        self.vlayer = ImageMobject(
            "data/images/Logo_304_color_on_dark.png"
        ).scale(0.8).next_to(self.logo, RIGHT, buff = 0.2)
        self.ecosystem = ImageMobject(
            "data/images/ecosystem_support_program.png"
        ).scale(0.17).next_to(self.logo, LEFT, buff = 0.2)
        
    def animate_in(self, scene):
        self.click_button(scene)
    
    def click_button(self, scene):
        self.button.shift(DOWN * 5)
        self.button_clicked.shift(DOWN * 5)
        scene.add(self.button, self.button_clicked)
        scene.add(self.logo, self.vlayer, self.ecosystem, self.title_text)
        scene.play(FadeIn(self.button), run_time=0.5)

        # Source of sound under Creative Commons 0 License.
        # https://freesound.org/people/joebro10/sounds/219318/
        scene.add_sound("data/sound/click.wav", gain=20)
        scene.play(FadeIn(self.button_clicked), run_time=0.2)
        scene.play(FadeOut(self.button_clicked), run_time=0.2)
        