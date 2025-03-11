from manim import Indicate, Create, UP, LEFT, ORIGIN, MoveToTarget, Write, Text, FadeOut, DOWN, RIGHT

from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR, PRIMARY_FONT, HIGHLIGHT_COLOR
from zkmarek.video.slides.e6.merkle_particia_trie import MerklePatriciaTrie as MPT
from zkmarek.video.slides.e6.worldstate import SimplifiedWorldState 

class ETHPatriciaMerkleTrie(SlideBase):
    def __init__(self)-> None:
        super().__init__("Ethereum Patricia Merkle Trie")
        
    def construct(self):
        self.title_label = Text("Ethereum's Merkle Patricia Trie", font = PRIMARY_FONT, color = PRIMARY_COLOR, font_size = 40).to_edge(UP)
        self.MPT = MPT().shift(UP*2.9+LEFT*1).scale(0.45)
        self.worldState = SimplifiedWorldState()

    def animate_in(self, scene):
        self.merkle_particia_trie(scene)
        
    def animate_out(self, scene):
        scene.play(FadeOut(self.title_label), FadeOut(self.MPT), FadeOut(self.worldState))
    
    def merkle_particia_trie(self, scene):
        self.new_subsection(scene, "Simplified world state", "data/sound/e6/slide2-6.mp3")
        scene.play(Write(self.title_label), run_time=0.7)
        self.worldState.appear_table(scene)
        
        self.new_subsection(scene, "MPT in a single node", "data/sound/e6/slide2-6a.mp3")
        scene.play(self.worldState.key_cells[0:7].animate.set_color(HIGHLIGHT_COLOR))
        self.MPT.leaf_replace.scale(0.45).scale(2).move_to(ORIGIN)
        scene.play(Create(self.MPT.leaf_replace), run_time=2.5)
        scene.play(self.worldState.key_cells[0:7].animate.set_color(HIGHLIGHT_COLOR))
        scene.wait(5)
        key_cells_shared = [self.worldState.key_cells[0], self.worldState.key_cells[1], 
                            self.worldState.key_cells[7], self.worldState.key_cells[8],
                            self.worldState.key_cells[14], self.worldState.key_cells[15],
                            self.worldState.key_cells[21], self.worldState.key_cells[22]]
        for i in range(0,4):
            scene.play(Indicate(key_cells_shared[2*i], color = SECONDARY_COLOR, scale_factor=1.5), 
                       Indicate(key_cells_shared[2*i+1], color = SECONDARY_COLOR), run_time=0.8)
        scene.wait(1)
    
        self.MPT.leaf_replace.generate_target()
        self.MPT.leaf_replace.target.next_to(self.MPT.branch1, DOWN+LEFT, buff = 0.0).scale(1/2).shift(RIGHT+UP*0.3)
        
        self.new_subsection(scene, "root extension", "data/sound/e6/slide2-6b.mp3")
        scene.play(MoveToTarget(self.MPT.leaf_replace), run_time=1)
        scene.play(Create(self.MPT.root))
        self.MPT.leaf_replace2.move_to(self.MPT.leaf_replace.get_center()).scale(0.45)
        self.MPT.replace_leaf1(scene)
        a7_label = None
        for field in self.MPT.root.field_group:
            _, text = field 
            if "a7" in text.text:
                a7_label = text[10:18]
                break
        if a7_label:
            scene.play(a7_label.animate.set_color(PRIMARY_COLOR).scale(1.2)) 
        
        self.new_subsection(scene, "branches", "data/sound/e6/slide2-6c.mp3")
        scene.play(Create(self.MPT.branch1), Write(self.MPT.arrow), run_time=1)
        scene.wait(1)
        scene.play(*[Indicate(slot_group, color = SECONDARY_COLOR) for slot_group in self.MPT.branch1.child_slot_map.values()], run_time=1)
        scene.wait(4.5)
        self.MPT.leaf1.move_to(self.MPT.leaf_replace2.get_center())
        self.MPT.replace_leaf2(scene)
        scene.play(Write(self.MPT.arrow2), run_time=1)
        scene.play(self.worldState.key_cells[7:14].animate.set_color(HIGHLIGHT_COLOR))
        scene.play(Create(self.MPT.leaf2), Write(self.MPT.arrow4), run_time=1)
        scene.wait(2)
        
        self.new_subsection(scene, "extensions", "data/sound/e6/slide2-6d.mp3")
        scene.play(Create(self.MPT.extension2), Write(self.MPT.arrow3), run_time=1)
        scene.wait(3)

        d3_label = None
        for field in self.MPT.extension2.field_group:
            _, text = field 
            if "d3" in text.text:
                d3_label = text[16:18]
                break
        if d3_label:
            scene.play(d3_label.animate.set_color(SECONDARY_COLOR).scale(1.2)) 
        scene.play(self.worldState.key_cells[14:21].animate.set_color(SECONDARY_COLOR))
        scene.play(self.worldState.key_cells[21:28].animate.set_color(SECONDARY_COLOR))
            
        self.new_subsection(scene, "leaves", "data/sound/e6/slide2-6e.mp3")
        scene.play(Create(self.MPT.branch2), Write(self.MPT.arrow5), run_time=1)
        scene.play(Create(self.MPT.leaf3), Write(self.MPT.arrow6), run_time=1)
        scene.play(Create(self.MPT.leaf4), Write(self.MPT.arrow7), run_time=1)
            
        self.new_subsection(scene, "4 level mpt", "data/sound/e6/slide2-6f.mp3")
        scene.wait(5.6)
        scene.play(Indicate(self.MPT.extension2, color = SECONDARY_COLOR, scale_factor=1.1))
        scene.play(Indicate(self.MPT.branch1, color = SECONDARY_COLOR, scale_factor=1.1))
        leaves = [self.MPT.leaf1, self.MPT.leaf2, self.MPT.leaf3, self.MPT.leaf4]
        for i in range(4):
            scene.play(Indicate(leaves[i], color = SECONDARY_COLOR, scale_factor=1.1), run_time=0.4)
            
        scene.wait(2)
        scene.play(Indicate(self.MPT.leaf1, color = PRIMARY_COLOR, scale_factor=1.1))
        scene.wait(1.5)

     
        path0 = [self.MPT.branch1.get_child_slot("1"), self.MPT.leaf1.field_group[0]]
        scene.play(Indicate(path0[0], color = PRIMARY_COLOR), path0[0].animate.set_color(PRIMARY_COLOR), run_time=0.5)

        
    
