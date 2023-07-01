from manim import (DOWN, LEFT, RIGHT, UP, FadeIn, FadeOut, Rectangle, Text,
                   VGroup)

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
        def label(text):
            return Text(text,
                font_size=32,
                font=PRIMARY_FONT,
                color=SECONDARY_COLOR)

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
            Signature(height=1),
            VGroup(
                label("BLS signatures"),
                label("Account abstraction"),
                label("Smart Wallets"))
                .arrange(direction=DOWN),
            VGroup(
                label("Verkle Trees"),
                VerkleTree().scale(0.5)).arrange(direction=DOWN),
            label("Tornado Cash"),
            label("zkRollups"),
            label("zkEVMs"),
        ]
        self.stack.align_on_border(LEFT, buff=1)
        self.back_stack.align_on_border(LEFT, buff=1)
        self.plonk.move_to(RIGHT * 3)

    def animate_in(self, scene):
        scene.play(FadeIn(self.plonk))
        scene.play(FadeIn(self.back_stack))
        for i, item in enumerate(self.stack):
            self.new_subsection(scene, item)
            if i > 0:
                scene.play(FadeOut(self.extras[i-1]))
            else:
                scene.play(FadeOut(self.plonk))
            scene.play(FadeIn(item))
            self.new_subsection(scene, f"{item} - extras")
            self.extras[i].move_to(RIGHT * 3)
            scene.play(FadeIn(self.extras[i]))
