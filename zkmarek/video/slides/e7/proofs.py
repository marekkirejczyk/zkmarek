from manim import (
    Text,
    Write,
    UP,
    RIGHT,
    DOWN,
    LEFT,
    VGroup,
    FadeOut,
    RoundedRectangle,
    Arrow,
    StealthTip,
    MoveToTarget,
    ORIGIN,
    FadeIn,
    MathTex,
    Group,
    Indicate,
    TransformMatchingShapes,
    Brace,
)
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import (
    PRIMARY_COLOR,
    PRIMARY_FONT,
    SECONDARY_COLOR,
    HIGHLIGHT_COLOR,
    HIGHLIGHT2_COLOR,
)


class Proofs(SlideBase):
    def __init__(self) -> None:
        super().__init__("Proofs")

    def construct(self):
        self.title_label = Text(
            "Proofs", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=40
        ).to_edge(UP)

        ## values (1 level)
        values_rectangles = RoundedRectangle(
            corner_radius=0.05,
            width=0.5,
            height=0.3,
            fill_opacity=0.25,
            stroke_width=0.0,
        ).set_color(SECONDARY_COLOR)

        self.values = VGroup(*[values_rectangles.copy() for _ in range(2)]).arrange(
            RIGHT, buff=0.65
        )
        self.cdots = Text(
            "...", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=30
        ).next_to(self.values[0], RIGHT, buff=0.21)
        self.values.add(self.cdots)

        self.values2 = self.values.copy()
        self.values3 = self.values.copy()
        self.values4 = self.values.copy()

        texts_values = [
            Text("4", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=16),
            Text("85", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=16),
        ]

        for i, text in enumerate(texts_values):
            text.move_to(self.values[i].get_center())
            self.values[i].add(text)

        self.values_all = (
            VGroup(self.values, self.values2, self.values3, self.values4)
            .arrange(RIGHT, buff=0.7)
            .shift(DOWN * 3)
        )
        self.cdots_val1 = self.cdots.copy().next_to(self.values[1], RIGHT, buff=0.21)
        self.cdots_val2 = self.cdots.copy().next_to(self.values2[1], RIGHT, buff=0.21)
        self.cdots_val3 = self.cdots.copy().next_to(self.values3[1], RIGHT, buff=0.21)
        self.values_all.add(self.cdots_val1, self.cdots_val2, self.cdots_val3)

        ## commitments (2 level)
        commitments_rectangles = RoundedRectangle(
            corner_radius=0.05,
            width=0.9,
            height=0.6,
            fill_opacity=0.25,
            stroke_width=0.0,
        ).set_color(PRIMARY_COLOR)
        self.hashes_commitments_level2 = (
            VGroup(*[commitments_rectangles.copy() for _ in range(4)])
            .arrange(RIGHT, buff=1.43)
            .next_to(self.values_all, UP, buff=1.3)
        )
        text_commitment_C0 = MathTex(
            r"{{C_0^0}}", color=PRIMARY_COLOR, font_size=28
        ).move_to(self.hashes_commitments_level2[0].get_center())
        self.cdots_level2 = self.cdots.copy().next_to(
            self.hashes_commitments_level2[0], RIGHT, buff=0.6
        )
        self.cdots_level2_1 = self.cdots.copy().next_to(
            self.hashes_commitments_level2[1], RIGHT, buff=0.6
        )
        self.cdots_level2_2 = self.cdots.copy().next_to(
            self.hashes_commitments_level2[2], RIGHT, buff=0.6
        )
        self.rectangle_all_commitments_left = (
            RoundedRectangle(
                corner_radius=0.05,
                width=3.8,
                height=0.8,
                fill_opacity=0.22,
                stroke_width=0.0,
            )
            .set_color(HIGHLIGHT_COLOR)
            .move_to(self.cdots_level2.get_center())
        )
        self.rectangle_all_commitments_right = (
            RoundedRectangle(
                corner_radius=0.05,
                width=3.8,
                height=0.8,
                fill_opacity=0.22,
                stroke_width=0.0,
            )
            .set_color(HIGHLIGHT_COLOR)
            .move_to(self.cdots_level2_2.get_center())
        )
        self.hashes_commitments_level2.add(
            text_commitment_C0,
            self.cdots_level2,
            self.cdots_level2_2,
            self.cdots_level2_1,
            self.rectangle_all_commitments_left,
            self.rectangle_all_commitments_right,
        )

        ## commitments (3 level)
        self.hashes_commitments_level3 = (
            VGroup(*[commitments_rectangles.copy() for _ in range(2)])
            .arrange(RIGHT, buff=3.5)
            .next_to(self.hashes_commitments_level2, UP, buff=1.3)
        )
        text_hash_commitmentH0 = MathTex(
            r"{{C_0^1}}", color=PRIMARY_COLOR, font_size=28
        ).move_to(self.hashes_commitments_level3[0].get_center())

        self.cdots_level3 = self.cdots.copy().next_to(
            self.hashes_commitments_level3[0], RIGHT, buff=1.65
        )
        self.rectangle_parent_commitments = (
            RoundedRectangle(
                corner_radius=0.05,
                width=6.0,
                height=0.8,
                fill_opacity=0.22,
                stroke_width=0.0,
            )
            .set_color(HIGHLIGHT_COLOR)
            .move_to(self.cdots_level3.get_center())
        )

        self.hashes_commitments_level3.add(
            text_hash_commitmentH0, self.cdots_level3, self.rectangle_parent_commitments
        )

        ## root commitment
        self.hashes_commitments_root = (
            commitments_rectangles.copy()
            .set_color(SECONDARY_COLOR)
            .next_to(self.hashes_commitments_level3, UP, buff=1.3)
        )
        text_hash_commitmentH = MathTex(
            r"{{C_0^2}}", color=PRIMARY_COLOR, font_size=32
        ).move_to(self.hashes_commitments_root.get_center())
        self.hashes_commitments_root.add(text_hash_commitmentH)

        ## arrows
        self.arrows = VGroup()
        for i in range(2):
            self.create_arrow(
                self.hashes_commitments_level2[0], self.values[i], self.arrows
            )
            self.create_arrow(
                self.hashes_commitments_level2[1], self.values2[i], self.arrows
            )
            self.create_arrow(
                self.hashes_commitments_level2[2], self.values3[i], self.arrows
            )
            self.create_arrow(
                self.hashes_commitments_level2[3], self.values4[i], self.arrows
            )

            self.create_arrow(
                self.hashes_commitments_level3[0],
                self.hashes_commitments_level2[i],
                self.arrows,
            )
            self.create_arrow(
                self.hashes_commitments_level3[1],
                self.hashes_commitments_level2[i + 2],
                self.arrows,
            )
            self.create_arrow(
                self.hashes_commitments_root,
                self.hashes_commitments_level3[i],
                self.arrows,
            )

        ## node rectangles
        self.tree = (
            VGroup(
                self.hashes_commitments_root,
                self.hashes_commitments_level3,
                self.hashes_commitments_level2,
                self.values_all,
                self.arrows,
            )
            .scale(0.8)
            .shift(LEFT * 0.5)
        )

        self.commitment = MathTex(r"C^0", color=PRIMARY_COLOR, font_size=35)

        self.proof_text = (
            Text("proof", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=25)
            .next_to(self.commitment, DOWN, buff=0.8)
            .shift(UP * 0.3)
        )
        self.pi = (
            MathTex(r"\pi^0", color=PRIMARY_COLOR, font_size=35)
            .next_to(self.commitment, RIGHT, buff=1.0)
            .shift(UP * 0.3)
        )
        self.proof = VGroup(self.pi)
        self.opening = (
            MathTex(r"a_{255} = 85", color=PRIMARY_COLOR, font_size=35)
            .next_to(self.commitment, LEFT, buff=1.0)
            .shift(UP * 0.3)
        )

        ## table
        self.rectangle_bg = RoundedRectangle(
            corner_radius=0.05,
            width=12,
            height=4,
            stroke_width=0.0,
            fill_opacity=0.2,
        ).set_color(PRIMARY_COLOR)
        self.pi_proof = MathTex(r"\pi^1", color=PRIMARY_COLOR, font_size=35)

        self.pi_proof_level3 = MathTex(r"\pi^2", color=PRIMARY_COLOR, font_size=35)

        self.commitment_label = Text(
            "commitments: ", font=PRIMARY_FONT, color=SECONDARY_COLOR, font_size=25
        ).next_to(self.hashes_commitments_level2, LEFT, buff=2)
        self.proof_label = Text(
            "proofs: ", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=25
        ).next_to(self.commitment_label, DOWN, buff=0.3)
        self.total_size = Text(
            "total size: ", font=PRIMARY_FONT, color=HIGHLIGHT_COLOR, font_size=25
        ).next_to(self.proof_label, DOWN, buff=0.3)

        self.kzg = Text(
            "KZG", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=30
        ).shift(RIGHT * 0.5 + UP)
        self.ipa = Text(
            "IPA", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=30
        ).next_to(self.kzg, LEFT, buff=2.0)

        self.kzg_scalar = MathTex(
            r"<32  \ \mathrm{B}", color=HIGHLIGHT_COLOR, font_size=35
        )
        self.ipa_scalar = MathTex(
            r"<32  \ \mathrm{B}", color=HIGHLIGHT_COLOR, font_size=35
        )
        self.kzg_ec_point = MathTex(
            r"<48  \ \mathrm{B}", color=SECONDARY_COLOR, font_size=35
        )
        self.ipa_ec_point = MathTex(
            r"<32  \ \mathrm{B}", color=SECONDARY_COLOR, font_size=35
        )
        self.ipa_proof = Text(
            "     16 x\n EC points",
            font=PRIMARY_FONT,
            color=PRIMARY_COLOR,
            font_size=25,
        )
        self.ipa_proof2 = MathTex(
            r"<512 \ \mathrm{B}", color=PRIMARY_COLOR, font_size=35
        )

        self.kzg_total = Text(
            "KZG proofs: 140 B", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=25
        )
        self.ipa_total = Text(
            "IPA proofs: 1.5 kB", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=25
        )

        self.trusted_setup = Text(
            "+trusted setup\n    pairings",
            font=PRIMARY_FONT,
            color=PRIMARY_COLOR,
            font_size=20,
        )

        self.multiproof = MathTex(r"\pi", color=PRIMARY_COLOR, font_size=60)

        ## calculation proof
        self.proof_kzg1 = MathTex(
            r"\sim 48\ \mathrm{B} \cdot 3 + 48 \ \mathrm{B} \cdot 2",
            color=HIGHLIGHT_COLOR,
            font_size=30,
        )
        self.proof_kzg2 = MathTex(
            r"\sim 240 \  \mathrm{B}", color=HIGHLIGHT_COLOR, font_size=30
        )

        self.proof_ipa1 = MathTex(
            r"\sim 3 \cdot  512 \ \mathrm{B} + 64 \mathrm{B}",
            color=HIGHLIGHT_COLOR,
            font_size=30,
        )
        self.proof_ipa2 = MathTex(
            r"\sim 1536 \ \mathrm{B} + 64 \mathrm{B}",
            color=HIGHLIGHT_COLOR,
            font_size=30,
        )
        self.proof_ipa3 = MathTex(
            r"\sim 1.6\ \mathrm{kB}", color=HIGHLIGHT_COLOR, font_size=30
        )

        self.verify_function = (
            MathTex(
                r"\texttt{verify}",
                r"\texttt{(opening = }{a_i,}",
                r"\texttt{ root = }{C_0^2,}",
                r"\texttt{ verkleProof = }",
                r"[{\pi^0,}\;",
                r"{\pi^1,}\; ",
                r"{\pi^2,}\; ",
                r"{C_0^0,}\; " ,
                r"{C_0^1}]",
                color=PRIMARY_COLOR,
                font_size=37,
            )
            .to_edge(DOWN)
            .shift(UP * 1.)
        )

    def animate_in(self, scene):
        self.new_subsection(scene, "85: proof C, opening", "data/sound/e7/slide5-1.mp3")
        scene.play(Write(self.title_label), run_time=0.7)
        self.values.scale(2).move_to(ORIGIN).shift(DOWN * 1.5)
        self.arrows_commitment = VGroup()
        for i in range(2):
            self.create_arrow(self.commitment, self.values[i], self.arrows_commitment)

        scene.play(Write(self.values), run_time=0.7)
        scene.wait(1)
        self.commitment.shift(UP * 0.3)
        scene.play(Write(self.commitment), run_time=0.7)
        scene.play(Write(self.arrows_commitment), run_time=0.7)
        scene.wait(2)
        scene.play(Write(self.opening), run_time=0.7)
        scene.wait(2.5)
        scene.play(Write(self.proof), run_time=0.5)
        self.terms = VGroup(self.commitment, self.proof, self.opening)
        scene.wait(2)
        scene.play(FadeOut(self.terms, self.arrows_commitment))

        self.new_subsection(scene, "multi-level", "data/sound/e7/slide5-2.mp3")
        self.values.generate_target()
        self.values.target.scale(1 / 2).next_to(self.values2, LEFT, buff=0.6)
        scene.play(MoveToTarget(self.values), run_time=1.3)
        scene.play(
            FadeIn(
                self.values2,
                self.values3,
                self.values4,
                self.hashes_commitments_root,
                self.hashes_commitments_level3,
                self.hashes_commitments_level2,
                self.arrows,
                self.cdots_val1,
                self.cdots_val2,
                self.cdots_val3,
            ),
            run_time=2,
        )

        self.new_subsection(
            scene, "C0, opening, proof pi", "data/sound/e7/slide5-3.mp3"
        )
        scene.wait(2.5)
        commitment_C0 = (
            MathTex(r"{{C_0^0}}", color=PRIMARY_COLOR, font_size=28)
            .next_to(self.tree, RIGHT, buff=0.3)
            .shift(UP)
            .scale(1.2)
        )
        scene.play(
            TransformMatchingShapes(
                self.hashes_commitments_level2[4].copy(), commitment_C0
            ),
            run_time=1.0,
        )
        self.opening.next_to(commitment_C0, DOWN, buff=0.5)
        self.proof.next_to(self.opening, DOWN, buff=0.5)
        scene.play(
            FadeIn(self.opening, self.proof),
            run_time=1.5,
        )

        self.new_subsection(
            scene, "parent commitment, opening", "data/sound/e7/slide5-4.mp3"
        )
        commtiment_C0_1 = (
            MathTex(r"{{C_0^1}}", color=PRIMARY_COLOR, font_size=28)
            .next_to(commitment_C0, RIGHT, buff=1.0)
            .scale(1.2)
        )

        scene.wait(1)
        scene.play(
            Indicate(self.hashes_commitments_level2[4], scale_factor=1.5), run_time=1
        )
        scene.wait(0.5)
        scene.play(
            Indicate(self.hashes_commitments_level3[2], scale_factor=1.5), run_time=1
        )
        scene.wait(1)
        scene.play(
            TransformMatchingShapes(
                self.hashes_commitments_level3[2].copy(), commtiment_C0_1
            ),
            run_time=1.5,
        )
        opening2 = (
            MathTex(r"H(C_0^0)", color=PRIMARY_COLOR, font_size=24)
            .next_to(commtiment_C0_1, DOWN, buff=0.5)
            .scale(1.2)
        )
        scene.wait(1)
        scene.play(
            TransformMatchingShapes(self.hashes_commitments_level2[4].copy(), opening2),
            run_time=1.5,
        )
        scene.play(
            Indicate(self.hashes_commitments_level2[4], scale_factor=1.5), run_time=1
        )
        scene.wait(1)
        self.pi_proof.next_to(opening2, DOWN, buff=0.5)
        scene.play(FadeIn(self.pi_proof), run_time=1.0)

        self.new_subsection(scene, "root, proof, opening", "data/sound/e7/slide5-5.mp3")
        root = (
            MathTex(r"{{C_0^2}}", color=PRIMARY_COLOR, font_size=28)
            .next_to(commtiment_C0_1, RIGHT, buff=1.0)
            .scale(1.2)
        )
        scene.wait(2)
        scene.play(
            Indicate(self.hashes_commitments_level3[2], scale_factor=1.5), run_time=1
        )
        scene.wait(0.5)
        scene.play(Indicate(self.hashes_commitments_root, scale_factor=1.5), run_time=1)
        scene.wait(1.5)
        scene.play(
            TransformMatchingShapes(self.hashes_commitments_root[1].copy(), root),
            run_time=1.5,
        )
        opening3 = (
            MathTex(r"H(C_0^1)", color=PRIMARY_COLOR, font_size=28)
            .next_to(root, DOWN, buff=0.5)
            .scale(1.2)
        )
        scene.wait(1)
        scene.play(
            TransformMatchingShapes(self.hashes_commitments_level3[2].copy(), opening3),
            run_time=1.5,
        )
        scene.wait(2.5)
        self.pi_proof_level3.next_to(opening3, DOWN, buff=0.5)
        scene.play(FadeIn(self.pi_proof_level3), run_time=1.0)

        self.new_subsection(
            scene, "2 commitments, 3 proofs", "data/sound/e7/slide5-6.mp3"
        )
        scene.wait(2)
        scene.play(self.tree.animate.scale(0.7).to_edge(LEFT), run_time=1)
        scene.play(FadeIn(self.verify_function[0], self.verify_function[3], run_time=1.5))
        scene.wait(0.2)
        scene.play(
            self.proof.animate.set_color(SECONDARY_COLOR),
            self.pi_proof.animate.set_color(SECONDARY_COLOR),
            self.pi_proof_level3.animate.set_color(SECONDARY_COLOR),
            run_time=1,
        )
        scene.play(
            TransformMatchingShapes(self.proof.copy(), self.verify_function[4]),
            TransformMatchingShapes(self.pi_proof.copy(), self.verify_function[5]),
            TransformMatchingShapes(self.pi_proof_level3, self.verify_function[6]),
            run_time=1,
        )
        scene.wait(1)
        scene.play(
            commitment_C0.animate.set_color(SECONDARY_COLOR),
            commtiment_C0_1.animate.set_color(SECONDARY_COLOR),
        )
        scene.play(
            TransformMatchingShapes(commitment_C0.copy(), self.verify_function[7]),
            TransformMatchingShapes(commtiment_C0_1.copy(), self.verify_function[8]),
            run_time=1,
        )
        scene.play(
            self.opening.animate.set_color(HIGHLIGHT_COLOR),
            root.animate.set_color(HIGHLIGHT_COLOR),
            run_time=1,
        )
        scene.play(
            TransformMatchingShapes(root.copy(), self.verify_function[2]), run_time=1
        )
        scene.play(
            TransformMatchingShapes(self.opening.copy(), self.verify_function[1]),
            run_time=1,
        )
        scene.wait(2)

        scene.play(FadeOut(self.opening, opening2, opening3, root), run_time=1.5)

        self.new_subsection(scene, "different weight", "data/sound/e7/slide5-6a.mp3")
        scene.wait(1.5)
        self.proofs = VGroup(self.pi_proof, self.pi_proof_level3, self.proof)
        self.commitments = VGroup(commitment_C0, commtiment_C0_1)
        self.commitments.generate_target()
        self.proofs.generate_target()
        self.commitments.target.shift(LEFT * 1.5 + DOWN * 0.5)
        self.proofs.target.shift(LEFT * 1.5)
        # scene.play(
        #     MoveToTarget(self.commitments),
        #     MoveToTarget(self.proofs),
        #     run_time=1.5,
        # )
        scene.play(FadeOut(self.commitments, self.proofs))
        rectangle_around_commitment_proofs = (
            RoundedRectangle(
                corner_radius=0.05,
                width=self.proofs.width + 0.7,
                height=2,
                fill_opacity=0.15,
                stroke_width=0.0,
            )
            .set_color(HIGHLIGHT2_COLOR)
            .move_to(self.proofs.get_center())
            .shift(UP * 0.6)
        )
        # scene.play(FadeIn(self.rectangle_bg, rectangle_around_commitment_proofs))
        self.verify_function_REST = self.verify_function[3:]
        scene.play(FadeOut(self.verify_function[0:3]), run_time=1)
        self.verify_function_REST.generate_target()
        self.verify_function_REST.target.shift(UP * 4 + LEFT * 1.8).scale(1.3)
        scene.play(
            MoveToTarget(self.verify_function_REST),
            run_time=1.5,
        )

        self.new_subsection(scene, "KZG", "data/sound/e7/slide5-6d.mp3")

        self.kzg.next_to(self.verify_function_REST[0], DOWN, buff=1.0).shift(RIGHT*0.3)
        self.ipa.next_to(self.kzg, DOWN, buff=1.0)
        self.kzg_ec_point.next_to(self.verify_function_REST[4], DOWN, buff=1.).shift(RIGHT*0.15)
        self.ipa_ec_point.next_to(self.kzg_ec_point, DOWN, buff=0.9)
        self.kzg_ecpoint2 = (
            self.kzg_ec_point.copy()
            .next_to(self.verify_function_REST[2], DOWN, buff=1.)
            .set_color(PRIMARY_COLOR)
        )
        self.commitment_label.next_to(self.ipa_ec_point, LEFT, buff=0.5)
        self.proof_label.next_to(self.commitment_label, DOWN, buff=0.8)
        self.ipa_proof.next_to(self.kzg_ecpoint2, DOWN, buff=0.8)
        self.ipa_proof2.next_to(self.kzg_ecpoint2, DOWN, buff=1.)
        self.total_size.next_to(self.proof_label, DOWN, buff=0.5)

        self.proof_ipa1.next_to(self.ipa_ec_point, RIGHT, buff=0.6)
        self.proof_ipa2.next_to(self.ipa_ec_point, RIGHT, buff=0.6)
        self.proof_ipa3.next_to(self.ipa_ec_point, RIGHT, buff=0.6)
        self.proof_kzg1.next_to(self.kzg_ec_point, RIGHT, buff=0.6)
        self.proof_kzg2.next_to(self.kzg_ec_point, RIGHT, buff=0.6)
        scene.play(FadeIn(self.kzg), run_time=1.0)

        self.brace_proofs = Brace(
            VGroup(self.verify_function_REST[1:4]), DOWN, buff=0.1
        ).set_color(PRIMARY_COLOR)
        self.brace_commitments = Brace(
            VGroup(self.verify_function_REST[4:]), DOWN, buff=0.1
        ).set_color(PRIMARY_COLOR)
        scene.play(FadeIn(self.brace_commitments), run_time=1.0)
        scene.play(FadeIn(self.brace_proofs), run_time=1.0)

        scene.play(FadeIn(self.kzg_ec_point, self.kzg_ecpoint2), run_time=1)
        scene.wait(1)

        self.new_subsection(scene, "total 240 B", "data/sound/e7/slide5-6e.mp3")
        scene.wait(1)

        scene.play(Write(self.proof_kzg1), run_time=1)
        scene.wait(1)
        scene.play(
            TransformMatchingShapes(self.proof_kzg1, self.proof_kzg2), run_time=1
        )
        scene.wait(2)

        self.new_subsection(scene, "IPA", "data/sound/e7/slide5-6b.mp3")
        scene.play(FadeIn(self.ipa), run_time=1)
        scene.wait(1)
        scene.play(FadeIn(self.ipa_ec_point), run_time=1)
        scene.wait(2)
        scene.wait(1)
        scene.wait(0.5)
        scene.play(FadeIn(self.ipa_proof), run_time=1)
        scene.wait(5)
        scene.play(TransformMatchingShapes(self.ipa_proof, self.ipa_proof2), run_time=1)

        self.new_subsection(scene, "total 1.5 kB", "data/sound/e7/slide5-6c.mp3")
        scene.wait(1)
        scene.play(Write(self.proof_ipa1), run_time=1)
        scene.wait(1)
        scene.play(
            TransformMatchingShapes(self.proof_ipa1, self.proof_ipa2), run_time=1
        )
        scene.wait(1)
        scene.play(
            TransformMatchingShapes(self.proof_ipa2, self.proof_ipa3), run_time=1
        )
        scene.wait(1)

        self.new_subsection(
            scene, "much smaller but pairings", "data/sound/e7/slide5-6f.mp3"
        )
        scene.wait(1)
        scene.play(Indicate(self.proof_ipa3, color=PRIMARY_COLOR), run_time=1)
        scene.play(Indicate(self.proof_kzg2, color=PRIMARY_COLOR), run_time=1)
        scene.wait(1)
        self.trusted_setup.next_to(self.proof_kzg2, DOWN, buff=0.3).shift(RIGHT * 0.2)
        scene.play(FadeIn(self.trusted_setup), run_time=1)

        self.new_subsection(
            scene, "simplified to sinlge proof", "data/sound/e7/slide5-7.mp3"
        )
        scene.wait(2)
        self.multiproof.next_to(self.verify_function_REST[2], UP, buff=0.2)
        self.multicommitment = MathTex(
            "C", color=SECONDARY_COLOR, font_size=40
        ).next_to(self.verify_function_REST[4], UP, buff = 0.2).shift(RIGHT*0.1)
        scene.play(
            TransformMatchingShapes(
                VGroup(self.proof, self.pi_proof, self.pi_proof_level3), self.multiproof
            ),
            run_time=1,
        )
        scene.play(
            TransformMatchingShapes(
                VGroup(commtiment_C0_1, commitment_C0), self.multicommitment
            ),
            run_time=1,
        )
        scene.wait(6.5)

        self.all = Group(
            self.title_label,
            self.multicommitment,
            self.kzg,
            self.kzg_ec_point,
            self.kzg_ecpoint2,
            self.ipa,
            self.ipa_ec_point,
            self.ipa_proof2,
            self.trusted_setup,
            self.multiproof,
            self.proof_kzg2,
            self.proof_ipa3,
            self.total_size,
            self.verify_function,
            self.brace_commitments,
            self.brace_proofs,
            self.tree,
        )

    def animate_out(self, scene):
        scene.play(FadeOut(self.all), run_time=1.)

    def create_arrow(self, start, end, arrow_array):
        arrow = Arrow(
            start.get_bottom(),
            end.get_top(),
            buff=0.0,
            color=PRIMARY_COLOR,
            stroke_width=0.8,
            max_tip_length_to_length_ratio=0.05,
            tip_length=0.1,
            tip_shape=StealthTip,
        )
        arrow_array.add(arrow)
