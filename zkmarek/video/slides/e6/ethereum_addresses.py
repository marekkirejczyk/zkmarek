from manim import (Text, FadeIn, Create, RoundedRectangle, Write, ImageMobject, FadeOut, UP, DOWN, Group, RIGHT, LEFT, ChangeDecimalToValue,
                   Integer, Brace, VGroup, MoveToTarget, ReplacementTransform)

from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT

class EthereumAddresses(SlideBase):
    def __init__(self) -> None:
        super().__init__("Storing Ethereum Data")
        
    def construct(self):
        self.title_label = Text("Storing Ethereum Data", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size = 40).to_edge(UP)
        self.block = RoundedRectangle(width=8.5, height=3, color=PRIMARY_COLOR, fill_opacity=0.17, stroke_width = 0.0)
        self.ethereum = ImageMobject("data/images/new_ethereum.png").scale(1).move_to(self.block.get_bottom()+RIGHT*3+UP*0.8)
        self.block = Group(self.block, self.ethereum)
        self.number = Integer(0, color = PRIMARY_COLOR).move_to(self.block.get_center()).shift(RIGHT+UP*0.3)
        self.addresses = Text("0x837416...934816", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=25)
        self.more_addresses = Text("0x123456...789012", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=25).next_to(self.addresses, DOWN, buff = 0.6)
        self.dots = Text("...\n...", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=30).next_to(self.more_addresses, DOWN, buff = 0.3)
        self.addresses_all = VGroup(self.addresses, self.more_addresses, self.dots).next_to(self.number, LEFT, buff = 0.8)
        self.brace_addresses = Brace(self.addresses_all, RIGHT, color=PRIMARY_COLOR).next_to(self.addresses_all, RIGHT, buff = 0.3)
        
        
    def animate_in(self, scene):
        self.new_subsection(scene, "Ethereum addresses", "data/sound/e6/slide2-3i.mp3")
        scene.play(Write(self.title_label), run_time=0.7)
        scene.play(FadeIn(self.block, self.addresses_all, self.brace_addresses))
        scene.play(ChangeDecimalToValue(self.number, 308105039), run_time=2)
        self.addresses.generate_target()
        self.addresses.target.move_to(self.block.get_center())
        scene.play(FadeOut(self.dots, self.more_addresses, self.number, self.brace_addresses), run_time=0.5)
        scene.play(MoveToTarget(self.addresses), run_time=0.5)
        
        self.length_brace = Brace(self.addresses[2:], DOWN, color = PRIMARY_COLOR)
        self.length_text = Text("40 nibbles", color = PRIMARY_COLOR, font=PRIMARY_FONT, font_size=20).next_to(self.length_brace, DOWN, buff = 0.1)
        self.length_text_bytes = Text("20 bytes", color = PRIMARY_COLOR, font=PRIMARY_FONT, font_size=20).next_to(self.length_brace, DOWN, buff = 0.1)
        scene.play(Create(self.length_brace), Write(self.length_text))
        scene.wait(3)
        scene.play(ReplacementTransform(self.length_text, self.length_text_bytes))
        scene.wait(1.5)
        scene.play(FadeOut(self.addresses, self.length_brace, self.length_text_bytes, self.block))
        
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.title_label))
        
        