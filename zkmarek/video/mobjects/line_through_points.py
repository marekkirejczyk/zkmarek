from manim import DARK_GREY, Line
from zkmarek.video.mobjects.dot_on_curve import DotOnCurve


class LineThroughDots(Line):
    def __init__(self, p1: DotOnCurve, p2: DotOnCurve, **kwargs):
        super().__init__(
            start=p1.to_coord(),
            end=p2.to_coord(),
            color=DARK_GREY,
            **kwargs
        )
        self.set_z_index(1, family=True)

    def update_start_and_end(self, p1, p2):
        self.put_start_and_end_on(p1.to_coord(), p2.to_coord())
