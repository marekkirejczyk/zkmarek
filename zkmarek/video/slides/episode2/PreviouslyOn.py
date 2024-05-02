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
    Transform,
    MoveToTarget,
)

from zkmarek.video.constant import (
    PRIMARY_COLOR,
    BACKGROUND_COLOR,
    HIGHLIGHT_COLOR,
)
from zkmarek.video.mobjects.discreet_elliptic_chart import DiscreteEllipticChart
from zkmarek.video.mobjects.wallet import Wallet
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.crypto.weierstrass_curve import Secp256k1_41
from zkmarek.video.mobjects.sidebar import Sidebar
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
        self.chart = DiscreteEllipticChart(self.curve).scale(0.8)
        self.chart.center()

        self.sidebar2 = Sidebar(title="", tex_path="data/ec/operations/addition.tex")
        self.sidebar = Sidebar(
            title="Operations", tex_path="data/ec/operations/negation.tex"
        )
        self.sidebar3 = Sidebar(
            title="",
            tex_path="data/ec/operations/scalar_multiplication.tex",
        )
        self.sidebar4 = Sidebar(title="", tex_path="data/ec/operations2.tex")
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
        # scene.wait(1)

        # animating weierstrass eqn

        # positions - weierstrass eqn
        self.weierstrass_form.next_to(self.weierstrass_equation, UP)
        self.chart.animate_align_left(scene)
        self.new_subsection(
            scene, "equation", sound="data/sound/episode2/ec_prev_on1.mp3"
        )
        scene.wait(2)
        scene.play(Write(self.weierstrass_form.to_edge(RIGHT)))
        scene.wait(2.5)
        scene.play(
            Write(self.weierstrass_equation.next_to(self.weierstrass_form, DOWN)),
            run_time=1,
        )
        scene.wait(2.5)
        # in a specific time - highlight points on a curve
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

        scene.wait(2)
        self.sidebar.set_color(HIGHLIGHT_COLOR)
        scene.wait(1.5)
        self.sidebar2.set_color(HIGHLIGHT_COLOR)
        scene.wait(1.5)
        self.sidebar3.set_color(HIGHLIGHT_COLOR)
        scene.wait(2.5)
        self.new_subsection(
            scene, "inverse", sound="data/sound/episode2/ec_prev_on3.mp3"
        )
        scene.play(Write(self.sidebar4), run_time=2)
        scene.wait(2)
        self.sidebar4.set_color(HIGHLIGHT_COLOR)
        scene.wait(2)

        # animating out
        scene.play(FadeOut(self.sidebar), run_time=0.5)
        scene.play(FadeOut(self.sidebar2), run_time=0.5)
        scene.play(FadeOut(self.sidebar3), run_time=0.5)
        scene.play(FadeOut(self.sidebar4), run_time=0.5)
        scene.wait(4)
        scene.play(FadeOut(self.chart), run_time=1.5)

        # wallet

        self.animate_secret_key(scene)

        self.animate_scalar_multiplication(scene)

        self.animate_generate_ethereum_address(scene)

        self.big_numbers_private_key(scene)

        scene.play(FadeOut(title))

    def animate_secret_key(self, scene):
        self.new_subsection(
            scene, "Generate random secret", sound="data/sound/episode2/ec_prev_on4.mp3"
        )
        self.wallet.animate_in(scene)

        # scene.wait(2)
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

        public_key_point = self.chart_wallet.find_dot_by_affine(
            ECAffine(39, 9, self.curve)
        )
        scene.play(Circumscribe(public_key_point, Circle))
        # scene.wait(1)
        # self.public_key_coordinates = MathTex(
        #     "=", "(", "{{39}}", ",", "{{9}}", ")", font_size=20, color=HIGHLIGHT_COLOR
        # )
        # self.public_key_coordinates.next_to(public_key_point, RIGHT, buff=0.7)
        # scene.play(Write(self.public_key_coordinates))
        # scene.wait(2)
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
            # FadeOut(self.public_key_coordinates),
        )

        self.wallet.generate_target()
        self.wallet.target.move_to(0)
        scene.play(MoveToTarget(self.wallet))
        scene.wait(1)

    def big_numbers_private_key(self, scene):
        self.wallet.animate_private_key(
            scene, "0x9de347a715a200cd....c8364d879483b69b", font_size=14
        )
        # scene.wait(2)
        self.wallet.animate_address_value(
            scene, "0xe31cc18f3f3718588e9a878a516c7889af047171"
        )
