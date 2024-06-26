from manim import (
    Sphere,
    VMobject,
    YELLOW,
    WHITE,
    NumberPlane,
    Transform,
    FadeIn,
    FadeOut,
    DEGREES,
    Axes,
    Text,
    MathTex,
    RIGHT,
    LEFT,
    Dot,
    Circle,
    VGroup,
    FadeTransform,
    MoveAlongPath,
)

import numpy as np
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import (
    SECONDARY_COLOR,
    PRIMARY_COLOR,
    PRIMARY_FONT,
    HIGHLIGHT_COLOR,
)


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
        self.sphere = Sphere(radius=3, resolution=(50, 50))
        self.sphere.set_fill(PRIMARY_COLOR, opacity=0.1)
        self.sphere.set_stroke(WHITE, opacity=0.6)
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
        self.equator_label = Text(
            "1", color=SECONDARY_COLOR, font_size=20, font=PRIMARY_FONT
        ).next_to(self.equatorial_plane, LEFT)
        self.south_pole = Dot(point=[0, 0, -3], color=YELLOW)
        self.north_pole = Dot(point=[0, 0, 3], color=YELLOW)

        self.south_pole_label = (
            Text(
                "point at infinity",
                color=PRIMARY_COLOR,
                font_size=20,
                font=SECONDARY_COLOR,
            )
            .next_to(self.south_pole, RIGHT)
            .rotate(angle=180 * DEGREES, axis=[1, 0, 0])
            .rotate(angle=180 * DEGREES, axis=[0, 0, 1])
        )

        self.north_pole_label = (
            Text("(0,0)", color=PRIMARY_COLOR, font_size=20, font=PRIMARY_FONT)
            .next_to(self.north_pole, RIGHT)
            .rotate(angle=180 * DEGREES, axis=[0, 0, 1])
        )

    def create_plane_and_curves(self):
        t_values = np.linspace(-10, 10, 10000)
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
        self.path = VMobject()
        self.path_arr = np.array(
            [p for p in self.plane_curve_points_positive if np.abs(p[1]) < 3]
        )
        self.path.set_points_smoothly(self.path_arr)

        self.path1 = VMobject()
        self.path1_arr = np.array(
            [p for p in self.plane_curve_points_negative if np.abs(p[1]) < 3]
        )
        self.path1.set_points_smoothly(self.path1_arr)

    def animate_in(self, scene):
        self.new_subsection(
            scene, "what is point at infinity?", "data/sound/short1/slide2-0.mp3"
        )
        scene.set_camera_orientation(phi=60 * DEGREES, theta=30 * DEGREES)
        self.create_plane_and_curves()
        scene.play(
            FadeIn(self.ax),
            FadeIn(self.labels),
            FadeIn(self.plane_curve_positive),
            FadeIn(self.plane_curve_negative),
        )

        dot = Dot(color=PRIMARY_COLOR)
        scene.add(dot)

        chaotic_path = VMobject()
        chaotic_points = []
        num_points = 30
        for i in range(num_points):
            x = np.random.uniform(-10, 10)
            y = np.random.uniform(-10, 10)
            z = np.random.uniform(-5, 5) if np.random.rand() > 0.7 else 0
            chaotic_points.append([x, y, z])
        chaotic_path.set_points_as_corners(chaotic_points)

        def custom_rate_func(t):
            if t < 0.2:
                return t * 0.5
            elif t < 0.4:
                return 0.1 + (t - 0.2) * 2.5
            elif t < 0.6:
                return 0.6 + (t - 0.4) * 0.5
            elif t < 0.8:
                return 0.7 + (t - 0.6) * 1.5
            else:
                return 1.0 - (t - 0.8) * 0.5

        scene.play(
            MoveAlongPath(dot, chaotic_path, run_time=5, rate_func=custom_rate_func)
        )

        position_index = len(self.path1_arr) // 2
        position = self.path_arr[position_index]

        dot1 = Text("?", font_size=35, font=PRIMARY_FONT, color=PRIMARY_COLOR)
        dot1.move_to(position)

        scene.play(FadeTransform(dot, dot1))

        self.new_subsection(
            scene, "projective coordinates", "data/sound/short1/slide2-1.mp3"
        )
        scene.play(FadeOut(dot1))
        self.animate_wrapping(scene)
        scene.play(FadeTransform(self.plane, self.sphere_ec), run_time=0.5)

        scene.play(FadeIn(self.north_pole), FadeIn(self.north_pole_label))

        scene.move_camera(phi=15 * DEGREES, theta=90 * DEGREES, run_time=1)
        scene.begin_ambient_camera_rotation(rate=0.1)

        self.new_subsection(scene, "north pole", "data/sound/short1/slide2-2.mp3")

        self.x_values = [0.01, 0.9, 0.7]
        colors = np.array(
            [
                SECONDARY_COLOR,
                HIGHLIGHT_COLOR,
                PRIMARY_COLOR,
            ]
        )
        scene.move_camera(phi=60 * DEGREES, theta=45 * DEGREES, run_time=3.5)
        for i in range(len(self.x_values)):
            point = self.elliptic_curve_points(self.x_values[i])
            if point is not None:
                projected_point = self.stereographic_projection(point[0], point[1])
                dot = Dot(point=projected_point, color=colors[i])
                label = Text(
                    f"({point[0]:.1f},{point[1]:.1f})",
                    color=colors[i],
                    font=PRIMARY_FONT,
                    font_size=18,
                ).next_to(dot, RIGHT)
                label.rotate(angle=60 * DEGREES, axis=[0, 1, 0])
                scene.add(dot, label)

        self.new_subsection(scene, "south pole", "data/sound/short1/slide2-3.mp3")
        self.x_values = [2, 4, 9]
        scene.play(
            FadeIn(self.equatorial_plane),
        )
        scene.move_camera(phi=100 * DEGREES, theta=45 * DEGREES, run_time=3.5)
        for i in range(len(self.x_values)):
            point = self.elliptic_curve_points(self.x_values[i])
            if point is not None:
                projected_point = self.stereographic_projection(point[0], point[1])
                dot = Dot(point=projected_point, color=colors[i])
                label = Text(
                    f"({point[0]:.1f},{point[1]:.1f})",
                    color=colors[i],
                    font=PRIMARY_FONT,
                    font_size=18,
                ).next_to(dot, RIGHT)
                label.rotate(angle=60 * DEGREES, axis=[0, 1, 0])
                scene.add(dot, label)

        scene.play(
            FadeIn(self.south_pole),
            FadeIn(self.south_pole_label),
        )
        scene.move_camera(phi=210 * DEGREES, theta=45 * DEGREES, run_time=3.5)
        scene.wait(1.5)
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
        scene.play(FadeOut(self.ax), FadeOut(self.labels))
        fade_in_animations = []
        for line in self.plane.family_members_with_points():
            line_points = line.points
            new_line_points = [
                self.stereographic_projection(p[0], p[1]) for p in line_points
            ]
            self.new_line = VMobject().set_points_smoothly(new_line_points)
            fade_in_animations.append(FadeIn(line, run_time=0.6))
            animations.append(Transform(line, self.new_line.set_color(PRIMARY_COLOR)))

        scene.play(*fade_in_animations)
        scene.play(*animations, run_time=4)

    def animate_out(self, scene):
        scene.play(
            FadeOut(self.south_pole),
            FadeOut(self.south_pole_label),
            FadeOut(self.equatorial_plane),
            FadeOut(self.equator_label),
        )
