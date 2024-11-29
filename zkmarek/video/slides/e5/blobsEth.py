from manim import (FadeOut, Text, RIGHT, DOWN, UP, MathTex, RemoveTextLetterByLetter, BLUE_E, ImageMobject, WHITE, Indicate, 
TransformMatchingShapes, Write, MoveToTarget, ORIGIN, FadeIn, GrowArrow, Rectangle, Tex, PURPLE, Group, Arrow, LEFT, StealthTip, 
PINK, Polygon, GREEN_C, GREEN_E, RED_D)
from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR, HIGHLIGHT_COLOR, PRIMARY_FONT, HIGHLIGHT2_COLOR
from zkmarek.video.slides.common.slide_base import SlideBase



class BlobsBlockchain(SlideBase):
    def __init__(self) -> None:
        super().__init__(title="Blobs in Ethereum")
        
    def construct(self):
        self.title_text = Text("Blobs in Ethereum", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 40).to_edge(UP)
        self.block1 = Rectangle(width=5.5, height=4.5, fill_opacity = 0.1)
        self.block1.set_color_by_gradient([WHITE, PURPLE, HIGHLIGHT2_COLOR])
        self.blob = ImageMobject("data/images/blob.png").move_to(self.block1)
        
        self.block2 = self.block1.copy().scale(0.3).next_to(self.block1, LEFT).shift(LEFT)
        self.block3 = self.block1.copy().scale(0.3).next_to(self.block1, RIGHT).shift(RIGHT)
        
        self.ethereum_logo = ImageMobject("data/images/ethereum_logo.png").scale(0.4)
        self.ethereum_logo.move_to(self.block2.get_center())
        self.block2_group = Group(self.block2, self.ethereum_logo)

        self.ethereum_logo3 = self.ethereum_logo.copy()
        self.ethereum_logo3.move_to(self.block3.get_center())
        self.block3_group = Group(self.block3, self.ethereum_logo3)
        

        self.arrow = Arrow(self.block2.get_right(), self.block1.get_left(), color=SECONDARY_COLOR, tip_shape=StealthTip, 
                           stroke_width=2, max_tip_length_to_length_ratio=0.15).set_color_by_gradient([SECONDARY_COLOR, WHITE])
        self.arrow2 = Arrow(self.block1.get_right(), self.block3.get_left(), color=SECONDARY_COLOR, tip_shape=StealthTip, 
                            stroke_width=2, max_tip_length_to_length_ratio=0.15).set_color_by_gradient([SECONDARY_COLOR, WHITE])
        
        self.commitment = Text("commitment", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 30)
        self.commitment_hash = Text("SHA256(C)", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 30)
        self.commitment.move_to(self.blob.get_bottom()).shift(UP)
        self.commitment_hash.move_to(self.blob.get_bottom()).shift(UP)
        self.blobIndex = Tex(r"\texttt{blobIndex = 1}", color = PRIMARY_COLOR, font_size = 20)
        self.blobIndex.move_to(self.blob.get_center())
        
        
        self.vector = MathTex(r"\boldsymbol{\left[ {{y_0}}, {{y_1}}, \cdots {{y_{4095}}}   \right]}", color = RED_D, font_size = 50).next_to(self.block1, UP)
        
        # time accelerating animation = back in time
        self.polygon1 = Polygon(ORIGIN, UP*0.5+RIGHT, DOWN*0.5+RIGHT, fill_opacity = 0.4).set_color_by_gradient([PRIMARY_COLOR, BLUE_E, HIGHLIGHT2_COLOR]).scale(0.4)
        self.polygon2 = self.polygon1.copy()
        self.polygon3 = self.polygon1.copy()
        
        self.polygon1.to_edge(UP+LEFT).shift(DOWN+RIGHT)
        self.polygon2.next_to(self.polygon1, RIGHT, buff = 0.1)
        self.polygon3.next_to(self.polygon2, RIGHT, buff = 0.1)
        
        self.two_weeks = Text("over two weeks ago...", color = PRIMARY_COLOR, font = PRIMARY_FONT, font_size = 20).next_to(self.polygon2, DOWN)
        
        # time accelerating = future
        self.polygon1_future = Polygon(ORIGIN, DOWN, DOWN*0.5+RIGHT, fill_opacity = 0.4).set_color_by_gradient([GREEN_E, GREEN_C, HIGHLIGHT_COLOR]).scale(0.4)
        self.polygon2_future = self.polygon1_future.copy()
        self.polygon3_future = self.polygon1_future.copy()
        
        self.polygon1_future.to_edge(UP+LEFT).shift(DOWN+RIGHT)
        self.polygon2_future.next_to(self.polygon1_future, RIGHT, buff = 0.1)
        self.polygon3_future.next_to(self.polygon2_future, RIGHT, buff = 0.1)
        
        self.two_weeks_future = Text("over two weeks in...", font = PRIMARY_FONT, font_size = 20, color = GREEN_C).next_to(self.polygon2_future, DOWN)
        
        self.blob2 = self.blob.copy().scale(0.5).move_to(self.block1.get_left()).shift(UP+RIGHT)
        self.blobIndex2 = Tex(r"\texttt{blobIndex = 2}", color = GREEN_C, font_size = 20).move_to(self.blob2.get_center()).shift(UP*0.1)
        self.blob3 = self.blob.copy().scale(0.5).move_to(self.block1.get_right()).shift(DOWN+LEFT)
        self.blobIndex3 = Tex(r"\texttt{blobIndex = 0}", color = PINK, font_size = 20).move_to(self.blob3.get_center()).shift(UP*0.1)
        
        self.commitmentHash2 = Text("SHA256(C2)", color = GREEN_C, font = PRIMARY_FONT, font_size = 15).move_to(self.blob2.get_bottom()).shift(UP*0.5)
        self.commitmentHash3 = Text("SHA256(C0)", color = PINK, font = PRIMARY_FONT, font_size = 15).move_to(self.blob3.get_bottom()).shift(UP*0.5)
        
        self.blobhash = Tex(r"\texttt{blobhash({{blobindex}}) = SHA256(C)}", color = PRIMARY_COLOR).shift(DOWN*1.5)

        
    def animate_in(self, scene):
        self.new_subsection(scene, "Block on L1", "data/sound/e5/slide5-1.mp3")
        scene.play(Write(self.title_text), run_time=0.7)
        scene.play(FadeIn(self.block1, self.block2_group, self.block3_group))
        scene.play(GrowArrow(self.arrow), GrowArrow(self.arrow2))
        
        scene.play(FadeIn(self.blob), FadeIn(self.commitment, self.vector))
        self.vector.generate_target()
        self.vector.target.move_to(self.blob.get_top()).shift(DOWN*1.5).scale(0.6)

        scene.play(MoveToTarget(self.vector))
        
        self.new_subsection(scene, "commitment ... hash Commitment", "data/sound/e5/slide5-2.mp3")
        scene.wait(2)
        scene.play(Indicate(self.commitment, color = PINK))
        scene.wait(4)
        scene.play(TransformMatchingShapes(self.commitment, self.commitment_hash), run_time=1)
        
        self.new_subsection(scene, "pruning after over 2 weeks", "data/sound/e5/slide5-3.mp3")
        scene.wait(1.5)
        scene.play(RemoveTextLetterByLetter(self.vector), run_time=2)
        scene.wait(1.5)
        scene.play(Indicate(self.commitment_hash, color = RED_D))
        
        self.new_subsection(scene, "Before pruning", "data/sound/e5/slide5-4.mp3")
        self.vector1 = MathTex(r"\boldsymbol{\left[ {{y_0}}, {{y_1}}, \cdots {{y_{4095}}}   \right]}", color = RED_D, font_size = 50).move_to(self.blob.get_top()).shift(DOWN*1.4).scale(0.6)

        scene.play(FadeIn(self.polygon1), FadeIn(self.polygon2), FadeIn(self.polygon3), Write(self.two_weeks), run_time=0.7)

        polygons = [self.polygon3, self.polygon2, self.polygon1, self.polygon3, self.polygon2, 
                    self.polygon1, self.polygon3, self.polygon2, self.polygon1, self.polygon3,
                    self.polygon2, self.polygon1]
        for i in range(len(polygons)):
            if i==3:
                scene.play(Indicate(polygons[i], color = WHITE, scale_factor=1), FadeIn(self.vector1), run_time=0.15)
            else:
                scene.play(Indicate(polygons[i], color = WHITE, scale_factor=1), run_time=0.15)
        scene.wait(0.5)
        scene.play(FadeOut(self.polygon1, self.polygon2, self.polygon3, self.two_weeks))
        
        self.new_subsection(scene, "After pruning", "data/sound/e5/slide5-5.mp3")
        scene.play(FadeIn(self.polygon1_future), FadeIn(self.polygon2_future), FadeIn(self.polygon3_future), Write(self.two_weeks_future), run_time=0.7)
        scene.wait(0.5)
        polygons = [self.polygon1_future, self.polygon2_future, self.polygon3_future, self.polygon1_future, self.polygon2_future, 
                    self.polygon3_future, self.polygon1_future, self.polygon2_future, self.polygon3_future, self.polygon1_future,
                    self.polygon2_future, self.polygon3_future, self.polygon1_future, self.polygon2_future, self.polygon3_future]
        for i in range(len(polygons)):
            if i==3:
                scene.play(Indicate(polygons[i], color = WHITE, scale_factor=1), FadeOut(self.vector1), run_time=0.15)
            else:
                scene.play(Indicate(polygons[i], color = WHITE, scale_factor=1), run_time=0.15)
        scene.wait(0.5)
        scene.play(FadeOut(self.polygon1_future, self.polygon2_future, self.polygon3_future, self.two_weeks_future))
        
        self.new_subsection(scene, "hash of the commitment", "data/sound/e5/slide5-6.mp3")
        scene.wait(1.3)
        scene.play(Indicate(self.commitment_hash, color = PINK))
        scene.wait(2)
        
        self.new_subsection(scene, "blockindex", "data/sound/e5/slide5-7.mp3")
        self.blob1 = Group(self.blob, self.commitment_hash)
        self.blob1.generate_target()
        self.blob1.target.scale(0.5)
        scene.wait(1)
        scene.play(MoveToTarget(self.blob1), FadeIn(self.blob2, self.blob3))
        scene.play(FadeIn(self.blobIndex, self.blobIndex2, self.blobIndex3))
        scene.play(FadeIn(self.commitmentHash2, self.commitmentHash3))
        
        self.new_subsection(scene, "blobhash", "data/sound/e5/slide5-8.mp3")
        self.block1_group = Group(self.block1, self.blob, self.blob2, self.blob3, self.commitment_hash, self.commitmentHash2, 
                                  self.commitmentHash3, self.blobIndex2, self.blobIndex3, self.blobIndex)
        self.block1_group.generate_target()
        self.block1_group.target.scale(0.3)
        
        self.block2_group.generate_target()
        self.block2_group.target.shift(RIGHT*1.6)
        
        self.arrow.generate_target()
        self.arrow.target.shift(RIGHT*1.3)
        
        self.block3_group.generate_target()
        self.block3_group.target.shift(LEFT*1.3)
        
        self.arrow2.generate_target()
        self.arrow2.target.shift(LEFT*1.6)
        
        scene.play(MoveToTarget(self.block1_group), MoveToTarget(self.block2_group), MoveToTarget(self.block3_group), MoveToTarget(self.arrow), MoveToTarget(self.arrow2), run_time=1.5)
        scene.wait(1)
        scene.play(FadeIn(self.blobhash), run_time=1.5)
        scene.wait(2.5)
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.block1_group, self.block2_group, self.block3_group, self.title_text, self.blobhash, self.arrow, self.arrow2))

