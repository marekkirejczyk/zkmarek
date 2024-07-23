from manim import FadeIn, FadeOut, LEFT, RIGHT, DOWN, MathTex, ImageMobject, AddTextLetterByLetter, Text
from zkmarek.video.constant import SECONDARY_COLOR, PRIMARY_COLOR

from zkmarek.video.slides.common.slide_base import SlideBase

class ToxicWaste(SlideBase):
    def __init__(self):
        super().__init__("Evaluating the polynomial")

    def construct(self):
        self.group = ImageMobject("zkmarek/video/slides/episode3/group.png")
        self.lock_open = ImageMobject("zkmarek/video/slides/episode3/Lock_Open.png").scale(0.2)
        self.angel = ImageMobject("zkmarek/video/slides/episode3/Angel.png").shift(RIGHT*2)
        self.person_tau0 = MathTex(r"\tau_0", color = SECONDARY_COLOR, font_size=70).next_to(self.group, DOWN, buff=0.01)
        self.person_tau1 = MathTex(r"\tau_1", color = SECONDARY_COLOR, font_size=70).next_to(self.group, LEFT, buff=0.1)
        self.person_tau2 = MathTex(r"\tau_2", color = SECONDARY_COLOR, font_size=70).next_to(self.group, RIGHT, buff=0.1)
        self.person_tau3 = MathTex(r"\tau_3", color = SECONDARY_COLOR, font_size=70).next_to(self.angel, RIGHT, buff=0.1)
        
        self.lock1 = self.lock_open.copy().next_to(self.group, DOWN, buff=0.01).shift(LEFT*0.3)
        self.lock2 = self.lock_open.copy().next_to(self.group, LEFT, buff=0.01).shift(LEFT*0.3)
        self.lock3 = self.lock_open.copy().next_to(self.group, RIGHT, buff=0.01).shift(RIGHT*0.3)

        self.toxic = Text("Toxic waste", font=PRIMARY_COLOR, font_size=70, color = PRIMARY_COLOR).next_to(self.group, DOWN)

    def animate_in(self, scene):
        self.new_subsection(scene, "toxic waste", "data/sound/episode3/slide7.5-0.mp3")
        scene.play(FadeIn(self.group))
        scene.play(FadeIn(self.person_tau0))
        scene.play(FadeIn(self.person_tau1))
        scene.play(FadeIn(self.person_tau2))
        scene.wait(1)
        scene.play(FadeIn(self.lock1))
        scene.play(FadeIn(self.lock2))
        scene.play(FadeIn(self.lock3))
        scene.wait(1)
        scene.play(AddTextLetterByLetter(self.toxic), run_time=2.5)
        scene.wait(2)
        scene.play(FadeOut(self.toxic))
        scene.play(FadeIn(self.angel, self.person_tau3))
        scene.wait(2)
    
    def animate_out(self, scene):
        scene.play(FadeOut(self.angel, self.person_tau0, self.person_tau1, self.person_tau2, self.person_tau3, self.group, self.lock1, self.lock2, self.lock3))