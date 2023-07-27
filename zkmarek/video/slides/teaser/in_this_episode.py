from manim import DOWN, LEFT, Create, Rectangle, Text, VGroup, Write, mobject
from zkmarek.video.constant import PRIMARY_FONT, PRIMARY_COLOR, SECONDARY_COLOR, HIGHLIGHT2_COLOR, HIGHLIGHT_COLOR, BACKGROUND_COLOR

from zkmarek.video.mobjects.clock import Clock
from zkmarek.video.mobjects.continuous_elliptic_chart import \
    ContinuousEllipticChart
from zkmarek.video.mobjects.discreet_elliptic_chart import \
    DiscreteEllipticChart
from zkmarek.video.mobjects.signature import Signature
from zkmarek.video.mobjects.standard import secp256k1_standard

from ..common.slide_base import SlideBase


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
            "Mathematical concept of Elliptic Curves ",
            "Arythmetics used in cryptography ",
            "Elliptic Curves used in cryptography ",
            "Curves used in real-life protocols ",
            "Digital signature algorithm used in Ethereum"
        ]
        self.thumbnails = [
            ContinuousEllipticChart(include_details=False),
            Clock(hour=1),
            DiscreteEllipticChart(include_details=False),
            secp256k1_standard(),
            Signature()
        ]
        self.sounds = [
            "data/sound/episode/s3/p1.m4a",
            "data/sound/episode/s3/p2.m4a",
            "data/sound/episode/s3/p3.m4a",
            "data/sound/episode/s3/p4.m4a",
            "data/sound/episode/s3/p5.m4a",
        ]

    def construct(self):
        self.labels = []
        for i in range(0, len(self.titles)):
            title = Text(self.titles[i], font=PRIMARY_FONT, color=PRIMARY_COLOR)
            description = Text(self.descriptions[i], font_size=24,
                font=PRIMARY_FONT, color=HIGHLIGHT_COLOR)
            description.next_to(title, DOWN)
            description.align_to(title, LEFT)
            self.labels.append(VGroup(title, description))

        for thumbnail in self.thumbnails:
            rect = Rectangle(width=1.5, height=1.25, color=PRIMARY_COLOR)
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
