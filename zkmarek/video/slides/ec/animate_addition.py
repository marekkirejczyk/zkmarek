from manim import Dot, GrowFromPoint, Line, Scene

from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.video.mobjects.discreet_elliptic_chart import \
    DiscreteEllipticChart
from zkmarek.video.utils import find_x_min_max


class AnimateAddition:
    chart: DiscreteEllipticChart
    start: Dot
    end: Dot
    result: Dot
    line1: Line
    line2: Line

    def __init__(self, chart: DiscreteEllipticChart) -> None:
        self.chart = chart

    def animate_in(self, scene: Scene, c1: ECAffine, c2: ECAffine):
        c4 = c1 + c2
        c3 = -c4
        p1 = self.chart.affine_to_point(c1)
        p2 = self.chart.affine_to_point(c2)
        p3 = self.chart.affine_to_point(c3)
        p4 = self.chart.affine_to_point(c4)
        (s, e) = find_x_min_max([p1, p2, p3])
        self.line1 = Line(s, e)
        self.line2 = Line(e, p4)
        scene.play(GrowFromPoint(self.line1, point=s, run_time=5))
        scene.play(GrowFromPoint(self.line2, point=e, run_time=5))

    def animate_out(self, scene):
        self.chart.animate_remove(scene, self.line1)
