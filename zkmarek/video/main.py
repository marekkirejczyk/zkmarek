import os
from manim import Scene
from manimpango import register_font
from presentation import Presentation
from zkmarek.video.utils import get_slides_from_names, get_deck_name

from zkmarek.video.slides.episode1.episode1 import EPISODE1
from zkmarek.video.slides.episode2.episode2 import EPISODE2
from zkmarek.video.slides.episode3.episode3 import EPISODE3
from zkmarek.video.slides.episode4.episode4 import EPISODE4
from zkmarek.video.slides.episode5.episode5 import EPISODE5
from zkmarek.video.slides.e6.episode6 import EPISODE6
from zkmarek.video.slides.episode2.schnorr_episode import EPISODE7

from zkmarek.video.slides.short2.short2 import SHORT2

from zkmarek.video.slides.teaser.teaser1 import TEASER
from zkmarek.video.slides.teaser2.teaser2 import TEASER2
from zkmarek.video.slides.teaser3.teaser3 import TEASER3

DECKS = {
    "TEASER": TEASER,
    "E1": EPISODE1,
    "T2": TEASER2,
    "E2": EPISODE2,
    "T3": TEASER3,
    "E3": EPISODE3,
    "E4": EPISODE4,
    "E5": EPISODE5,
    "E6": EPISODE6,
    "SHORT2": SHORT2,
    "E7": EPISODE7,
}

DEFAULT_DECK = "E5"


class Episode6(Scene):
    def construct(self):
        register_font("data/brand/Oxanium-Regular.ttf")

        name = get_deck_name(DEFAULT_DECK)
        deck = DECKS[name]

        env_slides = dict(os.environ).get("SLIDES")
        slides = get_slides_from_names(env_slides, deck, globals())
        presentation = Presentation(self, deck, slides)
        presentation.print_slides(name)
        presentation.play()
