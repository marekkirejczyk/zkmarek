from manim import (
    Sphere,
    BLUE,
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
    Indicate,
    Dot,
    Circle,
    RED,
)

import numpy as np
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import SECONDARY_COLOR, PRIMARY_COLOR, PRIMARY_FONT


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
            Text("Point at infinity", color=PRIMARY_COLOR, font=PRIMARY_FONT)
        ).to_edge(UP)
        self.new_coordinates = (MathTex(r"X, Y, Z")).to_edge(UP + RIGHT)
        self.equation = (MathTex(r"Z\cdot Y^2=X^3+aX\cdot Z^2+bZ^3")).next_to(
            self.new_coordinates, DOWN
        )
        self.equations = (MathTex(r"x=X/Z, \quad y=Y/Z")).next_to(self.equation, DOWN)

        self.sphere = Sphere(radius=3, resolution=(50, 50))
        self.sphere.set_fill(BLUE, opacity=0.1)
        self.sphere.set_stroke(WHITE, opacity=0.5)
        self.ax = Axes(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            axis_config={"include_numbers": False},
        )
        self.labels = self.ax.get_axis_labels(
            Text("x", color=SECONDARY_COLOR),
            Text("y", color=SECONDARY_COLOR),
        )
        self.equatorial_plane = Circle(radius=3, color=RED).rotate(
            90 * DEGREES, axis=RIGHT
        )
        self.south_pole = Dot(point=[0, 0, -3], color=YELLOW)

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

    def animate_in(self, scene):
        self.new_subsection(
            scene, "what is point at inifnity?", "data/sound/short1/slide1-0.mp3"
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

        self.new_subsection(
            scene, "x and y coordinates", "data/sound/short1/slide1-1.mp3"
        )

        scene.play(Indicate(self.labels))
        self.new_subsection(
            scene, "projective coordinates", "data/sound/short1/slide1-2.mp3"
        )
        # scene.wait(4)
        self.animate_wrapping(scene)
        scene.add_fixed_in_frame_mobjects(self.new_coordinates)

        self.new_subsection(scene, "equation", "data/sound/short1/slide1-3.mp3")
        # scene.wait(2)
        scene.add_fixed_in_frame_mobjects(self.equation)
        scene.play(
            FadeOut(self.ax),
            FadeOut(self.labels),
            FadeOut(self.plane_curve_positive),
            FadeOut(
                self.plane_curve_negative,
            ),
        )
        scene.add_fixed_in_frame_mobjects(self.equations)
        scene.play(
            FadeIn(self.equations),
        )

        self.new_subsection(scene, "data/sound/short1/slide1-4.mp3")
        scene.add(self.sphere)
        scene.play(FadeOut(self.ax), FadeOut(self.labels))
        scene.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES, run_time=2)
        scene.begin_ambient_camera_rotation(rate=0.1)
        # scene.wait(5)
        scene.stop_ambient_camera_rotation()
        self.new_subsection(scene, "data/sound/short1/slide1-5.mp3")
        scene.add(self.equatorial_plane, self.south_pole)

        scene.move_camera(phi=45 * DEGREES, theta=90 * DEGREES, run_time=2)
        scene.begin_ambient_camera_rotation(rate=0.1)
        # scene.wait(5)
        self.new_subsection(scene, "data/sound/short1/slide1-6.mp3")
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

        sphere_curve_positive = (
            VMobject().set_points_smoothly(new_points_positive).set_color(YELLOW)
        )
        sphere_curve_negative = (
            VMobject().set_points_smoothly(new_points_negative).set_color(YELLOW)
        )

        animations.append(Transform(self.plane_curve_positive, sphere_curve_positive))
        animations.append(Transform(self.plane_curve_negative, sphere_curve_negative))

        for line in self.plane.family_members_with_points():
            line_points = line.points
            new_line_points = [
                self.stereographic_projection(p[0], p[1]) for p in line_points
            ]
            new_line = VMobject().set_points_smoothly(new_line_points)
            animations.append(Transform(line, new_line.set_color("blue")))

        scene.play(*animations, run_time=5)

        scene.play(FadeIn(self.plane))

    def animate_out(self, scene):
        scene.play(FadeOut(self.equation), FadeOut(self.equations))
