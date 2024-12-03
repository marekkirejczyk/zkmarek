from manim import (FadeOut, Text, RIGHT, DOWN, UP, MathTex, RemoveTextLetterByLetter, BLUE_E, ImageMobject, WHITE, Indicate, 
TransformMatchingShapes, Write, MoveToTarget, ORIGIN, FadeIn, GrowArrow, Rectangle, PURPLE, Group, Arrow, LEFT, StealthTip, 
PINK, Polygon, GREEN_C, GREEN_E, RED_D, RoundedRectangle, GOLD_E)
from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR, HIGHLIGHT_COLOR, PRIMARY_FONT, HIGHLIGHT2_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase



class BlobsBlockchain(SlideBase):
    def __init__(self) -> None:
        super().__init__(title="Blobs in Ethereum")
        
    def construct(self):
        self.title_text = Text("Blobs in Ethereum", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 40).to_edge(UP)
        self.block1 = Rectangle(width=5.5, height=4.5, fill_opacity = 0.4).scale(0.4)
        self.block1.set_color_by_gradient([WHITE, PURPLE, HIGHLIGHT2_COLOR]).to_edge(DOWN)
        
        self.block2 = self.block1.copy().next_to(self.block1, LEFT).shift(LEFT)
        self.block3 = self.block1.copy().next_to(self.block1, RIGHT).shift(RIGHT)
        
        self.ethereum_logo = ImageMobject("data/images/ethereum_logo.png").scale(0.4)
        self.ethereum_logo.move_to(self.block1.get_center())
        self.block1_group = Group(self.block1, self.ethereum_logo)
        
        self.ethereum_logo2 = self.ethereum_logo.copy().move_to(self.block2.get_center())
        self.block2_group = Group(self.block2, self.ethereum_logo2)

        self.ethereum_logo3 = self.ethereum_logo.copy()
        self.ethereum_logo3.move_to(self.block3.get_center())
        self.block3_group = Group(self.block3, self.ethereum_logo3)
        

        self.arrow = Arrow(self.block2.get_right(), self.block1.get_left(), color=SECONDARY_COLOR, tip_shape=StealthTip, 
                           stroke_width=2, max_tip_length_to_length_ratio=0.15).set_color_by_gradient([SECONDARY_COLOR, WHITE])
        self.arrow2 = Arrow(self.block1.get_right(), self.block3.get_left(), color=SECONDARY_COLOR, tip_shape=StealthTip, 
                            stroke_width=2, max_tip_length_to_length_ratio=0.15).set_color_by_gradient([SECONDARY_COLOR, WHITE])
        
        self.blob_field = RoundedRectangle(corner_radius=0.5, width = 4.5, height = 4, fill_opacity = 0.4)
        self.blob_field.set_color_by_gradient([GOLD_E, GREEN_E, BLUE_E]).next_to(self.block1_group, UP, buff = 0.2)
        self.blob = ImageMobject("data/images/blob.png").move_to(self.blob_field)
        
        self.commitment = Text("commitment", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 30)
        self.commitment_hash = Text("hash(C)", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 24)
        self.commitment.move_to(self.blob.get_bottom()).shift(UP)
        self.commitment_hash.move_to(self.blob.get_bottom()).next_to(self.commitment, UP, buff=0.1).shift(LEFT*0.8)
        
        
        self.vector = MathTex(r"\boldsymbol{\left[ {{y_0}}, {{y_1}}, \cdots {{y_{4095}}}   \right]}", color = RED_D, font_size = 50).next_to(self.blob, UP).shift(DOWN*0.07)
        
        # time accelerating animation = back in time
        self.polygon1 = Polygon(ORIGIN, UP*0.5+RIGHT, DOWN*0.5+RIGHT, fill_opacity = 0.4).set_color_by_gradient([PRIMARY_COLOR, BLUE_E, HIGHLIGHT2_COLOR]).scale(0.4)
        self.polygon2 = self.polygon1.copy()
        self.polygon3 = self.polygon1.copy()
        
        self.polygon1.to_edge(UP+LEFT).shift(DOWN+RIGHT)
        self.polygon2.next_to(self.polygon1, RIGHT, buff = 0.1)
        self.polygon3.next_to(self.polygon2, RIGHT, buff = 0.1)
        
        self.two_weeks = Text("4096 epochs ago...", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 20).next_to(self.polygon2, DOWN)
        
        # time accelerating = future
        self.polygon1_future = Polygon(ORIGIN, DOWN, DOWN*0.5+RIGHT, fill_opacity = 0.4).set_color_by_gradient([GREEN_E, GREEN_C, HIGHLIGHT_COLOR]).scale(0.4)
        self.polygon2_future = self.polygon1_future.copy()
        self.polygon3_future = self.polygon1_future.copy()
        
        self.polygon1_future.to_edge(UP+LEFT).shift(DOWN+RIGHT)
        self.polygon2_future.next_to(self.polygon1_future, RIGHT, buff = 0.1)
        self.polygon3_future.next_to(self.polygon2_future, RIGHT, buff = 0.1)
        
        self.two_weeks_future = Text("4096 epochs in...", font = PRIMARY_FONT, font_size = 20, color = GREEN_C).next_to(self.polygon2_future, DOWN)
        
        
    def animate_in(self, scene):
        self.new_subsection(scene, "Block on L1", "data/sound/e5/slide5-1.mp3")
        scene.play(Write(self.title_text), run_time=0.7)
        scene.play(FadeIn(self.block1_group, self.block2_group, self.block3_group))
        scene.play(GrowArrow(self.arrow), GrowArrow(self.arrow2))
        
        scene.play(FadeIn(self.blob_field))
        scene.play(FadeIn(self.blob))
        
        scene.play(FadeIn(self.commitment, self.vector))

        self.vector.generate_target()
        self.vector.target.move_to(self.blob.get_top()).shift(DOWN*1.5).scale(0.6)

        
        self.new_subsection(scene, "commitment ... hash Commitment", "data/sound/e5/slide5-2.mp3")
        scene.play(MoveToTarget(self.vector), run_time=1)
        scene.wait(1)

        scene.play(Indicate(self.commitment, color = PINK))
        scene.wait(1.5)

        scene.play(TransformMatchingShapes(self.commitment.copy(), self.commitment_hash), run_time=1)
        scene.wait(2)
        self.commitment_hash.generate_target()
        self.commitment_hash.target.move_to(self.block1.get_top()).shift(DOWN*0.2)
        scene.play(MoveToTarget(self.commitment_hash))
        
        self.new_subsection(scene, "available for 4096 epochs", "data/sound/e5/slide5-3.mp3")
        scene.wait(1.5)
        scene.play(Indicate(self.vector, color = PINK), run_time=2)

        scene.wait(1.5)
        
        self.new_subsection(scene, "after pruning", "data/sound/e5/slide5-4.mp3")

        scene.play(FadeIn(self.polygon1_future), FadeIn(self.polygon2_future), FadeIn(self.polygon3_future), Write(self.two_weeks_future), run_time=0.7)

        polygons = [self.polygon1_future, self.polygon2_future, self.polygon3_future, self.polygon1_future, self.polygon2_future, 
                    self.polygon3_future, self.polygon1_future]
        for i in range(len(polygons)):
            if i % 3 !=2:
                if i==3:
                    scene.play(Indicate(polygons[i], color = WHITE, scale_factor=1), RemoveTextLetterByLetter(self.vector), run_time=0.25)
                else:
                    scene.play(Indicate(polygons[i], color = WHITE, scale_factor=1), run_time=0.25)
            else: 
                    scene.play(Indicate(polygons[i], color = WHITE, scale_factor=1), run_time=0.7)
        scene.wait(0.5)
        self.blob_field.generate_target()
        self.blob_field.target.scale(0.5)
        self.commitment.generate_target()
        self.commitment.target.scale(0.75).shift(UP*0.3)
        scene.play(MoveToTarget(self.blob_field), MoveToTarget(self.commitment), FadeOut(self.blob))
        scene.play(FadeOut(self.polygon1_future, self.polygon2_future, self.polygon3_future, self.two_weeks_future))
        self.blocks = Group(self.block1_group, self.block2_group, self.block3_group, self.arrow, self.arrow2, self.commitment_hash)
        self.blocks.generate_target()
        self.blocks.target.next_to(self.blob_field, DOWN, buff = 0.1)
        scene.play(MoveToTarget(self.blocks))
        
        self.new_subsection(scene, "hash of the commitment", "data/sound/e5/slide5-5.mp3")
        scene.play(Indicate(self.commitment_hash, color = PINK), Indicate(self.commitment, color = PINK))
        scene.wait(5.5)
        
        self.new_subsection(scene, "blockindex", "data/sound/e5/slide5-6.mp3")
        scene.wait(5)

        
    def animate_out(self, scene):
        scene.play(FadeOut(self.blob_field, self.commitment, self.title_text, self.blocks))

