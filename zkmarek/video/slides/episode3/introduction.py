from manim import FadeIn, FadeOut, ImageMobject, LEFT, RIGHT, UP, DOWN, MathTex, Create, Group, MoveToTarget
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import SECONDARY_COLOR
from zkmarek.video.mobjects.verkle_tree import VerkleTree

class Introduction(SlideBase):
    def __init__(self):
        super().__init__("Introduction to trusted setup")

    def construct(self):
        person = ImageMobject("zkmarek/video/slides/teaser3/person.png").scale(0.6)

        self.person1 = person.copy().shift(3*LEFT)
        self.person2 = person.copy().shift(3*RIGHT)
        self.person3 = person.copy().shift(2*UP)
        self.person4 = person.copy().shift(2*DOWN)

        thumb = ImageMobject("zkmarek/video/slides/episode3/Thumb_up.png").scale(0.3)

        self.thumb1 = thumb.copy().next_to(self.person1, UP+RIGHT).shift(DOWN+LEFT)
        self.thumb2 = thumb.copy().next_to(self.person2, UP+RIGHT).shift(DOWN+LEFT)
        self.thumb3 = thumb.copy().next_to(self.person3, UP+RIGHT).shift(DOWN+LEFT)
        self.thumb4 = thumb.copy().next_to(self.person4, UP+RIGHT).shift(DOWN+LEFT)

        self.tau = MathTex(r"\tau", font_size = 80, color = SECONDARY_COLOR)

        self.polynomial = MathTex(r"p(x) = a_n\cdot x^n + a_{n-1}\cdot x^{n-1} + \cdots + a_1 \cdot x + a_0", font_size = 50, color = SECONDARY_COLOR).shift(DOWN)
        self.polynomial1 = MathTex(r"p(\tau) = z", font_size = 50, color = SECONDARY_COLOR).next_to(self.polynomial, DOWN)

    def animate_in(self, scene):
        self.new_subsection(scene, "intro to tau", "data/sound/episode3/slide1-0.mp3")
        scene.play(FadeIn(self.person1, self.person2, self.person3, self.person4))
        scene.play(FadeIn(self.tau))
        scene.play(FadeIn(self.thumb1, self.thumb2, self.thumb3, self.thumb4))

        self.new_subsection(scene, "trusted setup Plonk, zk snarks", "data/sound/episode3/slide1-1.mp3")
        self.person_wthumb = Group(self.person1, self.thumb1, self.person2, self.person3, self.person4, self.thumb2, self.thumb3, self.thumb4, self.tau)
        self.person_wthumb.generate_target()
        self.person_wthumb.target.shift(LEFT*4+UP*2.5).scale(0.2)
        scene.play(MoveToTarget(self.person_wthumb))
        self.animate_tree(scene)

        self.new_subsection(scene, "any polynomial", "data/sound/episode3/slide1-2.mp3")
        self.person_wthumb.generate_target()
        self.person_wthumb.target.shift(RIGHT*2+DOWN*2).scale(2)
        scene.play(MoveToTarget(self.person_wthumb))
        scene.play(FadeIn(self.polynomial))
        scene.play(FadeIn(self.polynomial1))

    def animate_out(self, scene):
        scene.play(FadeOut(self.person_wthumb, self.polynomial, self.polynomial1))

    def animate_tree(self, scene):
        tree = VerkleTree().scale(0.8).shift(UP*1.5)
        scene.play(Create(tree))
        scene.wait(3)
        scene.play(FadeOut(tree))
