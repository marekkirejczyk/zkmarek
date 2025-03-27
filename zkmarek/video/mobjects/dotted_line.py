from manim import Line, Dot
class DottedLine(Line):

    """A dotted :class:`Line`.
    Parameters
    ----------
    args : Any
        Arguments to be passed to :class:`Line`
    dot_spacing : Optional[:class:`float`]
        Minimal spacing of the dots. The spacing is scaled up to fit the start and end of the line.
    dot_kwargs : Any
        Arguments to be passed to ::class::`Dot`
    kwargs : Any
        Additional arguments to be passed to :class:`Line`
    Examples
    --------
    .. manim:: DottedLineExample
        :save_last_frame:
        class DottedLineExample(Scene):
            def construct(self):
                # default dotted line
                dotted_1 = DottedLine(LEFT, RIGHT))
                # reduced spacing
                dotted_2 = DottedLine(LEFT, RIGHT, dot_spacing=.3).shift(.5*DOWN))
                # smaller and colored dots
                dotted_3 = DottedLine(LEFT, RIGHT, dot_kwargs=dict(radius=.04, color=YELLOW)).shift(DOWN))
        
                self.add(dotted_1, dotted_2, dotted_3)

    """

    def __init__(
        self,
        *args,
        dot_spacing=0.4,
        dot_kwargs={},
        **kwargs
    ):
        Line.__init__(self, *args, **kwargs)
        n_dots = int(self.get_length() / dot_spacing) + 1
        dot_spacing = self.get_length() / (n_dots - 1)
        unit_vector = self.get_unit_vector()
        start = self.start

        self.dot_points = [start + unit_vector * dot_spacing * x for x in range(n_dots)]
        self.dots = [Dot(point, **dot_kwargs) for point in self.dot_points]

        self.clear_points()

        self.add(*self.dots)

        self.get_start = lambda: self.dot_points[0]
        self.get_end = lambda: self.dot_points[-1]

    def get_first_handle(self):
        return self.dot_points[-1]

    def get_last_handle(self):
        return self.dot_points[-2]