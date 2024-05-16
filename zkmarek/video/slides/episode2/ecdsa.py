from manim import DOWN, UP, Code, FadeOut, Text, Write, Scene, Indicate
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR

from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.utils import find_in_code


class ECDSA(SlideBase):
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
        self.new_subsection(scene, "ECDSA sign", "data/sound/episode2/slide11-0.mp3")
        scene.play(Write(self.title_text))
        scene.play(Write(self.code))
        scene.wait(3.9)
        sign = ["secret_key: int", "msg_hash: int", "k: int"]
        for part in sign:
            self.indicate_code(scene, part, 0, run_time=1)
            scene.wait(0.5)
        scene.wait(2.2)
        tuple_sign = ["tuple[int, int, int]"]
        self.indicate_code(scene, tuple_sign[0], 0, run_time=1)
        self.new_subsection(scene, "r, s, v", "data/sound/episode2/slide11-1.mp3")

        values = [
            "r: int = R.x.value % n",
            "s = (pow(k, -1, n) * (msg_hash + (r * int(hex(secret_key), 16)))) % n",
            "v = R.y.value % 2",
        ]
        self.indicate_code(scene, values[0], 0, run_time=0.7)
        self.indicate_code(scene, values[1], 0, run_time=0.7)
        scene.wait(5)
        self.indicate_code(scene, values[2], 0, run_time=0.7)
        flipping = ["s = n - s", "s * 2 >= n:"]
        self.indicate_code(scene, flipping[0], 0, run_time=0.7)
        scene.wait(1)
        self.indicate_code(scene, flipping[1], 0, run_time=0.7)
        scene.wait(2)
        returns = ["r,", "s,", "27 + v"]
        self.indicate_code(scene, returns[0], 0, run_time=0.5)
        self.indicate_code(scene, returns[1], 0, run_time=0.5)
        self.indicate_code(scene, returns[2], 0, run_time=0.5)
        scene.wait(0.5)

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
