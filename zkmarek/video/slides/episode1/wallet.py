from typing import List

from manim import UP, MoveToTarget, RIGHT, Scene, ScaleInPlace, Text, MathTex, Write, FadeOut, \
    TransformMatchingTex, FadeIn, Circumscribe, Circle, DEFAULT_FONT_SIZE, LEFT, DOWN, Group, Indicate

from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.crypto.subgroup import Subgroup
from zkmarek.crypto.weierstrass_curve import WeierstrassCurve, Secp256k1_41
from zkmarek.video.constant import PRIMARY_COLOR, BACKGROUND_COLOR, PRIMARY_FONT, HIGHLIGHT_COLOR
from zkmarek.video.mobjects.discreet_elliptic_chart import DiscreteEllipticChart
from zkmarek.video.mobjects.wallet import Wallet
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.episode1.animate_subgroup import AnimateSubgroups


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
        self.chart = DiscreteEllipticChart(self.curve, dot_color=BACKGROUND_COLOR).scale(0.5).shift(1 * DOWN + 4 * LEFT)

    def animate_in(self, scene):
        self.animate_secret_key(scene)
        self.animate_public_key(scene)
        self.animate_scalar_multiplication(scene)
        self.animate_generate_ethereum_address(scene)
        self.animate_big_number_private_key(scene)

    def animate_secret_key(self, scene):
        self.new_subsection(scene, "Secret key", sound="data/sound/episode1/s27-1.wav")
        self.wallet.animate_in(scene)
        self.new_subsection(scene, "Generate random secret", sound="data/sound/episode1/s27-2.m4a")
        scene.wait()
        self.wallet.animate_random_secret_key(scene, 17, 41)
        scene.play(ScaleInPlace(self.wallet, 0.33), run_time=0.5)
        self.wallet.generate_target()
        self.wallet.target.shift(2 * UP + 5 * RIGHT)
        scene.play(MoveToTarget(self.wallet), run_time=0.5)

    def animate_public_key(self, scene):
        self.new_subsection(scene, "Public key", sound="data/sound/episode1/s27-4.wav")
        self.public_key = Text(r"Public key (pk)", font=PRIMARY_FONT, color=PRIMARY_COLOR)
        self.public_key_equation = MathTex(r"{{pk}}", "=", "{{secret\\_key}}", "*", "{{G}}", color=PRIMARY_COLOR)
        self.public_key.next_to(self.public_key_equation, UP)
        scene.play(Write(self.public_key), run_time=2)
        self.new_subsection(scene, "Public key", sound="data/sound/episode1/s27-5.wav")
        scene.play(Write(self.public_key_equation), run_time=3)
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

    def animate_scalar_multiplication(self, scene):
        scene.play(FadeIn(self.chart))

        generator = ECAffine(36, 28, self.curve)
        subgroup = Subgroup.from_generator(generator)
        animation = AnimateSubgroups(self.chart, runtime_per_step=0.1)
        animation.animate_generator(scene, generator)
        animation.animate_subgroup_mid(scene, subgroup, generator, 2, 18)

        scene.wait()
        self.new_subsection(scene, "Private key from point", sound="data/sound/episode1/s27-6.wav")
        public_key_point = self.chart.find_dot_by_affine(ECAffine(39, 9, self.curve))
        scene.play(Circumscribe(public_key_point, Circle))
        self.public_key_coordinates = MathTex("=", "(", "{{39}}", ",", "{{9}}", ")",
                                              font_size=20, color=HIGHLIGHT_COLOR)
        self.public_key_coordinates.next_to(public_key_point, RIGHT, buff=0.7)
        scene.play(Write(self.public_key_coordinates))

        scene.play(FadeOut(self.chart), FadeOut(*animation.labels), FadeOut(*animation.duplicates))

        new_public_key_equation = MathTex(r"{{pk}}", "=", "(", "{{39}}", ",", "{{9}}", ")", color=PRIMARY_COLOR)
        scene.play(TransformMatchingTex(Group(self.public_key_equation, self.public_key_coordinates),
                                        new_public_key_equation), run_time=0.5)
        self.public_key_coordinates = new_public_key_equation

    def animate_generate_ethereum_address(self, scene):
        def transform(into: List[str], font_size: int = DEFAULT_FONT_SIZE, run_time: float = 1):
            pkc = MathTex(*into, font_size=font_size, color=PRIMARY_COLOR)
            scene.play(TransformMatchingTex(self.public_key_coordinates, pkc), run_time=run_time)
            self.public_key_coordinates = pkc

        scene.play(FadeOut(self.public_key))
        transform(["(", "{{39}}", ",", "{{9}}", ")"], run_time=0.5)
        transform(["(", "{{0x}}", "{{27}}", ",", "{{0x}}", "{{09}}", ")"])
        transform(['keccak256(', '"', '{{27}}', '{{09}}', '"', ')'], run_time=2)
        transform(['{{0be4308d0014b842c2debb81}}', '{{7a629f45938a32a2117c186d46b29ef3aa599b4e}}'], font_size=20)
        transform(['{{7a629f45938a32a2117c186d46b29ef3aa599b4e}}'])
        self.new_subsection(scene, "Add 0x", sound="data/sound/episode1/s27-7.wav")
        scene.wait(4)
        transform(['0x', '{{7a629f45938a32a2117c186d46b29ef3aa599b4e}}'])
        self.new_subsection(scene, "Add 0x", sound="data/sound/episode1/s27-8.wav")

        self.wallet.generate_target()
        self.wallet.target.move_to(2 * UP)
        scene.play(MoveToTarget(self.wallet))
        scene.play(ScaleInPlace(self.wallet, 3))
        self.wallet.animate_address_value(scene, '0x7a629f45938a32a2117c186d46b29ef3aa599b4e',
                                          FadeOut(self.public_key_coordinates))

        self.wallet.generate_target()
        self.wallet.target.move_to(0)
        scene.play(MoveToTarget(self.wallet))

    def animate_big_number_private_key(self, scene: Scene):
        self.play_sound(scene, "data/sound/episode1/s27-9.wav")
        scene.wait(1)
        scene.play(Indicate(self.wallet.secret_key_value))
        self.play_sound(scene, "data/sound/episode1/s27-10.wav")
        self.play_sound(scene, "data/sound/episode1/s27-11.wav")
        secp256k1 = Text("Secp256k1", font=PRIMARY_FONT, color=PRIMARY_COLOR)
        secp256k1.move_to(2.5 * UP)
        scene.play(FadeIn(secp256k1))
        self.play_sound(scene, "data/sound/episode1/s27-12.wav")
        scene.play(FadeOut(secp256k1))
        self.wallet.animate_private_key(scene, '0x9de347a715a200cd....c8364d879483b69b', font_size=14)
        self.wallet.animate_address_value(scene, '')
        self.play_sound(scene, "data/sound/episode1/s27-13.wav")
        scene.wait(2)
        self.wallet.animate_address_value(scene, '0x9de347a715a200cd....c8364d879483b69b')
        scene.wait(1.5)
        self.wallet.animate_address_value(scene, '0x9de347a715a200cd....c8364d879483b69b * G')
        scene.wait(2)
        self.wallet.animate_address_value(scene, '(0xc4a0c0a9...7484e855, 0x32b5524f...fb56c074)')
        self.play_sound(scene, "data/sound/episode1/s27-14.wav")
        scene.wait(2)
        self.wallet.animate_address_value(scene, '0xe31cc18f3f3718588e9a878a516c7889af047171')
        self.play_sound(scene, "data/sound/episode1/s27-15.wav")
        self.play_sound(scene, "data/sound/episode1/s27-16.wav")
        self.play_sound(scene, "data/sound/episode1/s27-17.wav")
