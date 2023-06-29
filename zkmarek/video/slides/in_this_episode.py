from manim import DOWN, LEFT, Create, Rectangle, Text, VGroup, Write, mobject

from zkmarek.video.mobjects.clock import Clock
from zkmarek.video.mobjects.continuous_elliptic_chart import \
    ContinuousEllipticChart
from zkmarek.video.mobjects.discreet_elliptic_chart import \
    DiscreteEllipticChart
from zkmarek.video.mobjects.signature import Signature
from zkmarek.video.mobjects.standard import secp256k1_standard

from .common.slide_base import SlideBase


class InThisEpisode(SlideBase):
    titles: list[str]
    descriptions: list[Text]
    thumbnails: list[mobject]

    labels: list[VGroup]
    thumbnails_borders: list[Rectangle]

    def __init__(self):
        super().__init__(title="In this episode")
        self.description_labels = []
        self.thumbnails = []
        self.thumbnails_borders = []
        self.titles = [
            "1. Continuous Elliptic Curves",
            "2. Prime Fields",
            "3. Discrete Elliptic Curves",
            "4. Groups and standards",
            "5. Digital signature"
        ]
        self.descriptions = [
            "Mathematical concept of Elliptic Curves living in the realm of reals ",
            "Arythmetic of big prime numbers used in cryptography",
            "Discrete Elliptic Curves build on Prime Fields used in cryptography ",
            "Curves and groups standards applied in real-life protocols ",
            "Using Elliptic Curves to create keys and digital signatures "
        ]
        self.thumbnails = [
            ContinuousEllipticChart(include_details=False),
            Clock(hour=1),
            DiscreteEllipticChart(include_details=False),
            secp256k1_standard(),
            Signature()
        ]
        self.sounds = [
            "data/sound/in_this_episode/p1.m4a",
            "data/sound/in_this_episode/p2.m4a",
            "data/sound/in_this_episode/p3.m4a",
            "data/sound/in_this_episode/p4.m4a",
            "data/sound/in_this_episode/p5.m4a",
        ]

    def construct(self):
        self.labels = []
        for i in range(0, len(self.titles)):
            title = Text(self.titles[i])
            description = Text(self.descriptions[i], font_size=24)
            description.next_to(title, DOWN)
            description.align_to(title, LEFT)
            self.labels.append(VGroup(title, description))

        for thumbnail in self.thumbnails:
            rect = Rectangle(width=1.5, height=1.25)
            self.thumbnails_borders.append(rect)

        for (thumb, title) in zip(self.thumbnails_borders, self.labels):
            self.add(thumb, title)

        self.arrange_in_grid(cols=2, col_alignments="ll", row_alignments="uuuuu")

        for i, thumbnail in enumerate(self.thumbnails):
            thumbnail.scale(0.15)
            thumbnail.move_to(self.thumbnails_borders[i].get_center())
            self.add(thumbnail)

    def animate_in(self, scene):
        for i, label in enumerate(self.labels):
            self.new_subsection(scene, self.titles[i], sound=self.sounds[i])
            scene.play(Create(self.thumbnails_borders[i]))
            self.thumbnails[i].animate_in(scene)
            scene.play(Write(label))
