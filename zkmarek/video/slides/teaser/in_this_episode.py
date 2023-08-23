from manim import DOWN, LEFT, Create, Rectangle, Text, VGroup, Write, mobject

from zkmarek.video.constant import HIGHLIGHT_COLOR, PRIMARY_COLOR, PRIMARY_FONT
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
            "1. Continuous elliptic curves",
            "2. Prime fields",
            "3. Discrete elliptic curves",
            "4. Groups and standards",
            "5. Digital signature",
        ]
        self.descriptions = [
            "Mathematical concept of elliptic curves ",
            "Arythmetics used in cryptography ",
            "Elliptic curves used in cryptography ",
            "Curves used in real-life protocols ",
            "Digital Signature Algorithm used in Ethereum"
        ]
        self.thumbnails = [
            ContinuousEllipticChart(include_details=False),
            Clock(hour=1),
            DiscreteEllipticChart(include_details=False),
            secp256k1_standard(),
            Signature()
        ]
        self.sounds = [
            "data/sound/episode/s3-1.m4a",
            "data/sound/episode/s3-2.m4a",
            "data/sound/episode/s3-3.m4a",
            "data/sound/episode/s3-4.wav",
            "data/sound/episode/s3-5.wav",
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
        self.play_sound(scene, "data/sound/episode/s3-0.m4a")
        scene.wait(1)
        for i, label in enumerate(self.labels):
            self.new_subsection(scene, self.titles[i], sound=self.sounds[i])
            scene.play(Create(self.thumbnails_borders[i]))
            self.thumbnails[i].animate_in(scene)
            scene.play(Write(label), run_time=2)
