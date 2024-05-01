from manim import (
    UP,
    Scene,
    Text,
    MathTex,
    Write,
    FadeOut,
    FadeIn,
    LEFT,
    DOWN,
    RIGHT,
    Circumscribe,
    Circle,
    Tex,
    ReplacementTransform,
    SurroundingRectangle,
    Transform,
    MoveToTarget,
)
from typing import List

from zkmarek.crypto.weierstrass_curve import Secp256k1_41
from zkmarek.video.constant import (
    PRIMARY_COLOR,
    BACKGROUND_COLOR,
    PRIMARY_FONT,
    HIGHLIGHT_COLOR,
)
from zkmarek.video.mobjects.discreet_elliptic_chart import DiscreteEllipticChart
from zkmarek.video.mobjects.wallet import Wallet
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.crypto.weierstrass_curve import Secp256k1_41
from zkmarek.video.mobjects.discreet_elliptic_chart import DiscreteEllipticChart
from zkmarek.video.mobjects.sidebar import Sidebar
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.utils import load
from zkmarek.video.slides.ec.animate_subgroup import AnimateSubgroups
from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.crypto.subgroup import Subgroup


class PreviouslyOn(SlideBase):
    chart: DiscreteEllipticChart
    sidebar: Sidebar
    wallet: Wallet
    scene: Scene
    public_key: Text

    def __init__(self) -> None:
        super().__init__(title="Previously on zkMarek")

    def construct(self):
        self.title = "Previously On zkMarek"
        self.curve = Secp256k1_41
        self.weierstrass_form = Text(r"Weierstrass form", color=PRIMARY_COLOR)
        self.weierstrass_equation = MathTex(r"y^2 = x^3 + ax + b", color=PRIMARY_COLOR)
        self.secp256k1_label = Text(r"Secp256k1 equation", color=PRIMARY_COLOR)
        self.chart = DiscreteEllipticChart(self.curve)
        self.chart.center()

        self.sidebar = Sidebar(
            title="Operations:", tex_path="data/ec/operations/addition.tex"
        )
        self.sidebar2 = Sidebar(title="", tex_path="data/ec/operations/negation.tex")
        self.sidebar3 = Sidebar(
            title="",
            tex_path="data/ec/operations/scalar_multiplication.tex",
        )
        self.sidebar4 = Sidebar(title="inverse", tex_path="data/ec/operations2.tex")
        self.wallet = Wallet("private key", "address")
        self.chart_wallet = (
            DiscreteEllipticChart(self.curve, dot_color=BACKGROUND_COLOR)
            .scale(0.5)
            .shift(1 * DOWN + 4 * LEFT)
        )

    def animate_in(self, scene):
        self.new_subsection(scene, "intro", sound="data/sound/episode2/ec_prev_on0.mp3")
        title = Tex("Previously on zkMarek")
        scene.play(FadeIn(title))
        transformed_title = Tex("Previously on zkMarek")
        transformed_title.to_corner(UP + LEFT)
        scene.play(Transform(title, transformed_title))
        scene.wait(2)

        # positions - weierstrass eqn
        self.weierstrass_form.next_to(self.weierstrass_equation, UP)

        # animating weierstrass eqn
        self.new_subsection(
            scene, "equation", sound="data/sound/episode2/ec_prev_on1.mp3"
        )
        self.chart.animate_align_left(scene)
        scene.play(Write(self.weierstrass_form.to_edge(RIGHT)))
        scene.wait(3)
        scene.play(Write(self.weierstrass_equation.to_edge(RIGHT)))
        # scene.play(Write(self.weierstrass_equation), run_time=2)
        scene.wait(2)
        scene.play(FadeOut(self.weierstrass_form), FadeOut(self.weierstrass_equation))

        # positions operations
        self.sidebar2.next_to(self.sidebar, DOWN * 1)
        self.sidebar3.next_to(self.sidebar2, DOWN * 1)
        self.sidebar4.next_to(self.sidebar3, DOWN * 1)

        # animating operations on eliptic curves
        self.new_subsection(
            scene, "Operations", sound="data/sound/episode2/ec_prev_on2.mp3"
        )
        scene.play(FadeIn(self.sidebar), run_time=0.5)
        scene.play(FadeIn(self.sidebar2), run_time=0.5)
        scene.play(FadeIn(self.sidebar3), run_time=0.5)
        # adjust time to what is showing and do highlighted text when mentioned (negating, adding and multiplying)
        scene.wait(2)
        framebox1 = SurroundingRectangle(self.sidebar, buff=0.1)
        framebox2 = SurroundingRectangle(self.sidebar2, buff=0.1)
        framebox3 = SurroundingRectangle(self.sidebar3, buff=0.1)
        framebox4 = SurroundingRectangle(self.sidebar4, buff=0.1)
        scene.play(ReplacementTransform(framebox1, framebox2), run_time=3)
        scene.play(ReplacementTransform(framebox2, framebox3), run_time=3)

        self.new_subsection(
            scene, "inverse", sound="data/sound/episode2/ec_prev_on3.mp3"
        )
        scene.play(Write(self.sidebar4), run_time=1)
        scene.play(ReplacementTransform(framebox3, framebox4), run_time=2)
        # animating out
        scene.play(FadeOut(self.sidebar), run_time=0.5)
        scene.play(FadeOut(self.sidebar2), run_time=0.5)
        scene.play(FadeOut(self.sidebar3), run_time=0.5)
        scene.play(FadeOut(self.sidebar4), run_time=0.5)
        scene.play(FadeOut(framebox4), run_time=0.5)
        scene.play(FadeOut(self.chart))

        # wallet
        self.animate_secret_key(scene)

        self.animate_scalar_multiplication(scene)

        self.animate_generate_ethereum_address(scene)

        scene.play(FadeOut(title))

    def animate_secret_key(self, scene):
        self.new_subsection(
            scene, "Generate random secret", sound="data/sound/episode2/ec_prev_on4.mp3"
        )
        self.wallet.animate_in(scene)

        scene.wait()
        self.wallet.animate_random_secret_key(scene, 17, 41)
        self.transformed_wallet = self.wallet
        self.transformed_wallet.to_corner(RIGHT)
        scene.play(Transform(self.wallet, self.transformed_wallet))

    def animate_scalar_multiplication(self, scene):
        scene.play(FadeIn(self.chart_wallet))

        generator = ECAffine(36, 28, self.curve)
        subgroup = Subgroup.from_generator(generator)
        animation = AnimateSubgroups(self.chart_wallet, runtime_per_step=0.1)
        animation.animate_generator(scene, generator)
        animation.animate_subgroup_mid(scene, subgroup, generator, 2, 18)

        scene.wait()
        public_key_point = self.chart_wallet.find_dot_by_affine(
            ECAffine(39, 9, self.curve)
        )
        scene.play(Circumscribe(public_key_point, Circle))
        self.public_key_coordinates = MathTex(
            "=", "(", "{{39}}", ",", "{{9}}", ")", font_size=20, color=HIGHLIGHT_COLOR
        )
        self.public_key_coordinates.next_to(public_key_point, RIGHT, buff=0.7)
        scene.play(Write(self.public_key_coordinates))

        scene.play(
            FadeOut(self.chart_wallet),
            FadeOut(*animation.labels),
            FadeOut(*animation.duplicates),
        )

    def animate_generate_ethereum_address(self, scene):

        self.wallet.generate_target()
        scene.play(MoveToTarget(self.wallet))
        self.wallet.animate_address_value(
            scene,
            "0x7a629f45938a32a2117c186d46b29ef3aa599b4e",
            FadeOut(self.public_key_coordinates),
        )

        self.wallet.generate_target()
        self.wallet.target.move_to(0)
        scene.play(MoveToTarget(self.wallet))
