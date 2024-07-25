from manim import (
    Text,
    MathTex,
    Rectangle,
    LEFT,
    RIGHT,
    Line,
    DOWN,
    FadeIn,
    FadeOut,
    Write,
    UP,
    Create,
    ReplacementTransform,
    Scene,
    VGroup,
    MoveToTarget,
)
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import (
    PRIMARY_COLOR,
    SECONDARY_COLOR,
    HIGHLIGHT_COLOR,
)


class Verkle(SlideBase):
    polynomial: MathTex

    def __init__(self):
        super().__init__("Verkle Tree")

    def construct(self):
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

    def animate_in(self, scene: Scene):
        scene.play(
            FadeIn(self.polynomial),
        )
        scene.wait(1)
        scene.play(ReplacementTransform(self.polynomial, self.polynomial_copy))
        scene.wait(1)

        self.polynomial_copy.generate_target()
        self.polynomial_copy.target.scale(0.6).to_edge(DOWN)
        scene.play(MoveToTarget(self.polynomial_copy))
        scene.wait(1)

        self.polynomial_labels = [
            self.polynomial_copy[0][5:6].copy(),
            self.polynomial_copy[0][8:10].copy(),
            self.polynomial_copy[0][13:14].copy(),
            self.polynomial_copy[0][16:17].copy(),
        ]

        for i in range(4):
            leaf, label = self.leaves[i], self.polynomial_labels[i]
            scene.play(Create(leaf), run_time=0.3)
            label.generate_target()
            label.target.move_to(leaf.get_center())
            scene.play(MoveToTarget(label))

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
            .move_to(
                (leaf_hashes[i].get_center() + leaf_hashes[i + 1].get_center()) / 2
            )
            .shift(UP * 1.5)
            for i in range(0, len(leaf_hashes), 2)
        ]
        internal_hash_labels = [
            Text(f"H(H({self.data_text[i]})||H({self.data_text[i+1]}))", font_size=24)
            .scale(0.7)
            .move_to(internal_hashes[i // 2].get_center())
            for i in range(0, len(self.data_text), 2)
        ]

        for hash_rect, hash_label in zip(internal_hashes, internal_hash_labels):
            scene.play(Create(hash_rect), Write(hash_label))

        root_hash = (
            Rectangle(width=6, height=1.5, color=SECONDARY_COLOR)
            .scale(0.7)
            .move_to(
                (internal_hashes[0].get_center() + internal_hashes[1].get_center()) / 2
            )
            .shift(UP * 1.5)
        )
        self.root_hash_label = (
            Text(
                f"H(H(H({self.data_text[0]})||H({self.data_text[1]}))||H(H({self.data_text[2]})||H({self.data_text[3]})))",
                font_size=24,
            )
            .scale(0.7)
            .move_to(root_hash.get_center())
        )

        scene.play(Create(root_hash), Write(self.root_hash_label), run_time=0.4)

        lines = []
        for i in range(len(self.leaves)):
            line = Line(self.leaves[i].get_top(), leaf_hashes[i].get_bottom())
            lines.append(line)
            scene.play(Create(line), run_time=0.4)

        for i in range(0, len(leaf_hashes), 2):
            line1 = Line(leaf_hashes[i].get_top(), internal_hashes[i // 2].get_bottom())
            line2 = Line(
                leaf_hashes[i + 1].get_top(), internal_hashes[i // 2].get_bottom()
            )
            lines.append(line1)
            lines.append(line2)
            scene.play(Create(line1), run_time=0.4)
            scene.play(Create(line2), run_time=0.4)

        line3 = Line(internal_hashes[0].get_top(), root_hash.get_bottom())
        line4 = Line(internal_hashes[1].get_top(), root_hash.get_bottom())
        lines.append(line3)
        lines.append(line4)
        scene.play(Create(line3), run_time=0.4)
        scene.play(Create(line4), run_time=0.4)

        scene.wait(2)

        self.all_mobjects = (
            [self.polynomial_copy]
            + self.leaves
            + self.polynomial_labels
            + leaf_hashes
            + leaf_hash_labels
            + internal_hashes
            + internal_hash_labels
            + [root_hash, self.root_hash_label]
            + lines
        )

    def animate_out(self, scene):
        scene.play(FadeOut(VGroup(*self.all_mobjects)))
