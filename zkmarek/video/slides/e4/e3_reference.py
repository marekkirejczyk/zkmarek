from manim import LEFT, UP, DOWN, MathTex, Write, FadeOut, Text, RIGHT, ImageMobject, FadeIn, Rectangle, TransformMatchingShapes

from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR, HIGHLIGHT_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.episode3.ceremony import Ceremony
from zkmarek.video.slides.episode3.polynomial import Polynomial


class Episode3Reference(SlideBase):
    slide: Ceremony
    slide2: Polynomial

    def __init__(self):
        super().__init__("E3 Reference")

    def construct(self):
        self.title_label = Text("Previously on zkMarek", color = PRIMARY_COLOR, font = PRIMARY_FONT)
        self.title_label.to_edge(UP)
        self.group = ImageMobject("data/images/group.png")
        self.tau0 = MathTex(r"\tau_0", color = SECONDARY_COLOR, font_size=70).next_to(self.group, DOWN, buff=0)
        self.tau1 = MathTex(r"\tau_1", color = SECONDARY_COLOR, font_size=70).next_to(self.group, LEFT, buff=0.1)
        self.tau2 = MathTex(r"\tau_2", color = SECONDARY_COLOR, font_size=70).next_to(self.group, RIGHT, buff=0.1)

    def animate_in(self, scene):
        self.new_subsection(scene, "Intro", sound="data/sound/e4/slide0-1.mp3")
        scene.play(Write(self.title_label), run_time=1.2)
        scene.play(FadeIn(self.group), run_time=1)
        scene.play(Write(self.tau0), run_time=1)
        scene.play(Write(self.tau1), run_time=1)
        scene.play(Write(self.tau2), run_time=1)
        self.slide = Ceremony()
        self.slide.construct()
        self.slide2 = Polynomial()
        self.slide2.construct()


        self.new_subsection(scene, "to recap", "data/sound/e4/slide0-2.mp3")
        scene.play(FadeOut(self.tau0, self.tau1, self.tau2, self.group))
        self.slide.animate_miniature(scene)

        self.new_subsection(scene, "polynomial", "data/sound/e4/slide0-3.mp3")
        scene.wait(0.5)
        self.slide2.animate_miniature(scene)
        
        self.new_subsection(scene, "pairings", "data/sound/e4/slide0-4a.mp3")
        self.definition = MathTex(r"e(G_1, G_2) \rightarrow G_T", color = PRIMARY_COLOR).shift(UP*1.5)
        rectangle = Rectangle(color=PRIMARY_COLOR, width=15, height=8)
        text = Text("Pairings", color=SECONDARY_COLOR,
            font=PRIMARY_FONT, font_size=50).scale(0.65)
        self.add(rectangle, self.definition)
        text.next_to(rectangle, DOWN, buff=0.4)
        scene.play(FadeIn(text, rectangle, self.definition))
        self.scale(0.65)
    
        self.new_subsection(scene, "bilinearity", "data/sound/e4/slide0-4b.mp3")
        self.thesis = MathTex(r"a\cdot b = c \cdot d", color = HIGHLIGHT_COLOR).next_to(self.definition, DOWN)
        self.bilinearity = MathTex(r"e({{a}}\cdot {{G_1}}, {{b}} \cdot {{G_2}} ) \stackrel{?}{=} e({{c}} \cdot {{G_1}}, {{d}} \cdot {{G_2}})", color = SECONDARY_COLOR).next_to(self.thesis, DOWN)
        self.bilinearity2 = MathTex(r"{{e(}} {{a}} \cdot {{b}} \cdot {{G_1}}, {{G_2}} ) \stackrel{?}{=} {{e(}} {{c}} \cdot {{d}} \cdot {{G_1}}, {{G_2}} )", color = SECONDARY_COLOR).next_to(self.thesis, DOWN)
        self.bilinearity3 = MathTex(r"{{}} {{a}} \cdot {{b}} {{}} {{}} = {{}} {{c}} \cdot {{d}} {{}} {{}}").next_to(self.bilinearity2, DOWN)
        scene.play(Write(self.thesis))
        scene.wait(2)
        scene.play(Write(self.bilinearity))
        scene.wait(2)
        scene.play(TransformMatchingShapes(self.bilinearity, self.bilinearity2), run_time=2)
        scene.wait(1)
        scene.play(Write(self.bilinearity3))
        scene.wait(1)
        scene.play(FadeOut(self.bilinearity2, self.bilinearity3, self.thesis, self.definition, rectangle, text))
        
    def animate_out(self, scene):
        self.wait_for_sound(scene)
        scene.play(FadeOut(self.title_label))
