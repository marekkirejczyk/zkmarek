from manim import VGroup, Text, RoundedRectangle, Create, DOWN, RIGHT, UP
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, HIGHLIGHT_COLOR


class MerkleVerkleTable(VGroup):
    def __init__(self):
        super().__init__()

        categories = [
            "node type",
            "Proof depth",
            "single value\nproof size",
            "1000 values\nproof size",
        ]

        merkle_values = [
            "Hashes",
            "~9",
            "~4 kB",
            "~4 MB",
        ]

        ipa_values = [
            "IPA commitment",
            "~4",
            "~600 B",
            "~72 kB",
        ]

        kzg_values = [
            "KZG commitment",
            "~4",
            "~200 B",
            "~109 kB",
        ]

        cell_width = 2.7
        cell_height = 0.8
        spacing = 0.1
        num_rows = len(categories)

        bg_width = (cell_width * 4) + 1.2
        bg_height = (cell_height + spacing) * num_rows + 1.2
        self.background = RoundedRectangle(
            width=bg_width,
            height=bg_height,
            corner_radius=0.3,
            color=PRIMARY_COLOR,
            fill_opacity=0.2,
            stroke_width=0.0,
        )

        headers = [
            Text("Merkle Tree", font=PRIMARY_FONT, font_size=22, color=PRIMARY_COLOR),
            Text("Verkle Tree (IPA)", font=PRIMARY_FONT, font_size=22, color=PRIMARY_COLOR),
            Text("Verkle Tree (KZG)", font=PRIMARY_FONT, font_size=22, color=PRIMARY_COLOR),
        ]

        vec_column = VGroup()
        merkle_col = VGroup()
        ipa_col = VGroup()
        kzg_col = VGroup()

        for i, (cat, m_val, ipa_val, kzg_val) in enumerate(
            zip(categories, merkle_values, ipa_values, kzg_values)
        ):
            base_y = (
                self.background.get_top()
                + self.background.get_left()
                + DOWN * (i + 1.5) * (cell_height + spacing)
                + RIGHT * 1.5
            )

            def make_cell(text, width=cell_width, color=PRIMARY_COLOR):
                cell = RoundedRectangle(
                    width=width,
                    height=cell_height,
                    corner_radius=0.07,
                    fill_opacity=0.3,
                    color=color,
                    stroke_width=0.0,
                ).move_to(base_y)
                return cell, Text(
                    text, font=PRIMARY_FONT, font_size=18, color=color
                ).move_to(cell)

            cat_cell, cat_text = make_cell(cat, color=HIGHLIGHT_COLOR)
            m_cell, m_text = make_cell(m_val)
            merkle = VGroup(m_cell, m_text)
            ipa_cell, ipa_text = make_cell(ipa_val)
            ipa = VGroup(ipa_cell, ipa_text)
            kzg_cell, kzg_text = make_cell(kzg_val)
            kzg = VGroup(kzg_cell, kzg_text)

            merkle.next_to(cat_cell, RIGHT, buff=0.3)
            ipa.next_to(m_cell, RIGHT, buff=0.3)
            kzg.next_to(ipa_cell, RIGHT, buff=0.3)

            vec_column.add(VGroup(cat_cell, cat_text))
            merkle_col.add(VGroup(m_cell, m_text))
            ipa_col.add(VGroup(ipa_cell, ipa_text))
            kzg_col.add(VGroup(kzg_cell, kzg_text))

        headers[0].next_to(merkle_col[0], UP, buff=0.4)
        headers[1].next_to(ipa_col[0], UP, buff=0.4)
        headers[2].next_to(kzg_col[0], UP, buff=0.4)

        self.headers = VGroup(*headers)
        self.merkle_col = VGroup(*merkle_col)
        self.ipa_col = VGroup(*ipa_col)
        self.kzg_col = VGroup(*kzg_col)
        self.vec = VGroup(*vec_column)

        self.add(
            self.background,
            self.headers,
            self.merkle_col,
            self.ipa_col,
            self.kzg_col,
            self.vec,
        )

    def reveal(self, scene):
        scene.play(Create(self.background))
        for group in self[1:]:
            for cell in group:
                scene.play(Create(cell), run_time=0.15)

    def reveal_header(self, scene):
        scene.play(Create(self.background), run_time=0.7)
        scene.play(Create(self.headers[0]), run_time=1)
        scene.play(Create(self.vec), run_time=1)
