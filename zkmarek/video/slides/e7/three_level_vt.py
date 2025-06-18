from manim import (
    Write,
    UP,
    Text,
    FadeOut,
    RoundedRectangle,
    VGroup,
    Create,
    MoveToTarget,
    Indicate,
    ChangeDecimalToValue,
    DecimalNumber,
    TransformMatchingShapes,
    Arrow,
    DOWN,
    LEFT,
    RIGHT,
    Brace,
    MathTex,
    FadeIn,
    StealthTip,
)

from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import (
    PRIMARY_COLOR,
    PRIMARY_FONT,
    SECONDARY_COLOR,
    HIGHLIGHT_COLOR,
)


class ThreeLevelVerkleTree(SlideBase):
    def __init__(self) -> None:
        super().__init__("Three-level Verkle tree")

    def construct(self):
        self.title_label = Text(
            "Multi-level Verkle tree",
            font=PRIMARY_FONT,
            color=PRIMARY_COLOR,
            font_size=40,
        ).to_edge(UP)
        rectangle = RoundedRectangle(
            corner_radius=0.05,
            width=0.5,
            height=0.3,
            fill_opacity=0.25,
            stroke_width=0.0,
        ).set_color(SECONDARY_COLOR)

        self.internal_node = [rectangle.copy().scale(2.0) for _ in range(2)]
        self.internal_node = (
            VGroup(*self.internal_node).arrange(RIGHT, buff=0.6).shift(DOWN * 1.5)
        )
        self.internal_node2 = [rectangle.copy().scale(1.0) for _ in range(2)]
        self.internal_node2 = (
            VGroup(*self.internal_node2)
            .arrange(RIGHT, buff=0.3)
            .shift(DOWN * 1.7 + RIGHT * 1.0)
        )

        txs = [r"a_0", r"a_{255}"]
        txs2 = [r"", r""]
        self.node1_texts = [
            MathTex(txs[i], font_size=40, color=PRIMARY_COLOR).move_to(
                self.internal_node[i]
            )
            for i in range(len(txs))
        ]
        self.node2_texts = [
            MathTex(txs2[i], font_size=18, color=PRIMARY_COLOR).move_to(
                self.internal_node2[i]
            )
            for i in range(len(txs))
        ]
        self.node1_texts = VGroup(*self.node1_texts)
        self.node2_texts = VGroup(*self.node2_texts)

        for i in range(len(self.node1_texts)):
            node = self.internal_node[i]
            node.move_to(self.internal_node[i])
            node2 = self.internal_node2[i]
            node2.move_to(self.internal_node2[i])

        self.commitment_to_C0 = (
            rectangle.copy()
            .scale(3.6)
            .set_color(HIGHLIGHT_COLOR)
            .next_to(self.internal_node, UP, buff=0.8)
            .shift(UP * 0.5)
        )
        self.commitment_to_C255 = (
            rectangle.copy()
            .scale(1.8)
            .set_color(HIGHLIGHT_COLOR)
            .next_to(self.internal_node2, UP, buff=0.65)
        )

        self.commitment_to_c0_text = MathTex(
            r"C_0^0", font_size=50, color=PRIMARY_COLOR
        ).move_to(self.commitment_to_C0.get_center())
        self.commitment_to_c255_text = MathTex(
            r"C_{255}^0", font_size=25, color=PRIMARY_COLOR
        ).move_to(self.commitment_to_C255.get_center())
        self.commitment_255 = VGroup(
            self.commitment_to_C255, self.commitment_to_c255_text
        )

        self.arrows_C0 = []
        for rectangle in self.internal_node:
            self.create_arrow(self.commitment_to_C0, rectangle, self.arrows_C0)

        self.arrows_C255 = []
        for rectangle in self.internal_node2:
            self.create_arrow(self.commitment_to_C255, rectangle, self.arrows_C255)
        self.internal_node2_whole = VGroup(
            self.internal_node2,
            self.node2_texts,
            self.commitment_255,
            *self.arrows_C255,
        ).shift(RIGHT * 0.1)

        self.commitment_cdots = rectangle.copy().scale(1.2).set_color(HIGHLIGHT_COLOR)
        self.commitment_to_cdots_text = Text(
            r"...", font=PRIMARY_FONT, font_size=20, color=PRIMARY_COLOR
        ).move_to(self.commitment_cdots.get_center())

        self.commitmentcdots = VGroup(self.commitment_to_cdots_text)
        self.rectangle_node_commitments = RoundedRectangle(
            corner_radius=0.05,
            width=3.5,
            height=0.8,
            fill_opacity=0.15,
            stroke_width=0.0,
        ).set_color(HIGHLIGHT_COLOR)
        self.rectangle_node_commitments.move_to(
            self.commitment_to_cdots_text.get_center()
        )

        self.commitment_to_ec_values = Text(
            "commitment to EC points?",
            font=PRIMARY_FONT,
            font_size=20,
            color=PRIMARY_COLOR,
        )

        self.hashaes_of_commitments_rec = [
            rectangle.copy().scale(1.8).set_color(PRIMARY_COLOR) for _ in range(2)
        ]
        self.hashaes_of_commitments_rec = VGroup(
            *self.hashaes_of_commitments_rec
        ).arrange(RIGHT, buff=1.0)
        iss = ["0", "255"]
        self.text_hashes_of_commitments = [
            MathTex(f"H(C^0_{{{iss[i]}}})", font_size=22, color=PRIMARY_COLOR).move_to(
                self.hashaes_of_commitments_rec[i]
            )
            for i in range(len(self.hashaes_of_commitments_rec))
        ]
        self.hashaes_of_commitments = VGroup(
            *self.hashaes_of_commitments_rec, *self.text_hashes_of_commitments
        )

        self.commitment_C01_rec = rectangle.copy().scale(1.8).set_color(HIGHLIGHT_COLOR)
        self.commiemtnt_c01_text = MathTex(
            r"C_0^1", font_size=26, color=PRIMARY_COLOR
        ).move_to(self.commitment_C01_rec.get_center())

        self.commitment_C01 = VGroup(self.commitment_C01_rec, self.commiemtnt_c01_text)

        self.other_commitments = [
            rectangle.copy().scale(1.8).set_color(HIGHLIGHT_COLOR) for _ in range(1)
        ]
        self.other_commitments = VGroup(*self.other_commitments).arrange(
            RIGHT, buff=3.5
        )
        self.text_other_commitments = [
            MathTex(f"C_{{{iss[i+1]}}}^1", font_size=26, color=PRIMARY_COLOR).move_to(
                self.other_commitments[i]
            )
            for i in range(len(self.other_commitments))
        ]

        self.other_commitments.add(*self.text_other_commitments)
        self.text_other_commitments = VGroup(*self.text_other_commitments)

        self.other_hashes_rec = [
            rectangle.copy().stretch(1, 2).scale(1.8).set_color(HIGHLIGHT_COLOR)
            for _ in range(2)
        ]
        self.other_hashes_rec = VGroup(*self.other_hashes_rec).arrange(RIGHT, buff=2.5)
        self.text_other_hashes = [
            MathTex(f"C_{{{iss[i]}}}^1", font_size=26, color=PRIMARY_COLOR).move_to(
                self.other_hashes_rec[i]
            )
            for i in range(len(self.other_hashes_rec))
        ]

        self.other_hashes = VGroup(*self.other_hashes_rec, *self.text_other_hashes)

        self.final_parent_node_rec = (
            rectangle.copy().scale(2).set_color(SECONDARY_COLOR)
        )
        self.final_parent_node_text = MathTex(
            r"C_0^2", font_size=30, color=SECONDARY_COLOR
        ).move_to(self.final_parent_node_rec.get_center())
        self.final_parent_node = VGroup(
            self.final_parent_node_rec, self.final_parent_node_text
        )

        self.values256 = MathTex(
            r"256 \  \texttt{values}", font_size=45, color=PRIMARY_COLOR
        )

        self.single_commitment = Text(
            "a single commitment has...",
            font=PRIMARY_FONT,
            font_size=20,
            color=PRIMARY_COLOR,
        )
        self.three_level = Text(
            "so three level...", font=PRIMARY_FONT, font_size=20, color=PRIMARY_COLOR
        )
        self.four_level = Text(
            "and four level...", font=PRIMARY_FONT, font_size=20, color=PRIMARY_COLOR
        )

        self.values2_to_8 = MathTex(r"256 = {{2^8}}", font_size=45, color=PRIMARY_COLOR)
        self.values2_to_24 = MathTex(
            r"({{256}})^3 = ({{2^8}})^3 = {{2^{24}}}", font_size=45, color=PRIMARY_COLOR
        )
        self.values2_to_24 = MathTex(
            r"({{256}})^3 = ({{2^8}})^3 = {{2^{24}}}", font_size=45, color=PRIMARY_COLOR
        )
        self.values_four_level = MathTex(
            r"({{256}})^4 = ({{2^8}})^4 = {{2^{32}}} = {{...}}", color=PRIMARY_COLOR
        )

        hashes_copy_recs = [
            rectangle.copy().scale(1.8).set_color(HIGHLIGHT_COLOR) for _ in range(2)
        ]
        self.hashes_copy_recs = VGroup(*hashes_copy_recs).arrange(RIGHT, buff=1.0)

        self.rectangle_with_hashes = RoundedRectangle(
            corner_radius=0.05,
            width=3.5,
            height=0.8,
            fill_opacity=0.15,
            stroke_width=0.0,
        ).set_color(HIGHLIGHT_COLOR)
        self.rectangle_node_commitments2 = (
            self.rectangle_with_hashes.copy()
            .set_color(HIGHLIGHT_COLOR)
            .move_to(self.hashes_copy_recs.get_center())
        )

        values = self.internal_node2.copy().next_to(
            self.hashes_copy_recs[0], DOWN, buff=0.65
        )
        values2 = self.internal_node2.copy().next_to(
            self.hashes_copy_recs[1], DOWN, buff=0.65
        )
        arrows = []
        for i in range(len(self.internal_node2)):
            node = values[i]
            node.move_to(values[i])
            self.create_arrow(self.hashes_copy_recs[0], node, arrows)
            node2 = values2[i]
            self.create_arrow(self.hashes_copy_recs[1], node2, arrows)

        self.rectangle_on_parent_commitments = RoundedRectangle(
            corner_radius=0.05,
            width=5.5,
            height=0.8,
            fill_opacity=0.15,
            stroke_width=0.0,
        ).set_color(HIGHLIGHT_COLOR)
        self.cdots_text = Text(
            "...", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=30
        )

        self.cdots_node1 = (
            self.cdots_text.copy()
            .next_to(self.internal_node[0], RIGHT, buff=0.17)
            .scale(2)
        )
        self.cdots_node2 = self.cdots_text.copy().next_to(
            self.internal_node2[0], RIGHT, buff=0.03
        )
        self.cdots_node3 = self.cdots_text.copy().next_to(
            self.internal_node2[0], LEFT, buff=0.15
        )

        self.cdots_hashes1 = self.cdots_text.copy()
        self.cdots_hashes2 = self.cdots_text.copy()
        self.cdots_right_nodes1 = self.cdots_text.copy().next_to(
            values[0], RIGHT, buff=0.03
        )
        self.cdots_right_nodes3 = self.cdots_text.copy().next_to(
            values[1], RIGHT, buff=0.15
        )
        self.cdots_right_nodes2 = self.cdots_text.copy().next_to(
            values2[0], RIGHT, buff=0.03
        )
        self.cdots_right_hashes = self.cdots_text.copy().next_to(
            self.hashes_copy_recs[0], RIGHT, buff=0.35
        )
        
        self.cdots_value_right_left = self.cdots_text.copy().next_to(
            values[0], LEFT, buff=0.5
        )
        
        self.cdots_commitments_right_left = self.cdots_text.copy().next_to(
            self.rectangle_node_commitments2, LEFT, buff=0.3
        )

        self.right_commitments = VGroup(
            *values,
            *values2,
            *arrows,
            *self.hashes_copy_recs,
            self.rectangle_node_commitments2,
            self.cdots_right_hashes,
            self.cdots_right_nodes1,
            self.cdots_right_nodes2,
            self.cdots_right_nodes3,
            self.cdots_value_right_left,
            self.cdots_commitments_right_left,
        )
        self.right_commitments_opacity = VGroup(
            *values, *values2, *self.hashes_copy_recs
        )
        self.values_right = VGroup(*values, *values2)

    def animate_in(self, scene):
        # self.new_subsection(scene, "3 levels", "data/sound/e7/slide4-0.mp3")
        # self.generate_multi_level_snapshot(scene)

        self.new_subsection(scene, "C0", "data/sound/e7/slide4-1.mp3")
        scene.play(Write(self.title_label), run_time=1)
        scene.play(
            Create(self.internal_node),
            Write(self.node1_texts),
            Write(self.cdots_node1),
            run_time=1,
        )
        self.arrows_C0 = VGroup(*self.arrows_C0)
        scene.play(Write(self.arrows_C0), run_time=0.5)
        scene.play(
            Write(self.commitment_to_c0_text),
            Create(self.commitment_to_C0),
            run_time=0.5,
        )
        scene.wait(0.5)
        scene.play(
            Indicate(self.internal_node[0], color=PRIMARY_COLOR),
            Indicate(self.node1_texts[0], color=PRIMARY_COLOR),
            run_time=0.5,
        )
        scene.play(Indicate(self.cdots_node1, color=PRIMARY_COLOR), run_time=0.5)
        scene.play(
            Indicate(self.internal_node[1], color=PRIMARY_COLOR),
            Indicate(self.node1_texts[1], color=PRIMARY_COLOR),
            run_time=0.5,
        )
        scene.wait(1.5)
        scene.play(
            Indicate(self.commitment_to_c0_text, color=PRIMARY_COLOR), run_time=1
        )

        self.new_subsection(scene, "internal node", "data/sound/e7/slide4-2.mp3")
        self.internal_node_whole = VGroup(
            self.internal_node,
            self.node1_texts,
            self.commitment_to_c0_text,
            self.commitment_to_C0,
            self.arrows_C0,
            self.cdots_node1,
        )
        self.internal_node_whole.generate_target()
        self.internal_node_whole.target.scale(0.5).next_to(
            self.internal_node2_whole, LEFT, buff=0.6
        )
        scene.play(MoveToTarget(self.internal_node_whole), run_time=1)
        scene.play(
            FadeIn(self.internal_node2_whole, self.cdots_node2, self.cdots_node3),
            run_time=1,
        )
        self.internal_node2_whole.add(self.cdots_node2)

        self.commitmentcdots.next_to(self.commitment_to_c255_text, LEFT, buff=0.65)
        self.rectangle_node_commitments.move_to(self.commitmentcdots.get_center())

        scene.play(
            Create(self.commitmentcdots),
            Create(self.rectangle_node_commitments),
            run_time=0.5,
        )
        scene.play(
            Indicate(self.rectangle_node_commitments, color=PRIMARY_COLOR), run_time=1
        )
        scene.wait(1)
        commitments = [
            self.commitment_to_C0,
            self.commitmentcdots,
            self.commitment_to_C255,
        ]
        for commitment in commitments:
            scene.play(Indicate(commitment), run_time=0.4)

        self.new_subsection(scene, "parent to 256 value", "data/sound/e7/slide4-3.mp3")
        scene.wait(1)
        scene.play(Indicate(self.commitment_to_C0, color=PRIMARY_COLOR), run_time=0.8)
        scene.play(Indicate(self.internal_node_whole, color=PRIMARY_COLOR), run_time=1)

        scene.play(Indicate(self.commitment_to_C255, color=PRIMARY_COLOR), run_time=0.8)
        scene.play(Indicate(self.internal_node2_whole, color=PRIMARY_COLOR), run_time=1)

        all_nodes = VGroup(self.internal_node_whole, self.internal_node2_whole)

        all_values = Text(
            "65536 values", font=PRIMARY_FONT, font_size=25, color=PRIMARY_COLOR
        )
        brace_all_values = Brace(all_nodes, DOWN, buff=0.1)
        all_values.next_to(brace_all_values, DOWN, buff=0.1)
        scene.play(Write(brace_all_values), Write(all_values), run_time=1)

        self.new_subsection(scene, "array of commitments", "data/sound/e7/slide4-4.mp3")
        scene.wait(1.5)
        scene.play(
            Indicate(self.commitmentcdots),
            Indicate(self.commitment_to_C0),
            Indicate(self.commitment_to_c0_text),
            Indicate(self.commitment_to_c255_text),
            Indicate(self.commitment_to_C255),
            run_time=1.0,
        )
        scene.play(FadeOut(all_values, brace_all_values))

        self.new_subsection(
            scene, "how to commit to ec points?", "data/sound/e7/slide4-5.mp3"
        )
        scene.wait(2)
        values = [self.internal_node, self.internal_node2]
        for value in values:
            scene.play(Indicate(value), run_time=0.3)

        self.commitment_size_brace = Brace(self.commitment_to_C0, UP, buff=0.1)
        self.scalar_brace = Brace(self.internal_node[0], DOWN, buff=0.1)

        self.ec_point = Text(
            "EC point", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=20
        )
        self.commitment_size_brace.put_at_tip(self.ec_point)

        self.scalar = Text(
            "scalar", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=20
        )
        self.scalar_brace.put_at_tip(self.scalar)
        scene.play(Write(self.scalar_brace), Write(self.scalar), run_time=1)
        scene.wait(3)
        scene.play(Write(self.commitment_size_brace), Write(self.ec_point), run_time=1)
        scene.wait(0.5)
        self.commitment_to_ec_values.next_to(self.commitmentcdots, UP, buff=1.0).shift(
            LEFT * 0.5 + UP
        )
        scene.play(Write(self.commitment_to_ec_values), run_time=1)
        scene.wait(1)

        self.new_subsection(
            scene, "sizes ec and scalar in KZG", "data/sound/e7/slide4-5a.mp3"
        )
        scene.play(FadeOut(self.commitment_to_ec_values), run_time=1)

        kzg_text = Text(
            "KZG", font=PRIMARY_FONT, font_size=25, color=PRIMARY_COLOR
        ).next_to(self.commitment_to_C0, LEFT, buff=1.0)
        ipa_text = Text(
            "IPA", font=PRIMARY_FONT, font_size=25, color=PRIMARY_COLOR
        ).next_to(self.commitment_to_C0, LEFT, buff=1.0)
        self.commitment_size = Text(
            "<381 b", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=20
        )
        self.scalar_size = Text(
            "<255 b", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=20
        )
        self.commitment_size_ipa = Text(
            "<255 b", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=20
        )
        self.scalar_size_ipa = Text(
            "<253 b", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=20
        )
        self.commitment_size_brace.put_at_tip(self.commitment_size_ipa)
        self.commitment_size.move_to(self.commitment_size_ipa.get_center())

        self.scalar_brace.put_at_tip(self.scalar_size)
        self.scalar_brace.put_at_tip(self.scalar_size_ipa)
        scene.play(FadeOut(self.scalar, self.ec_point))
        scene.wait(1)
        scene.play(Write(self.commitment_size), Write(kzg_text), run_time=1)
        scene.wait(2)
        scene.play(Write(self.scalar_size), run_time=1)

        self.new_subsection(
            scene, "sizes ec and scalar in IPA", "data/sound/e7/slide4-5b.mp3"
        )
        scene.wait(1)
        scene.play(
            TransformMatchingShapes(self.commitment_size, self.commitment_size_ipa),
            FadeOut(kzg_text),
            FadeIn(ipa_text),
            run_time=1,
        )
        scene.wait(1)
        scene.play(Indicate(self.commitment_size_ipa), run_time=1)
        scene.play(TransformMatchingShapes(self.scalar_size, self.scalar_size_ipa))
        scene.wait(1)
        scene.play(Indicate(self.scalar_size_ipa), run_time=1)

        self.new_subsection(scene, "truncate", "data/sound/e7/slide4-6.mp3")

        self.hashaes_of_commitments.move_to(self.commitmentcdots.get_center())
        self.cdots_hashes1.move_to(self.commitmentcdots.get_center())
        self.hashaes_of_commitments.add(self.cdots_hashes1)
        self.rectangle_with_hashes.move_to(
            self.hashaes_of_commitments.get_center()
        ).shift(DOWN * 0.35)

        scene.play(
            self.commitment_size_ipa.animate.shift(UP * 0.8),
            self.commitment_size_brace.animate.shift(UP * 0.8),
            run_time=1,
        )
        hash = MathTex(
            r"\texttt{hash}(C_0^0)", color=PRIMARY_COLOR, font_size=25
        ).next_to(self.commitment_size_ipa, DOWN, buff=0.7)
        hash_255 = MathTex(
            r"\texttt{hash}(C_{255}^0)", color=PRIMARY_COLOR, font_size=25
        ).next_to(self.commitment_to_C255, UP, buff=0.3).shift(RIGHT * 0.2)
        arrow_hash = Arrow(
            hash.get_bottom(),
            self.commitment_to_C0.get_top(),
            color=PRIMARY_COLOR,
            buff=0.1,
            tip_shape=StealthTip,
            stroke_width=1.5,
            # max_stroke_width_to_length_ratio=1.,
        )
        scene.play(FadeIn(hash), run_time=1)
        scene.play(Write(arrow_hash), run_time=1)
        self.scalar_size_hash = Text(
            "<253 b", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=20
        ).move_to(self.commitment_size_ipa.get_center())
        scene.play(
            TransformMatchingShapes(self.commitment_size_ipa, self.scalar_size_hash),
            run_time=1,
        )
        scene.wait(2)
        scene.play(Indicate(self.scalar_size_hash), run_time=1)
        scene.play(Indicate(self.scalar_size_ipa), run_time=1)

        self.new_subsection(scene, "commitment C^1_0", "data/sound/e7/slide4-7.mp3")
        self.commitments = VGroup(self.commitment_255, self.commitment_to_C0)
        self.whole_tree_until_C10 = VGroup(
            self.internal_node,
            self.node1_texts,
            hash,
            hash_255,
            self.arrows_C0,
            self.internal_node2,
            self.node2_texts,
            self.cdots_node3,
            self.cdots_node2,
            self.cdots_node1,
            *self.arrows_C255,
            self.rectangle_node_commitments,
            *self.arrows_C0,
            *self.arrows_C255,
            self.commitmentcdots,
            self.commitment_255,
            self.commitment_to_C0,
            self.commitment_to_c0_text,
        )
        scene.play(
            FadeOut(
                self.scalar_brace,
                arrow_hash,
                self.commitment_size_brace,
                self.scalar_size_hash,
                self.scalar_size_ipa,
                ipa_text,
            ),
            FadeIn(hash_255),
            run_time=0.5,
        )
        self.whole_tree_until_C10.generate_target()
        self.whole_tree_until_C10.target.shift(DOWN)
        scene.play(MoveToTarget(self.whole_tree_until_C10), run_time=1)
        self.commitment_C01.next_to(self.commitmentcdots, UP, buff=0.9)
        scene.play(Create(self.commitment_C01), hash.animate.shift(DOWN*0.15+LEFT*0.2), run_time=1)

        self.arrow_commitment_C01 = []
        for rectangle in self.commitments:
            self.create_arrow(
                self.commitment_C01_rec, rectangle, self.arrow_commitment_C01
            )
        self.arrow_commitment_C01 = VGroup(*self.arrow_commitment_C01)
        scene.play(Create(self.arrow_commitment_C01), run_time=1)

        self.new_subsection(
            scene, "and it gathers 256 commitments", "data/sound/e7/slide4-8.mp3"
        )
        scene.play(Indicate(self.commitment_to_C0), run_time=0.5)
        scene.play(Indicate(self.commitment_to_C255), run_time=0.5)

        self.commitment_C01.generate_target()
        self.commitment_C01.target.next_to(self.commitment_to_C0, UP, buff=0.9).shift(
            LEFT * 1.25
        )
        self.whole_tree_until_C10.generate_target()
        self.whole_tree_until_C10.target.shift(LEFT * 2.2)
        scene.play(FadeOut(self.arrow_commitment_C01), run_time=0.5)
        scene.play(
            MoveToTarget(self.commitment_C01),
            MoveToTarget(self.whole_tree_until_C10),
            run_time=1,
        )
        self.arrow_commitment_C01 = []

        for rectangle in self.commitments:
            self.create_arrow(
                self.commitment_C01_rec, rectangle, self.arrow_commitment_C01
            )
        self.other_commitments.next_to(self.commitment_C01, RIGHT, buff=3.5)
        self.right_commitments.next_to(self.other_commitments[0], DOWN, buff=0.78).shift(LEFT*0.3)
        self.rectangle_on_parent_commitments.move_to(
            self.other_commitments.get_center()
        ).shift(LEFT * 2.2)

        self.cdots_hashes2.next_to(self.commitment_C01, RIGHT, buff=1.5)
        self.other_commitments.add(self.cdots_hashes2)
        scene.play(
            Create(self.right_commitments),
            FadeIn(self.rectangle_on_parent_commitments),
            run_time=1,
        )

        for node in self.hashes_copy_recs:
            self.create_arrow(
                self.other_commitments[0], node, self.arrow_commitment_C01
            )

        self.arrow_commitment_C01 = VGroup(*self.arrow_commitment_C01)
        # self.arrow_commitment_C01.add(hash_parent, hash_parent_255)
        scene.play(
            Create(self.other_commitments), Write(self.arrow_commitment_C01), run_time=1
        )

        self.new_subsection(
            scene,
            "reduce root commitments->commit to them->with final parent node",
            "data/sound/e7/slide4-10.mp3",
        )
        self.other_commitments.add(self.commitment_C01)
        self.other_hashes[:][0].move_to(self.commitment_C01.get_center())
        self.other_hashes[:][1].move_to(self.other_commitments[0][0].get_center())
        self.other_hashes[:][2].move_to(self.commitment_C01.get_center())
        self.other_hashes[:][3].move_to(self.other_commitments[0][0].get_center())
        hash_parent = MathTex(
            r"\texttt{hash}(C_0^{1})", color=PRIMARY_COLOR, font_size=25
        ).next_to(self.commitment_C01, UP, buff=0.2)
        hash_parent_255 = MathTex(
            r"\texttt{hash}(C_{255}^1)", color=PRIMARY_COLOR, font_size=25
        ).next_to(self.other_hashes[:][3], UP, buff=0.3)
        self.whole_tree_until_C10.add(self.other_hashes, hash_parent, hash_parent_255)
        scene.play(
            Create(self.other_hashes),
            FadeIn(hash_parent_255, hash_parent),
            FadeOut(self.other_commitments, self.commitment_C01),
            run_time=1,
        )
        scene.wait(1)
        self.final_parent_node.next_to(self.other_hashes, UP, buff=0.9)
        scene.play(Create(self.final_parent_node), run_time=1)
        arrows_final = []
        for i in range(len(self.other_hashes_rec)):
            node = self.other_hashes_rec[i]
            self.create_arrow(self.final_parent_node_rec, node, arrows_final)
            scene.play(Write(arrows_final[i]), run_time=0.3)
        self.whole_tree_until_C10.add(
            self.final_parent_node,
            *arrows_final,
            self.arrow_commitment_C01,
            self.rectangle_on_parent_commitments,
            self.right_commitments,
            self.cdots_hashes2,
        )

        self.new_subsection(scene, "simple math", "data/sound/e7/slide4-11.mp3")
        scene.wait(1)
        self.whole_tree_until_C10.generate_target()
        self.whole_tree_until_C10.target.scale(0.75).shift(LEFT * 2.5 + UP)
        scene.play(MoveToTarget(self.whole_tree_until_C10), run_time=2.5)
        nodes = VGroup(
            self.internal_node2,
            self.internal_node,
            self.commitments,
            self.right_commitments_opacity,
            self.other_hashes_rec,
            self.final_parent_node_rec,
        )

        texts = VGroup(
            self.node2_texts,
            self.node1_texts,
            self.commitment_to_c0_text,
            self.commitment_to_c255_text,
            self.final_parent_node_text,
            *self.text_other_hashes,
            hash, hash_255, hash_parent, hash_parent_255,
        )
        scene.play(
            nodes.animate.set_opacity(0.15), texts.animate.set_opacity(0.15), run_time=2
        )

        self.new_subsection(
            scene, "simple level VT holds 256 vals", "data/sound/e7/slide4-11a.mp3"
        )

        self.values256.next_to(self.whole_tree_until_C10, RIGHT, buff=1.0).shift(
            RIGHT * 0.5 + UP * 0.5
        )
        self.single_commitment.next_to(self.values256, UP, buff=0.3)
        self.values2_to_8.next_to(self.whole_tree_until_C10, RIGHT, buff=1.0).shift(
            RIGHT * 0.5 + UP * 0.5
        )
        self.values2_to_24.next_to(self.values2_to_8, DOWN, buff=1.0)
        self.three_level.next_to(self.values2_to_24, UP, buff=0.3)
        self.four_level.next_to(self.values2_to_8, DOWN, buff=0.3)
        self.values_four_level.next_to(self.values2_to_8, DOWN, buff=1.0).shift(
            RIGHT * 0.5
        ).scale(0.7)
        scene.play(Write(self.values256), Write(self.single_commitment), run_time=1)
        scene.play(
            self.commitment_to_c0_text.animate.set_opacity(1.0),
            self.commitment_to_c255_text.animate.set_opacity(1.0),
            run_time=0.5,
        )

        scene.play(
            Indicate(self.commitment_to_c0_text, color=PRIMARY_COLOR),
            Indicate(self.commitment_to_c255_text, color=PRIMARY_COLOR),
            run_time=1.0,
        )
        scene.play(
            self.internal_node.animate.set_opacity(0.4),
            self.node1_texts.animate.set_opacity(1.0),
            run_time=1,
        )
        scene.wait(0.5)
        scene.play(
            TransformMatchingShapes(self.values256, self.values2_to_8), run_time=0.5
        )
        scene.wait(2)

        scene.play(Write(self.three_level), run_time=0.5)
        scene.play(
            self.internal_node2.animate.set_opacity(0.4),
            self.node2_texts.animate.set_opacity(1.0),
            self.values_right.animate.set_opacity(0.4),
            run_time=1,
        )

        scene.play(
            TransformMatchingShapes(self.values2_to_8.copy(), self.values2_to_24),
            run_time=0.5,
        )
        scene.play(nodes.animate.set_opacity(0.4), run_time=1)
        scene.play(texts.animate.set_opacity(1.0), run_time=1)
        scene.wait(2)

        self.new_subsection(
            scene,
            "4 level deep squeeze in all of the ETH acc",
            "data/sound/e7/slide4-11b.mp3",
        )
        scene.play(
            TransformMatchingShapes(self.three_level, self.four_level), run_time=0.5
        )
        scene.wait(1.5)
        scene.play(
            TransformMatchingShapes(self.values2_to_24, self.values_four_level),
            run_time=0.5,
        )
        self.create_ethereum_addresses_counter(scene)

    def animate_out(self, scene):
        scene.play(
            FadeOut(
                self.title_label,
                self.four_level,
                self.block,
                self.ethereum_addresses,
                self.number,
                self.whole_tree_until_C10,
                self.values_four_level,
            ),
            run_time=1,
        )

    def generate_multi_level_snapshot(self, scene):
        rectangle = RoundedRectangle(
            corner_radius=0.05,
            width=0.5,
            height=0.5,
            fill_opacity=0.25,
            stroke_width=0.0,
        ).set_color(SECONDARY_COLOR)
        self.first_block = [rectangle.copy() for _ in range(10)]
        self.first_block = VGroup(*self.first_block).arrange(RIGHT, buff=0.05)
        self.cdots = (
            Text(r"...", font=PRIMARY_FONT, font_size=40, color=PRIMARY_COLOR)
            .move_to(self.first_block[5])
            .shift(LEFT * 0.22)
        )

        self.third_block = self.first_block.copy()
        self.second_block = self.first_block.copy()
        self.cdots3 = self.cdots.copy().move_to(self.third_block[5]).shift(LEFT * 0.22)
        self.first_block.add(self.cdots)
        self.cdots2 = self.cdots.copy().move_to(self.second_block[5]).shift(LEFT * 0.22)
        self.second_block.add(self.cdots2)
        self.third_block.add(self.cdots3)

        self.first_block.remove(*self.first_block[4:6])
        scene.play(Create(self.first_block), run_time=1)
        self.first_block.generate_target()
        self.first_block.target.scale(0.5).shift(LEFT * 3 + DOWN * 2)
        scene.play(MoveToTarget(self.first_block), run_time=1)
        self.second_block.scale(0.5).shift(DOWN * 2)
        self.third_block.scale(0.5).shift(RIGHT * 3 + DOWN * 2)
        self.second_block.remove(*self.second_block[4:6])
        self.third_block.remove(*self.third_block[4:6])

        scene.play(Create(self.second_block), Create(self.third_block), run_time=1)

        self.commitment_to_first = (
            rectangle.copy()
            .set_color(PRIMARY_COLOR)
            .next_to(self.first_block, UP, buff=1.0)
        )
        self.commitment_to_second = (
            rectangle.copy()
            .set_color(PRIMARY_COLOR)
            .next_to(self.second_block, UP, buff=1.0)
        )
        self.commitment_to_third = (
            rectangle.copy()
            .set_color(PRIMARY_COLOR)
            .next_to(self.third_block, UP, buff=1.0)
        )

        self.commitment_to_commitment = (
            rectangle.copy()
            .set_color(HIGHLIGHT_COLOR)
            .next_to(self.commitment_to_second, UP, buff=1.0)
        )
        arrows = []
        for rectangle in self.first_block:
            self.create_arrow(self.commitment_to_first, rectangle, arrows)
        for rectangle in self.second_block:
            self.create_arrow(self.commitment_to_second, rectangle, arrows)
        for rectangle in self.third_block:
            self.create_arrow(self.commitment_to_third, rectangle, arrows)

        arrows = VGroup(*arrows)
        arrows.remove(*arrows[26:35], *arrows[8:9], *arrows[17:18])

        arrows2 = []
        scene.play(
            Create(self.commitment_to_first),
            Write(arrows),
            Create(self.commitment_to_second),
            Create(self.commitment_to_third),
            run_time=0.5,
        )
        self.create_arrow(
            self.commitment_to_commitment, self.commitment_to_first, arrows2
        )
        self.create_arrow(
            self.commitment_to_commitment, self.commitment_to_second, arrows2
        )
        self.create_arrow(
            self.commitment_to_commitment, self.commitment_to_third, arrows2
        )
        arrows2 = VGroup(*arrows2)
        scene.play(Write(arrows2), Create(self.commitment_to_commitment), run_time=0.5)
        scene.wait(1)
        scene.play(
            FadeOut(
                self.first_block,
                self.commitment_to_commitment,
                self.commitment_to_first,
                self.commitment_to_second,
                self.commitment_to_third,
                arrows,
            ),
            FadeOut(self.second_block, arrows2),
            FadeOut(self.third_block),
            run_time=1,
        )

    def create_arrow(self, start, end, arrows):
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
        arrows.append(arrow)

    def create_ethereum_addresses_counter(self, scene):
        scene.play(FadeOut(self.values2_to_8, self.single_commitment))
        self.block = RoundedRectangle(
            corner_radius=0.05, width=4, height=2, fill_opacity=0.25, stroke_width=0.0
        ).set_color(PRIMARY_COLOR)
        self.block.next_to(self.four_level, DOWN, buff=1.5)
        self.ethereum_addresses = (
            Text(
                "Ethereum addresses",
                font=PRIMARY_FONT,
                font_size=30,
                color=PRIMARY_COLOR,
            )
            .move_to(self.block.get_center())
            .shift(UP * 0.5)
        )
        scene.play(FadeIn(self.block, self.ethereum_addresses), run_time=1)
        self.number = (
            DecimalNumber(0, font_size=50, color=PRIMARY_COLOR)
            .move_to(self.block.get_center())
            .shift(DOWN * 0.5 + LEFT)
        )
        scene.play(ChangeDecimalToValue(self.number, 308105039), run_time=2)
