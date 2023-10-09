from manim import Line

from zkmarek.video.constant import PRIMARY_COLOR
from zkmarek.video.mobjects.dot_on_curve import DotOnCurve


class LineThroughDots(Line):
    p1: DotOnCurve
    p2: DotOnCurve

    def __init__(self, p1: DotOnCurve, p2: DotOnCurve, **kwargs):
        super().__init__(
            start=p1.to_coord(),
            end=p2.to_coord(),
            color=PRIMARY_COLOR,
            **kwargs
        )
        self.set_z_index(1, family=True)

    def update_start_and_end(self, p1: DotOnCurve, p2: DotOnCurve):
        self.put_start_and_end_on(p1.to_coord(), p2.to_coord())
        self.p1 = p1
        self.p2 = p2

    def extend_to(self, y_bound=20):
        a = (self.p1.p.x - self.p2.p.x) / (self.p1.p.y - self.p2.p.y)
        b = self.p1.p.x - a * self.p1.p.y
        y = y_bound
        x = a * y + b
        self.put_start_and_end_on(self.p1.to_coord(), self.p2.ax.c2p(x, y))
