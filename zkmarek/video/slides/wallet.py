from manim import UP, MoveToTarget, RIGHT, Scene, ScaleInPlace

from zkmarek.video.mobjects.wallet import Wallet
from zkmarek.video.slides.common.slide_base import SlideBase


class WalletSlide(SlideBase):
    wallet: Wallet
    scene: Scene

    def __init__(self):
        super().__init__("Ethereum Wallet")

    def construct(self):
        self.wallet = Wallet("private key", "address")

    def animate_in(self, scene):
        self.wallet.animate_in(scene)
        self.wallet.generate_random_secret_key(scene, 7)
        scene.wait()
        scene.play(ScaleInPlace(self.wallet, 0.5))
        self.wallet.generate_target()
        self.wallet.target.shift(2 * UP + 4 * RIGHT)
        scene.play(MoveToTarget(self.wallet))
