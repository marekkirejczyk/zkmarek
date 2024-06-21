from manim import (
    Sphere,
    WHITE,
    VMobject,
    YELLOW,
    NumberPlane,
    Transform,
    FadeIn,
    FadeOut,
    DEGREES,
    Axes,
    Text,
    MathTex,
    UP,
    DOWN,
    RIGHT,
    LEFT,
    Indicate,
    Dot,
    Circle,
    VGroup,
    ReplacementTransform,
    Write,
)

import numpy as np
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import SECONDARY_COLOR, PRIMARY_COLOR, PRIMARY_FONT
from zkmarek.video.mobjects.sidebar import Sidebar


class EllipticCurveProjection(SlideBase):
    def __init__(self):
        super().__init__("Stereographic projection of elliptic curve")

    def elliptic_curve_points(self, t):
        a, b = -1, 1
        x = t
        y_squared = x**3 + a * x + b
        if y_squared >= 0:
            y = np.sqrt(y_squared)
            return x, y

    def stereographic_projection(self, x, y, radius=3):
        denom = radius**2 + x**2 + y**2
        if denom == 0:
            return np.array([0, 0, -radius])
        xs = 2 * radius**2 * x / denom
        ys = 2 * radius**2 * y / denom
        zs = -radius * (radius**2 - x**2 - y**2) / denom
        return np.array([xs, ys, -zs])

    def construct(self):
        self.title = (
            (Text("Point at infinity", color=PRIMARY_COLOR, font=PRIMARY_FONT))
            .to_edge(UP)
            .scale(0.8)
        )
        self.new_coordinates = (
            MathTex(r"X, Y, Z", color=SECONDARY_COLOR).to_edge(UP).shift(RIGHT * 4.5)
        )
        self.equation = (
            MathTex(r"{{Z}}\cdot Y^2=X^3+aX\cdot {{Z^2}}+b{{Z^3}}", color=PRIMARY_COLOR)
            .next_to(self.new_coordinates, DOWN)
            .scale(0.7)
        )
        self.equations = (
            VGroup(
                MathTex(r"x=\frac{X}{Z}", color=SECONDARY_COLOR),
                MathTex(r"y=\frac{Y}{Z}", color=SECONDARY_COLOR),
            )
            .arrange(DOWN)
            .next_to(self.equation, DOWN)
        )

        self.sphere = Sphere(radius=3, resolution=(50, 50))
        self.sphere.set_fill(PRIMARY_COLOR, opacity=0.1)
        self.sphere.set_stroke(WHITE, opacity=0.5)
        self.ax = Axes(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            axis_config={"include_numbers": False},
        )
        self.labels = self.ax.get_axis_labels(
            MathTex("x", color=SECONDARY_COLOR),
            MathTex("y", color=SECONDARY_COLOR),
        )
        self.equatorial_plane = Circle(radius=3, color=SECONDARY_COLOR)
        self.equator_label = MathTex("1", color=SECONDARY_COLOR).next_to(
            self.equatorial_plane, LEFT
        )
        self.south_pole = Dot(point=[0, 0, -3], color=YELLOW)
        self.north_pole = Dot(point=[0, 0, 3], color=YELLOW)

        self.south_pole_label = Text(
            "point at infinity", color=PRIMARY_COLOR, font_size=20, font=PRIMARY_FONT
        ).next_to(self.south_pole, RIGHT)

        self.north_pole_label = Text(
            "0", color=PRIMARY_COLOR, font_size=20, font=PRIMARY_FONT
        ).next_to(self.north_pole, RIGHT)

        self.sidebar = Sidebar(
            "Operations", tex_path="zkmarek/video/slides/episode2/tex/operations.tex"
        )
        self.equation1 = (
            MathTex(r"Z=0", color=PRIMARY_COLOR)
            .shift(4.5 * LEFT)
            .to_edge(UP)
            .scale(0.7)
        )
        self.equation2 = (
            MathTex(
                r"{{0\cdot Y^2}}=X^3+{{aX\cdot 0^2}}+{{b\cdot0^3}}", color=PRIMARY_COLOR
            )
            .next_to(self.equation1, DOWN)
            .scale(0.7)
        )
        self.equation3 = (
            MathTex(r"0=X^3", color=PRIMARY_COLOR)
            .next_to(self.equation1, DOWN)
            .scale(0.7)
        )
        self.equation4 = (
            MathTex(r"[X,Y,Z]=[0,1,0]", color=PRIMARY_COLOR)
            .next_to(self.equation3, DOWN)
            .scale(0.7)
        )

    def create_plane_and_curves(self):
        t_values = np.linspace(-5, 5, 10000)
        self.plane_curve_points_positive = []
        self.plane_curve_points_negative = []
        for t in t_values:
            point = self.elliptic_curve_points(t)
            if point is not None:
                self.plane_curve_points_positive.append(
                    np.array([point[0], point[1], 0])
                )
                self.plane_curve_points_negative.append(
                    np.array([point[0], -point[1], 0])
                )

        self.plane_curve_positive = VMobject()
        if self.plane_curve_points_positive:
            self.plane_curve_positive.set_points_as_corners(
                self.plane_curve_points_positive
            )
            self.plane_curve_positive.set_color(YELLOW)

        self.plane_curve_negative = VMobject()
        if self.plane_curve_points_negative:
            self.plane_curve_negative.set_points_as_corners(
                self.plane_curve_points_negative
            )
            self.plane_curve_negative.set_color(YELLOW)

        self.plane = NumberPlane(
            x_range=[-10, 10, 1], y_range=[-10, 10, 1], color=SECONDARY_COLOR
        )
        self.plane.prepare_for_nonlinear_transform()
        self.sphere_ec = VGroup(
            self.sphere,
            self.plane_curve_positive,
            self.plane_curve_negative,
        )

    def animate_in(self, scene):
        self.new_subsection(
            scene, "what is point at infinity?", "data/sound/short1/slide1-0.mp3"
        )
        scene.add_fixed_in_frame_mobjects(self.title)
        self.title.to_edge(UP)
        scene.play(FadeIn(self.title))
        scene.set_camera_orientation(phi=60 * DEGREES, theta=30 * DEGREES)
        self.create_plane_and_curves()
        scene.play(
            FadeIn(self.ax),
            FadeIn(self.labels),
            FadeIn(self.plane_curve_positive),
            FadeIn(self.plane_curve_negative),
        )
        scene.add_fixed_in_frame_mobjects(self.sidebar)
        scene.play(Write(self.sidebar))
        self.new_subsection(
            scene, "x and y coordinates", "data/sound/short1/slide1-1.mp3"
        )
        scene.play(FadeOut(self.sidebar))
        scene.wait(2.2)
        scene.play(Indicate(self.labels))
        self.new_subsection(
            scene, "projective coordinates", "data/sound/short1/slide1-2.mp3"
        )
        scene.play(FadeOut(self.ax), FadeOut(self.labels))
        self.animate_wrapping(scene)
        scene.play(ReplacementTransform(self.plane, self.sphere_ec))
        scene.add_fixed_in_frame_mobjects(self.new_coordinates)
        scene.move_camera(phi=90 * DEGREES, theta=-60 * DEGREES, run_time=4)
        scene.begin_ambient_camera_rotation(rate=0.1)
        self.new_subsection(scene, "equation", "data/sound/short1/slide1-3.mp3")
        scene.wait(3)
        scene.add_fixed_in_frame_mobjects(self.equation)
        scene.add_fixed_in_frame_mobjects(self.equations)
        scene.play(FadeIn(self.equations), Write(self.equation))
        scene.play(
            Indicate(self.equation[0]),
        )
        scene.play(
            Indicate(self.equation[2]),
        )
        scene.play(
            Indicate(self.equation[4]),
        )
        scene.add_fixed_in_frame_mobjects(self.equation2)
        scene.play(Write(self.equation1))
        scene.add_fixed_in_frame_mobjects(self.equation2)
        scene.add_fixed_in_frame_mobjects(self.equation3)
        scene.play(ReplacementTransform(self.equation2, self.equation3))
        scene.add_fixed_in_frame_mobjects(self.equation4)
        self.new_subsection(scene, "south pole", "data/sound/short1/slide1-4.mp3")
        scene.play(
            FadeOut(self.equation1), FadeOut(self.equation3), FadeOut(self.equation4)
        )
        scene.stop_ambient_camera_rotation()
        scene.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES, run_time=4)
        scene.begin_ambient_camera_rotation(rate=0.1)
        scene.add(self.equatorial_plane, self.south_pole, self.south_pole)
        scene.stop_ambient_camera_rotation()
        scene.move_camera(phi=45 * DEGREES, theta=90 * DEGREES, run_time=2)
        scene.begin_ambient_camera_rotation(rate=0.1)
        scene.play(FadeIn(self.south_pole), FadeIn(self.south_pole_label))
        scene.wait(2)
        scene.play(FadeIn(self.equatorial_plane), FadeIn(self.equator_label))
        self.new_subsection(scene, "conclusion", "data/sound/short1/slide1-6.mp3")
        scene.move_camera(phi=30 * DEGREES, theta=60 * DEGREES, run_time=4)
        scene.stop_ambient_camera_rotation()

    def animate_wrapping(self, scene):
        animations = []

        new_points_positive = [
            self.stereographic_projection(p[0], p[1])
            for p in self.plane_curve_points_positive
        ]
        new_points_negative = [
            self.stereographic_projection(p[0], p[1])
            for p in self.plane_curve_points_negative
        ]

        self.sphere_curve_positive = (
            VMobject().set_points_smoothly(new_points_positive).set_color(YELLOW)
        )
        self.sphere_curve_negative = (
            VMobject().set_points_smoothly(new_points_negative).set_color(YELLOW)
        )

        animations.append(
            Transform(self.plane_curve_positive, self.sphere_curve_positive)
        )
        animations.append(
            Transform(self.plane_curve_negative, self.sphere_curve_negative)
        )

        for line in self.plane.family_members_with_points():
            line_points = line.points
            new_line_points = [
                self.stereographic_projection(p[0], p[1]) for p in line_points
            ]
            self.new_line = VMobject().set_points_smoothly(new_line_points)
            animations.append(Transform(line, self.new_line.set_color("blue")))

        scene.play(*animations, run_time=5)

    def animate_out(self, scene):
        scene.play(
            FadeOut(self.equation),
            FadeOut(self.equations),
            FadeOut(self.new_coordinates),
            FadeOut(self.south_pole),
            FadeOut(self.south_pole_label),
            FadeOut(self.equatorial_plane),
            FadeOut(self.equator_label),
        )
