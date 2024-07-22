from manim import FadeIn, FadeOut, ImageMobject, LEFT, RIGHT, UP, DOWN, MathTex, Create, Group, MoveToTarget, Text, AddTextLetterByLetter, TransformMatchingShapes, VGroup
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import SECONDARY_COLOR, PRIMARY_FONT, PRIMARY_COLOR
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

        self.question = Text("?", font = PRIMARY_COLOR, font_size=100, color = PRIMARY_COLOR)
        self.tau = MathTex(r"\tau", font_size = 80, color = SECONDARY_COLOR)
        self.plonk = Text("PLONK", font_size=100, font=PRIMARY_FONT, color=SECONDARY_COLOR)
        self.groth = Text("Groth 16", font_size=80, font = PRIMARY_FONT, color = PRIMARY_COLOR)
        self.polynomial = MathTex(r"p(x) = x^5+9x^4+6", font_size = 60, color = SECONDARY_COLOR).shift(DOWN)
        self.polynomial2 =  MathTex(r"p(\tau) = \tau^5+9\tau^4+6", font_size = 60, color = SECONDARY_COLOR).shift(DOWN)
        self.polynomial3 =  MathTex(r"f(\tau) = \tau^{24}-84\tau^{10}-16", font_size = 60, color = SECONDARY_COLOR).shift(RIGHT*3+DOWN*2).scale(0.6)
        self.polynomial4 =  MathTex(r"g(\tau) = \tau^{32}-18\tau^{20}+63\tau^3", font_size = 60, color = SECONDARY_COLOR).shift(LEFT*3+DOWN*2).scale(0.6)
        self.polynomial5 =  MathTex(r"h(\tau) = \tau^{18}-17\tau^{19}+6\tau", font_size = 60, color = SECONDARY_COLOR).shift(DOWN*3).scale(0.6)

    def animate_in(self, scene):
        self.new_subsection(scene, "intro to tau", "data/sound/episode3/slide1-0.mp3")
        scene.play(FadeIn(self.person1, self.person2, self.person3, self.person4))
        scene.play(FadeIn(self.tau))
        scene.play(FadeIn(self.thumb1))
        scene.play(FadeIn(self.thumb3))
        scene.play(FadeIn(self.thumb2))
        scene.play(FadeIn(self.thumb4))

        self.new_subsection(scene, "trusted setup Plonk, zk snarks", "data/sound/episode3/slide1-1.mp3")
        self.person_wthumb = Group(self.person1, self.thumb1, self.person2, self.person3, self.person4, self.thumb2, self.thumb3, self.thumb4, self.tau)
        self.person_wthumb.generate_target()
        self.person_wthumb.target.shift(LEFT*4+UP*2.5).scale(0.2)
        scene.play(MoveToTarget(self.person_wthumb))
        self.animate_tree(scene)

        self.new_subsection(scene, "no one knows", "data/sound/episode3/slide1-2.mp3")
        scene.play(FadeIn(self.question))
        scene.wait(2)
        scene.play(FadeOut(self.question))
        self.new_subsection(scene, "calculate polynomial", "data/sound/episode3/slide1-3.mp3")
        self.person_wthumb.generate_target()
        self.person_wthumb.target.shift(RIGHT*4+DOWN).scale(2)
        scene.play(MoveToTarget(self.person_wthumb))

        scene.play(FadeIn(self.polynomial))
        scene.wait(0.7)
        scene.play(TransformMatchingShapes(VGroup(self.tau, self.polynomial), self.polynomial2))
        scene.wait(2)
        scene.play(FadeIn(self.polynomial3))
        scene.play(FadeIn(self.polynomial4))
        scene.play(FadeIn(self.polynomial5))
        scene.wait(1.3)

    def animate_out(self, scene):
        scene.play(FadeOut(self.person1, self.person2, self.person3, self.person4, self.polynomial2, self.thumb2, self.thumb3, self.thumb4, self.thumb1, self.polynomial3, self.polynomial4, self.polynomial5))

    def animate_tree(self, scene):
        tree = VerkleTree().scale(0.8).shift(UP*1.5)
        scene.play(AddTextLetterByLetter(self.plonk), run_time=1.5)
        scene.wait(0.4)
        scene.play(FadeOut(self.plonk), FadeIn(self.groth))
        scene.play(FadeOut(self.groth))
        scene.play(Create(tree))
        scene.wait(0.5)
        scene.play(FadeOut(tree))
