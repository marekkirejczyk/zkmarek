from manim import (RIGHT, UP, ApplyWave, Brace, Circle, Circumscribe, FadeIn,
                   FadeOut, Indicate, Tex, VGroup, Wait)

from zkmarek.crypto.weierstrass_curve import Secp256k1_41, WeierstrassCurve
from zkmarek.video.constant import HIGHLIGHT_COLOR, SECONDARY_COLOR
from zkmarek.video.mobjects.discreet_elliptic_chart import \
    DiscreteEllipticChart
from zkmarek.video.mobjects.sidebar import Sidebar
from zkmarek.video.slides.common.slide_base import SlideBase


class Introduction(SlideBase):
    curve: WeierstrassCurve
    chart: DiscreteEllipticChart
    sidebar: Sidebar

    def __init__(self):
        super().__init__("Discrete elliptic curves chart")

    def construct(self):
        self.curve = Secp256k1_41
        self.chart = DiscreteEllipticChart(self.curve)
        self.chart.center()

    def animate_symmetry(self, scene):
        line = self.chart.create_horizontal_line()
        scene.play(FadeIn(line, run_time=2))
        scene.wait(5)
        scene.play(FadeOut(line, run_time=2))

    def animate_vertical(self, scene):
        for x in range(1, 8):
            line = self.chart.create_vertical_line(x)
            dots = self.chart.find_dots_by_x(x)
            if len(dots) > 0:
                scene.play(FadeIn(line))
                scene.play(Indicate(dots[0], color=HIGHLIGHT_COLOR), Indicate(dots[1],
                    color=HIGHLIGHT_COLOR))
                scene.play(FadeOut(line))

    def animate_single_point(self, scene):
        line = self.chart.create_vertical_line(17)
        scene.play(FadeIn(line), Wait())
        dot = self.chart.find_dots_by_x(17)[0]
        scene.wait(8)
        scene.play(Indicate(dot, color=HIGHLIGHT_COLOR))
        scene.play(FadeOut(line))


    def animate_in(self, scene):
        self.new_subsection(scene, "Elliptic Curve",
            sound="data/sound/episode1/s13-0.wav")
        self.chart.animate_in(scene)
        scene.wait(4)
        scene.play(Circumscribe(self.chart.labels[1], Circle, color=SECONDARY_COLOR),
            Circumscribe(self.chart.labels[0], Circle, color=SECONDARY_COLOR))

        self.new_subsection(scene, "Elliptic Curve - Discrete World",
            sound="data/sound/episode1/s13-1.wav")

        scene.wait(1)
        scene.play(ApplyWave(self.chart.ax[0]),
            ApplyWave(self.chart.ax[1]), DIRECTION=UP)

        scene.wait(6.5)
        dots = VGroup(*self.chart.dots)
        scene.play(Indicate(dots, color=HIGHLIGHT_COLOR, scale=1.05))
        self.new_subsection(scene, "Elliptic Curve - Symmetry",
            sound="data/sound/episode1/s13-2.wav")
        scene.wait(1)

        self.animate_symmetry(scene)

        self.new_subsection(scene, "Order of the curve",
            sound="data/sound/episode1/s13-3.wav")
        self.new_subsection(scene, "Order of the curve",
            sound="data/sound/episode1/s13-4.wav")

        scene.play(Indicate(dots, color=HIGHLIGHT_COLOR, scale=1.05))
        brace = Brace(dots, direction=RIGHT, z_index=3, color=SECONDARY_COLOR)
        label = Tex("42", color=SECONDARY_COLOR)
        brace.put_at_tip(label)
        scene.play(FadeIn(brace), FadeIn(label))
        scene.wait(3)
        scene.play(FadeOut(brace), FadeOut(label))

        self.new_subsection(scene, "Prime field vs. elliptic curve group order",
            sound="data/sound/episode1/s13-5.wav")

        self.new_subsection(scene, "Elliptic Curve - Vertical lines ",
            sound="data/sound/episode1/s13-6.wav")

        self.animate_vertical(scene)

        self.new_subsection(scene, "Elliptic Curve - point on x axis",
            sound="data/sound/episode1/s13-7.m4a")

        self.animate_single_point(scene)


    def animate_out(self, scene):
        scene.remove(self.chart)
