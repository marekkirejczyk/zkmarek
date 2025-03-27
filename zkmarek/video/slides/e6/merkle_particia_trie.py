from manim import (
    VGroup,
    Text,
    RIGHT,
    DOWN,
    LEFT,
    UP,
    RoundedRectangle,
    StealthTip,
    Arrow,
    DashedVMobject,
    TransformMatchingShapes,
    FadeIn,
    FadeOut,
)
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, HIGHLIGHT_COLOR


class MPTNode(VGroup):
    """Base class for nodes in the Merkle Patricia Trie."""

    def __init__(
        self,
        title,
        fields,
        width=6,
        height=2,
        font_size=25,
        color=HIGHLIGHT_COLOR,
        include_labels=True,
    ):
        super().__init__()
        self.title = title
        self.fields = fields
        self.color = color
        self.rect = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.1,
            color=self.color,
            fill_opacity=0.14,
            stroke_width=0.0,
        )
        if self.title is not None:
            self.title_text = Text(
                self.title,
                font_size=font_size + 3,
                color=PRIMARY_COLOR,
                font=PRIMARY_FONT,
            ).move_to(self.rect.get_top() + 0.3 * DOWN)

        self.field_group = VGroup()
        for i, (key, value) in enumerate(self.fields.items()):
            field_rect = RoundedRectangle(
                # width=width * 0.45,
                width=3.75 * 0.45,
                height=1.2,
                color=self.color,
                stroke_width=0.0,
                fill_opacity=0.4,
                corner_radius=0.1,
            )
            field_text = Text(
                f"{key}: {value}" if include_labels else "",
                font_size=font_size,
                font=PRIMARY_FONT,
            ).move_to(field_rect.get_center())

            if self.title is not None:
                # field_rect.next_to(self.title_text, DOWN, buff = (0.2 + 0.8 * i))
                shifts = [LEFT, RIGHT]
                field_rect.next_to(self.title_text, DOWN, buff = (0.26)).shift(shifts[i] * 0.9)
                field_text.move_to(field_rect.get_center())
                self.add(self.title_text)
            else:
                shifts = [LEFT, RIGHT]
                field_rect.move_to(self.rect.get_center()).shift(shifts[i] * 0.9)
                field_text.move_to(field_rect.get_center())

            self.field_group.add(VGroup(field_rect, field_text))

        self.add(self.rect, self.field_group)


class MPTBranchNode(MPTNode):
    """Specialized class for a Branch Node with rectangular child slots."""

    def __init__(
        self,
        content,
        width=12,
        height=1.5,
        child_width=0.6,
        child_height=0.6,
        font_size=24,
        color=HIGHLIGHT_COLOR,
        include_labels=True,
    ):
        super().__init__(
            "Branch Node", {}, width=width, height=height, font_size=font_size
        )

        self.child_slots = VGroup()
        self.child_slot_map = {}
        self.color = color

        for i, value in enumerate(content.keys()):
            slot = RoundedRectangle(
                width=child_width,
                height=child_height,
                corner_radius=0.1,
                color=self.color,
                fill_opacity=0.4,
                stroke_width=0.0,
            )
            label = Text(
                str(value) if include_labels else "",
                font_size=font_size,
                font=PRIMARY_FONT,
            ).move_to(slot.get_center())
            slot_group = VGroup(slot, label)

            self.child_slot_map[value] = slot_group
            self.child_slots.add(slot_group)

        self.child_slots.arrange(RIGHT, buff=0.15).move_to(
            self.rect.get_center()
        ).shift(DOWN * 0.2)
        self.add(self.child_slots)

        if self.title is not None:
            self.add(self.title_text)

    def get_child_slot(self, value):
        """Retrieve a specific child slot by its label (e.g., '4')."""
        return self.child_slot_map.get(str(value), None)


class MerklePatriciaTrie(VGroup):
    """Class to create and animate a Merkle Patricia Trie."""

    def __init__(self, include_labels=True):
        super().__init__()
        self.root = MPTNode(
            "Root: extension node",
            {"key-part": "\n      a7", " next\n node": ""},
            include_labels=include_labels,
            width=4.0,
        )

        values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        self.branch1 = MPTBranchNode({i: "" for i in values}, include_labels=include_labels)
        self.leaf_replace = MPTNode(
            title=None,
            fields={"    key": "\na711355", "   value": "\n 45.0 ETH"},
            color=PRIMARY_COLOR,
            width=3.75,
            include_labels=include_labels,
        )
        self.leaf2_replace = MPTNode(
            title=None,
            fields={"   key": "\na7f9365", "  value": "\n 1.0 WEI"},
            color=PRIMARY_COLOR,
            width=3.75,
            include_labels=include_labels,
        )
        self.leaf2_replace2 = MPTNode(
            title=None,
            fields={"key-end": "\n   f9365", "  value": "\n 1.0 WEI"},
            color=PRIMARY_COLOR,
            width=3.75,
            include_labels=include_labels,
        )
        self.extension2 = MPTNode(
            "Extension Node",
            {"key-part": "\n     d3", " next\n node": ""},
            include_labels=include_labels,
            width=3.75,
        )
        self.leaf2 = MPTNode(
            "Leaf Node",
            {"key-end": "\n   9365", " value": "\n1.1 ETH"},
            color=PRIMARY_COLOR,
            width=3.5,
            include_labels=include_labels,
        )
        self.branch2 = MPTBranchNode(
            {i: "" for i in values}, include_labels=include_labels
        )
        self.leaf3 = MPTNode(
            "Leaf Node",
            {"key-end": "\n      7", "  value": "\n0.12 ETH"},
            color=PRIMARY_COLOR,
            width=3.5,
            include_labels=include_labels,
        )
        self.leaf4 = MPTNode(
            "Leaf Node",
            {"key-end": "\n      7", "  value": "\n1.00 WEI"},
            color=PRIMARY_COLOR,
            width=3.5,
            include_labels=include_labels,
        )
        self.leaf_replace2 = MPTNode(
            title=None,
            fields={"key-end": "\n  11335", "  value": "\n45.0 ETH"},
            color=PRIMARY_COLOR,
            width=3.5,
            include_labels=include_labels,
        )
        self.leaf1 = MPTNode(
            "Leaf Node",
            {"key-end": "\n   1335", "  value": "\n45.0 ETH"},
            color=PRIMARY_COLOR,
            width=3.5,
            include_labels=include_labels,
        )
        self.root.move_to(2 * UP)
        self.branch1.next_to(self.root, DOWN, buff=0.7)
        self.leaf1.next_to(self.branch1.get_child_slot("1"), DOWN, buff=0.9)
        self.leaf_replace.next_to(self.branch1.get_child_slot("1"), DOWN, buff=0.7)
        self.leaf_replace2.next_to(self.branch1.get_child_slot("1"), DOWN, buff=0.7)
        self.extension2.next_to(self.branch1, DOWN, buff=0.7)
        self.leaf2.next_to(self.branch1.get_child_slot("f"), DOWN, buff=0.9)
        self.leaf2_replace.next_to(self.branch1.get_child_slot("f"), DOWN, buff=0.85)
        self.leaf2_replace2.next_to(self.branch1.get_child_slot("f"), DOWN, buff=0.85)
        self.branch2.next_to(self.extension2, DOWN, buff=0.7)
        self.leaf3.next_to(self.branch2.get_child_slot("3"), DOWN, buff=0.85)
        self.leaf4.next_to(self.branch2.get_child_slot("8"), DOWN, buff=0.85)

        self.arrow = create_arrow(
            end=self.root.field_group[1].get_bottom(), start=self.root.field_group[1].get_bottom() + DOWN * 0.8
        )
        self.arrow2 = create_arrow(
            end=self.branch1.get_child_slot("1").get_bottom(),
            start=self.branch1.get_child_slot("1").get_bottom() + DOWN * 0.85,
        )

        self.arrow3 = create_arrow(
            end=self.branch1.get_child_slot("7").get_bottom(),
            start=self.branch1.get_child_slot("7").get_bottom() + DOWN * 0.85,
        )
        self.arrow4 = create_arrow(
            end=self.branch1.get_child_slot("f").get_bottom(),
            start=self.leaf2.get_top(),
        )

        self.arrow5 = create_arrow(
            end=self.extension2.field_group[1].get_bottom(),
            start=self.extension2.field_group[1].get_bottom() + DOWN * 0.8,
        )
        self.arrow6 = create_arrow(
            end=self.branch2.get_child_slot("3").get_bottom(),
            start=self.leaf3.get_top(),
        )
        self.arrow7 = create_arrow(
            end=self.branch2.get_child_slot("8").get_bottom(),
            start=self.leaf4.get_top(),
        ).shift(UP * 0.01)

        self.add(
            self.root,
            self.branch1,
            self.leaf1,
            self.extension2,
            self.leaf2,
            self.branch2,
            self.leaf3,
            self.leaf4,
        )
        self.add(
            self.arrow,
            self.arrow2,
            self.arrow3,
            self.arrow4,
            self.arrow5,
            self.arrow6,
            self.arrow7,
        )

    def replace_leaf1(self, scene):
        self.leaf_replace2.move_to(self.leaf_replace.get_center())
        scene.play(
            FadeOut(self.leaf_replace), FadeIn(self.leaf_replace2), run_time=1
        )

    def replace_leaf2(self, scene):
        self.leaf1.move_to(self.leaf_replace2.get_center())
        scene.play(TransformMatchingShapes(self.leaf_replace2, self.leaf1), run_time=1)

    def replace_2leaf(self, scene):
        self.leaf2_replace2.move_to(self.leaf2_replace.get_center())
        scene.play(
            FadeOut(self.leaf2_replace), FadeIn(self.leaf2_replace2), run_time=1
        )

    def replace_2leaf2(self, scene):
        self.leaf2.move_to(self.leaf2_replace2.get_center())
        scene.play(
            TransformMatchingShapes(self.leaf2_replace2, self.leaf2), run_time=1
        )

def create_arrow(start, end, stroke_width=1.8, dash_density=8):
    arrow = Arrow(
        start=end,
        end=start + UP * 0.1,
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
