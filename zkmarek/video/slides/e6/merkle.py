from manim import (
    VGroup,
    Group,
    Text,
    ImageMobject,
    UP,
    LEFT,
    RIGHT,
    DOWN,
    Write,
    Create,
    Indicate,
    FadeOut,
    MathTex,
    RoundedRectangle,
    Transform,
    TransformMatchingShapes,
    Arrow,
    StealthTip,
    FadeIn,
    DashedVMobject,
)
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import (
    PRIMARY_COLOR,
    PRIMARY_FONT,
    HIGHLIGHT2_COLOR,
    SECONDARY_COLOR,
    HIGHLIGHT_COLOR,
)
from zkmarek.video.slides.e6.tree import MerkleTree as Tree


class MerkleTree(SlideBase):
    def __init__(self) -> None:
        super().__init__("Merkle Trees")

    def construct(self):
        self.title_label = Text(
            "Merkle Trees", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=40
        ).to_edge(UP)

        self.markle_tree_2_3 = (
            Tree(num_children=2, num_levels=3, include_labels=False)
            .shift(RIGHT * 3.5 + UP * 2.8)
            .scale(0.3)
        )
        self.markle_tree_2_3.stretch(2, dim=1)

        self.account_data_vector = Text(
            "Account Data Vector", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=30
        ).shift(LEFT * 3.5 + UP)
        self.arrow_acc_tree = Arrow(
            self.account_data_vector.get_right() + DOWN * 0.2 + RIGHT * 1,
            RIGHT * 1.3 + UP * 0.8,
            color=SECONDARY_COLOR,
            stroke_width=1.5,
            tip_shape=StealthTip,
            tip_length=0.15,
        )
        self.arrow_acc_tree = DashedVMobject(self.arrow_acc_tree, num_dashes=5)

        self.account_vector_rectangles = [
            RoundedRectangle(
                width=2,
                height=0.8,
                fill_opacity=0.3,
                stroke_width=0.0,
                corner_radius=0.1,
            )
            for _ in range(4)
        ]
        for i in range(4):
            self.account_vector_rectangles[i].set_color(PRIMARY_COLOR).scale(0.6)
        self.account_group = (
            VGroup(*self.account_vector_rectangles)
            .arrange(RIGHT, buff=0.4)
            .next_to(self.account_data_vector, DOWN)
        )
        self.account_group[1].shift(LEFT * 0.2)
        self.account_group[2].shift(RIGHT * 0.2)
        self.vec0 = Text(
            "1 ETH", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=16
        ).move_to(self.account_vector_rectangles[0])
        self.vec1 = Text(
            "0.1 ETH", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=16
        ).move_to(self.account_vector_rectangles[1])
        self.dots_vec = (
            MathTex(r"\boldsymbol{\cdots}", color=PRIMARY_COLOR, font_size=35)
            .next_to(self.account_data_vector, DOWN)
            .scale(0.8)
            .shift(DOWN * 0.2)
        )
        self.vec2 = Text(
            "0.8 ETH", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=16
        ).move_to(self.account_vector_rectangles[2])
        self.vec3 = Text(
            "1.1 ETH", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=16
        ).move_to(self.account_vector_rectangles[3])
        self.vecs = VGroup(self.vec0, self.vec1, self.dots_vec, self.vec2, self.vec3)

        self.vector_8element = Text(
            r"46735083", color=PRIMARY_COLOR, font_size=24, font=PRIMARY_FONT
        ).next_to(self.account_data_vector, DOWN)
        self.merkle_tree_2_4 = (
            Tree(num_children=2, num_levels=4, include_labels=False)
            .shift(UP * 4)
            .scale(0.56)
        )
        self.account_vector_rectangles_8_elements = [
            RoundedRectangle(
                width=2.5,
                height=2.5,
                fill_opacity=0.3,
                stroke_width=0.0,
                corner_radius=0.5,
            )
            for _ in range(8)
        ]
        for i in range(8):
            self.account_vector_rectangles_8_elements[i].set_color(PRIMARY_COLOR).scale(
                0.2
            )
        self.account_group_8_elements = (
            VGroup(*self.account_vector_rectangles_8_elements)
            .arrange(RIGHT, buff=0.2)
            .next_to(self.account_data_vector, DOWN)
        )

        for i in range(8):
            self.vector_8element[i].move_to(
                self.account_vector_rectangles_8_elements[i].get_center()
            )

        self.seal_of_authenticity = ImageMobject("data/images/Badge.png").scale(0.3)
        self.title_merkle_proof = Text(
            "Merkle proof", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=40
        ).to_edge(UP)

    def animate_in(self, scene):

        self.new_subsection(scene, "8 element vector", "data/sound/e6/slide2-2.mp3")
        scene.play(Write(self.title_label))
        self.merkle24_nodes_level3 = [
            self.merkle_tree_2_4.get_node(3, 0),
            self.merkle_tree_2_4.get_node(3, 1),
            self.merkle_tree_2_4.get_node(3, 2),
            self.merkle_tree_2_4.get_node(3, 3),
            self.merkle_tree_2_4.get_node(3, 4),
            self.merkle_tree_2_4.get_node(3, 5),
            self.merkle_tree_2_4.get_node(3, 6),
            self.merkle_tree_2_4.get_node(3, 7),
        ]
        for i in range(8):
            self.account_group_8_elements[i].next_to(
                self.merkle24_nodes_level3[i], DOWN, buff=0.3
            )
            self.vector_8element[i].move_to(
                self.account_group_8_elements[i].get_center()
            )
        for i in range(8):
            scene.play(
                Write(self.vector_8element[i]),
                Create(self.account_group_8_elements[i]),
                run_time=0.07,
            )
        scene.wait(1.5)
        scene.play(Create(self.merkle_tree_2_4), run_time=2)
        scene.wait(2)

        self.new_subsection(scene, "leaf: value+hash", "data/sound/e6/slide2-2a.mp3")

        self.hashes_of_8_element(scene)

        self.new_subsection(
            scene, "root hash - immutable", "data/sound/e6/slide2-2c.mp3"
        )
        scene.wait(1)
        self.seal_of_authenticity.next_to(self.merkle24_nodes_level0, LEFT, buff=0.3)
        scene.play(FadeIn(self.seal_of_authenticity))
        scene.wait(1)
        scene.play(FadeOut(self.seal_of_authenticity))
        self.update_nodes(scene)

        level = [
            self.merkle24_nodes_level3[0],
            self.merkle24_nodes_level2[0],
            self.merkle24_nodes_level1[0],
            self.merkle24_nodes_level0,
        ]
        for i in range(4):
            levels = level[i]
            levels.set_color(HIGHLIGHT_COLOR)
        self.account_group_8_elements[0].set_color(PRIMARY_COLOR)

        self.new_subsection(scene, "merkle proofs", "data/sound/e6/slide2-3.mp3")
        self.merkle_proof(scene)
        scene.wait(1)

        self.merkle_tree_all = Group(
            self.merkle_tree_2_4,
            self.vector_8element,
            self.account_group_8_elements,
            self.all_hashes,
        )

        # self.new_subsection(scene, "merkle proofs", "data/sound/e6/slide2-3b.mp3")
        # self.calculate_merkle_proof(scene)

    def animate_out(self, scene):
        scene.play(
            FadeOut(self.title_merkle_proof, self.merkle_tree_all, *self.nodes_copy)
        )

    def hashes_of_8_element(self, scene):
        self.level3_hashes_not_numerical = [
            Text("H(4)", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=16),
            Text("H(6)", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=16),
            Text("H(7)", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=16),
            Text("H(3)", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=16),
            Text("H(5)", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=16),
            Text("H(0)", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=16),
            Text("H(8)", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=16),
            Text("H(3)", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=16),
        ]
        self.level_3_hashes = [
            Text("e2a1f...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=16),
            Text("f7c3b...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=16),
            Text("c1d04...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=16),
            Text("eccbc...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=16),
            Text("36279...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=16),
            Text("4b227...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=16),
            Text("cd573...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=16),
            Text("eccbc...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=16),
        ]

        self.level_2_hashes = [
            Text("a6a68...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=16),
            Text("ae5a7...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=16),
            Text("e326b...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=16),
            Text("8dbb1...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=16),
        ]

        self.level_1_hashes = [
            Text("56f15...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=16),
            Text("913a7...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=16),
        ]

        self.level_0_hashes = Text(
            "d7f0c...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=16
        )

        self.merkle24_nodes_level3 = [
            self.merkle_tree_2_4.get_node(3, 0),
            self.merkle_tree_2_4.get_node(3, 1),
            self.merkle_tree_2_4.get_node(3, 2),
            self.merkle_tree_2_4.get_node(3, 3),
            self.merkle_tree_2_4.get_node(3, 4),
            self.merkle_tree_2_4.get_node(3, 5),
            self.merkle_tree_2_4.get_node(3, 6),
            self.merkle_tree_2_4.get_node(3, 7),
        ]
        for i in range(8):
            level = self.merkle24_nodes_level3[i]
            self.level_3_hashes[i].move_to(level.get_center())
            not_numerical = self.level3_hashes_not_numerical[i]
            not_numerical.move_to(level.get_center())

        self.merkle24_nodes_level2 = [
            self.merkle_tree_2_4.get_node(2, 0),
            self.merkle_tree_2_4.get_node(2, 1),
            self.merkle_tree_2_4.get_node(2, 2),
            self.merkle_tree_2_4.get_node(2, 3),
        ]
        for i in range(4):
            level = self.merkle24_nodes_level2[i]
            self.level_2_hashes[i].move_to(level.get_center())

        self.merkle24_nodes_level1 = [
            self.merkle_tree_2_4.get_node(1, 0),
            self.merkle_tree_2_4.get_node(1, 1),
        ]
        for i in range(2):
            level = self.merkle24_nodes_level1[i]
            self.level_1_hashes[i].move_to(level.get_center())

        self.merkle24_nodes_level0 = self.merkle_tree_2_4.get_node(0, 0)
        level = self.merkle24_nodes_level0
        self.level_0_hashes.move_to(level.get_center())
        scene.wait(0.6)
        scene.play(
            Indicate(self.vector_8element, color=HIGHLIGHT_COLOR),
            Indicate(self.account_group_8_elements, color=HIGHLIGHT_COLOR),
            run_time=0.8,
        )
        scene.wait(0.5)
        for i in range(8):
            scene.play(Create(self.level3_hashes_not_numerical[i]), run_time=0.1)
        scene.play(
            TransformMatchingShapes(
                self.level3_hashes_not_numerical[0], self.level_3_hashes[0]
            ),
            TransformMatchingShapes(
                self.level3_hashes_not_numerical[1], self.level_3_hashes[1]
            ),
            TransformMatchingShapes(
                self.level3_hashes_not_numerical[2], self.level_3_hashes[2]
            ),
            TransformMatchingShapes(
                self.level3_hashes_not_numerical[3], self.level_3_hashes[3]
            ),
            TransformMatchingShapes(
                self.level3_hashes_not_numerical[4], self.level_3_hashes[4]
            ),
            TransformMatchingShapes(
                self.level3_hashes_not_numerical[5], self.level_3_hashes[5]
            ),
            TransformMatchingShapes(
                self.level3_hashes_not_numerical[6], self.level_3_hashes[6]
            ),
            TransformMatchingShapes(
                self.level3_hashes_not_numerical[7], self.level_3_hashes[7]
            ),
            run_time=0.5,
        )

        scene.wait(0.2)

        self.new_subsection(scene, "children hashes", "data/sound/e6/slide2-2b.mp3")
        scene.play(
            *[
                Indicate(self.merkle24_nodes_level2[i], color=SECONDARY_COLOR)
                for i in range(4)
            ],
            *[
                Indicate(self.merkle24_nodes_level1[i], color=SECONDARY_COLOR)
                for i in range(2)
            ],
            run_time=0.8
        )
        for i in range(4):
            if i == 0:
                scene.play(
                    Indicate(self.merkle24_nodes_level2[i]),
                    Create(self.level_2_hashes[i]),
                )
                scene.play(
                    Indicate(self.merkle24_nodes_level3[0], color=SECONDARY_COLOR),
                    run_time=0.5,
                )
                scene.play(
                    Indicate(self.merkle24_nodes_level3[1], color=SECONDARY_COLOR),
                    run_time=0.5,
                )
            else:
                scene.play(Create(self.level_2_hashes[i]), run_time=0.5)
        for i in range(2):
            scene.play(Create(self.level_1_hashes[i]), run_time=0.5)
        scene.play(Create(self.level_0_hashes), run_time=0.8)
        scene.wait(0.5)
        scene.play(
            Indicate(self.level_0_hashes, color=SECONDARY_COLOR),
            Indicate(self.merkle_tree_2_4.get_node(0, 0), color=SECONDARY_COLOR),
        )

    def update_nodes(self, scene):
        index_of_the_node = 0
        new_value = 9
        new_numerical_value = Text(
            str(new_value), color=PRIMARY_COLOR, font_size=26, font=PRIMARY_FONT
        ).move_to(self.account_group_8_elements[0].get_center())
        self.account_group_8_elements[0].set_color(SECONDARY_COLOR)
        scene.play(
            Transform(self.vector_8element[index_of_the_node], new_numerical_value)
        )
        self.new_hashes = [
            Text("19581...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=16),
            Text("3c825...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=16),
            Text("9c493...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=16),
            Text("d313e...", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=16),
        ]
        level = [
            self.merkle24_nodes_level3[0],
            self.merkle24_nodes_level2[0],
            self.merkle24_nodes_level1[0],
            self.merkle24_nodes_level0,
        ]
        for i in range(4):
            levels = level[i]
            self.new_hashes[i].move_to(levels.get_center())

        prev_hashes = [
            self.level_3_hashes[0],
            self.level_2_hashes[0],
            self.level_1_hashes[0],
            self.level_0_hashes,
        ]
        for i in range(4):
            levels = level[i]
            prev_hash = prev_hashes[i]
            levels.set_color(SECONDARY_COLOR)
            scene.play(
                TransformMatchingShapes(prev_hash, self.new_hashes[i]), run_time=0.9
            )

        self.all_hashes = VGroup(
            *self.new_hashes,
            *self.level_3_hashes[1:9],
            *self.level_2_hashes[1:4],
            *self.level_1_hashes[1:]
        )
        scene.wait(2.5)
        scene.play(Indicate(self.new_hashes[3], color = SECONDARY_COLOR))

    def merkle_proof(self, scene):
        all_nodes = VGroup(
            *self.account_group_8_elements[0:3],
            *self.account_group_8_elements[4:],
            self.merkle_tree_2_4.get_node(3, 0),
            self.merkle_tree_2_4.get_node(3, 1),
            self.merkle_tree_2_4.get_node(3, 2),
            self.merkle_tree_2_4.get_node(3, 3),
            self.merkle_tree_2_4.get_node(3, 4),
            self.merkle_tree_2_4.get_node(3, 5),
            self.merkle_tree_2_4.get_node(3, 6),
            self.merkle_tree_2_4.get_node(3, 7),
            self.merkle_tree_2_4.get_node(2, 0),
            self.merkle_tree_2_4.get_node(2, 1),
            self.merkle_tree_2_4.get_node(2, 2),
            self.merkle_tree_2_4.get_node(2, 3),
            self.merkle_tree_2_4.get_node(1, 0),
            self.merkle_tree_2_4.get_node(1, 1),
            self.merkle_tree_2_4.get_node(0, 0)
        )
        all_hashes_in_order = VGroup(
            *self.vector_8element[0:3],
            *self.vector_8element[4:],
            self.new_hashes[0],
            *self.level_3_hashes[1:9],
            self.new_hashes[1],
            *self.level_2_hashes[1:4],
            self.new_hashes[2],
            self.level_1_hashes[1],
            self.new_hashes[3]
        )

        node_prove = self.merkle_tree_2_4.get_node(3, 3)
        scene.play(
            Indicate(node_prove, color=SECONDARY_COLOR),
            Indicate(self.account_group_8_elements[3], color=SECONDARY_COLOR),
            TransformMatchingShapes(self.title_label, self.title_merkle_proof),
        )
        node_prove.set_color(SECONDARY_COLOR)
        self.account_group_8_elements[3].set_color(SECONDARY_COLOR)
        # nodes_unused = [self.merkle_tree_2_4.get_node(3, 0), self.merkle_tree_2_4.get_node(3, 1), self.merkle_tree_2_4.get_node(3, 4), self.merkle_tree_2_4.get_node(3, 5),
        # self.merkle_tree_2_4.get_node(3, 6), self.merkle_tree_2_4.get_node(3, 7), self.merkle_tree_2_4.get_node(2, 2), self.merkle_tree_2_4.get_node(2, 3)]
        self.hashes_unused = [
            self.new_hashes[0],
            self.level_3_hashes[1],
            self.level_3_hashes[4],
            self.level_3_hashes[5],
            self.level_3_hashes[6],
            self.level_3_hashes[7],
            self.level_2_hashes[2],
            self.level_2_hashes[3],
        ]

        self.hashes_on_path = [
            self.level_3_hashes[3],
            self.level_2_hashes[1],
            self.new_hashes[2],
            self.new_hashes[3],
        ]
        nodes_directly_used = [
            self.merkle_tree_2_4.get_node(3, 3),
            self.merkle_tree_2_4.get_node(2, 1),
            self.merkle_tree_2_4.get_node(1, 0),
            self.merkle_tree_2_4.get_node(0, 0),
        ]
        for i in range(len(all_nodes)):
            node = all_nodes[i]
            hash = all_hashes_in_order[i]
            scene.play(
                node.animate.set_opacity(0.1),
                hash.animate.set_opacity(0.1),
                run_time=0.1,
            )
        for i in range(len(nodes_directly_used)):
            node = nodes_directly_used[i]
            hash = self.hashes_on_path[i]
            scene.play(
                node.animate.set_opacity(0.4).set_color(SECONDARY_COLOR),
                hash.animate.set_opacity(1.0),
                run_time=0.3,
            )
            scene.play(
                node.animate.set_opacity(0.1),
                hash.animate.set_opacity(0.1),
                run_time=0.3,
            )

        scene.wait(1.2)
        nodes_needed_to_proof = [
            self.merkle_tree_2_4.get_node(3, 2),
            self.merkle_tree_2_4.get_node(2, 0),
            self.merkle_tree_2_4.get_node(1, 1),
        ]
        hashes_needed_to_proof = [
            self.level_3_hashes[2],
            self.new_hashes[1],
            self.level_1_hashes[1],
        ]
        for i in range(len(nodes_needed_to_proof)):
            node = nodes_needed_to_proof[i]
            hash = hashes_needed_to_proof[i]
            scene.play(
                node.animate.set_opacity(1.0).set_color(HIGHLIGHT2_COLOR),
                hash.animate.set_opacity(1.0),
                run_time=0.3,
            )
            scene.play(
                node.animate.set_opacity(0.1),
                hash.animate.set_opacity(0.1),
                run_time=0.3,
            )

        scene.wait(0.5)

        nodes_copy = []
        for i in range(len(nodes_needed_to_proof)):
            node = nodes_needed_to_proof[i]
            node = node.copy()
            node.set_opacity(0.4)
            hash = hashes_needed_to_proof[i]
            hash = hash.copy()
            hash.set_opacity(1.0)
            node.set_color(HIGHLIGHT2_COLOR).next_to(
                self.merkle_tree_2_4, DOWN, buff=1.0
            ).shift(LEFT * 2 + RIGHT * 2 * i + DOWN * 0.2)
            hash.move_to(node.get_center())
            scene.play(
                TransformMatchingShapes(
                    VGroup(nodes_needed_to_proof[i], hashes_needed_to_proof[i]),
                    VGroup(node, hash),
                ),
                run_time=0.4,
            )
            nodes_copy.append(node)
            nodes_copy.append(hash)
        scene.wait(0.5)
        self.nodes_copy = nodes_copy

        self.new_subsection(
            scene, "lets see how this works", "data/sound/e6/slide2-3a1.mp3"
        )
        scene.wait(2)
        scene.play(
            nodes_needed_to_proof[0]
            .animate.set_opacity(0.4)
            .set_color(HIGHLIGHT2_COLOR),
            hashes_needed_to_proof[0].animate.set_opacity(1.0),
            Indicate(self.nodes_copy[0], color=HIGHLIGHT2_COLOR),
        )
        scene.play(
            node_prove.animate.set_opacity(0.4).set_color(SECONDARY_COLOR),
            self.level_3_hashes[3].animate.set_opacity(1.0),
        )
        scene.wait(1)
        scene.play(
            self.hashes_on_path[1].animate.set_opacity(1.0),
            nodes_directly_used[1].set_color(SECONDARY_COLOR).animate.set_opacity(0.4),
            run_time=0.5,
        )
        scene.wait(0.5)
        scene.play(
            nodes_needed_to_proof[1]
            .animate.set_opacity(0.4)
            .set_color(HIGHLIGHT2_COLOR),
            hashes_needed_to_proof[1].animate.set_opacity(1.0),
            Indicate(self.nodes_copy[2], color=HIGHLIGHT2_COLOR),
            run_time=0.5,
        )
        scene.play(
            self.hashes_on_path[2].animate.set_opacity(1.0),
            nodes_directly_used[2].set_color(SECONDARY_COLOR).animate.set_opacity(0.4),
            run_time=0.5,
        )
        scene.play(
            nodes_needed_to_proof[2]
            .animate.set_opacity(0.4)
            .set_color(HIGHLIGHT2_COLOR),
            hashes_needed_to_proof[2].animate.set_opacity(1.0),
            Indicate(self.nodes_copy[4], color=HIGHLIGHT2_COLOR),
            run_time=0.5,
        )
        scene.play(
            self.hashes_on_path[3].animate.set_opacity(1.0),
            nodes_directly_used[3].set_color(SECONDARY_COLOR).animate.set_opacity(0.4),
            run_time=0.5,
        )
        scene.wait(1)


    def animate_miniature(self, scene):
        rectangle = RoundedRectangle(width = 11, height = 5, corner_radius=0.1).set_color(PRIMARY_COLOR)
        self.merkle_tree_2_4.scale(0.75).move_to(rectangle.get_center())
        rectangle.shift(DOWN * 0.4)
        scene.play(FadeIn(rectangle), run_time=0.5)
        scene.play(Create(self.merkle_tree_2_4), run_time=0.5)

        all_nodes = VGroup(
            self.merkle_tree_2_4.get_node(3, 0),
            self.merkle_tree_2_4.get_node(3, 1),
            self.merkle_tree_2_4.get_node(3, 2),
            self.merkle_tree_2_4.get_node(3, 3),
            self.merkle_tree_2_4.get_node(3, 4),
            self.merkle_tree_2_4.get_node(3, 5),
            self.merkle_tree_2_4.get_node(3, 6),
            self.merkle_tree_2_4.get_node(3, 7),
            self.merkle_tree_2_4.get_node(2, 0),
            self.merkle_tree_2_4.get_node(2, 1),
            self.merkle_tree_2_4.get_node(2, 2),
            self.merkle_tree_2_4.get_node(2, 3),
            self.merkle_tree_2_4.get_node(1, 0),
            self.merkle_tree_2_4.get_node(1, 1),
            self.merkle_tree_2_4.get_node(0, 0)
        )
        node_prove = self.merkle_tree_2_4.get_node(3, 3)

        node_prove.set_color(SECONDARY_COLOR)

        nodes_directly_used = [
            self.merkle_tree_2_4.get_node(3, 3),
            self.merkle_tree_2_4.get_node(2, 1),
            self.merkle_tree_2_4.get_node(1, 0),
            self.merkle_tree_2_4.get_node(0, 0),
        ]
        for i in range(len(all_nodes)):
            node = all_nodes[i]
            node.set_opacity(0.1)
            
        for i in range(len(nodes_directly_used)):
            node = nodes_directly_used[i]
            node.set_opacity(0.4).set_color(SECONDARY_COLOR)
            node.animate.set_opacity(0.1)

        nodes_needed_to_proof = [
            self.merkle_tree_2_4.get_node(3, 2),
            self.merkle_tree_2_4.get_node(2, 0),
            self.merkle_tree_2_4.get_node(1, 1),
        ]

        for i in range(len(nodes_needed_to_proof)):
            node = nodes_needed_to_proof[i]
            node.set_opacity(1.0).set_color(HIGHLIGHT2_COLOR),

            node.set_opacity(0.1),



        nodes_copy = []
        for i in range(len(nodes_needed_to_proof)):
            node = nodes_needed_to_proof[i]
            node = node.copy()
            node.set_opacity(0.4)
            node.set_color(HIGHLIGHT2_COLOR).next_to(
                self.merkle_tree_2_4, DOWN, buff=0.7
            ).shift(LEFT * 2 + RIGHT * 2 * i)
            scene.play(
                TransformMatchingShapes(
                    nodes_needed_to_proof[i],
                    node,
                ),
                run_time=0.4,
            )
            nodes_copy.append(node)
            nodes_copy.append(hash)
        self.nodes_copy = nodes_copy

        scene.play(
            nodes_needed_to_proof[0]
            .animate.set_opacity(0.4)
            .set_color(HIGHLIGHT2_COLOR),
            Indicate(self.nodes_copy[0], color=HIGHLIGHT2_COLOR),
        )
        scene.play(
            node_prove.animate.set_opacity(0.4).set_color(SECONDARY_COLOR),
        )
        scene.play(
            nodes_directly_used[1].set_color(SECONDARY_COLOR).animate.set_opacity(0.4),
            run_time=0.5,
        )
        scene.play(
            nodes_needed_to_proof[1]
            .animate.set_opacity(0.4)
            .set_color(HIGHLIGHT2_COLOR),
            Indicate(self.nodes_copy[2], color=HIGHLIGHT2_COLOR),
            run_time=0.5,
        )
        scene.play(
            nodes_directly_used[2].set_color(SECONDARY_COLOR).animate.set_opacity(0.4),
            run_time=0.5,
        )
        scene.play(
            nodes_needed_to_proof[2]
            .animate.set_opacity(0.4)
            .set_color(HIGHLIGHT2_COLOR),
            Indicate(self.nodes_copy[4], color=HIGHLIGHT2_COLOR),
            run_time=0.5,
        )
        scene.play(
            nodes_directly_used[3].set_color(SECONDARY_COLOR).animate.set_opacity(0.4),
            run_time=0.5,
        )
        
        scene.play(FadeOut(rectangle, self.merkle_tree_2_4, self.nodes_copy[0], self.nodes_copy[2], self.nodes_copy[4]), run_time=0.5)