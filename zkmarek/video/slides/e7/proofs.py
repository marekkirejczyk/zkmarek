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
    DashedVMobject,
    Create,
)
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import (
    PRIMARY_COLOR,
    PRIMARY_FONT,
    SECONDARY_COLOR,
    HIGHLIGHT_COLOR,
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
            width=0.6,
            height=0.6,
            fill_opacity=0.25,
            stroke_width=0.0,
        ).set_color(SECONDARY_COLOR)

        self.values = VGroup(*[values_rectangles.copy() for _ in range(2)]).arrange(
            RIGHT, buff=0.35
        )
        self.cdots = Text(
            "...", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=30
        ).next_to(self.values[0], RIGHT, buff=0.05)
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
            width=0.6,
            height=0.6,
            fill_opacity=0.25,
            stroke_width=0.0,
        ).set_color(HIGHLIGHT_COLOR)
        self.hashes_commitments_level2 = (
            VGroup(*[commitments_rectangles.copy() for _ in range(4)])
            .arrange(RIGHT, buff=1.6)
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
            .set_color(PRIMARY_COLOR)
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
            .set_color(PRIMARY_COLOR)
            .move_to(self.cdots_level2_2.get_center())
        )
        self.hash = MathTex(
            r"\texttt{hash}(C_0^0)", color=PRIMARY_COLOR, font_size=25
        ).next_to(self.hashes_commitments_level2[0], UP, buff=0.6).shift(LEFT*0.2)
        hash_255 = MathTex(
            r"\texttt{hash}(C_{255}^0)", color=PRIMARY_COLOR, font_size=25
        ).next_to(self.hashes_commitments_level2[3], UP, buff=0.6).shift(RIGHT*0.2)
        self.hashes_commitments_level2.add(
            text_commitment_C0,
            self.cdots_level2,
            self.cdots_level2_2,
            self.cdots_level2_1,
            self.rectangle_all_commitments_left,
            self.rectangle_all_commitments_right,
            self.hash,
            hash_255
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
            .set_color(PRIMARY_COLOR)
            .move_to(self.cdots_level3.get_center())
        )
        self.hash_parent = MathTex(
            r"\texttt{hash}(C_0^1)", color=PRIMARY_COLOR, font_size=25
        ).next_to(self.hashes_commitments_level3[0], UP, buff=0.6)
        hash_255_parent = MathTex(
            r"\texttt{hash}(C_{255}^1)", color=PRIMARY_COLOR, font_size=25
        ).next_to(self.hashes_commitments_level3[1], UP, buff=0.6).shift(RIGHT*0.05)

        self.hashes_commitments_level3.add(
            text_hash_commitmentH0, self.cdots_level3, self.rectangle_parent_commitments,
            hash_255_parent, 
            self.hash_parent,
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
            .shift(LEFT * 2.5+DOWN * 1.)
        )
        ## verify function
        self.verify_function0 = MathTex(
            r"\texttt{verify}(",
            r"a_{255}=85, \;",
            r"C_0^0, \;",
            r"\pi^0",
            r")",
            font_size=35,
            color=PRIMARY_COLOR,
        ).shift(UP)
        self.brace_public = Brace(
            self.verify_function0[1:3], UP, buff=0.1, color=HIGHLIGHT_COLOR
        )
        self.public_imput = Text(
            "public input", font=PRIMARY_FONT, color=HIGHLIGHT_COLOR, font_size=25
        ).next_to(self.brace_public, UP, buff=0.1)

        self.verify_function1_commitment = (
            MathTex(
                r"\texttt{verify}(",
                r"a_{255}=85, \;",
                r"C_0^1, \;",
                r"C_0^0,\;",
                r"\pi^0",
                r")",
                font_size=35,
                color=PRIMARY_COLOR,
            )
            .to_edge(RIGHT)
            .shift(UP * 1 + LEFT * 0.5)
        )
        self.verify_function1_commitment[1:3].set_color(HIGHLIGHT_COLOR)
        self.hash_opening = MathTex(
            r"C_0^0\rightarrow \texttt{hash}(C_0^0)", color=PRIMARY_COLOR, font_size=30
        ).next_to(self.verify_function1_commitment[3], UP, buff=0.3)
        self.verify_function1_proof = (
            MathTex(
                r"\texttt{verify}(",
                r"a_{255}=85, \;",
                r"C_0^1, \;",
                r"C_0^0,\;",
                r"\pi^0,\;",
                r"\pi^1",
                r")",
                color=PRIMARY_COLOR,
                font_size=35,
            )
            .to_edge(RIGHT)
            .shift(UP * 1 + RIGHT * 0.01)
        )

        self.verify_function2_commitment = (
            MathTex(
                r"\texttt{verify}(",
                r"a_{255}=85,\; ",
                r"C_0^2,\; ",
                r"C_0^1,\;",
                r"C_0^0\;",
                r"\pi^0\;",
                r"\pi^1",
                r")",
                font_size=35,
                color=PRIMARY_COLOR,
            )
            .to_edge(RIGHT)
            .shift(UP * 1 + LEFT * 0.1)
        )
        self.verify_function2_commitment[1:3].set_color(HIGHLIGHT_COLOR)
        self.hash_opening2 = MathTex(
            r"C_0^1\rightarrow \texttt{hash}(C_0^1)", color=PRIMARY_COLOR, font_size=30
        ).next_to(self.verify_function2_commitment[4], UP, buff=0.3)
        self.verify_function2_proof = (
            MathTex(
                r"\texttt{verify}(",
                r"a_{255}=85, \;",
                r"C_0^2,\; ",
                r"C_0^1, \;",
                r"C_0^0,\;",
                r"\pi^0,\;",
                r"\pi^1,\;",
                r"\pi^2",
                r")",
                color=PRIMARY_COLOR,
                font_size=35,
            )
            .to_edge(RIGHT)
            .shift(UP * 1 + LEFT * 0.1)
        )

        rectangle_C0 = (
            RoundedRectangle(
                corner_radius=0.05,
                width=self.values.width+0.2,
                height=2.3,
                fill_opacity=0.0,
                stroke_width=1.0,
            )
            .move_to(self.values.get_top())
            .shift(UP * 0.5)
        )
        self.rectancle_C0 = DashedVMobject(rectangle_C0, num_dashes=60)

        rectangle_C1 = RoundedRectangle(
            corner_radius=0.05,
            width=self.values_all.width/2+0.2,
            height=4.4,
            fill_opacity=0.0,
            stroke_width=1.0,
        ).move_to(self.hashes_commitments_level2.get_center()).shift(UP*0.07+LEFT*1.8)
        self.rectancle_C1 = DashedVMobject(rectangle_C1, num_dashes=120)

        rectangle_C2 = RoundedRectangle(
            corner_radius=0.05,
            width=self.tree.width+0.5,
            height=self.tree.height + 0.2,
            fill_opacity=0.0,
            stroke_width=1.0,
        ).move_to(self.tree.get_center()).shift(DOWN*0.05)
        self.rectancle_C2 = DashedVMobject(rectangle_C2, num_dashes=200)

        ## table

        self.kzg = Text(
            "KZG", font=PRIMARY_FONT, color=SECONDARY_COLOR, font_size=30
        ).shift(RIGHT * 0.5 + UP)
        self.ipa = Text(
            "IPA", font=PRIMARY_FONT, color=HIGHLIGHT_COLOR, font_size=30
        ).next_to(self.kzg, LEFT, buff=2.0)

        self.kzg_scalar = MathTex(
            r"<32  \ \texttt{B}", color=SECONDARY_COLOR, font_size=35
        )
        self.ipa_scalar = MathTex(
            r"<32  \ \texttt{B}", color=HIGHLIGHT_COLOR, font_size=35
        )
        self.kzg_ec_point = MathTex(
            r"\sim 2 \cdot 48  \ \texttt{B}", color=SECONDARY_COLOR, font_size=35
        )
        self.ipa_ec_point = MathTex(
            r"\sim 2\cdot 32  \ \texttt{B}", color=HIGHLIGHT_COLOR, font_size=35
        )
        self.ipa_proof = Text(
            "   3 x 16 x\n EC points",
            font=PRIMARY_FONT,
            color=HIGHLIGHT_COLOR,
            font_size=25,
        )
        self.ipa_proof2 = MathTex(
            r"\sim 3 \cdot 512 \ \texttt{B}", color=HIGHLIGHT_COLOR, font_size=35
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
            r"\sim 48\ \texttt{B} \cdot 3 + 48 \ \texttt{B} \cdot 2",
            color=HIGHLIGHT_COLOR,
            font_size=30,
        )
        self.proof_kzg2 = MathTex(
            r"\sim 240 \  \texttt{B}", color=SECONDARY_COLOR, font_size=30
        )

        self.proof_ipa1 = MathTex(
            r"\sim 3 \cdot  512 \ \texttt{B} + 64 \texttt{B}",
            color=HIGHLIGHT_COLOR,
            font_size=30,
        )
        self.proof_ipa2 = MathTex(
            r"\sim 1536 \ \texttt{B} + 64 \texttt{B}",
            color=HIGHLIGHT_COLOR,
            font_size=30,
        )
        self.proof_ipa3 = MathTex(
            r"\sim 1.6\ \texttt{kB}", color=HIGHLIGHT_COLOR, font_size=30
        )

        self.verify_function = (
            MathTex(
                r"\texttt{verify}( ",
                r"{a_{255},\;}",
                r"{C_0^2,\;}",
                r"\texttt{ verkleProof = }",
                r"[{\pi^0,}\;",
                r"{\pi^1,}\; ",
                r"{\pi^2,}\; ",
                r"{C_0^0,}\; ",
                r"{C_0^1}])",
                color=PRIMARY_COLOR,
                font_size=32,
            )
            .to_edge(RIGHT)
            .shift(UP * 1 + LEFT * 0.1)
        )
        self.brace_pub_in = Brace(self.verify_function[1:3], UP, buff=0.1, color=HIGHLIGHT_COLOR)
        self.public_input2 = Text("public input", font=PRIMARY_FONT, color=HIGHLIGHT_COLOR, font_size=25).next_to(self.brace_pub_in, UP, buff=0.1)

    def animate_in(self, scene):
        self.new_subsection(scene, "85: proof C, opening", "data/sound/e7/slide5-1.mp3")
        scene.play(Write(self.title_label), run_time=0.7)
        self.values.scale(2).move_to(ORIGIN).shift(DOWN * 1.5)

        scene.play(Write(self.values), run_time=0.7)
        scene.wait(1)
        scene.play(Write(self.verify_function0[0]), run_time=0.7)
        scene.play(Write(self.verify_function0[1]), run_time=1)
        scene.wait(1.7)
        scene.play(Write(self.verify_function0[2]), run_time=0.7)
        scene.play(
            FadeIn(self.public_imput, self.brace_public),
            self.verify_function0[1:3].animate.set_color(HIGHLIGHT_COLOR),
            run_time=1.0,
        )
        scene.wait(1.5)
        scene.play(Write(self.verify_function0[3:]), run_time=0.5)
        scene.wait(2)
        scene.play(
            FadeOut(self.brace_public, self.public_imput),
            self.verify_function0.animate.to_edge(RIGHT).shift(LEFT * 0.5),
        )

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
        scene.play(Create(self.rectancle_C0), run_time=1.)
        scene.wait(2.5)
        scene.play(
            Indicate(self.verify_function0[2]),
            run_time=1.0,
        )
        scene.play(
            Indicate(self.verify_function0[1]),
            run_time=1.0,
        )
        scene.play(
            Indicate(self.verify_function0[3]),
            run_time=1.0,
        )

        self.new_subsection(
            scene, "parent commitment, opening", "data/sound/e7/slide5-4.mp3"
        )
        scene.play(TransformMatchingShapes(self.rectancle_C0, self.rectancle_C1), run_time=1)
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
                self.verify_function0, self.verify_function1_commitment
            ),
            run_time=1.5,
        )
        scene.wait(1)
        scene.play(self.verify_function1_commitment[3].animate.set_color(SECONDARY_COLOR), run_time=1)
        scene.play(Write(self.hash_opening), run_time=1.5)
        scene.play(
            Indicate(self.hashes_commitments_level2[4], scale_factor=1.5), run_time=1
        )
        scene.play(self.hash.animate.set_color(SECONDARY_COLOR), run_time=1
        )
        scene.wait(0.5)
        scene.play(
            TransformMatchingShapes(
                self.verify_function1_commitment, self.verify_function1_proof
            ),
            FadeOut(self.hash_opening),
            run_time=1.0,
        )

        self.new_subsection(scene, "root, proof, opening", "data/sound/e7/slide5-5.mp3")
        scene.play(TransformMatchingShapes(self.rectancle_C1, self.rectancle_C2), run_time=1)
        scene.wait(1)
        scene.play(
            Indicate(self.hashes_commitments_level3[2], scale_factor=1.5), run_time=1
        )
        scene.wait(0.5)
        scene.play(Indicate(self.hashes_commitments_root, scale_factor=1.5), run_time=1)
        scene.wait(0.5)
        scene.play(self.tree.animate.scale(0.7).to_edge(LEFT),
                   self.rectancle_C2.animate.scale(0.7).to_edge(LEFT).shift(LEFT*0.1), run_time=1)
        scene.play(
            TransformMatchingShapes(
                self.verify_function1_proof, self.verify_function2_commitment
            ),
            run_time=1.5,
        )
        scene.play(self.verify_function2_commitment[3].animate.set_color(SECONDARY_COLOR), run_time=1)
        scene.play(Write(self.hash_opening2), run_time=1.5)
        scene.play(self.hash_parent.animate.set_color(SECONDARY_COLOR), run_time=1
        )
        scene.wait(1.5)
        scene.play(
            TransformMatchingShapes(
                self.verify_function2_commitment, self.verify_function2_proof
            ),
            FadeOut(self.hash_opening2),
            run_time=1.0,
        )

        self.new_subsection(
            scene, "2 commitments, 3 proofs", "data/sound/e7/slide5-6.mp3"
        )
        scene.wait(1)
        scene.play(FadeOut(self.rectancle_C2), run_time=1)
        scene.wait(1)
        scene.play(
            TransformMatchingShapes(self.verify_function2_proof, self.verify_function),
            run_time=1.5,
        )
        scene.wait(1)
        scene.play(Indicate(self.verify_function[4], scale_factor=1.5), run_time=0.5)
        scene.play(Indicate(self.verify_function[5], scale_factor=1.5), run_time=0.5)
        scene.play(Indicate(self.verify_function[6], scale_factor=1.5), run_time=0.5)
        scene.wait(0.5)
        scene.play(Indicate(self.verify_function[7], scale_factor=1.5), run_time=0.5)
        scene.play(Indicate(self.verify_function[8], scale_factor=1.5), run_time=0.5)
        scene.wait(1.5)
        scene.play(Indicate(self.verify_function[1], scale_factor=1.5), run_time=0.7)
        scene.play(Indicate(self.verify_function[2], scale_factor=1.5), run_time=0.7)
        scene.play(Write(self.public_input2), FadeIn(self.brace_pub_in), run_time=1.0)

        self.new_subsection(scene, "different weight", "data/sound/e7/slide5-6a.mp3")
        scene.wait(1.5)

        self.verify_function_REST = self.verify_function[3:]
        scene.play(FadeOut(self.verify_function[0:3], self.brace_pub_in, self.public_input2), run_time=1)
        self.verify_function_REST.generate_target()
        self.verify_function_REST.target.shift(LEFT * 2.2).scale(1.3)
        scene.play(
            MoveToTarget(self.verify_function_REST),
            run_time=1.5,
        )

        self.new_subsection(scene, "KZG", "data/sound/e7/slide5-6d.mp3")

        self.kzg.next_to(self.verify_function_REST[0], DOWN, buff=1.0).shift(
            RIGHT * 0.3
        )
        self.ipa.next_to(self.kzg, DOWN, buff=1.0)
        self.kzg_ec_point.next_to(self.verify_function_REST[4], DOWN, buff=1.0).shift(
            RIGHT * 0.3+UP*0.05
        )
        self.ipa_ec_point.next_to(self.kzg_ec_point, DOWN, buff=0.9)
        self.kzg_ecpoint2 = (
            MathTex(r"\sim 3\cdot 48 \ \texttt{B}", color = SECONDARY_COLOR, font_size = 35)
            .next_to(self.verify_function_REST[2], DOWN, buff=1.0)
        )
        self.ipa_proof.next_to(self.kzg_ecpoint2, DOWN, buff=0.8)
        self.ipa_proof2.next_to(self.ipa_ec_point, LEFT, buff=0.15)

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
        scene.wait(3)
        scene.play(
            Write(self.proof_kzg2), run_time=1
        )
        scene.wait(2)

        self.new_subsection(scene, "IPA", "data/sound/e7/slide5-6b.mp3")
        scene.play(FadeIn(self.ipa), run_time=1)
        scene.wait(1)
        scene.play(FadeIn(self.ipa_ec_point), run_time=1)
        scene.wait(3.5)
        scene.play(FadeIn(self.ipa_proof), run_time=1)
        scene.wait(6)
        scene.play(TransformMatchingShapes(self.ipa_proof, self.ipa_proof2), run_time=1)

        self.new_subsection(scene, "total 1.5 kB", "data/sound/e7/slide5-6c.mp3")
        scene.wait(4)
        scene.play(
            Write(self.proof_ipa3), run_time=1
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

        self.new_subsection(
            scene, "simplified to sinlge proof", "data/sound/e7/slide5-7.mp3"
        )
        scene.wait(2)
        self.multiproof.next_to(self.verify_function_REST[2], UP, buff=0.2)
        self.multicommitment = (
            MathTex("C", color=SECONDARY_COLOR, font_size=40)
            .next_to(self.verify_function_REST[4], UP, buff=0.2)
            .shift(RIGHT * 0.1)
        )
        scene.play(
            TransformMatchingShapes(
                VGroup(self.verify_function_REST[1:4].copy()), self.multiproof
            ),
            run_time=1,
        )
        scene.play(
            TransformMatchingShapes(
                VGroup(self.verify_function_REST[4:].copy()), self.multicommitment
            ),
            run_time=1,
        )
        scene.wait(5.)

        self.all = Group(
            self.title_label,
            self.multicommitment,
            self.kzg,
            self.kzg_ec_point,
            self.kzg_ecpoint2,
            self.ipa,
            self.ipa_ec_point,
            self.ipa_proof2,
            self.multiproof,
            self.proof_kzg2,
            self.proof_ipa3,
            self.verify_function_REST,
            self.brace_commitments,
            self.brace_proofs,
            self.tree,
        )

    def animate_out(self, scene):
        scene.play(FadeOut(self.all), run_time=1.0)

    def create_arrow(self, start, end, arrow_array, dash_density=10.):
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
        arrow_length = arrow.get_length()
        num_dashes = max(2, int(arrow_length * dash_density)) 
        arrow = DashedVMobject(arrow, num_dashes= num_dashes)
        arrow_array.add(arrow)
