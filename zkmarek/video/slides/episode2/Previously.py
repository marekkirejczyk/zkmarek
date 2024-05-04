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
    Unwrite,
    ReplacementTransform,
    TexTemplate,
    Indicate,
)

from zkmarek.video.constant import (
    PRIMARY_COLOR,
    SECONDARY_COLOR,
    BACKGROUND_COLOR,
    HIGHLIGHT_COLOR,
)
from zkmarek.video.mobjects.discreet_elliptic_chart import DiscreteEllipticChart
from zkmarek.video.mobjects.wallet import Wallet

# from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.common.tex_slide import TexSlide
from zkmarek.crypto.weierstrass_curve import Secp256k1_41
from zkmarek.video.mobjects.sidebar import Sidebar
from zkmarek.video.slides.ec.animate_subgroup import AnimateSubgroups
from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.crypto.subgroup import Subgroup
from zkmarek.video.utils import load


class PreviouslyOn(TexSlide):
    chart: DiscreteEllipticChart
    sidebar: Sidebar
    wallet: Wallet
    scene: Scene
    public_key: Text

    def __init__(self) -> None:
        super().__init__(
            "Previously on zkMarek",
            "zkmarek/video/slides/episode2/TeX files/operations.tex",
        )

    def create_tex_below(self, path) -> Tex:
        tex = Tex(load(path), tex_template=self.template, color=SECONDARY_COLOR)
        tex.next_to(self.tex, DOWN, buff=0.5)
        tex.align_to(self.tex, LEFT)
        return tex

    def animate_in(self, scene):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{cancel}")
        self.curve = Secp256k1_41
        self.weierstrass_form = Text(r"Weierstrass form", color=PRIMARY_COLOR)
        self.weierstrass_equation = MathTex(r"y^2 = x^3 + ax + b", color=PRIMARY_COLOR)
        self.chart = DiscreteEllipticChart(self.curve).scale(0.8)
        self.chart.center()

        self.wallet = Wallet("private key", "address")
        self.chart_wallet = (
            DiscreteEllipticChart(self.curve, dot_color=BACKGROUND_COLOR)
            .scale(0.5)
            .shift(1 * DOWN + 4 * LEFT)
        )

        self.new_subsection(scene, "intro", sound="data/sound/episode2/ec_prev_on0.mp3")
        scene.play(Write(self.title_text.center()))
        self.title_text.generate_target()
        self.title_text.target.shift(3 * LEFT + 3 * UP)
        scene.play(MoveToTarget(self.title_text))
        self.weierstrass_form.next_to(self.weierstrass_equation, UP)
        scene.play(FadeIn(self.chart))
        self.new_subsection(
            scene, "equation", sound="data/sound/episode2/ec_prev_on1.mp3"
        )
        scene.wait(3)
        scene.play(Indicate(self.chart), run_time=2, color=HIGHLIGHT_COLOR)
        scene.wait(2.5)
        self.chart.animate_align_left(scene)
        scene.play(Write(self.weierstrass_form.to_edge(RIGHT)))
        scene.wait(1.5)
        scene.play(
            Write(self.weierstrass_equation.next_to(self.weierstrass_form, DOWN)),
            run_time=1,
        )
        scene.wait(3)
        scene.play(FadeOut(self.weierstrass_form), FadeOut(self.weierstrass_equation))

        self.new_subsection(
            scene, "Operations", sound="data/sound/episode2/ec_prev_on2.mp3"
        )
        scene.play(Write(self.tex.shift(RIGHT * 3)))
        scene.wait(2)
        self.tex[0][0:14].set_color(HIGHLIGHT_COLOR)
        scene.wait(1.5)
        self.tex[0][14:27].set_color(HIGHLIGHT_COLOR)
        scene.wait(1.5)
        self.tex[0][27:52].set_color(HIGHLIGHT_COLOR)
        scene.wait(5)
        self.new_subsection(
            scene, "inverse", sound="data/sound/episode2/ec_prev_on3.mp3"
        )

        tex2 = self.create_tex_below(
            "zkmarek/video/slides/episode2/TeX files/inv_operations.tex"
        )
        tex3 = self.create_tex_below(
            "zkmarek/video/slides/episode2/TeX files/sout_inv_operations.tex"
        )
        scene.play(Write(tex2))
        scene.wait(2)
        scene.play(ReplacementTransform(tex2, tex3))
        scene.wait(6)
        scene.play(Indicate(self.chart, color=HIGHLIGHT_COLOR))
        scene.play(Unwrite(self.tex))
        scene.play(Unwrite(tex3))
        scene.play(FadeOut(self.chart), run_time=1.5)

        # wallet

        self.animate_secret_key(scene)

        self.animate_scalar_multiplication(scene)

        self.animate_generate_ethereum_address(scene)

        self.big_numbers_private_key(scene)

        scene.play(Unwrite(self.title_text))

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
