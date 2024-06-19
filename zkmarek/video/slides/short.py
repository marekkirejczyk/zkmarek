from manim import (
    Sphere,
    BLUE,
    WHITE,
    VMobject,
    YELLOW,
    NumberPlane,
    RED,
    Transform,
    DEGREES,
    FadeIn,
    FadeOut,
)
import numpy as np
from zkmarek.video.slides.common.slide_base import SlideBase


class EllipticCurveProjection(SlideBase):

    def __init__(self):
        super().__init__("Stereographic projection of elliptic curve")

    def construct(self):
        self.sphere = Sphere(radius=3, resolution=(50, 50))
        self.sphere.set_fill(BLUE, opacity=0.1)
        self.sphere.set_stroke(WHITE, opacity=0.5)

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

    def animate_in(self, scene):
        # scene.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

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

        self.plane = NumberPlane(x_range=[-10, 10, 1], y_range=[-10, 10, 1], color=RED)
        self.plane.prepare_for_nonlinear_transform()
        scene.add(self.plane, self.plane_curve_positive, self.plane_curve_negative)

        self.animate_wrapping(scene)
        scene.add(self.sphere)
        scene.play(FadeOut(self.plane))

        scene.begin_ambient_camera_rotation(rate=0.1)
        scene.wait(5)
        scene.stop_ambient_camera_rotation()

        scene.wait(2)

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
