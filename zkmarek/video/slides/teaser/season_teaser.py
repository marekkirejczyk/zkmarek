from manim import (DOWN, LEFT, RIGHT, UP, AddTextLetterByLetter, Create,
                   FadeIn, FadeOut, Rectangle, RemoveTextLetterByLetter, Text,
                   VGroup, Indicate)

from zkmarek.video.constant import (BACKGROUND_COLOR, PRIMARY_COLOR,
                                    PRIMARY_FONT, SECONDARY_COLOR)
from zkmarek.video.mobjects.signature import Signature
from zkmarek.video.mobjects.verkle_tree import VerkleTree
from zkmarek.video.slides.common.slide_base import SlideBase

class Box(VGroup):
    def __init__(self, label):
        super().__init__()
        self.rect = Rectangle(
            width=5,
            height=0.8,
            color=BACKGROUND_COLOR,
            fill_color=BACKGROUND_COLOR,
            fill_opacity=1)
        self.text = Text(label,
            font_size=28,
            font=PRIMARY_FONT,
            color=PRIMARY_COLOR)
        self.add(self.rect, self.text)

class EmptyBox(Rectangle):
    def __init__(self):
        super().__init__(width=5, height=0.8, color=BACKGROUND_COLOR)

class Stack(VGroup):
    def __init__(self, items):
        super().__init__()
        for item in items:
            self.add(item)
        self.arrange(direction=UP)


class SeasonTeaser(SlideBase):
    stack: Stack
    back_stack: Stack

    def __init__(self):
        super().__init__("Season Teaser")

    def construct(self):
        self.plonk = Text("PLONK", font_size=100,
            font=PRIMARY_FONT,
            color=SECONDARY_COLOR)
        self.labels = [
            "Elliptic curves",
            "Pairings",
            "Commitment schemes",
            "zk-SNARKs",
            "Recursive proofs\n",
            "Arithmetization"]
        self.stack = Stack([Box(label) for label in self.labels])
        self.back_stack = Stack([EmptyBox() for _ in range(6)])

        self.extras = [
            self.animate_1,
            self.animate_2,
            self.animate_3,
            self.animate_4,
            self.animate_5,
            self.animate_6,
        ]
        self.stack.align_on_border(LEFT, buff=1)
        self.back_stack.align_on_border(LEFT, buff=1)

    def label(self, text):
        return Text(text,
            font_size=32,
            font=PRIMARY_FONT,
            color=SECONDARY_COLOR)

    def animate_1(self, scene):
        signature = Signature(height=1).move_to(RIGHT * 3)
        signature.animate_in(scene)
        return signature

    def animate_2(self, scene):
        group = VGroup(
            self.label("BLS signatures"),
            self.label("Account abstraction"),
            self.label("Smart Wallets")).arrange(direction=DOWN).move_to(RIGHT * 3)
        for i in range(3):
            scene.wait(1)
            scene.play(AddTextLetterByLetter(group[i]))
        return group

    def animate_3(self, scene):
        group = VGroup(
            self.label("Verkle Trees"),
            VerkleTree().scale(0.5)).arrange(direction=DOWN).move_to(RIGHT * 3)
        scene.wait(1)
        scene.play(AddTextLetterByLetter(group[0]), run_time=2)
        scene.play(Create(group[1]), run_time=3)
        scene.wait(2)
        return group

    def animate_4(self, scene):
        scene.wait(1)
        result = self.label("Tornado Cash").move_to(RIGHT * 3)
        scene.play(AddTextLetterByLetter(result))
        scene.wait(4)
        return result

    def animate_5(self, scene):
        scene.wait(1)
        result = self.label("zkRollups").move_to(RIGHT * 3)
        scene.play(AddTextLetterByLetter(result))
        scene.wait(3.5)
        return result

    def animate_6(self, scene):
        result = self.label("zkEVMs").move_to(RIGHT * 3)
        scene.play(AddTextLetterByLetter(result))
        scene.wait(3)
        return result

    def animate_in(self, scene):
        self.play_sound(scene, "data/sound/teaser/s3-0.wav")
        scene.wait(0.5)
        scene.play(AddTextLetterByLetter(self.plonk), run_time=2)
        scene.wait(0.5)
        scene.play(self.plonk.animate.move_to(RIGHT * 3), run_time=2)
        scene.wait(1)
        scene.play(FadeIn(self.back_stack), run_time=2)
        scene.wait(1)
        scene.play(RemoveTextLetterByLetter(self.plonk), run_time=2)
        for i, item in enumerate(self.stack):
            if i > 0:
                scene.play(FadeOut(self.extras[i-1]))
            self.new_subsection(scene, item,
                sound=f"data/sound/teaser/s3-{i+1}.wav")
            scene.play(FadeIn(item))
            self.extras[i] = self.extras[i](scene)

    def animate_miniature(self, scene):
        rectangle = Rectangle(color=PRIMARY_COLOR, width=15, height=8)
        tree = VerkleTree().scale(0.2)
        text = Text("Zero Knowledge Proofs context", color=SECONDARY_COLOR,
            font=PRIMARY_FONT, font_size=70)
        self.add(rectangle, self.stack)
        self.scale(0.4)
        text.scale(0.4)
        self.move_to(RIGHT * 3.4)
        tree.next_to(self.stack, RIGHT, buff=0.2)
        text.next_to(rectangle, DOWN, buff=0.4)
        scene.play(FadeIn(self), Create(tree), FadeIn(text))
        self.rest = [tree, text]

