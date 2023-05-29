from manim import Scene

from zkmarek.video.mobjects.discreet_elliptic_chart import DiscreteEllipticChart
from zkmarek.video.mobjects.sidebar import Sidebar
from zkmarek.video.slides.ec.animate_addition import AnimateAddition
from zkmarek.video.slides.common.slide_base import SlideBase


class Addition(SlideBase):
    chart: DiscreteEllipticChart
    sidebar: Sidebar

    def __init__(self, chart: DiscreteEllipticChart):
        super().__init__(title="Discrete elliptic curves - addition")
        self.chart = chart
        self.sidebar = Sidebar(
            title="Addition", code_path="data/ec/add.py", tex_path="data/ec/add.tex"
        )

    def animate_in(self, scene):
        AnimateAddition.play(scene, self.chart, 5, 1, 10, 0)
        AnimateAddition.play(scene, self.chart, 5, 1, 9, 1)
        self.chart.animate_align_left(scene)
        self.sidebar.animate_appear(scene, self)

    def animate_out(self, scene):
        self.sidebar.animate_disappear(scene)
        self.chart.animate_align_center(scene)

    @staticmethod
    def play(scene: Scene, chart: DiscreteEllipticChart):
        instance = Addition(chart)
        instance.animate_in(scene)
        instance.animate_out(scene)
