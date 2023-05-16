from manim import DARK_GREY, Line


class LineThroughPoints(Line):
    def __init__(self, p1, p2, **kwargs):
        Line.__init__(
            self,
            start=p1.to_coord(),
            end=p2.to_coord(),
            color=DARK_GREY,
            **kwargs
        )

    def update_start_and_end(self, p1, p2):
        self.put_start_and_end_on(p1.to_coord(), p2.to_coord())
