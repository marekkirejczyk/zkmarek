
from zkmarek.video.mobjects.wallet import Wallet
from zkmarek.video.slides.common.slide_base import SlideBase


class WalletSlide(SlideBase):
    wallet: Wallet
    def __init__(self):
        super().__init__("Ethereum Wallet")

    def construct(self):
        self.wallet = Wallet("private key", "address")

    def animate_in(self, scene):
        self.wallet.animate_in(scene)
