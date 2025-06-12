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
    MoveToTarget,
    Unwrite,
    ReplacementTransform,
    Indicate,
    Dot,
    VGroup,
    ApplyWave,
    RoundedRectangle,
    Create
)
from random import randint
from zkmarek.video.constant import (
    PRIMARY_COLOR,
    SECONDARY_COLOR,
    BACKGROUND_COLOR,
    HIGHLIGHT_COLOR,
    PRIMARY_FONT,
    HIGHLIGHT2_COLOR
)
from zkmarek.video.mobjects.discreet_elliptic_chart import (
    DiscreteEllipticChart,
)
from zkmarek.video.mobjects.wallet import Wallet

from zkmarek.video.slides.common.tex_slide import TexSlide
from zkmarek.crypto.weierstrass_curve import Secp256k1_41
from zkmarek.video.mobjects.sidebar import Sidebar
from zkmarek.video.slides.episode1.animate_subgroup import AnimateSubgroups
from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.crypto.subgroup import Subgroup
from zkmarek.video.utils import load
from zkmarek.video.mobjects.standard import (
    secp256k1_standard,
)


class PreviouslyOn(TexSlide):
    chart: DiscreteEllipticChart
    sidebar: Sidebar
    wallet: Wallet
    scene: Scene
    public_key: Text
    dots: list[Dot]
    dot_color: str
    duplicates: list[Dot]

    def __init__(self) -> None:
        super().__init__(
            "Previously on ZKMarek",
            "zkmarek/video/slides/episode2/tex/operations.tex",
        )

    def create_tex_below(self, path) -> Tex:
        tex = Tex(load(path), tex_template=self.template, color=SECONDARY_COLOR)
        tex.next_to(self.tex, DOWN, buff=0.5)
        return tex

    def animate_in(self, scene):
        self.curve = Secp256k1_41
        self.weierstrass_form = Text(r"Weierstrass form", color=PRIMARY_COLOR).scale(
            0.8
        )
        self.weierstrass_equation = MathTex(r"y^2 = x^3 + ax + b", color=PRIMARY_COLOR)
        self.labels = []
        self.chart = DiscreteEllipticChart(self.curve).scale(0.8)
        self.secp256k1 = secp256k1_standard()
        self.label_standards = Text(
            r"Standards", color=HIGHLIGHT_COLOR, font=PRIMARY_FONT
        ).scale(0.8)
        self.wallet = Wallet("private key", "address")
        self.chart_wallet = (
            DiscreteEllipticChart(self.curve, dot_color=BACKGROUND_COLOR)
            .scale(0.7)
            .shift(LEFT * 0.5)
        )

        self.new_subsection(scene, "intro", sound="data/sound/episode2/slide2-0.mp3")
        scene.play(Write(self.title_text.center()))
        self.title_text.generate_target()
        self.title_text.target.to_edge(UP)
        scene.play(MoveToTarget(self.title_text))
        self.weierstrass_form.next_to(self.weierstrass_equation, UP)

        self.new_subsection(scene, "equation", sound="data/sound/episode2/slide2-1.mp3")
        self.chart.next_to(self.title_text.target, DOWN)
        scene.play(Write(self.chart), run_time=1)
        scene.wait(0.75)
        dots = VGroup(*self.chart.dots)
        scene.play(Indicate(dots, color=HIGHLIGHT_COLOR, scale=1.05))
        scene.play(
            ApplyWave(self.chart.ax[0]), ApplyWave(self.chart.ax[1]), DIRECTION=UP
        )
        self.chart.animate_align_left(scene)
        scene.play(
            FadeIn(self.weierstrass_form.to_edge(RIGHT)),
            FadeIn(self.weierstrass_equation.next_to(self.weierstrass_form, DOWN)),
        )
        scene.wait(1)
        scene.play(FadeOut(self.weierstrass_form), FadeOut(self.weierstrass_equation))

        self.new_subsection(
            scene, "Operations", sound="data/sound/episode2/slide2-2.mp3"
        )
        self.tex.scale(0.8)
        scene.play(Write(self.tex.shift(RIGHT * 3)))
        scene.wait(1.5)
        self.tex[0][0:14].set_color(HIGHLIGHT_COLOR)
        scene.wait(1.5)
        self.tex[0][14:27].set_color(HIGHLIGHT_COLOR)
        scene.wait(1.5)
        self.tex[0][27:52].set_color(HIGHLIGHT_COLOR)
        scene.wait(2.5)

        self.new_subsection(scene, "inverse", sound="data/sound/episode2/slide2-3.mp3")
        self.tex2 = (
            self.create_tex_below(
                "zkmarek/video/slides/episode2/tex/inv_operations.tex"
            )
            .scale(0.8)
            .shift(LEFT * 0.5)
        )
        self.tex3 = (
            self.create_tex_below(
                "zkmarek/video/slides/episode2/tex/sout_inv_operations.tex"
            )
            .scale(0.8)
            .shift(LEFT * 0.5)
        )
        scene.wait(1.2)
        scene.play(Indicate(self.tex[0][27:52]))
        scene.wait(2)
        scene.play(Write(self.tex2))
        scene.wait(0.8)
        scene.play(ReplacementTransform(self.tex2, self.tex3))
        scene.wait(0.7)

    def animate_out(self, scene):
        scene.play(Unwrite(self.tex3), Unwrite(self.tex), Unwrite(self.chart))

        secp = []
        for i in range(0, 3):
            secp.append(self.secp256k1.copy_with_rows(i + 1))
        self.label_standards.move_to(UP * 2)
        scene.play(FadeIn(self.label_standards), FadeIn(secp[2]))
        scene.play(Indicate(secp[2].rows[0][0][0]), color=SECONDARY_COLOR)

        scene.wait(4.7)
        scene.play(Indicate(secp[2].rows[0][0][1]), color=SECONDARY_COLOR)
        scene.play(Indicate(secp[2].rows[1][0]), color=SECONDARY_COLOR)
        scene.play(Indicate(secp[2].rows[2][0]), color=SECONDARY_COLOR)
        scene.wait(0.6)
        scene.play(FadeOut(secp[2]), FadeOut(self.label_standards))

        self.animate_secret_key(scene)

        self.animate_scalar_multiplication(scene)

        self.animate_generate_ethereum_address(scene)

        scene.play(Unwrite(self.title_text))

    def animate_secret_key(self, scene):
        self.new_subsection(
            scene, "Generate random secret", sound="data/sound/episode2/slide2-4.mp3"
        )
        self.wallet.animate_in(scene)

        rounds = 20
        rand_max = 41
        final_value = 17
        for key in [str(randint(0, rand_max)) for i in range(rounds)] + [
            str(final_value),
        ]:
            last = key.startswith("0x")
            if last:
                scene.wait(2.5)
            self.wallet.animate_private_key(scene, key, 1 if last else 0.1)
        scene.play(self.wallet.animate.shift(UP * 2 + RIGHT * 3).scale(0.5), run_time=1)

    def animate_scalar_multiplication(self, scene):
        scene.play(FadeIn(self.chart_wallet))

        generator = ECAffine(36, 28, self.curve)
        subgroup = Subgroup.from_generator(generator)
        animation = AnimateSubgroups(self.chart_wallet, runtime_per_step=0.05)
        animation.animate_generator(scene, generator)
        scene.wait(3.5)
        animation.animate_subgroup_mid(scene, subgroup, generator, 2, 18)

        public_key_point = self.chart_wallet.find_dot_by_affine(
            ECAffine(39, 9, self.curve)
        )
        scene.play(Circumscribe(public_key_point, Circle))
        self.public_key_coordinates = MathTex(
            "=(39,9)", font_size=20, color=HIGHLIGHT_COLOR
        )
        self.public_key_coordinates.next_to(public_key_point, RIGHT, buff=0.7)
        scene.play(Write(self.public_key_coordinates))
        scene.play(
            FadeOut(self.public_key_coordinates),
            FadeOut(self.chart_wallet),
            FadeOut(*animation.labels),
            FadeOut(*animation.duplicates),
        )

    def animate_generate_ethereum_address(self, scene):

        scene.play(self.wallet.animate.shift(DOWN * 2 + LEFT * 3).scale(2), run_time=1)
        self.wallet.animate_address_value(scene, "(39, 9)")
        self.wallet.animate_address_value(scene, "(0x27, 0x09)")
        scene.wait(1)
        self.play_sound(scene, "data/sound/episode2/slide2-5.mp3")
        self.wallet.animate_address_value(scene, "keccak256(2709)")
        scene.wait(0.3)
        self.wallet.animate_address_value(
            scene,
            "0be4308d0014b842c2debb817a629f45938a32a2117c186d46b29ef3aa599b4e",
        )
        self.wallet.animate_address_value(
            scene,
            "0x7a629f45938a32a2117c186d46b29ef3aa599b4e",
        )

        scene.wait(1.5)
        scene.play(FadeOut(self.wallet))

    def animate_miniature(self, scene):
        self.curve = Secp256k1_41

        rectangle = RoundedRectangle(corner_radius=0.3, width = 4, height = 2, color = PRIMARY_COLOR).set_color_by_gradient([PRIMARY_COLOR, HIGHLIGHT2_COLOR]).shift(LEFT * 4.5 + UP * 1.5)
        self.chart = DiscreteEllipticChart(self.curve, dot_color=HIGHLIGHT_COLOR).scale(0.25).move_to(rectangle.get_center()).shift(LEFT * 0.8)
        self.tex.scale(0.3).next_to(self.chart, RIGHT, buff=0.0)
        self.tex.shift(LEFT * 2.8)
        self.chart.gen_points()
        self.add(self.chart, self.tex, rectangle)
        scene.play(FadeIn(rectangle))
        scene.play(Create(self.chart), run_time=0.5)
        scene.play(Write(self.tex.shift(RIGHT * 3)))
        scene.play(self.tex[0][0:14].animate.set_color(HIGHLIGHT_COLOR), run_time=0.3)
        scene.play(self.tex[0][14:27].animate.set_color(HIGHLIGHT_COLOR), run_time=0.3)
        scene.play(self.tex[0][27:52].animate.set_color(HIGHLIGHT_COLOR), run_time=0.3)
