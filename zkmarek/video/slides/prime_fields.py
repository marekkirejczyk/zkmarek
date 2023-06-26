from typing import Optional

from manim import LEFT, FadeIn, FadeOut, ReplacementTransform
from zkmarek.video.mobjects.clock import Clock
from zkmarek.video.mobjects.fill_angle import FillAngle
from zkmarek.video.mobjects.sidebar import Sidebar

from .common.slide_base import SlideBase


class PrimeFields(SlideBase):
    clock: Optional[Clock] = None
    sidebar: Sidebar

    def __init__(self):
        super().__init__(title="Prime Fields")

    def animate_in(self, scene):
        clock = Clock(hour=9)
        clock.set_z_index(3)
        clock.animate_in(scene)
        self.new_subsection(scene, "Add 2")
        angle = FillAngle(deg1=270, deg2=330)
        scene.play(FadeIn(angle))

        clock2 = Clock(hour=11)
        scene.play(ReplacementTransform(clock, clock2))
        scene.play(FadeOut(angle))

        self.new_subsection(scene, "Add 2 modulo")
        angle2 = FillAngle(deg1=330, deg2=30)
        scene.play(FadeIn(angle2))
        clock3 = Clock(hour=1)


        scene.play(ReplacementTransform(clock2, clock3))
        scene.play(FadeOut(angle2))

        self.new_subsection(scene, "Use zero")
        clock4 = Clock(use_zero=True, hour=1)
        scene.play(ReplacementTransform(clock3, clock4))

        self.new_subsection(scene, "Modulo 200")
        clock5 = Clock(use_zero=True, hour=4, modulus=200)
        scene.play(ReplacementTransform(clock4, clock5))
        scene.wait(1)

        self.new_subsection(scene, "Modulo 41")
        clock6 = Clock(use_zero=True, hour=4, modulus=41)
        scene.play(ReplacementTransform(clock5, clock6))

        self.new_subsection(scene, "Sidebar")
        scene.play(clock6.animate.align_on_border(LEFT, buff=0.2))
        self.sidebar = Sidebar("Prime Field", code_path="data/pf/field.py")
        self.sidebar.animate_in(scene)


