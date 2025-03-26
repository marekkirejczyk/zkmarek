from manim import (
    Text,
    RoundedRectangle,
    DashedVMobject,
    Create,
    Write,
    FadeOut,
    Indicate,
    Brace,
    MathTex,
    VGroup,
    MoveToTarget,
    RIGHT,
    UP,
    LEFT,
    DOWN,
    FadeIn,
    TransformMatchingShapes,
)
from zkmarek.video.constant import (
    PRIMARY_COLOR,
    PRIMARY_FONT,
    SECONDARY_COLOR,
    HIGHLIGHT_COLOR,
)
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.e6.bin_mpt import BinaryMPT as BinMPT
from zkmarek.video.slides.e6.table import TableKeyValue
from zkmarek.video.slides.e6.merkle16 import SelectiveMerkleTree as MT16
from zkmarek.video.slides.e6.tree import MerkleTree as Tree


class PatriciaTries(SlideBase):
    def __init__(self) -> None:
        super().__init__("Patricia Tries")

    def construct(self):
        self.title_pt = Text(
            "Patricia Tries", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=40
        ).to_edge(UP)
        self.bin_mpt = BinMPT(include_labels=False).shift(LEFT * 2.5).scale(0.7)
        self.bin_mpt_labels = BinMPT(include_labels=True)
        texts = ["T", "R", "I", "A", "O", "K"]
        nodes = [
            self.bin_mpt.root_branch,
            self.bin_mpt.branch1,
            self.bin_mpt.branch3,
            self.bin_mpt.branch4,
            self.bin_mpt.branch2,
            self.bin_mpt.branch5,
        ]
        self.keys_on_nodes = []
        for i in range(len(texts)):
            text = texts[i]
            self.keys_on_nodes.append(
                Text(
                    text, font=PRIMARY_FONT, color=HIGHLIGHT_COLOR, font_size=20
                ).move_to(nodes[i].get_center())
            )
        leaf_texts = ["E", "N", "W", "EN"]

        leaf_nodes = [
            self.bin_mpt.leaf1,
            self.bin_mpt.leaf2,
            self.bin_mpt.leaf4,
            self.bin_mpt.leaf3,
        ]

        self.leaf_keys = []
        for i in range(len(leaf_texts)):
            text = leaf_texts[i]
            self.leaf_keys.append(
                Text(
                    text, font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=20
                ).move_to(leaf_nodes[i].get_center())
            )

        node = RoundedRectangle(
            width=5,
            height=5,
            corner_radius=0.1,
            color=PRIMARY_COLOR,
            fill_opacity=0.27,
        )
        self.node = DashedVMobject(node, num_dashes=60)

        self.key = RoundedRectangle(
            width=1.8,
            height=0.6,
            corner_radius=0.1,
            color=PRIMARY_COLOR,
            fill_opacity=0.27,
            stroke_width=0.0,
        ).next_to(node, UP, buff=0.5).align_to(node, LEFT).shift(RIGHT * 0.8 + DOWN * 1.7)

        self.value = RoundedRectangle(
            width=1,
            height=0.6,
            corner_radius=0.1,
            color=PRIMARY_COLOR,
            fill_opacity=0.27,
            stroke_width=0.0,
        ).next_to(node, UP, buff=0.5).align_to(node, RIGHT).shift(LEFT * 0.8 + DOWN * 1.7)

        self.key_text = Text(
            "Keys", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=20
        ).move_to(self.key)

        self.value_text = Text(
            "Values", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=20
        ).move_to(self.value)

        self.account_addresses = Text(
            " 0x1234...5678 \n\n\n 0x9187...2378 \n\n\n 0x1294...3894 \n\n\n 0x0319...2614 ",
            color=PRIMARY_COLOR,
            font=PRIMARY_FONT,
            font_size=18,
        ).next_to(self.key, DOWN, buff=0.35).align_to(self.key, LEFT).shift(RIGHT * 0.07)

        self.account_balances = Text(
            "7 ETH \n\n\n 9 ETH \n\n\n 1 ETH \n\n\n 7 ETH",
            color=PRIMARY_COLOR,
            font=PRIMARY_FONT,
            font_size=18,
        ).next_to(self.value, DOWN, buff=0.38).align_to(self.value, RIGHT).shift(LEFT*0.16)

        self.nodes_for_address = VGroup(*[
            self.key.copy().next_to(self.key, DOWN, buff=0.4)
            for _ in range(4)
        ]).arrange(DOWN, buff=0.13).align_to(self.key, LEFT).shift(DOWN*0.28)

        self.nodes_for_balances = VGroup(*[
            self.value.copy().next_to(self.value, DOWN, buff=0.4)
            for _ in range(4)
        ]).arrange(DOWN, buff=0.13).align_to(self.value, RIGHT).shift(DOWN * 0.28)

    def animate_in(self, scene):
        self.key_value_pairs(scene)

        self.brace_levels(scene)

    def key_value_pairs(self, scene):
        self.new_subsection(scene, "key and value", "data/sound/e6/slide2-4a.mp3")
        scene.play(Write(self.title_pt), run_time=0.7)
        table_key_value = TableKeyValue().scale(0.85)
        scene.play(Create(table_key_value))
        scene.wait(1.8)
        scene.play(
            Indicate(table_key_value.key_header, color=SECONDARY_COLOR), run_time=1
        )
        scene.play(
            Indicate(table_key_value.value_header, color=SECONDARY_COLOR), run_time=1
        )
        scene.wait(1)
        prefixes1 = [
            table_key_value.key_cells[0][1],
            table_key_value.key_cells[1][1],
            table_key_value.key_cells[2][1],
            table_key_value.key_cells[3][1],
        ]

        self.new_subsection(scene, "common prefixes", "data/sound/e6/slide2-4b.mp3")
        scene.wait(2)
        for i in range(2):
            pref1 = prefixes1[2 * i]
            pref2 = prefixes1[2 * i + 1]
            scene.play(Indicate(pref1[0:2], color=SECONDARY_COLOR), run_time=0.5)
            scene.play(Indicate(pref2[0:2], color=SECONDARY_COLOR), run_time=0.5)
            scene.wait(0.3)
        table_key_value.generate_target()
        table_key_value.target.scale(0.75).shift(RIGHT * 4.5)
        scene.wait(0.2)
        scene.play(MoveToTarget(table_key_value))
        scene.play(Create(self.bin_mpt), run_time=1)

        self.new_subsection(
            scene, "indexed along the path", "data/sound/e6/slide2-4c.mp3"
        )
        self.add_values()
        pref1 = prefixes1[0]
        pref2 = prefixes1[1]
        pref3 = prefixes1[2]
        pref4 = prefixes1[3]

        # for j in range(3):
        #     scene.play(Indicate(pref1[j], color = SECONDARY_COLOR, scale_factor=1.5), run_time=1)
        #     scene.play(Write(self.keys_on_nodes[j]), run_time=0.5)

        # T to the root
        scene.play(
            Indicate(pref1[0], color=SECONDARY_COLOR),
            Indicate(pref2[0], color=SECONDARY_COLOR),
            Indicate(pref3[0], color=SECONDARY_COLOR),
            Indicate(pref4[0], color=SECONDARY_COLOR),
            TransformMatchingShapes(
                VGroup(
                    pref3[0].copy(), pref1[0].copy(), pref2[0].copy(), pref4[0].copy()
                ),
                self.keys_on_nodes[0],
            ),
            run_time=1.9,
        )

        # R to the trie
        scene.play(
            Indicate(pref1[1], color=SECONDARY_COLOR),
            Indicate(pref2[1], color=SECONDARY_COLOR),
            TransformMatchingShapes(
                VGroup(pref1[1].copy(), pref2[1].copy()), self.keys_on_nodes[1]
            ),
            run_time=1.5,
        )

        # O to the trie
        scene.play(
            Indicate(pref3[1], color=SECONDARY_COLOR),
            Indicate(pref4[1], color=SECONDARY_COLOR),
            TransformMatchingShapes(
                VGroup(pref3[1].copy(), pref4[1].copy()), self.keys_on_nodes[4]
            ),
            run_time=1.5,
        )

        scene.play(
            Indicate(pref1[3], color=SECONDARY_COLOR),
            Indicate(pref1[2], color=SECONDARY_COLOR),
            Indicate(table_key_value.value_cells[0][1], color=SECONDARY_COLOR),
            run_time=1,
        )
        scene.play(Write(self.leaf_keys[0]), Create(self.values0), Create(self.keys_on_nodes[2]), run_time=0.3)

        scene.play(
            Indicate(pref2, color=SECONDARY_COLOR),
            Indicate(table_key_value.value_cells[1][1], color=SECONDARY_COLOR),
            run_time=1,
        )
        scene.play(
            Write(self.leaf_keys[1]),
            Write(self.keys_on_nodes[3]),
            Create(self.values1),
            run_time=0.3,
        )

        scene.play(
            Indicate(prefixes1[2], color=SECONDARY_COLOR),
            Indicate(prefixes1[3], color=SECONDARY_COLOR),
            run_time=0.8,
        )
        scene.play(
            Write(self.keys_on_nodes[4]),
            Write(self.leaf_keys[2]),
            Write(self.keys_on_nodes[5]),
            Write(self.leaf_keys[3]),
            Create(self.values3),
            Create(self.values2),
            run_time=0.3,
        )

        self.new_subsection(scene, "key and value", "data/sound/e6/slide2-5.mp3")
        scene.play(
            FadeOut(
                self.bin_mpt,
                table_key_value,
                *self.keys_on_nodes,
                *self.leaf_keys,
                *self.values,
                *self.rectangles_values
            )
        )

        self.title_state_trie = Text(
            "State Trie", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=40
        ).to_edge(UP)

        scene.play(Create(self.node), run_time=1)
        scene.play(
            Create(self.key),
            Write(self.key_text),
            TransformMatchingShapes(self.title_pt, self.title_state_trie),
            run_time=1,
        )
        scene.play(
            FadeIn(*self.nodes_for_address, self.account_addresses),
        )
        scene.wait(0.5)
        scene.play(Create(self.value), Write(self.value_text))
        scene.play(
            FadeIn(*self.nodes_for_balances, self.account_balances),
        )
        scene.wait(1)

        self.new_subsection(
            scene, "not efficient enough", "data/sound/e6/slide2-5a.mp3"
        )
        scene.play(
            FadeOut(
                self.node,
                self.key,
                self.value,
                self.key_text,
                self.value_text,
                self.account_addresses,
                self.account_balances,
                *self.nodes_for_address,
                *self.nodes_for_balances,
            )
        )

    def animate_out(self, scene):
        scene.play(FadeOut(self.title_state_trie))

    def brace_levels(self, scene):
        self.merkle_tree_binary = (
            Tree(num_levels=4, include_labels=False)
            .scale(0.5)
            .shift(UP * 3.7 + LEFT * 1)
        )
        self.dots_bin_merkle1 = (
            MathTex(r"\boldsymbol{\cdots}", color=PRIMARY_COLOR, font_size=40)
            .next_to(self.merkle_tree_binary.get_node(2, 0), DOWN, buff=1.0)
            .shift(DOWN * 0.2)
        )
        self.dots_bin_merkle2 = (
            MathTex(r"\boldsymbol{\cdots}", color=PRIMARY_COLOR, font_size=40)
            .next_to(self.merkle_tree_binary.get_node(2, 1), DOWN, buff=1.0)
            .shift(DOWN * 0.2)
        )
        self.dots_bin_merkle3 = (
            MathTex(r"\boldsymbol{\cdots}", color=PRIMARY_COLOR, font_size=40)
            .next_to(self.merkle_tree_binary.get_node(2, 2), DOWN, buff=1.0)
            .shift(DOWN * 0.2)
        )
        self.dots_bin_merkle4 = (
            MathTex(r"\boldsymbol{\cdots}", color=PRIMARY_COLOR, font_size=40)
            .next_to(self.merkle_tree_binary.get_node(2, 3), DOWN, buff=1.0)
            .shift(DOWN * 0.2)
        )
        self.merkle_tree_binary = VGroup(
            self.merkle_tree_binary,
            self.dots_bin_merkle1,
            self.dots_bin_merkle2,
            self.dots_bin_merkle3,
            self.dots_bin_merkle4,
        )
        scene.play(Create(self.merkle_tree_binary))
        self.brace_160_levels = (
            Brace(self.merkle_tree_binary, direction=RIGHT, color=PRIMARY_COLOR)
            .scale(1.2)
            .shift(DOWN * 0.3)
        )
        self.brace_text_levels160 = Text(
            "160 levels", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=20
        ).next_to(self.brace_160_levels, RIGHT, buff=0.1)

        scene.play(FadeIn(self.brace_160_levels), Write(self.brace_text_levels160))
        scene.wait(3)

        self.merkle_tree_hexary = (
            MT16(num_levels=4, focused_node_path=[7, 8, 7])
            .scale(0.6)
            .shift(UP * 4 + LEFT)
        )
        self.dots_hex_merkle = MathTex(
            r"\boldsymbol{\cdots}", color=PRIMARY_COLOR, font_size=40
        ).next_to(self.merkle_tree_hexary, DOWN, buff=0.3)

        self.brace_7_levels = (
            Brace(self.merkle_tree_hexary, direction=RIGHT, color=PRIMARY_COLOR)
            .scale(1.2)
            .shift(DOWN * 0.3)
        )
        self.brace_text_levels7 = Text(
            "40 levels", color=PRIMARY_COLOR, font=PRIMARY_FONT, font_size=20
        ).next_to(self.brace_7_levels, RIGHT, buff=0.1)
        scene.wait(3.8)

        self.new_subsection(scene, "bin->hex", "data/sound/e6/slide2-5b.mp3")
        nodes = [self.merkle_tree_hexary.get_node(1, i) for i in range(16)]
        scene.wait(1)
        scene.play(
            FadeOut(
                self.merkle_tree_binary,
                self.brace_160_levels,
                self.brace_text_levels160,
            )
        )
        scene.play(Create(self.merkle_tree_hexary), Write(self.dots_hex_merkle))
        for i in range(16):
            scene.play(Indicate(nodes[i], color=SECONDARY_COLOR), run_time=0.15)

        self.new_subsection(scene, "300m ->8 levels", "data/sound/e6/slide2-5c.mp3")
        scene.wait(1)
        scene.play(FadeIn(self.brace_7_levels), Write(self.brace_text_levels7))
        scene.wait(2)

        self.new_subsection(
            scene,
            "nice optimization but still a lot of calc",
            "data/sound/e6/slide2-5d.mp3",
        )
        scene.wait(5)
        # scene.play(
        #     *[Indicate(nodes[i], color = SECONDARY_COLOR) for i in range(16)],
        #     run_time=0.8
        # )
        # scene.wait(0.2)
        # nodes2 = [self.merkle_tree_hexary.get_node(2, i) for i in range(16)]
        # nodes3 = [self.merkle_tree_hexary.get_node(3, i) for i in range(16)]
        # scene.play(
        #     *[Indicate(nodes2[i], color = SECONDARY_COLOR) for i in range(16)],
        #     run_time=0.8
        # )
        # scene.wait(0.2)
        # scene.play(
        #     *[Indicate(nodes3[i], color = SECONDARY_COLOR) for i in range(16)],
        #     run_time=0.8
        # )
        path = [
            self.merkle_tree_hexary.get_node(1, 7),
            self.merkle_tree_hexary.get_node(2, 8),
            self.merkle_tree_hexary.get_node(3, 2),
        ]
        for node in path:
            scene.play(Indicate(node, color=SECONDARY_COLOR), run_time=1)
        scene.wait(1)

        self.play_sound(scene, "data/sound/e6/slide2-5e.mp3")
        scene.wait(2)

        scene.play(
            FadeOut(
                self.merkle_tree_hexary,
                self.brace_7_levels,
                self.brace_text_levels7,
                self.dots_hex_merkle,
            )
        )

    def add_values(self):
        rectangles_values = RoundedRectangle(
            width=0.4,
            height=0.4,
            corner_radius=0.05,
            color=PRIMARY_COLOR,
            fill_opacity=0.27,
            stroke_width=0.0,
        )
        self.rectangles_values = []
        leaves = [
            self.bin_mpt.leaf1,
            self.bin_mpt.leaf2,
            self.bin_mpt.leaf4,
            self.bin_mpt.leaf3,
        ]
        for i in range(4):
            rectangle = rectangles_values.copy().next_to(leaves[i], DOWN, buff=0.1)
            self.rectangles_values.append(rectangle)
        values = ["7", "9", "1", "7"]

        self.values = []
        for i in range(len(values)):
            text = values[i]
            self.values.append(
                Text(
                    text, font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=20
                ).move_to(self.rectangles_values[i].get_center())
            )

        self.values0 = VGroup(self.values[0], self.rectangles_values[0])
        self.values1 = VGroup(self.values[1], self.rectangles_values[1])
        self.values2 = VGroup(self.values[2], self.rectangles_values[2])
        self.values3 = VGroup(self.values[3], self.rectangles_values[3])
