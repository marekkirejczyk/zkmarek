from manim import Line, Mobject, DOWN, LEFT, RIGHT, UP

class StrikeLine(Line):
    def __init__(self, mobj: Mobject):
        start=mobj.get_critical_point(DOWN + LEFT)
        end=mobj.get_critical_point(UP + RIGHT)
        super().__init__(start=start, end=end)
