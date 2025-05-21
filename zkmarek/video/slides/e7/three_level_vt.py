from manim import (Write, UP, Text, FadeOut, RoundedRectangle, VGroup, Create, MoveToTarget, Indicate, 
                   ChangeDecimalToValue, DecimalNumber, TransformMatchingShapes, Arrow, DOWN, LEFT, RIGHT,
                   Brace, MathTex, FadeIn, StealthTip)

from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR, HIGHLIGHT_COLOR

class ThreeLevelVerkleTree(SlideBase):
    def __init__(self) -> None:
        super().__init__("Three-level Verkle tree")
        
    def construct(self):
        self.title_label = (
            Text(
                "Multi-level Verkle tree",
                font=PRIMARY_FONT,
                color=PRIMARY_COLOR,
                font_size=40,
            )
            .to_edge(UP)
        )
        rectangle = RoundedRectangle(corner_radius=0.1, width = 0.5, height = 0.5, fill_opacity = 0.25,  stroke_width = 0.0).set_color(SECONDARY_COLOR)
        
        self.internal_node = [rectangle.copy().scale(2.4) for _ in range(3)]
        self.internal_node = VGroup(*self.internal_node).arrange(RIGHT, buff = 0.15).shift(DOWN * 3)
        self.internal_node2 = [rectangle.copy().scale(1.2) for _ in range(3)]
        self.internal_node2 = VGroup(*self.internal_node2).arrange(RIGHT, buff = 0.15).shift(DOWN*1.7+RIGHT*1)
        
        txs = [r"a0", r"...", r"a255"]
        txs2 = [r"FF0", r"...", r"FF255"]
        self.node1_texts = [Text(txs[i], font=PRIMARY_FONT, font_size=20, color=PRIMARY_COLOR).move_to(self.internal_node[i]) for i in range(len(txs))]
        self.node2_texts = [Text(txs2[i], font=PRIMARY_FONT, font_size=10, color=PRIMARY_COLOR).move_to(self.internal_node2[i]) for i in range(len(txs))]
        self.node1_texts = VGroup(*self.node1_texts)
        self.node2_texts = VGroup(*self.node2_texts)
        
        for i in range(len(self.node1_texts)):
            node = self.internal_node[i]
            node.move_to(self.internal_node[i])
            node2 = self.internal_node2[i]
            node2.move_to(self.internal_node2[i])
            
        self.commitment_to_C0 = rectangle.copy().scale(3).set_color(HIGHLIGHT_COLOR).next_to(self.internal_node, UP, buff = 0.8).shift(UP*0.5)
        self.commitment_to_C255 = rectangle.copy().scale(1.5).set_color(HIGHLIGHT_COLOR).next_to(self.internal_node2, UP, buff = 0.65)
        
        self.commitment_to_c0_text = Text(r"C0", font=PRIMARY_FONT, font_size=40, color=PRIMARY_COLOR).move_to(self.commitment_to_C0.get_center())
        self.commitment_to_c255_text = Text(r"C255", font=PRIMARY_FONT, font_size=20, color=PRIMARY_COLOR).move_to(self.commitment_to_C255.get_center())
        self.commitment_255 = VGroup(self.commitment_to_C255, self.commitment_to_c255_text)
        
        self.arrows_C0 = []
        for rectangle in self.internal_node:
            self.create_arrow(self.commitment_to_C0, rectangle, self.arrows_C0)    
        
        self.arrows_C255 = []
        for rectangle in self.internal_node2:
            self.create_arrow(self.commitment_to_C255, rectangle, self.arrows_C255)
        self.internal_node2_whole = VGroup(self.internal_node2, self.node2_texts,
                                          self.commitment_255,
                                          *self.arrows_C255)
        
        self.commitment_cdots = rectangle.copy().scale(1.2).set_color(HIGHLIGHT_COLOR)
        self.commitment_to_cdots_text = Text(r"...", font=PRIMARY_FONT, font_size=20, color=PRIMARY_COLOR).move_to(self.commitment_cdots.get_center())
        
        self.commitmentcdots = VGroup(self.commitment_cdots, self.commitment_to_cdots_text)
        self.rectangle_node_commitments = RoundedRectangle(corner_radius=0.1, width = 3.5, height = 1, fill_opacity = 0.15, stroke_width = 0.0).set_color(HIGHLIGHT_COLOR)
        self.rectangle_node_commitments.move_to(self.commitment_to_cdots_text.get_center())
        
        
        self.commitment_to_ec_values = Text("commitment to EC points?", font=PRIMARY_FONT, font_size=20, color=PRIMARY_COLOR)
        
        self.hashaes_of_commitments_rec = [rectangle.copy().scale(1.2).set_color(PRIMARY_COLOR) for _ in range(3)]
        self.hashaes_of_commitments_rec = VGroup(*self.hashaes_of_commitments_rec).arrange(RIGHT, buff = 0.5)
        iss = ["0", "...", "255"]
        self.text_hashes_of_commitments = [Text(f"H(C{iss[i]})", font=PRIMARY_FONT, font_size=14, color=PRIMARY_COLOR).move_to(self.hashaes_of_commitments_rec[i]) for i in range(len(self.hashaes_of_commitments_rec))]
        self.hashaes_of_commitments = VGroup(*self.hashaes_of_commitments_rec, *self.text_hashes_of_commitments)
        
        tilde = Text("~", font_size=30, color=PRIMARY_COLOR)
        
        self.commitment_C01_rec = rectangle.copy().scale(1.2).set_color(HIGHLIGHT_COLOR)
        self.commiemtnt_c01_text = Text(r"C0", font=PRIMARY_FONT, font_size=20, color=PRIMARY_COLOR).move_to(self.commitment_C01_rec.get_center())
        tilde2 = tilde.copy().scale(1.2).move_to(self.commiemtnt_c01_text.get_top()).shift(UP*0.1)
        self.commiemtnt_c01_text = VGroup(self.commiemtnt_c01_text, tilde2)
        self.commitment_C01 = VGroup(self.commitment_C01_rec, self.commiemtnt_c01_text)
        
        self.other_commitments = [rectangle.copy().scale(1.2).set_color(HIGHLIGHT_COLOR) for _ in range(2)]
        self.other_commitments = VGroup(*self.other_commitments).arrange(RIGHT, buff = 2.0)
        self.text_other_commitments = [Text(f"C{iss[i+1]}", font=PRIMARY_FONT, font_size=20, color=PRIMARY_COLOR).move_to(self.other_commitments[i]) for i in range(len(self.other_commitments))]
        for i in range(len(self.text_other_commitments)):
            tilde3 = tilde.copy().scale(1.2).move_to(self.text_other_commitments[i].get_top()).shift(UP*0.1)
            self.text_other_commitments[i] = VGroup(self.text_other_commitments[i], tilde3)
        self.other_commitments.add(*self.text_other_commitments)
        self.text_other_commitments = VGroup(*self.text_other_commitments)
        
        self.other_hashes_rec = [rectangle.copy().stretch(1, 2).scale(1.2).set_color(PRIMARY_COLOR) for _ in range(3)]
        self.other_hashes_rec = VGroup(*self.other_hashes_rec).arrange(RIGHT, buff = 2.0)
        self.text_other_hashes = [Text(f"H(C{iss[i]})", font=PRIMARY_FONT, font_size=14, color=PRIMARY_COLOR).move_to(self.other_hashes_rec[i]) for i in range(len(self.other_hashes_rec))]
        for i in range(len(self.text_other_hashes)):
            tilde4 = tilde.copy().move_to(self.text_other_hashes[i].get_top()).shift(UP*0.1)
            self.text_other_hashes[i] = VGroup(self.text_other_hashes[i], tilde4)
        
        self.other_hashes = VGroup(*self.other_hashes_rec, *self.text_other_hashes)
        
        self.final_parent_node_rec = rectangle.copy().scale(2).set_color(SECONDARY_COLOR)
        self.final_parent_node_text = Text(r"C", font=PRIMARY_FONT, font_size=30, color=SECONDARY_COLOR).move_to(self.final_parent_node_rec.get_center())
        self.final_parent_node = VGroup(self.final_parent_node_rec, self.final_parent_node_text)
        
        self.values256 = MathTex(r"256 \  \mathrm{values}", font_size=45, color = PRIMARY_COLOR)
        
        self.single_commitment = Text("a sinlge commitment has...", font=PRIMARY_FONT, font_size=20, color=PRIMARY_COLOR)
        self.three_level = Text("so three level...", font=PRIMARY_FONT, font_size=20, color=PRIMARY_COLOR)
        self.four_level = Text("and four level...", font=PRIMARY_FONT, font_size=20, color=PRIMARY_COLOR)
        
        self.values2_to_8 = MathTex(r"256 = {{2^8}}", font_size=45, color = PRIMARY_COLOR)
        self.values2_to_24 = MathTex(r"({{256}})^3 = ({{2^8}})^3 = {{2^{24}}}", font_size=45, color = PRIMARY_COLOR)
        self.values2_to_24 = MathTex(r"({{256}})^3 = ({{2^8}})^3 = {{2^{24}}}", font_size=45, color = PRIMARY_COLOR)
        self.values_four_level = MathTex(r"({{256}})^3 = ({{2^8}})^3 = {{2^{24}}} = {{...}}", color = PRIMARY_COLOR)
        
        hashes_copy_recs = [rectangle.copy().scale(1.2).set_color(PRIMARY_COLOR) for _ in range(3)]
        self.hashes_copy_recs = VGroup(*hashes_copy_recs).arrange(RIGHT, buff = 0.5)
    
        commitments_copy_recs = [rectangle.copy().scale(1.2).set_color(HIGHLIGHT_COLOR) for _ in range(3)]
        self.commitments_copy_recs = VGroup(*commitments_copy_recs).arrange(RIGHT, buff = 0.5).next_to(self.hashes_copy_recs, DOWN, buff = 0.1)
        
        self.rectangle_with_hashes = RoundedRectangle(corner_radius=0.1, width = 3.5, height = 1.9, fill_opacity = 0.15, stroke_width = 0.0).set_color(HIGHLIGHT_COLOR)
        self.rectangle_node_commitments2 = self.rectangle_with_hashes.copy().set_color(HIGHLIGHT_COLOR).move_to(self.commitments_copy_recs.get_center()).shift(UP * 0.45)
        
        values = self.internal_node2.copy().next_to(self.commitments_copy_recs[0], DOWN, buff = 0.6)
        values2 = self.internal_node2.copy().next_to(self.commitments_copy_recs[2], DOWN, buff = 0.6)
        arrows = []
        for i in range(len(self.internal_node2)):
            node = values[i]
            node.move_to(values[i])
            self.create_arrow(self.commitments_copy_recs[0], node, arrows)
            node2 = values2[i]
            self.create_arrow(self.commitments_copy_recs[2], node2, arrows)
        self.right_commitments = VGroup(*self.commitments_copy_recs, *values, *values2, *arrows, *self.hashes_copy_recs,
                                        self.rectangle_node_commitments2)
        self.right_commitments_opacity = VGroup(*self.commitments_copy_recs, *values, *values2, *arrows, *self.hashes_copy_recs)
        
        self.rectangle_on_parent_commitments = RoundedRectangle(corner_radius=0.1, width = 7, height = 1.9, fill_opacity = 0.15, stroke_width = 0.0).set_color(HIGHLIGHT_COLOR)
        
        
    def animate_in(self, scene):
        self.new_subsection(scene, "3 levels", "data/sound/e7/slide4-0.mp3")
        scene.play(Write(self.title_label), run_time=1)
        self.generate_multi_level_snapshot(scene)
        
        self.new_subsection(scene, "C0", "data/sound/e7/slide4-1.mp3")
        scene.play(Create(self.internal_node), Write(self.node1_texts), run_time=1)
        self.arrows_C0 = VGroup(*self.arrows_C0)
        scene.play(Write(self.arrows_C0), run_time=0.5)
        scene.play(Write(self.commitment_to_c0_text), Create(self.commitment_to_C0), run_time=0.5)
        
        self.new_subsection(scene, "internal node", "data/sound/e7/slide4-2.mp3")
        self.internal_node_whole = VGroup(self.internal_node, self.node1_texts, 
                                          self.commitment_to_c0_text, self.commitment_to_C0,
                                          self.arrows_C0)
        self.internal_node_whole.generate_target()
        self.internal_node_whole.target.scale(0.5).next_to(self.internal_node2_whole, LEFT, buff = 0.4)
        scene.play(MoveToTarget(self.internal_node_whole), run_time=1)
        scene.play(FadeIn(self.internal_node2_whole), run_time=1)

        self.commitmentcdots.next_to(self.commitment_to_c255_text, LEFT, buff = 0.57)
        self.rectangle_node_commitments.move_to(self.commitmentcdots.get_center())
        
        
        
        scene.play(Create(self.commitmentcdots), Create(self.rectangle_node_commitments), run_time=0.5)
        commitments = [self.commitment_to_C0, self.commitmentcdots, self.commitment_to_C255]
        for commitment in commitments:
            scene.play(Indicate(commitment), run_time=0.4)
            
        self.new_subsection(scene, "parent to 256 value", "data/sound/e7/slide4-3.mp3")
        values = [self.internal_node, self.internal_node2]
        for value in self.internal_node:
            Indicate(value, run_time=0.3) 
        for value in self.internal_node2:
            Indicate(value, run_time=0.3)
            
        self.new_subsection(scene, "array of commitments", "data/sound/e7/slide4-4.mp3")
        scene.wait(1.5)
        scene.play(Indicate(self.commitment_cdots),
                   Indicate(self.commitment_to_C0),
                   Indicate(self.commitment_to_c0_text),
                   Indicate(self.commitment_to_c255_text),
                   Indicate(self.commitment_to_C255), run_time=1.0)
        
        self.new_subsection(scene, "how to commit to ec points?", "data/sound/e7/slide4-5.mp3")
        scene.wait(1.5)
        scene.play(Indicate(self.commitment_to_C0), run_time=1.0)
        for value in values:
            scene.play(Indicate(value), run_time=0.3)
            
        self.commitment_size_brace = Brace(self.commitment_to_C0, UP, buff =0.1)
        self.scalar_brace = Brace(self.internal_node[0], DOWN, buff =0.1)
        
        self.ec_point = Text("EC point", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 20)
        self.commitment_size_brace.put_at_tip(self.ec_point)
        
        self.scalar = Text("scalar", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 20)
        self.scalar_brace.put_at_tip(self.scalar)
        scene.play(Write(self.scalar_brace), Write(self.scalar), run_time=1)
        scene.wait(1)
        scene.play(Write(self.commitment_size_brace), Write(self.ec_point), run_time=1)
        scene.wait(2)
        self.commitment_to_ec_values.next_to(self.commitmentcdots, UP, buff = 1.0).shift(LEFT * 0.5)
        scene.play(Write(self.commitment_to_ec_values), run_time=1)
        scene.wait(1)
        
        self.new_subsection(scene, "sizes ec and scalar in KZG", "data/sound/e7/slide4-5a.mp3")
        scene.play(FadeOut(self.commitment_to_ec_values), run_time=1)
        
        
        kzg_text = Text("KZG", font=PRIMARY_FONT, font_size=25, color=PRIMARY_COLOR).next_to(self.commitment_to_C0, LEFT, buff = 1.0)
        ipa_text = Text("IPA", font=PRIMARY_FONT, font_size=25, color=PRIMARY_COLOR).next_to(self.commitment_to_C0, LEFT, buff = 1.0)
        self.commitment_size = Text("381 b", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 20)
        self.scalar_size = Text("255 b", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 20)
        self.commitment_size_ipa = Text("255 b", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 20)
        self.scalar_size_ipa = Text("253 b", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 20)
        self.commitment_size_brace.put_at_tip(self.commitment_size)
        self.commitment_size_brace.put_at_tip(self.commitment_size_ipa)
        
        self.scalar_brace.put_at_tip(self.scalar_size)
        self.scalar_brace.put_at_tip(self.scalar_size_ipa)
        scene.play(FadeOut(self.scalar, self.ec_point))
        scene.wait(1)
        scene.play(Write(self.commitment_size), Write(kzg_text), run_time=1)
        scene.wait(2)
        scene.play(Write(self.scalar_size), run_time=1)
        
        self.new_subsection(scene, "sizes ec and scalar in IPA", "data/sound/e7/slide4-5b.mp3")
        scene.wait(1)
        scene.play(TransformMatchingShapes(self.commitment_size, self.commitment_size_ipa), FadeOut(kzg_text), FadeIn(ipa_text), run_time=1)
        scene.wait(1)
        scene.play(TransformMatchingShapes(self.scalar_size, self.scalar_size_ipa))
        scene.wait(1)
        
        self.new_subsection(scene, "truncate", "data/sound/e7/slide4-6.mp3")
        self.commitment_size_brace = VGroup(self.commitment_size_brace, self.commitment_size_ipa)
        self.commitment_size_brace.generate_target()
        self.commitment_size_brace.target.shift(UP)
        scene.play(MoveToTarget(self.commitment_size_brace), run_time=1)
        self.hashaes_of_commitments.next_to(self.commitmentcdots, UP, buff = 0.1)
        self.rectangle_with_hashes.move_to(self.hashaes_of_commitments.get_center()).shift(DOWN*0.35)
        scene.play(Create(self.hashaes_of_commitments),
                   FadeOut(self.rectangle_node_commitments), FadeIn(self.rectangle_with_hashes), run_time=1)
        self.scalar_size_hash = Text("253 b", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 20).move_to(self.commitment_size_ipa.get_center())
        scene.play(TransformMatchingShapes(self.commitment_size_ipa, self.scalar_size_hash), run_time=1)
        
        self.new_subsection(scene, "commitment C^1_0", "data/sound/e7/slide4-7.mp3")
        self.whole_tree_until_C10 = VGroup(self.internal_node_whole, self.internal_node2_whole,
                                          self.commitment_to_c255_text, self.commitmentcdots, self.rectangle_with_hashes,
                                          *self.arrows_C0, *self.arrows_C255, self.hashaes_of_commitments)
        scene.play(FadeOut(self.scalar_brace, self.commitment_size_brace, self.scalar_size_hash, self.scalar_size_ipa, ipa_text), run_time=0.5)
        self.whole_tree_until_C10.generate_target()
        self.whole_tree_until_C10.target.shift(DOWN*2)
        scene.play(MoveToTarget(self.whole_tree_until_C10), run_time=1) 
        self.commitment_C01.next_to(self.hashaes_of_commitments, UP, buff = 0.5)
        scene.play(Create(self.commitment_C01), run_time=1)
        
        self.arrow_commitment_C01 = []
        for rectangle in self.hashaes_of_commitments_rec:
            self.create_arrow(self.commitment_C01_rec, rectangle, self.arrow_commitment_C01)
        self.arrow_commitment_C01 = VGroup(*self.arrow_commitment_C01)
        scene.play(Create(self.arrow_commitment_C01), run_time=1)
        
                
        self.new_subsection(scene, "and it gathers 256 commitments", "data/sound/e7/slide4-8.mp3")
        for hash in self.hashaes_of_commitments[:]:
            scene.play(Indicate(hash), run_time=0.3)
        self.commitment_C01.generate_target()
        self.commitment_C01.target.next_to(self.hashaes_of_commitments[:][0], UP, buff = 0.4).shift(LEFT * 1.25)
        scene.play(MoveToTarget(self.commitment_C01), FadeOut(self.arrow_commitment_C01), run_time=1)
        self.whole_tree_until_C10.generate_target()
        self.whole_tree_until_C10.target.shift(LEFT*2.45)
        scene.play(MoveToTarget(self.whole_tree_until_C10), run_time=1)
        self.arrow_commitment_C01 = []
        
        for rectangle in self.hashaes_of_commitments_rec:
            self.create_arrow(self.commitment_C01_rec, rectangle, self.arrow_commitment_C01)
        self.other_commitments.next_to(self.commitment_C01, RIGHT, buff = 2.0)
        self.right_commitments.next_to(self.other_commitments[1], DOWN, buff = 0.2)
        scene.play(Create(self.right_commitments), FadeIn(self.rectangle_on_parent_commitments), run_time=1)
        
        for node in self.hashes_copy_recs:
            self.create_arrow(self.other_commitments[1], node, self.arrow_commitment_C01)
        
        self.arrow_commitment_C01 = VGroup(*self.arrow_commitment_C01)
        
        scene.play(Create(self.other_commitments), Write(self.arrow_commitment_C01), run_time=1)  
        
        self.new_subsection(scene, "reduce root commitments->commit to them->with final parent node", "data/sound/e7/slide4-10.mp3")
        self.other_commitments.add(self.commitment_C01, self.arrow_commitment_C01)
        self.other_hashes.next_to(self.other_commitments[0], UP, buff = 0.01)
        self.whole_tree_until_C10.add(self.other_commitments, self.other_hashes)
        scene.play(Create(self.other_hashes), run_time=1)
        scene.wait(1)
        self.final_parent_node.next_to(self.other_hashes, UP, buff = 0.4)
        scene.play(Create(self.final_parent_node), run_time=1)
        arrows_final = []
        for i in range(len(self.other_hashes_rec)):
            node = self.other_hashes_rec[i]
            self.create_arrow(self.final_parent_node_rec, node, arrows_final)
            scene.play(Write(arrows_final[i]), run_time=0.3)
        self.whole_tree_until_C10.add(self.final_parent_node,*arrows_final, 
                                      self.rectangle_on_parent_commitments, self.right_commitments)
        
        self.new_subsection(scene, "simple math", "data/sound/e7/slide4-11.mp3")
        scene.wait(1)
        self.whole_tree_until_C10.generate_target()
        self.whole_tree_until_C10.target.scale(0.75).shift(LEFT*2)
        scene.play(MoveToTarget(self.whole_tree_until_C10), run_time=2.5)
        
        scene.play(self.whole_tree_until_C10.animate.set_opacity(0.15), run_time=2)
        
        self.new_subsection(scene, "simple level VT holds 256 vals", "data/sound/e7/slide4-11a.mp3")
        scene.play(self.commitment_to_C0.animate.set_opacity(0.4),
                   self.commitment_to_c0_text.animate.set_opacity(1.0), run_time=2)
        for nodes in self.internal_node:
            scene.play(nodes.animate.set_opacity(0.4), run_time=0.5)
        
        self.values256.next_to(self.whole_tree_until_C10, RIGHT, buff = 1.0).shift(RIGHT*0.5+UP*2)
        self.single_commitment.next_to(self.values256, UP, buff = 0.3)
        self.values2_to_8.next_to(self.whole_tree_until_C10, RIGHT, buff = 1.0).shift(RIGHT*0.5+UP*2)
        self.values2_to_24.next_to(self.values2_to_8, DOWN, buff = 1.0)
        self.three_level.next_to(self.values2_to_24, UP, buff = 0.3)
        self.four_level.next_to(self.values2_to_8, DOWN, buff = 0.3)
        self.values_four_level.next_to(self.values2_to_8, DOWN, buff = 1.0)
        scene.play(Write(self.values256), Write(self.single_commitment), run_time=1)
        scene.wait(1.5)
        scene.play(TransformMatchingShapes(self.values256, self.values2_to_8),run_time=0.5)
        scene.wait(1)

        other_nodes = self.internal_node2

        scene.play(Write(self.three_level), run_time=0.5)
        scene.play(other_nodes.animate.set_opacity(0.4), run_time=0.5)
        scene.play(self.right_commitments_opacity.animate.set_opacity(0.4),
                   self.commitment_255.animate.set_opacity(0.4),
                   self.commitment_cdots.animate.set_opacity(0.4), run_time=0.5)
        scene.play(self.other_commitments.animate.set_opacity(0.4), 
                   self.hashaes_of_commitments.animate.set_opacity(0.4), run_time=0.5)
        scene.play(self.other_commitments.animate.set_opacity(0.4), run_time=0.5)
        scene.play(self.commitment_C01.animate.set_opacity(0.4),
                   self.other_hashes_rec.animate.set_opacity(0.4),
                   self.final_parent_node_rec.animate.set_opacity(0.4), run_time=0.5)

        scene.play(TransformMatchingShapes(self.values2_to_8.copy(), self.values2_to_24),)
    
    
        scene.wait(2)
        
        self.new_subsection(scene, "4 level deep squeeze in all of the ETH acc", "data/sound/e7/slide4-11b.mp3")
        scene.play(TransformMatchingShapes(self.three_level, self.four_level), run_time=0.5)
        scene.wait(1.5)
        scene.play(TransformMatchingShapes(self.values2_to_24, self.values_four_level), run_time=0.5)
        self.create_ethereum_addresses_counter(scene)
        
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.title_label, self.four_level, self.block, self.ethereum_addresses, 
                           self.number, self.whole_tree_until_C10, self.values_four_level), run_time=1)
        
        
    def generate_multi_level_snapshot(self, scene):
        rectangle = RoundedRectangle(corner_radius=0.1, width = 0.5, height = 0.5, fill_opacity = 0.25,  stroke_width = 0.0).set_color(SECONDARY_COLOR)
        self.first_block = [rectangle.copy() for _ in range(10)]
        self.first_block = VGroup(*self.first_block).arrange(RIGHT, buff = 0.05)
        self.cdots = Text(r"...", font=PRIMARY_FONT, font_size=40, color=PRIMARY_COLOR).move_to(self.first_block[5]).shift(LEFT*0.22)
                
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
        self.first_block.target.scale(0.5).shift(LEFT*3+DOWN*2)
        scene.play(MoveToTarget(self.first_block), run_time=1)
        self.second_block.scale(0.5).shift(DOWN * 2)
        self.third_block.scale(0.5).shift(RIGHT * 3 + DOWN * 2)
        self.second_block.remove(*self.second_block[4:6])
        self.third_block.remove(*self.third_block[4:6])
        
        scene.play(Create(self.second_block), Create(self.third_block), run_time=1)
        
        self.commitment_to_first = rectangle.copy().set_color(PRIMARY_COLOR).next_to(self.first_block, UP, buff = 1.0)
        self.commitment_to_second = rectangle.copy().set_color(PRIMARY_COLOR).next_to(self.second_block, UP, buff = 1.0)
        self.commitment_to_third = rectangle.copy().set_color(PRIMARY_COLOR).next_to(self.third_block, UP, buff = 1.0)
        
        self.commitment_to_commitment = rectangle.copy().set_color(HIGHLIGHT_COLOR).next_to(self.commitment_to_second, UP, buff = 1.0)
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
        scene.play(Create(self.commitment_to_first), Write(arrows), Create(self.commitment_to_second), Create(self.commitment_to_third), run_time=0.5)
        self.create_arrow(self.commitment_to_commitment, self.commitment_to_first, arrows2)
        self.create_arrow(self.commitment_to_commitment, self.commitment_to_second, arrows2)
        self.create_arrow(self.commitment_to_commitment, self.commitment_to_third, arrows2)
        arrows2 = VGroup(*arrows2)
        scene.play(Write(arrows2), Create(self.commitment_to_commitment), run_time=0.5)
        scene.wait(2)
        scene.play(FadeOut(self.first_block, self.commitment_to_commitment, self.commitment_to_first, self.commitment_to_second,
                           self.commitment_to_third, arrows), FadeOut(self.second_block, arrows2), FadeOut(self.third_block), run_time=1)
        
    def create_arrow(self, start, end, arrows):
        arrow = Arrow(start.get_bottom(), end.get_top(), 
                      buff = 0.0, color=PRIMARY_COLOR,
                      stroke_width=0.8, max_tip_length_to_length_ratio=0.05,
                      tip_length = 0.1, 
                      tip_shape = StealthTip)
        arrows.append(arrow)
        
    def create_ethereum_addresses_counter(self, scene):
        scene.play(FadeOut(self.values2_to_8, self.single_commitment))
        self.block = RoundedRectangle(corner_radius=0.1, width = 4, height = 2, fill_opacity = 0.25,  stroke_width = 0.0).set_color(PRIMARY_COLOR)
        self.block.next_to(self.four_level, DOWN, buff = 1.5)
        self.ethereum_addresses = Text("Ethereum addresses", font=PRIMARY_FONT, font_size=30, color=PRIMARY_COLOR).move_to(self.block.get_center()).shift(UP*0.5)
        scene.play(FadeIn(self.block, self.ethereum_addresses), run_time=1)
        self.number = DecimalNumber(0, font_size=50, color=PRIMARY_COLOR).move_to(self.block.get_center()).shift(DOWN*0.5+LEFT)
        scene.play(ChangeDecimalToValue(self.number, 308105039), run_time=2)