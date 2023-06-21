from typing import Optional

from manim import LEFT, FadeIn, FadeOut, Transform
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
        scene.play(Transform(clock, clock2))
        scene.play(FadeOut(angle))

        self.new_subsection(scene, "Add 2 modulo")
        angle2 = FillAngle(deg1=330, deg2=30)
        scene.play(FadeIn(angle2))
        clock3 = Clock(hour=1)
        scene.remove(clock)
        scene.play(Transform(clock2, clock3))
        scene.play(FadeOut(angle2))

        scene.remove(clock2)
        self.new_subsection(scene, "Add 2 modulo")
        clock4 = Clock(use_zero=True, hour=1)
        scene.play(Transform(clock3, clock4))

        self.new_subsection(scene, "Use zero")
        scene.remove(clock3)
        clock5 = Clock(use_zero=True, hour=4, modulus=41)
        scene.play(Transform(clock4, clock5))

        self.new_subsection(scene, "Modulo 41")
        scene.remove(clock4)
        scene.play(clock5.animate.align_on_border(LEFT, buff=0.2))
        self.sidebar = Sidebar("Prime Field", code_path="data/pf/field.py")
        self.sidebar.animate_in(scene)
