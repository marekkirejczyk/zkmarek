from manim import UP, MoveToTarget, RIGHT, Scene, ScaleInPlace, Text, MathTex, Write, FadeOut, \
    TransformMatchingTex

from zkmarek.video.constant import PRIMARY_COLOR
from zkmarek.video.mobjects.wallet import Wallet
from zkmarek.video.slides.common.slide_base import SlideBase


class WalletSlide(SlideBase):
    wallet: Wallet
    scene: Scene
    public_key: Text
    public_key_equation: MathTex

    def __init__(self):
        super().__init__("Ethereum Wallet")

    def construct(self):
        self.wallet = Wallet("private key", "address")

    def animate_in(self, scene):
        self.generate_secret_key(scene)

        self.public_key = Text(r"Public key (pk)", color=PRIMARY_COLOR)
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

    def generate_secret_key(self, scene):
        self.wallet.animate_in(scene)
        self.wallet.animate_random_secret_key(scene, 17, 41)
        scene.wait()
        scene.play(ScaleInPlace(self.wallet, 0.5))
        self.wallet.generate_target()
        self.wallet.target.shift(2 * UP + 5 * RIGHT)
        scene.play(MoveToTarget(self.wallet))
