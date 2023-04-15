from manim import *

class LineThroughPoints(DashedLine):
    def __init__(self, p1, p2, **kwargs):
        DashedLine.__init__(self, start=p1.to_coord(),
                            end=p2.to_coord(), dashed_ratio=0.6, color=DARK_GREY, **kwargs)
