from typing import Optional

from manim import (DOWN, LEFT, RED, FadeIn, FadeOut, Indicate, NumberLine,
                   ReplacementTransform, MathTex, TransformMatchingShapes,
                   TransformMatchingTex, TexTemplate)

from zkmarek.video.constant import PRIMARY_COLOR
from zkmarek.video.mobjects.clock import Clock
from zkmarek.video.mobjects.fill_angle import FillAngle
from zkmarek.video.mobjects.sidebar import Sidebar

from ..common.slide_base import SlideBase


class PrimeFields(SlideBase):
    clock: Optional[Clock] = None
    sidebar: Sidebar
    order13: MathTex
    order256: MathTex
    order41: MathTex

    def __init__(self):
        super().__init__(title="Prime Fields")


    def animate_in(self, scene):
        self.animate_pf(scene)
        self.animate_sidebar(scene)

    def animate_pf(self, scene):
        self.new_subsection(scene,
            "Prime fields - clock",
            sound="data/sound/episode1/s11-1.wav")

        clock = Clock(hour=9)
        clock.set_z_index(3)
        clock.animate_in(scene)
        angle = FillAngle(deg1=270, deg2=330)
        scene.wait(2)

        scene.play(FadeIn(angle))
        scene.wait(1)
        clock.move_hand_by_hours(scene, 2)
        scene.play(FadeOut(angle))

        angle2 = FillAngle(deg1=330, deg2=30)
        scene.play(FadeIn(angle2))

        clock.move_hand_by_hours(scene, 2)
        scene.play(FadeOut(angle2))

        self.new_subsection(scene,
            "Prime fields - use zero",
            sound="data/sound/episode1/s11-2.m4a")

        clock4 = Clock(use_zero=True, hour=1)
        scene.wait(1)
        scene.play(ReplacementTransform(clock, clock4))
        scene.wait(2)
        scene.play(Indicate(clock4.markings[1]))
        scene.wait(1)
        scene.play(Indicate(clock4.markings[23]))

        scene.wait(3)
        self.new_subsection(scene,
            "Prime fields - use 13",
            sound="data/sound/episode1/s11-3.wav")
        clock5 = Clock(use_zero=True, modulus=13, hour=1)
        scene.play(ReplacementTransform(clock4, clock5))

        scene.wait(5)

        self.new_subsection(scene,
            "Prime fields - Order 13",
            sound="data/sound/episode1/s11-4.wav")
        self.order13 = MathTex("{{Order}} = 13", color=PRIMARY_COLOR).next_to(
            clock.get_center(), direction=DOWN, buff=0.2)
        scene.wait(2)
        scene.play(FadeIn(self.order13))

        self.new_subsection(scene,
            "Prime fields - modulo 200",
            sound="data/sound/episode1/s11-5.wav")

        scene.wait(3)
        clock6 = Clock(use_zero=True, hour=4, modulus=200)
        scene.play(ReplacementTransform(clock5, clock6))

        scene.wait(2)

        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{MnSymbol,bm}")

        self.order256 = MathTex(r"{{Order}} \approx 2^{256}",
            color=PRIMARY_COLOR,
            tex_template=template).next_to(
            clock.get_center(), direction=DOWN, buff=0.2)
        scene.play(TransformMatchingTex(self.order13, self.order256))

        self.new_subsection(scene,
            "Prime fields - modulo 41",
            sound="data/sound/episode1/s11-6.wav")
        scene.wait(1)
        clock7 = Clock(use_zero=True, hour=4, modulus=41)

        self.order41 = MathTex("{{Order}} = 41", color=PRIMARY_COLOR).next_to(
            clock.get_center(), direction=DOWN, buff=0.2)
        scene.play(ReplacementTransform(clock6, clock7),
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
        scene.play(TransformMatchingShapes(clock7, line))
        scene.play(line.animate.align_on_border(LEFT, buff=0.2))
        scene.wait(2)

    def animate_sidebar(self, scene):
        self.new_subsection(scene,
            "Prime fields - code",
            sound="data/sound/episode1/s11-8.wav")
        self.sidebar = Sidebar("Prime Field", code_path="data/pf/field_element.py")
        self.sidebar.animate_in(scene)
        self.new_subsection(scene,
            "Prime fields - class",
            sound="data/sound/episode1/s11-9.wav")

        self.sidebar.indicate_code(scene, "class FieldElement", run_time=1)
        scene.wait(2)
        self.sidebar.indicate_code(scene, "value: int", run_time=1)
        scene.wait(1)
        self.sidebar.indicate_code(scene, "order: int", run_time=1)

        self.new_subsection(scene,
            "Prime fields - class",
            sound="data/sound/episode1/s11-10.wav")
        scene.wait(2)
        self.sidebar.indicate_code(scene, "# BigInteger", 0, run_time=1)
        self.sidebar.indicate_code(scene, "# BigInteger", 1, run_time=1)

        self.new_subsection(scene,
            "Prime fields - class",
            sound="data/sound/episode1/s11-11.wav")
        self.sidebar.indicate_code(scene, "__init__", run_time=1)
        scene.wait(1)
        self.sidebar.indicate_code(scene, "value: int", 1, run_time=1)
        self.sidebar.indicate_code(scene, "order: int", 1, run_time=1)

        self.sidebar.indicate_code(scene, r"self.value = value", run_time=1)
        self.sidebar.indicate_code(scene, r"% order", run_time=1)

        self.new_subsection(scene,
            "Prime fields - class",
            sound="data/sound/episode1/s11-12.wav")

        scene.wait(2)
        for e in ["__eq__", "__add__", "__sub__", "__mul__"]:
            self.sidebar.indicate_code(scene, e, run_time=1)

        self.new_subsection(scene,
            "Prime fields - class",
            sound="data/sound/episode1/s11-13.wav")
        scene.wait(1)
        for i in range(0, 4):
            self.sidebar.indicate_code(scene,
                "assert self.order == other.order",
                i, run_time=1)

        self.new_subsection(scene,
            "Prime fields - class",
            sound="data/sound/episode1/s11-14.wav")
        scene.wait(3)
        self.sidebar.indicate_code(scene, "self.value == other.value", run_time=1)

        self.new_subsection(scene,
            "Prime fields - class",
            sound="data/sound/episode1/s11-15.wav")

        for e in ["__add__", "__sub__", "__mul__"]:
            self.sidebar.indicate_code(scene, e, run_time=1)

        for e in ["self.value + other.value", "self.value - other.value",
            "self.value * other.value"]:
            self.sidebar.indicate_code(scene, e, run_time=0.5)

        self.new_subsection(scene,
            "Prime fields - inverting and division",
            sound="data/sound/episode1/s11-16.m4a")
        self.sidebar.indicate_code(scene, "inv(self)", run_time=1)
        self.new_subsection(scene,
            "Prime fields - save for another time",
            sound="data/sound/episode1/s11-17.wav")
        scene.wait(1)
