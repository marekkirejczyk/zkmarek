from typing import Optional
from manim import VGroup, FadeOut
from pydub import AudioSegment

class SlideBase(VGroup):
    title: str = ""
    start_time: Optional[float]
    current_sound: Optional[str]

    def __init__(self, title:str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.title = title
        self.start_time = None
        self.current_sound = None

    def __str__(self):
        return self.title

    def construct(self):
        pass

    def new_subsection(self, scene, title, sound=None):
        if self.current_sound is not None:
            end_time = scene.renderer.time
            sound_len = get_sound_length(self.current_sound)
            wait_time = sound_len - end_time + self.start_time
            scene.wait(wait_time)
            self.start_time = None
            self.current_sound = None

        scene.next_section(f"{self.title}: {title}")

        if sound is not None:
            self.start_time = scene.renderer.time
            self.current_sound = sound
            scene.add_sound(sound)


    def animate_in(self, scene):
        pass

    def animate_out(self, scene):
        scene.play(FadeOut(self))


def get_sound_length(path):
    return len(AudioSegment.from_file(path))/1000
