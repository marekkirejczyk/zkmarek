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
    UP,
    DOWN,
    ImageMobject,
    Dot,
    Circle,
    VGroup,
    FadeTransform,
    MoveAlongPath,
    linear,
    ThreeDAxes,
)


import numpy as np
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import (
    SECONDARY_COLOR,
    PRIMARY_COLOR,
    PRIMARY_FONT,
    HIGHLIGHT_COLOR,
    HIGHLIGHT2_COLOR,
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
        self.logo = ImageMobject("data/brand/logo.png").scale(1.5)
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

        self.button = ImageMobject("data/subscribe/normal.png").scale(0.4)
        self.button_clicked = ImageMobject(
            "data/subscribe/clicked.png", z_index=1
        ).scale(0.4)
        self.button.shift(DOWN * 5)
        self.button_clicked.shift(DOWN * 5)

    def create_plane_and_curves(self):
        t_values = np.linspace(-12, 12, 10000)
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
            x_range=[-15, 15, 1], y_range=[-15, 15, 1], color=SECONDARY_COLOR
        )
        self.plane.prepare_for_nonlinear_transform()
        self.sphere_ec = VGroup(
            self.sphere,
            self.plane_curve_positive,
            self.plane_curve_negative,
        )

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

        spiral_path = VMobject()
        spiral_points = []
        num_points = 100
        for i in range(num_points):
            angle = i * DEGREES * 36 / num_points
            radius = 0.05 * i
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            z = i * 0.01
            spiral_points.append([x, y, z])
        spiral_path.set_points_as_corners(spiral_points)

        dot = Dot(color=PRIMARY_COLOR)
        label = Text(
            "point at infinity", font_size=20, color=PRIMARY_COLOR, font=PRIMARY_FONT
        ).rotate(80 * DEGREES)

        label.add_updater(lambda m: m.next_to(dot, UP))
        scene.wait(2.7)
        scene.add(dot, label)

        scene.play(MoveAlongPath(dot, spiral_path, run_time=2.3, rate_func=linear))

        dot1 = Text("?", font_size=50, font=PRIMARY_FONT, color=PRIMARY_COLOR).rotate(
            90 * DEGREES
        )
        dot1.move_to(UP * 3 + RIGHT * 4)

        scene.play(FadeTransform(dot, dot1), FadeOut(label))

        self.new_subsection(
            scene, "projective coordinates", "data/sound/short1/slide2-1.mp3"
        )
        scene.play(FadeOut(dot1))
        self.animate_wrapping(scene)
        scene.play(
            FadeTransform(self.plane, self.sphere_ec),
            FadeIn(self.sphere_ec),
            run_time=0.25,
        )
        self.fixed_axes = ThreeDAxes(
            x_range=[-20, 20, 1],
            y_range=[-10, 10, 1],
            z_range=[-10, 10, 1],
            axis_config={"include_numbers": False, "color": WHITE},
        )
        self.labels_3d = self.fixed_axes.get_axis_labels(
            MathTex("x", color=SECONDARY_COLOR),
            MathTex("y", color=SECONDARY_COLOR),
            MathTex("z", color=SECONDARY_COLOR),
        )
        scene.add(self.fixed_axes, self.labels_3d)
        scene.play(FadeIn(self.north_pole), FadeIn(self.north_pole_label))

        scene.move_camera(phi=15 * DEGREES, theta=90 * DEGREES, run_time=1)
        scene.begin_ambient_camera_rotation(rate=0.1)

        scene.move_camera(phi=60 * DEGREES, theta=110 * DEGREES, run_time=1)

        self.x_axis_line = (
            VMobject()
            .set_points_as_corners(
                [self.stereographic_projection(x, 0) for x in np.linspace(-10, 10, 100)]
            )
            .set_color(HIGHLIGHT2_COLOR)
        )
        self.y_axis_line = (
            VMobject()
            .set_points_as_corners(
                [self.stereographic_projection(0, y) for y in np.linspace(-10, 10, 100)]
            )
            .set_color(HIGHLIGHT2_COLOR)
        )
        self.new_subsection(scene, "north pole", "data/sound/short1/slide2-2.mp3")
        scene.play(FadeIn(self.x_axis_line), FadeIn(self.y_axis_line))

        points_north_hemisphere = [(0, 0.6), (0, 1), (-2, 0)]
        colors = [SECONDARY_COLOR, HIGHLIGHT_COLOR, PRIMARY_COLOR]
        dots_south = VGroup()
        labels_south = VGroup()

        for (x, y), color in zip(points_north_hemisphere, colors):
            projected_point = self.stereographic_projection(x, y)
            dot = Dot(point=projected_point, color=color)
            label = Text(f"({x/3:.1f},{y/3:.1f})", color=color, font_size=18)
            label.next_to(dot, RIGHT)
            label.rotate(scene.camera.get_phi() + 10 * DEGREES, axis=[1, 0, 0]).rotate(
                scene.camera.get_phi(), axis=[0, 0, 1]
            )
            dots_south.add(dot)
            labels_south.add(label)

        scene.add(dots_south, labels_south)

        self.new_subsection(scene, "south pole", "data/sound/short1/slide2-3.mp3")

        scene.play(
            FadeIn(self.equatorial_plane),
        )
        scene.move_camera(phi=130 * DEGREES, theta=30 * DEGREES, run_time=3.5)

        scene.play(
            FadeIn(self.south_pole),
            FadeIn(self.south_pole_label),
            FadeOut(self.equatorial_plane),
        )

        points_south_hemisphere = [(5, 0), (4, 0), (0, 7)]
        dots_north = VGroup()
        labels_north = VGroup()
        for x, y in points_south_hemisphere:
            projected_point = self.stereographic_projection(x, y)
            dot = Dot(point=projected_point, color=PRIMARY_COLOR)
            label = Text(
                f"({x/3:.1f},{y/3:.1f})",
                color=PRIMARY_COLOR,
                font=PRIMARY_FONT,
                font_size=18,
            ).next_to(dot, RIGHT)
            label.rotate(scene.camera.get_phi() + 10 * DEGREES, axis=[1, 0, 0]).rotate(
                scene.camera.get_phi(), axis=[0, 0, 1]
            )
            dots_north.add(dot)
            labels_north.add(label)
        scene.add(dots_north, labels_north)

        scene.move_camera(phi=210 * DEGREES, theta=45 * DEGREES, run_time=4.5)
        scene.wait(3.5)
        scene.stop_ambient_camera_rotation()
        scene.add_fixed_in_frame_mobjects(self.button, self.button_clicked)
        scene.play(FadeIn(self.button), run_time=0.5)

        # Source of sound under Creative Commons 0 License.
        # https://freesound.org/people/joebro10/sounds/219318/
        scene.add_sound("data/sound/click.wav", gain=20)
        scene.play(FadeIn(self.button_clicked), run_time=0.2)
        scene.play(FadeOut(self.button_clicked), run_time=0.2)
        scene.remove(dots_north, labels_north, dots_south, labels_south)
        scene.play(
            FadeOut(self.sphere_ec),
            FadeOut(self.south_pole_label),
            FadeOut(self.south_pole),
            FadeOut(self.north_pole),
            FadeOut(self.north_pole_label),
            FadeOut(self.fixed_axes),
            FadeOut(self.labels_3d),
            FadeOut(self.y_axis_line),
            FadeOut(self.x_axis_line),
            FadeIn(self.logo),
        )

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
        scene.play(*animations, run_time=3.5)

    def animate_out(self, scene):

        scene.play(FadeOut(self.logo))
