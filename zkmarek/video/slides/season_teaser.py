from manim import (DOWN, LEFT, RIGHT, UP, FadeIn, FadeOut, Rectangle, Text,
                   VGroup)

from zkmarek.video.mobjects.signature import Signature
from zkmarek.video.mobjects.verkle_tree import VerkleTree
from zkmarek.video.slides.common.slide_base import SlideBase


class Box(VGroup):
    def __init__(self, label):
        super().__init__()
        background_color = "#eadadb"
        fore_color = "#343434"
        self.rect = Rectangle(
            width=5,
            height=0.8,
            color=background_color,
            fill_color=background_color,
            fill_opacity=1)
        self.text = Text(label,
            font_size=28,
            color=fore_color)
        self.add(self.rect, self.text)




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
        font_size=32
        self.plonk = Text("PLONK", font_size=100, color="#646464")
        self.labels = [
            "Elliptic curves",
            "Pairings",
            "Commitment schemes",
            "zk-SNARKs",
            "Recursive proofs\n",
            "Arithmetization"]
        self.stack = Stack([Box(label) for label in self.labels])
        self.back_stack = Stack([Rectangle(width=5, height=0.8) for _ in range(6)])

        self.extras = [
            Signature(height=1),
            VGroup(
                Text("BLS signatures", font_size=font_size),
                Text("Account abstraction", font_size=font_size),
                Text("Smart Wallets", font_size=font_size))
                .arrange(direction=DOWN),
            VGroup(
                Text("Verkle Trees", font_size=font_size),
                VerkleTree()).arrange(direction=DOWN),
            Text("Tornado Cash", font_size=font_size),
            Text("zkRollups", font_size=font_size),
            Text("zkEVMs", font_size=font_size),
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
