from manim import UP, MoveToTarget, RIGHT, Scene, ScaleInPlace, Text, MathTex, Write, FadeOut, \
    TransformMatchingTex, FadeIn, Circumscribe, Circle, Indicate

from zkmarek.crypto.ec_affine import ECAffine
from zkmarek.crypto.subgroup import Subgroup
from zkmarek.crypto.weierstrass_curve import WeierstrassCurve, Secp256k1_41
from zkmarek.video.constant import PRIMARY_COLOR, BACKGROUND_COLOR, PRIMARY_FONT
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

    def __init__(self):
        super().__init__("Ethereum Wallet")

    def construct(self):
        self.wallet = Wallet("private key", "address")
        self.chart = DiscreteEllipticChart(self.curve, dot_color=BACKGROUND_COLOR)

    def animate_in(self, scene):
        self.animate_secret_key(scene)
        self.animate_public_key(scene)
        self.animate_scalar_multiplication(scene)

    def animate_secret_key(self, scene):
        self.wallet.animate_in(scene)
        self.wallet.animate_random_secret_key(scene, 17, 41)
        scene.wait()
        scene.play(ScaleInPlace(self.wallet, 0.5))
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

        generator1 = ECAffine(36, 28, self.curve)
        subgroup1 = Subgroup.from_generator(generator1)
        animation1 = AnimateSubgroups(self.chart, runtime_per_step=0.6)

        animation1.animate_generator(scene, generator1, split_animation=True)
        scene.wait(2)
        animation1.animate_subgroup_mid(scene, subgroup1, generator1, 2, 18)

        scene.wait(1)
        gen_dot = self.chart.find_dot_by_affine(ECAffine(39, 9, self.curve))
        scene.play(Circumscribe(gen_dot, Circle))
        scene.play(Write(animation1.coordinates[16]))
