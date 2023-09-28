from typing import List

from manim import UP, MoveToTarget, RIGHT, Scene, ScaleInPlace, Text, MathTex, Write, FadeOut, \
    TransformMatchingTex, FadeIn, Circumscribe, Circle, DEFAULT_FONT_SIZE

from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.crypto.subgroup import Subgroup
from zkmarek.crypto.weierstrass_curve import WeierstrassCurve, Secp256k1_41
from zkmarek.video.constant import PRIMARY_COLOR, BACKGROUND_COLOR, PRIMARY_FONT, HIGHLIGHT_COLOR
from zkmarek.video.mobjects.discreet_elliptic_chart import DiscreteEllipticChart
from zkmarek.video.mobjects.wallet import Wallet
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.ec.animate_subgroup import AnimateSubgroups


class WalletSlide(SlideBase):
    wallet: Wallet
    scene: Scene
    public_key: Text
    public_key_equation: MathTex
    chart: DiscreteEllipticChart
    curve: WeierstrassCurve = Secp256k1_41
    public_key_coordinates: MathTex

    def __init__(self):
        super().__init__("Ethereum Wallet")

    def construct(self):
        self.wallet = Wallet("private key", "address")
        self.chart = DiscreteEllipticChart(self.curve, dot_color=BACKGROUND_COLOR)

    def animate_in(self, scene):
        self.animate_secret_key(scene)
        self.animate_public_key(scene)
        self.animate_scalar_multiplication(scene)
        self.animate_generate_ethereum_address(scene)

    def animate_secret_key(self, scene):
        self.wallet.animate_in(scene)
        self.wallet.animate_random_secret_key(scene, 17, 41)
        scene.wait()
        scene.play(ScaleInPlace(self.wallet, 0.33))
        self.wallet.generate_target()
        self.wallet.target.shift(2 * UP + 5 * RIGHT)
        scene.play(MoveToTarget(self.wallet))

    def animate_public_key(self, scene):
        self.public_key = Text(r"Public key (pk)", font=PRIMARY_FONT, color=PRIMARY_COLOR)
        self.public_key_equation = MathTex(r"{{pk}}", "=", "{{sk}}", "*", "{{G}}", color=PRIMARY_COLOR)
        self.public_key.next_to(self.public_key_equation, UP)
        scene.play(Write(self.public_key), run_time=2)
        scene.play(Write(self.public_key_equation), run_time=2)
        scene.wait()
        new_public_key_equation = MathTex(r"{{pk}}", "=", "0x11", "*", "{{G}}", color=PRIMARY_COLOR)
        scene.play(TransformMatchingTex(
            self.public_key_equation,
            new_public_key_equation
        ))
        self.public_key_equation = new_public_key_equation
        scene.wait()
        new_public_key_equation = MathTex(r"{{pk}}", "=", "17", "*", "{{G}}", color=PRIMARY_COLOR)
        scene.play(TransformMatchingTex(
            self.public_key_equation,
            new_public_key_equation
        ))
        self.public_key_equation = new_public_key_equation
        scene.wait()
        scene.play(FadeOut(self.public_key, self.public_key_equation))

    def animate_scalar_multiplication(self, scene):
        scene.play(FadeIn(self.chart))

        generator = ECAffine(36, 28, self.curve)
        subgroup = Subgroup.from_generator(generator)
        animation = AnimateSubgroups(self.chart, runtime_per_step=0.6)
        animation.animate_generator(scene, generator, split_animation=True)

        scene.wait()
        animation.animate_subgroup_mid(scene, subgroup, generator, 2, 18)

        scene.wait()
        public_key_point = self.chart.find_dot_by_affine(ECAffine(39, 9, self.curve))
        scene.play(Circumscribe(public_key_point, Circle))
        self.public_key_coordinates = MathTex("= ", "(", "{{39}}", ",", "{{9}}", ")",
                                              font_size=20, color=HIGHLIGHT_COLOR)
        self.public_key_coordinates.next_to(public_key_point, RIGHT, buff=0.7)
        scene.play(Write(self.public_key_coordinates))

        scene.wait()
        animation.animate_out_labels(scene)
        animation.animate_out_dots(scene)
        scene.play(FadeOut(self.chart))

    def animate_generate_ethereum_address(self, scene):
        def transform(into: List[str], font_size=DEFAULT_FONT_SIZE):
            pkc = MathTex(*into, font_size=font_size)
            scene.play(TransformMatchingTex(self.public_key_coordinates, pkc), run_time=2)
            self.public_key_coordinates = pkc

        transform(["(", "{{39}}", ",", "{{9}}", ")"])
        transform(["(", "{{0x27}}", ",", "{{0x09}}", ")"])
        transform(["(", '{{27}}', ',', '{{09}}', ')'])
        transform(['"', '{{27}}', '"+"', '{{09}}', '"'])
        transform(['"', '{{27}}', '{{09}}', '"'])
        transform(['keccak256(', '"', '{{27}}', '{{09}}', '"', ')'])
        transform(['{{0be4308d0014b842c2debb81}}', '{{7a629f45938a32a2117c186d46b29ef3aa599b4e}}'], font_size=20)
        transform(['{{7a629f45938a32a2117c186d46b29ef3aa599b4e}}'])
        transform(['0x', '{{7a629f45938a32a2117c186d46b29ef3aa599b4e}}'])

        self.wallet.generate_target()
        self.wallet.target.move_to(2 * UP)
        scene.play(MoveToTarget(self.wallet))
        scene.play(ScaleInPlace(self.wallet, 3))
        self.wallet.animate_address_value(scene, '0x7a629f45938a32a2117c186d46b29ef3aa599b4e',
                                          FadeOut(self.public_key_coordinates))

        self.wallet.generate_target()
        self.wallet.target.move_to(0)
        scene.play(MoveToTarget(self.wallet))
