from manim import (
    FadeIn,
    FadeOut,
    Arrow,
    Text,
    StealthTip,
    DashedVMobject,
    UP,
    LEFT,
    RoundedRectangle,
    DOWN,
    VGroup,
    RIGHT,
    Write,
    Create,
    Indicate,
    MoveToTarget,
    Group,
    TransformMatchingShapes,
    Polygon,
    ImageMobject,
)
from zkmarek.video.constant import (
    SECONDARY_COLOR,
    PRIMARY_COLOR,
    PRIMARY_FONT,
    HIGHLIGHT_COLOR,
)
from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.slides.e6.tree import MerkleTree as Tree
from zkmarek.video.slides.e6.merkle_particia_trie import MerklePatriciaTrie as MPT
from zkmarek.video.slides.e6.ethereum_block import EthereumBlock
from zkmarek.video.slides.e6.proof_sizes import ProofSize
from zkmarek.video.slides.e6.merkle import MerkleTree


class Recap(SlideBase):
    def __init__(self) -> None:
        super().__init__("Recap of previous episodes")

    def construct(self):
        self.title_label = Text(
            "Previously on zkMarek...",
            font=PRIMARY_FONT,
            color=PRIMARY_COLOR,
            font_size=40,
        ).to_edge(UP)

    def animate_in(self, scene):
        self.new_subsection(scene, "Merkle trees", "data/sound/e7/slide1-0.mp3")
        scene.play(Write(self.title_label), run_time=0.7)
        self.merkle_tree(scene)

        self.new_subsection(scene, "four MPTs", "data/sound/e7/slide1-1.mp3")
        self.block_tries(scene)

        self.new_subsection(
            scene, "efficient lookups", "data/sound/e7/slide1-4.mp3"
        )
        self.merkle_patricia_trie(scene)

        self.new_subsection(
            scene, "proof size: 9 levels", "data/sound/e7/slide1-5.mp3"
        )
        self.proof_sizes(scene)

        self.new_subsection(
            scene, "more efficient?", "data/sound/e7/slide1-10.mp3"
        )
        self.efficient_kzg(scene)

    def merkle_tree(self, scene):
        self.merkle_tree_2_4 = (
            Tree(num_children=2, num_levels=4, include_labels=False)
            .shift(UP * 4)
            .scale(0.56)
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
        self.account_group_8_elements = VGroup(
            *self.account_vector_rectangles_8_elements
        ).arrange(RIGHT, buff=0.2)
        for i in range(8):
            self.account_group_8_elements[i].next_to(
                self.merkle24_nodes_level3[i], DOWN, buff=0.3
            )
        for i in range(8):
            scene.play(
                Create(self.account_group_8_elements[i]),
                run_time=0.07,
            )
        scene.wait(1.5)
        scene.play(Create(self.merkle_tree_2_4), run_time=2)
        scene.wait(2)

    def block_tries(self, scene):
        self.slide_block = EthereumBlock()
        self.slide_block.construct()
        self.block = self.slide_block.block_header_whole

        scene.play(
            FadeOut(self.merkle_tree_2_4, self.account_group_8_elements), run_time=0.5
        )
        scene.play(FadeIn(self.block), run_time=0.7)
        scene.wait(1.5)
        scene.play(*[Indicate(trie, color=SECONDARY_COLOR) for trie in self.slide_block.tries], run_time = 1.0)
        scene.wait(0.3)
        for i in range(0, 4):
            scene.play(
                Indicate(self.slide_block.tries[i], color=HIGHLIGHT_COLOR),
                run_time=0.8,
            )
            scene.wait(0.2)
        self.block.generate_target()
        self.block.target.scale(0.5).shift(UP*1.5)
        scene.play(MoveToTarget(self.block), run_time=1)

        self.new_subsection(scene, "key value", "data/sound/e7/slide1-2.mp3")
        self.key_value(scene)

        self.new_subsection(
            scene,
            "state trie: acc balanaces, nonces...",
            "data/sound/e7/slide1-3.mp3",
        )
        self.create_state_trie()

        scene.play(Create(self.state_trie), run_time=1)

        self.account_balance_node = RoundedRectangle(
            width=3,
            height=0.5,
            corner_radius=0.1,
            color=HIGHLIGHT_COLOR,
            fill_opacity=0.15,
            stroke_width=0.0,
        )
        self.account_balance_node.move_to(self.nodes[5]).shift(RIGHT * 1.5)

        address_rectangle = RoundedRectangle(
            width=1.3,
            height=0.4,
            corner_radius=0.1,
            color=HIGHLIGHT_COLOR,
            fill_opacity=0.25,
            stroke_width=0.0,
        )
        address_rectangle.move_to(self.account_balance_node.get_center()).shift(
            LEFT * 0.75
        )
        address_text = Text(
            "address", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=18
        ).move_to(address_rectangle.get_center())
        self.address = VGroup(address_rectangle, address_text)

        balance_rectangle = RoundedRectangle(
            width=1.3,
            height=0.4,
            corner_radius=0.1,
            color=HIGHLIGHT_COLOR,
            fill_opacity=0.25,
            stroke_width=0.0,
        )
        balance_rectangle.move_to(self.account_balance_node.get_center()).shift(
            RIGHT * 0.75
        )
        balance_text = Text(
            "balance", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=18
        ).move_to(balance_rectangle.get_center())
        self.balance = VGroup(balance_rectangle, balance_text)

        self.acc_balance_node = VGroup(
            self.balance, self.address, self.account_balance_node
        )

        scene.play(FadeOut(self.nodes[5]), FadeIn(self.acc_balance_node))
        self.block_and_state_trie = Group(
            self.block,
            self.acc_balance_node,
            self.arrows1,
            self.nodes_wo_5,
        )
        self.block_and_state_trie.generate_target()
        self.block_and_state_trie.target.shift(LEFT * 0.5)

        self.rectangle_state_trie = RoundedRectangle(
            width=5.9,
            height=0.5,
            corner_radius=0.1,
            color=HIGHLIGHT_COLOR,
            fill_opacity=0.15,
            stroke_width=0.0,
        )

        scene.play(Indicate(self.address, color = SECONDARY_COLOR, scale_factor=1.1), run_time=0.9)
        scene.play(MoveToTarget(self.block_and_state_trie), run_time=1)
        self.rectangle_state_trie.move_to(self.nodes[5]).shift(RIGHT * 1.5)
        labels_state_trie = ["Nonce", "Balance", "Code Hash", "Storage root"]
        self.labels_state_trie = VGroup()
        self.rectangles_state_trie = Group()
        rectangle_all = RoundedRectangle(
            width=1.05,
            height=0.4,
            corner_radius=0.1,
            color=HIGHLIGHT_COLOR,
            fill_opacity=0.25,
            stroke_width=0.0,
        )
        rectangle_storage = RoundedRectangle(
            width=1.55,
            height=0.4,
            corner_radius=0.1,
            color=HIGHLIGHT_COLOR,
            fill_opacity=0.25,
            stroke_width=0.0,
        )

        for i, label in enumerate(labels_state_trie):
            if i == 0:
                rectangle = (
                    rectangle_all.copy()
                    .move_to(self.rectangle_state_trie.get_center())
                    .shift(LEFT * 2.27)
                )
            elif i < 2:
                rectangle = rectangle_all.copy().next_to(
                    self.rectangles_state_trie[i - 1], RIGHT, buff=0.13
                )
            elif i > 1:
                rectangle = rectangle_storage.copy().next_to(
                    self.rectangles_state_trie[i - 1], RIGHT, buff=0.13
                )

            label_text = Text(
                label, font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=16
            ).move_to(rectangle.get_center())
            self.rectangles_state_trie.add(rectangle)
            self.labels_state_trie.add(label_text)
        self.array_4_item = Group(
            self.rectangles_state_trie,
            self.labels_state_trie,
            self.rectangle_state_trie,
        )
        scene.play(FadeOut(self.acc_balance_node), FadeIn(self.array_4_item))
        scene.play(
            Indicate(self.labels_state_trie[1], color=SECONDARY_COLOR, scale_factor=1.2)
        )
        scene.play(
            Indicate(self.labels_state_trie[0], color=SECONDARY_COLOR, scale_factor=1.2)
        )
        scene.play(
            Indicate(self.labels_state_trie[2], color=SECONDARY_COLOR, scale_factor=1.2)
        )
        scene.play(
            Indicate(self.labels_state_trie[3], color=SECONDARY_COLOR, scale_factor=1.2)
        )
        self.create_storage_trie(scene)

        scene.play(
            FadeOut(
                self.nodes_wo_5,
                self.storage_trie,
                self.block,
                self.arrows1,
                self.array_4_item,
            ),
            run_time=1,
        )
        
    def merkle_patricia_trie(self, scene):
        self.mpt_proof = MPT(include_labels=True).shift(UP*2.9).scale(0.45)
        scene.play(Create(self.mpt_proof), run_time=1.0)
        scene.wait(1)
        scene.play(Indicate(self.mpt_proof.leaf1.field_group[1][0], color = SECONDARY_COLOR), run_time=0.7)
        scene.play(Indicate(self.mpt_proof.leaf2.field_group[1][0], color = SECONDARY_COLOR), run_time=0.7)
        scene.play(Indicate(self.mpt_proof.leaf3.field_group[1][0], color = SECONDARY_COLOR), run_time=0.7)
        scene.play(Indicate(self.mpt_proof.leaf4.field_group[1][0], color = SECONDARY_COLOR), run_time=0.7)
        scene.wait(1)
        scene.play(Indicate(self.mpt_proof.leaf1.field_group, color = SECONDARY_COLOR), run_time=0.7)
        scene.wait(0.5)
        scene.play(Indicate(self.mpt_proof.branch1.get_child_slot("1"), color = PRIMARY_COLOR, scale_factor=1.5), run_time=0.8)
        scene.play(Indicate(self.mpt_proof.root.field_group[1][0], color = PRIMARY_COLOR, scale_factor=1.5), run_time=0.8)
        scene.wait(2.5)
        scene.play(FadeOut(self.mpt_proof), run_time=1.0)

    def proof_sizes(self, scene):
        self.slide_proof = ProofSize()
        self.slide_proof.construct()

        scene.play(
            Create(self.slide_proof.merkle_tree),
            FadeIn(self.slide_proof.dots),
            run_time=1.5,
        )
        scene.wait(1)
        scene.play(
            FadeIn(self.slide_proof.brace_levels, self.slide_proof.levels_text),
            run_time=0.7,
        )
        scene.wait(1)
        self.slide_proof.formula.scale(0.8).next_to(self.slide_proof.merkle_tree, RIGHT, buff=0.2)
        self.slide_proof.formula1.next_to(self.slide_proof.merkle_tree, RIGHT, buff=1.0)
        self.slide_proof.formula2.next_to(self.slide_proof.merkle_tree, RIGHT, buff=1.0)
        self.slide_proof.formula3.next_to(self.slide_proof.merkle_tree, RIGHT, buff=0.5)
        scene.play(
            Write(self.slide_proof.formula),
            FadeOut(self.slide_proof.brace_levels, self.slide_proof.levels_text),
            run_time=0.7,
        )
        scene.play(
            TransformMatchingShapes(self.slide_proof.formula, self.slide_proof.formula1)
        )
        scene.wait(1)

        self.new_subsection(scene, "4 kB", "data/sound/e7/slide1-6.mp3")
        scene.wait(1)
        scene.play(
            TransformMatchingShapes(
                self.slide_proof.formula1, self.slide_proof.formula2
            )
        )
        scene.wait(1)

        self.new_subsection(scene, "4 MB", "data/sound/e7/slide1-7.mp3")
        scene.wait(1)
        scene.play(
            TransformMatchingShapes(
                self.slide_proof.formula2, self.slide_proof.formula3
            )
        )
        scene.wait(1)

        self.new_subsection(scene, "a lot", "data/sound/e7/slide1-8.mp3")
        scene.wait(1)

        self.new_subsection(scene, "watch full", "data/sound/e7/slide1-9.mp3")
        scene.play(
            FadeOut(
                self.slide_proof.merkle_tree,
                self.slide_proof.dots,
                self.slide_proof.formula3,
            ),
            run_time=0.5,
        )
        self.miniature_merkle(scene)
        
    def key_value(self, scene):
        node = RoundedRectangle(width = 4.2, height = 2.4, corner_radius=0.1, fill_opacity = 0.4).set_color(HIGHLIGHT_COLOR)
        node = DashedVMobject(node, num_dashes=60).next_to(self.block, DOWN, buff = 0.3)
        key = RoundedRectangle(width = 1.75, height = 1, corner_radius=0, fill_opacity = 0.3).set_color(SECONDARY_COLOR)
        key = DashedVMobject(key, num_dashes=30).align_to(node, LEFT).shift(DOWN*1.5+RIGHT*0.2)
        value = RoundedRectangle(width = 1.75, height = 1, corner_radius=0.1, fill_opacity = 0.3).set_color(PRIMARY_COLOR)
        value = DashedVMobject(value, num_dashes=30).align_to(node, RIGHT).shift(DOWN*1.5+LEFT*0.2)
        
        key_text = Text("key", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=20).move_to(key.get_center())
        value_text = Text("value", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=20).move_to(value.get_center())
        self.key_value_pair = VGroup(node, key, value, key_text, value_text)
        scene.play(Create(self.key_value_pair), run_time=1)
        scene.wait(2)
        scene.play(
            FadeOut(self.key_value_pair))

    def create_state_trie(self):
        node1_0 = RoundedRectangle(
            corner_radius=0.15,
            height=0.5,
            width=0.5,
            color=HIGHLIGHT_COLOR,
            fill_opacity=0.25,
            stroke_width=0.0,
        )
        node1_0.next_to(self.slide_block.tries[0], LEFT + DOWN, buff=0.8)

        node1_1 = node1_0.copy()
        node1_1.next_to(self.slide_block.tries[0], RIGHT + DOWN, buff=0.8)

        node2_0 = node1_0.copy()
        node2_0.next_to(node1_0, DOWN + LEFT, buff=0.8).shift(RIGHT * 0.5)

        node2_1 = node1_0.copy()
        node2_1.next_to(node1_0, DOWN + RIGHT, buff=0.8).shift(LEFT * 0.5)

        node2_2 = node1_0.copy()
        node2_2.next_to(node1_1, DOWN + LEFT, buff=0.8).shift(RIGHT * 0.5)

        node2_3 = node1_0.copy()
        node2_3.next_to(node1_1, DOWN + RIGHT, buff=0.8).shift(LEFT * 0.5)

        self.nodes = VGroup(node1_0, node1_1, node2_0, node2_1, node2_2, node2_3)
        self.nodes_wo_5 = VGroup(node1_0, node1_1, node2_0, node2_1, node2_2)

        arrow1 = create_arrow(self.slide_block.tries[0], node1_0, add_down_shift=True)
        arrow2 = create_arrow(self.slide_block.tries[0], node1_1, add_down_shift=True)

        arrow3 = create_arrow(node1_0, node2_0)
        arrow4 = create_arrow(node1_0, node2_1)

        arrow5 = create_arrow(node1_1, node2_2)
        arrow6 = create_arrow(node1_1, node2_3)

        self.arrows1 = VGroup(arrow1, arrow2, arrow3, arrow4, arrow5, arrow6)

        self.state_trie = VGroup(self.nodes, self.arrows1)

    def create_storage_trie(self, scene):
        node1_0 = RoundedRectangle(
            corner_radius=0.12,
            height=0.3,
            width=0.3,
            color=HIGHLIGHT_COLOR,
            fill_opacity=0.25,
            stroke_width=0.0,
        )
        node1_0.next_to(self.labels_state_trie[3], LEFT + DOWN, buff=0.2).shift(
            RIGHT * 0.6 + DOWN * 0.3
        )

        node1_1 = node1_0.copy()
        node1_1.next_to(self.labels_state_trie[3], RIGHT + DOWN, buff=0.2).shift(
            LEFT * 0.6 + DOWN * 0.3
        )

        node2_0 = node1_0.copy()
        node2_0.next_to(node1_0, DOWN + LEFT, buff=0.2).shift(RIGHT * 0.2)

        node2_1 = node1_0.copy()
        node2_1.next_to(node1_0, DOWN + RIGHT, buff=0.2).shift(LEFT * 0.2)

        node2_2 = node1_0.copy()
        node2_2.next_to(node1_1, DOWN + LEFT, buff=0.2).shift(RIGHT * 0.2)

        node2_3 = node1_0.copy()
        node2_3.next_to(node1_1, DOWN + RIGHT, buff=0.2).shift(LEFT * 0.2)

        self.nodes = VGroup(node1_0, node1_1, node2_0, node2_1, node2_2, node2_3)

        arrow1 = create_arrow(
            self.labels_state_trie[3], node1_0, dash_density=15, add_down_shift=True
        )
        arrow2 = create_arrow(
            self.labels_state_trie[3], node1_1, dash_density=15, add_down_shift=True
        )

        arrow3 = create_arrow(node1_0, node2_0, dash_density=15)
        arrow4 = create_arrow(node1_0, node2_1, dash_density=15)

        arrow5 = create_arrow(node1_1, node2_2, dash_density=15)
        arrow6 = create_arrow(node1_1, node2_3, dash_density=15)

        self.arrows = VGroup(arrow1, arrow2, arrow3, arrow4, arrow5, arrow6)

        self.storage_trie = VGroup(self.nodes, self.arrows)
        scene.play(Create(self.storage_trie), run_time=1.5)
        scene.wait(0.5)
        for i in range(4):
            scene.play(Indicate(self.nodes[i], color = SECONDARY_COLOR), run_time=0.5)
        scene.wait(1)
        
    def miniature_merkle(self, scene):
        self.slide_merkle = MerkleTree()
        self.slide_merkle.construct()
        self.slide_merkle.animate_miniature(scene)
        
    def efficient_kzg(self, scene):
        question_mark = Text("?", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size=50)
        scene.play(Write(question_mark), run_time = 1)
        scene.wait(1)
        
        self.new_subsection(
            scene, "vector commitment!", "data/sound/e7/slide1-11.mp3"
        )
        scene.play(FadeOut(question_mark), run_time = 0.5)
        envelope = RoundedRectangle(width = 8 * 0.3, height = 2 * 0.3, fill_opacity = 0.3, stroke_width = 0.0, corner_radius=0.1).set_color(PRIMARY_COLOR)
        envelope_flap_closed = Polygon(
            [-4, 1, 0],
            [4, 1, 0],
            [0, -0.6, 0],
            fill_color=HIGHLIGHT_COLOR,
            fill_opacity=0.2,
        ).scale(0.3).shift(DOWN*0.1)
        kzg = Text("kzg", font=PRIMARY_FONT, color=PRIMARY_COLOR, font_size=40).move_to(envelope.get_center())
        envelope = VGroup(envelope, envelope_flap_closed, kzg).shift(LEFT*2+UP)
        person = ImageMobject("data/images/person.png").scale(0.7).shift(LEFT*3)
        person2 = ImageMobject("data/images/person_blue.png").scale(0.7).shift(RIGHT*3)
        scene.play(FadeIn(person), FadeIn(person2))

        self.new_subsection(
            scene, "kzg-> vec commitment", "data/sound/e7/slide1-12.mp3"
        )
        scene.play(Create(envelope), run_time=1)
        envelope.generate_target()
        envelope.target.shift(4*RIGHT)
        scene.play(MoveToTarget(envelope), run_time=1)
        scene.wait(1)
        scene.play(FadeOut(envelope), FadeOut(person), FadeOut(person2))
        scene.wait(1)
        
        self.new_subsection(scene, "lets recap", "data/sound/e7/slide1-13.mp3")



def create_arrow(start, end, stroke_width=1.8, dash_density=4.5, add_down_shift=False):
    if add_down_shift:
        arrow = Arrow(
            start=start.get_bottom() + DOWN * 0.1,
            end=end.get_top(),
            color=PRIMARY_COLOR,
            buff=0,
            max_tip_length_to_length_ratio=0.1,
            stroke_width=stroke_width,
            tip_shape=StealthTip,
            tip_length=0.15,
        )
    else:
        arrow = Arrow(
            start=start.get_bottom(),
            end=end.get_top(),
            color=PRIMARY_COLOR,
            buff=0,
            max_tip_length_to_length_ratio=0.1,
            stroke_width=stroke_width,
            tip_shape=StealthTip,
            tip_length=0.15,
        )

    arrow_length = arrow.get_length()

    num_dashes = max(2, int(arrow_length * dash_density))

    return DashedVMobject(arrow, num_dashes=num_dashes)
