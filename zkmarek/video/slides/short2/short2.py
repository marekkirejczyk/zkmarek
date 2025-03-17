from zkmarek.video.slides.short2.full_videos import FullVideos
from zkmarek.video.slides.short2.previously import Previously
from zkmarek.video.slides.short2.sponsors_subscribe import SubscribeSponsors
from zkmarek.video.slides.common.title import TitleSlide

SHORT2 = [
    TitleSlide("Vector commitment in 90 s", sound = "data/sound/e6/slide1-0.mp3", wait_time=0.5, font_size=70,
               background_sound="data/sound/e6/background_short.mp3"),
    Previously(),
    FullVideos(),
    SubscribeSponsors()
]