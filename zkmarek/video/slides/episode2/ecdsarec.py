from manim import DOWN, UP, Code, FadeOut, Text, Write, Indicate, Scene
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR

from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.utils import find_in_code


class ECDSARec(SlideBase):
    title_text: Text
    title: str
    code: Code
    code_path: str
    kwargs: dict

    def __init__(self, title, code_path, **kwargs):
        super().__init__(title)
        self.code_path = code_path
        self.kwargs = kwargs
        self.title = title

    def construct(self):
        self.title_text = Text(self.title, font=PRIMARY_FONT, color=PRIMARY_COLOR)
        code_params = {
            "background": "window",
            "insert_line_no": True,
            "font": "Monospace",
            "font_size": 18,
            "margin": 0.2,
            "style": "fruity",
            "line_no_buff": 0.2,
        }

        code_params.update(self.kwargs)

        self.code = Code(self.code_path, **code_params)
        self.title_text.to_edge(UP, buff=1)
        self.code.next_to(self.title_text, DOWN, buff=0.5)

    def __str__(self):
        return f"{self.title} (CODE)"

    def animate_in(self, scene):
        scene.play(Write(self.title_text))
        scene.play(Write(self.code))
        self.new_subsection(scene, "ECDSA recover", "data/sound/episode2/slide11-2.mp3")
        scene.wait(2)
        recover = ["message: int", "r: int", "s: int", "v: int"]
        self.indicate_code(scene, recover[0], 0, run_time=0.7)
        scene.wait(1.2)
        self.indicate_code(scene, recover[1], 0, run_time=0.7)
        self.indicate_code(scene, recover[2], 0, run_time=0.7)
        self.indicate_code(scene, recover[3], 0, run_time=0.7)

        scene.wait(1)
        self.new_subsection(scene, "ecrecover", "data/sound/episode2/slide11-3.mp3")
        scene.wait(3.1)
        eliptic = [
            "ECAffine.from_x(r, v, curve)",
            "r,",
            "u1 = -message * r_inverse % n",
            "u2 = s * r_inverse % n",
            "v,",
            "Q = generator * u1 + R * u2",
        ]
        self.indicate_code(scene, eliptic[0], 0, run_time=0.7)
        scene.wait(1.8)
        self.indicate_code(scene, eliptic[1], 0, run_time=0.7)
        scene.wait(3.7)
        self.indicate_code(scene, eliptic[4], 0, run_time=0.7)
        scene.wait(4)
        self.indicate_code(scene, eliptic[2], 0, run_time=0.7)
        self.indicate_code(scene, eliptic[3], 0, run_time=0.7)
        self.indicate_code(scene, eliptic[5], 0, run_time=0.9)
        self.new_subsection(scene, "generate k", "data/sound/episode2/slide11-4.mp3")

        self.new_subsection(scene, "ending", "data/sound/episode2/slide11-5.mp3")
        scene.wait(3.5)

    def animate_out(self, scene):
        scene.play(FadeOut(self.code))
        scene.play(FadeOut(self.title_text))

    def indicate_code(self, scene: Scene, fragment: str, index=0, run_time=0.5):
        chars = find_in_code(self.code, fragment)
        scene.play(Indicate(chars[index]), color=SECONDARY_COLOR, run_time=run_time)

    @staticmethod
    def _get_code(path: str, font_size: int):
        return Code(
            path,
            font_size=font_size,
            background="rectangle",
            insert_line_no=False,
            font="Monospace",
            margin=0.2,
            style="fruity",
            line_no_buff=0.2,
        )
