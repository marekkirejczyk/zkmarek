from manim import (DOWN, LEFT, RIGHT, UP, Create, FadeIn, FadeOut, Graph,
                   Rectangle, Text, VGroup)

from zkmarek.video.mobjects.signature import Signature
from zkmarek.video.slides.common.slide_base import SlideBase
import networkx as nx


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
    def __init__(self, labels):
        super().__init__()
        for item in labels:
            self.add(Box(item))
        self.arrange(direction=UP)

class Tree(Graph):
    def __init__(self):
        G = nx.Graph()
        G.add_node("ROOT")
        for i in range(5):
            G.add_node("Child_%i" % i)
            G.add_node("Grandchild_%i" % i)
            G.add_node("Greatgrandchild_%i" % i)
            G.add_edge("ROOT", "Child_%i" % i)
            G.add_edge("Child_0", "Grandchild_%i" % i)
            G.add_edge("Grandchild_1", "Greatgrandchild_%i" % i)
        super().__init__(list(G.nodes), list(G.edges), layout="tree", root_vertex="ROOT")


class SeasonTeaser(SlideBase):

    stack: Stack

    def __init__(self):
        super().__init__("Season Teaser")

    def construct(self):
        font_size=font_size=32
        self.stack = Stack([
            "Elliptic curves",
            "Pairings",
            "Commitment schemes",
            "SNARKS",
            "Recursive proofs\n",
            "Arithmetization"])
        self.extras = [
            Signature(height=1),
            VGroup(
                Text("BLS signatures", font_size=font_size),
                Text("Account abstraction", font_size=font_size),
                Text("Smart Wallets", font_size=font_size))
                .arrange(direction=DOWN),
            VGroup(
                Text("Verkle Trees", font_size=font_size),
                Tree()).arrange(direction=DOWN),
            Text("Tornado Cash", font_size=font_size),
            Text("zkRollups", font_size=font_size),
            Text("zkEVMs", font_size=font_size),
        ]
        self.stack.align_on_border(LEFT, buff=1)

    def animate_in(self, scene):
        for i, item in enumerate(self.stack):
            if i > 0:
                scene.play(FadeOut(self.extras[i-1]))
            self.new_subsection(scene, item)
            scene.play(FadeIn(item))
            self.new_subsection(scene, f"{item} - extras")
            self.extras[i].move_to(RIGHT * 3)
            scene.play(FadeIn(self.extras[i]))
