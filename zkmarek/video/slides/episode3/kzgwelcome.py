from manim import (
    Text,
    MathTex,
    Rectangle,
    LEFT,
    RIGHT,
    Line,
    DOWN,
    UL,
    UR,
    FadeIn,
    FadeOut,
    Write,
    UP,
    Create,
    ReplacementTransform,
    Indicate,
)

from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import (
    PRIMARY_COLOR,
    PRIMARY_FONT,
    SECONDARY_COLOR,
    HIGHLIGHT_COLOR,
)


class KZGwelcome(SlideBase):
    polynomial: MathTex

    def __init__(self):
        super().__init__("KZG_welcome")

    def construct(self):
        self.prover = Text(
            r"Prover", font_size=30, color=PRIMARY_COLOR, font=PRIMARY_FONT
        )
        self.verifier = Text(
            r"Verifier", font_size=30, color=PRIMARY_COLOR, font=PRIMARY_FONT
        )
        self.polynomial = MathTex("p(x) = 1x^3 - 2x^2 + 3x + 4", color=HIGHLIGHT_COLOR)
        self.polynomial_copy = self.polynomial.copy()
        self.polynomial_copy[0][5:6].set_color(SECONDARY_COLOR)
        self.polynomial_copy[0][8:10].set_color(SECONDARY_COLOR)
        self.polynomial_copy[0][13:14].set_color(SECONDARY_COLOR)
        self.polynomial_copy[0][16:17].set_color(SECONDARY_COLOR)
        self.data_text = ["1", "-2", "3", "4"]
        self.leaves = [
            Rectangle(width=2, height=1, color=PRIMARY_COLOR).scale(0.7)
            for _ in self.data_text
        ]
        self.leaf_labels = [
            Text(text, font_size=24).scale(0.7).move_to(leaf.get_center())
            for leaf, text in zip(self.leaves, self.data_text)
        ]
        for i, leaf in enumerate(self.leaves):
            leaf.move_to(3 * LEFT + i * 2 * RIGHT + 2 * DOWN)
        for i, label in enumerate(self.leaf_labels):
            label.move_to(3 * LEFT + i * 2 * RIGHT + 2 * DOWN)

    def animate_in(self, scene):
        scene.play(
            FadeIn(self.prover.to_corner(UL)),
            FadeIn(self.verifier.to_corner(UR)),
            FadeIn(self.polynomial),
        )
        scene.wait(1)
        scene.play(ReplacementTransform(self.polynomial, self.polynomial_copy))
        scene.wait(1)
        scene.play(FadeOut(self.polynomial_copy))
        for leaf, label in zip(self.leaves, self.leaf_labels):
            scene.play(Create(leaf), Write(label), run_time=0.3)
        for label in self.leaf_labels:
            scene.play(Indicate(label), color=SECONDARY_COLOR)
        leaf_hashes = [
            Rectangle(width=2, height=1, color=HIGHLIGHT_COLOR)
            .scale(0.7)
            .next_to(leaf, UP, buff=0.5)
            for leaf in self.leaves
        ]
        leaf_hash_labels = [
            Text(f"H({text})", font_size=24).scale(0.7).move_to(hash_rect.get_center())
            for hash_rect, text in zip(leaf_hashes, self.data_text)
        ]

        for hash_rect, hash_label in zip(leaf_hashes, leaf_hash_labels):
            scene.play(Create(hash_rect), Write(hash_label), run_time=0.3)

        internal_hashes = [
            Rectangle(width=3, height=1.5, color=SECONDARY_COLOR)
            .scale(0.7)
            .next_to(leaf_hashes[i], UP, buff=0.5)
            for i in range(0, len(leaf_hashes), 2)
        ]
        internal_hash_labels = [
            Text(f"H(H({self.data_text[i]}) || H({self.data_text[i+1]}))", font_size=24)
            .scale(0.7)
            .move_to(internal_hashes[i // 2].get_center())
            for i in range(0, len(self.data_text), 2)
        ]

        for hash_rect, hash_label in zip(internal_hashes, internal_hash_labels):
            scene.play(Create(hash_rect), Write(hash_label))

        root_hash = (
            Rectangle(width=6, height=1.5, color=SECONDARY_COLOR)
            .scale(0.7)
            .next_to(internal_hashes[0], UP, buff=0.5)
        )
        root_hash_label = (
            Text("H(H(H(1)||H(-2))||H(H(3)||H(4)))", font_size=24)
            .scale(0.7)
            .move_to(root_hash.get_center())
        )

        scene.play(Create(root_hash), Write(root_hash_label), run_time=0.4)

        for i in range(len(self.leaves)):
            scene.play(
                Create(
                    Line(self.leaves[i].get_top(), leaf_hashes[i].get_bottom()),
                    run_time=0.4,
                )
            )

        for i in range(0, len(leaf_hashes), 2):
            scene.play(
                Create(
                    Line(leaf_hashes[i].get_top(), internal_hashes[i // 2].get_bottom())
                ),
                run_time=0.4,
            )
            scene.play(
                Create(
                    Line(
                        leaf_hashes[i + 1].get_top(),
                        internal_hashes[i // 2].get_bottom(),
                    )
                ),
                run_time=0.4,
            )

        scene.play(
            Create(Line(internal_hashes[0].get_top(), root_hash.get_bottom())),
            run_time=0.4,
        )
        scene.play(
            Create(Line(internal_hashes[1].get_top(), root_hash.get_bottom())),
            run_time=0.4,
        )

        scene.wait(2)

    def animate_out(self, scene):
        scene.play(FadeOut(self.prover), FadeOut(self.verifier))
