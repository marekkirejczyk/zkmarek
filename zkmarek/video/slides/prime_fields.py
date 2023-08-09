from typing import Optional

from manim import (DOWN, LEFT, RED, FadeIn, FadeOut, Indicate, NumberLine,
                   ReplacementTransform, MathTex, TransformMatchingShapes,
                   TransformMatchingTex)

from zkmarek.video.constant import PRIMARY_COLOR
from zkmarek.video.mobjects.clock import Clock
from zkmarek.video.mobjects.fill_angle import FillAngle
from zkmarek.video.mobjects.sidebar import Sidebar

from .common.slide_base import SlideBase


class PrimeFields(SlideBase):
    clock: Optional[Clock] = None
    sidebar: Sidebar
    order12: MathTex
    order256: MathTex
    order41: MathTex

    def __init__(self):
        super().__init__(title="Prime Fields")


    def animate_in(self, scene):
        self.new_subsection(scene,
            "Prime fields - clock",
            sound="data/sound/episode/s10-1.wav")

        clock = Clock(hour=9)
        clock.set_z_index(3)
        clock.animate_in(scene)
        angle = FillAngle(deg1=270, deg2=330)
        scene.wait(2)

        scene.play(FadeIn(angle))
        scene.wait(1)
        clock2 = Clock(hour=11)
        scene.play(ReplacementTransform(clock, clock2))
        scene.play(FadeOut(angle))

        angle2 = FillAngle(deg1=330, deg2=30)
        scene.play(FadeIn(angle2))
        clock3 = Clock(hour=1)

        scene.play(ReplacementTransform(clock2, clock3))
        scene.play(FadeOut(angle2))

        self.new_subsection(scene,
            "Prime fields - use zero",
            sound="data/sound/episode/s10-2.wav")

        clock4 = Clock(use_zero=True, hour=1)
        scene.wait(1)
        scene.play(ReplacementTransform(clock3, clock4))
        scene.wait(2)
        scene.play(Indicate(clock4.markings[1]))
        scene.wait(1)
        scene.play(Indicate(clock4.markings[23]))

        scene.wait(5)

        self.order12 = MathTex("{{Order}} = 12", color=PRIMARY_COLOR).next_to(
            clock.get_center(), direction=DOWN, buff=0.2)
        scene.play(FadeIn(self.order12))

        self.new_subsection(scene,
            "Prime fields - modulo 200",
            sound="data/sound/episode/s10-3.wav")

        scene.wait(3)
        clock5 = Clock(use_zero=True, hour=4, modulus=200)
        scene.play(ReplacementTransform(clock4, clock5))

        scene.wait(2)

        self.order256 = MathTex("{{Order}} = 2^{256}", color=PRIMARY_COLOR).next_to(
            clock.get_center(), direction=DOWN, buff=0.2)
        scene.play(TransformMatchingTex(self.order12, self.order256))

        self.new_subsection(scene,
            "Prime fields - modulo 41",
            sound="data/sound/episode/s10-4.wav")
        scene.wait(1)
        clock6 = Clock(use_zero=True, hour=4, modulus=41)

        self.order41 = MathTex("{{Order}} = 41", color=PRIMARY_COLOR).next_to(
            clock.get_center(), direction=DOWN, buff=0.2)
        scene.play(ReplacementTransform(clock5, clock6),
            TransformMatchingTex(self.order256, self.order41), run_time=2)

        scene.wait(4)
        scene.play(FadeOut(self.order41))

        line = NumberLine(
            x_range=[0, 41, 2],
            length=10,
            color=RED,
            include_numbers=True,
            label_direction=DOWN,
            include_tip=True,
        ).scale(0.6)
        scene.play(TransformMatchingShapes(clock6, line))

        self.new_subsection(scene, "Sidebar")
        scene.play(line.animate.align_on_border(LEFT, buff=0.2))
        self.sidebar = Sidebar("Prime Field", code_path="data/pf/field.py")
        self.sidebar.animate_in(scene)


