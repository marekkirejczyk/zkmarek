from manim import FadeIn, FadeOut, LEFT, RIGHT, DOWN, UP, MathTex, ImageMobject, AddTextLetterByLetter, Text, Group, MoveToTarget
from zkmarek.video.constant import SECONDARY_COLOR, PRIMARY_COLOR, PRIMARY_FONT

from zkmarek.video.slides.common.slide_base import SlideBase

class ToxicWaste(SlideBase):
    def __init__(self):
        super().__init__("Evaluating the polynomial")

    def construct(self):
        self.group = ImageMobject("data/images/group.png").shift(UP*2)
        self.lock_open = ImageMobject("data/images/Lock_Open.png").scale(0.3)
        self.angel = ImageMobject("data/images/Angel.png").shift(RIGHT*3).scale(0.75).shift(UP*0.3)
        self.person_tau0 = MathTex(r"\tau_0", color = SECONDARY_COLOR, font_size=80).next_to(self.group, DOWN, buff=0.01)
        self.person_tau1 = MathTex(r"\tau_1", color = SECONDARY_COLOR, font_size=80).next_to(self.group, LEFT, buff=0.1)
        self.person_tau2 = MathTex(r"\tau_2", color = SECONDARY_COLOR, font_size=80).next_to(self.group, RIGHT, buff=0.1)
        self.person_tau3 = MathTex(r"\tau_3", color = SECONDARY_COLOR, font_size=80).next_to(self.angel, RIGHT, buff=0.1)
        
        self.lock1 = self.lock_open.copy().next_to(self.group, DOWN, buff=0.01).shift(LEFT*0.8).shift(UP*0.3)
        self.lock2 = self.lock_open.copy().next_to(self.group, LEFT, buff=0.01).shift(LEFT*0.8)
        self.lock3 = self.lock_open.copy().next_to(self.group, RIGHT, buff=0.01).shift(RIGHT*0.8)
        self.toxic = Text("Toxic waste", font=PRIMARY_FONT, font_size=70, color = PRIMARY_COLOR).next_to(self.group, DOWN).shift(DOWN)
        self.lock = ImageMobject("data/images/Locked@2x.png").to_edge(RIGHT).scale(0.3).next_to(self.person_tau3, RIGHT, buff = 0.1)
    def animate_in(self, scene):
        self.new_subsection(scene, "toxic waste", "data/sound/episode3/slide7.5-0.mp3")
        scene.play(FadeIn(self.group))
        scene.play(FadeIn(self.person_tau0))
        scene.play(FadeIn(self.person_tau1))
        scene.play(FadeIn(self.person_tau2))
        scene.play(FadeIn(self.lock1))
        scene.play(FadeIn(self.lock2))
        scene.play(FadeIn(self.lock3))
        
        self.new_subsection(scene, "toxic waste", "data/sound/episode4/slide7.5-1.mp3")
        scene.play(AddTextLetterByLetter(self.toxic), run_time=2.5)
        scene.wait(2.5)
        scene.play(FadeOut(self.toxic))
        self.group_person = Group(self.group, self.person_tau0, self.person_tau1, self.person_tau2, self.lock1, self.lock2, self.lock3)
        self.group_person.generate_target()
        self.group_person.target.move_to(LEFT*2)
        scene.play(MoveToTarget(self.group_person))
        scene.play(FadeIn(self.angel, self.person_tau3))
        scene.wait(1.5)
        scene.play(FadeIn(self.lock))
        scene.wait(3.5)
    
    def animate_out(self, scene):
        scene.play(FadeOut(self.angel, self.person_tau0, self.person_tau1, self.person_tau2, self.person_tau3, self.group, self.lock1, self.lock2, self.lock3))