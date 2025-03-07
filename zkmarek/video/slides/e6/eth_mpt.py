from manim import Indicate, Create, UP, LEFT, RIGHT, DOWN, MoveToTarget, Write

from zkmarek.video.slides.common.slide_base import SlideBase
from zkmarek.video.constant import PRIMARY_COLOR, SECONDARY_COLOR
from zkmarek.video.slides.e6.merkle_particia_trie import MerklePatriciaTrie as MPT
from zkmarek.video.slides.e6.worldstate import SimplifiedWorldState 

class ETHPatriciaMerkleTrie(SlideBase):
    def __init__(self)-> None:
        super().__init__("Ethereum Patricia Merkle Trie")
        
    def construct(self):
        self.MPT = MPT().shift(UP*2.9+LEFT*1).scale(0.45)
        self.worldState = SimplifiedWorldState()
        self.worldState.construct()
        self.worldState.next_to(self.MPT, RIGHT+UP, buff = 0).shift(DOWN*2+LEFT*4)
        
    def animate_in(self, scene):
        self.merkle_particia_trie(scene)
    
    def merkle_particia_trie(self, scene):
        self.new_subsection(scene, "Simplified world state", "data/sound/e6/slide2-6.mp3")
        self.worldState.appear_table(scene)
        self.worldState.keys_table.get_rows()[0].set_color(PRIMARY_COLOR)
        
        self.new_subsection(scene, "MPT in a single node", "data/sound/e6/slide2-6a.mp3")
        scene.play(Create(self.MPT.root.scale(2).shift(LEFT+DOWN)), run_time=2.5)
        scene.play(Indicate(self.worldState.keys_table.get_rows()[0], color = PRIMARY_COLOR, scale_factor=1.5))
        self.MPT.replace_root(scene)
        scene.wait(3)
        for row in self.worldState.keys_table.get_rows():
            scene.play(Indicate(row, color = PRIMARY_COLOR, scale_factor=1.5), run_time=0.8)
        scene.wait(1)
        self.MPT.root.generate_target()
        self.MPT.root.target.shift(RIGHT+UP).scale(1/2)
        
        self.new_subsection(scene, "branches", "data/sound/e6/slide2-6b.mp3")
        scene.play(MoveToTarget(self.MPT.root), run_time=1)
        scene.play(Create(self.MPT.branch1), Write(self.MPT.arrow), run_time=1)
        scene.wait(1)
        scene.play(*[Indicate(slot_group, color = SECONDARY_COLOR) for slot_group in self.MPT.branch1.child_slot_map.values()], run_time=1)
        
        self.new_subsection(scene, "extensions", "data/sound/e6/slide2-6c.mp3")
        scene.play(Create(self.MPT.extension2), Write(self.MPT.arrow3), run_time=1)
        scene.wait(1)
        scene.play(Create(self.MPT.branch2), Write(self.MPT.arrow5), run_time=1)
        scene.wait(1)
        a7_label = None
        for field in self.MPT.root.field_group:
            _, text = field 
            if "a7" in text.text:
                a7_label = text[16:18]
                break
        if a7_label:
            scene.play(a7_label.animate.set_color(PRIMARY_COLOR).scale(1.2)) 
            
        d3_label = None
        for field in self.MPT.extension2.field_group:
            _, text = field 
            if "d3" in text.text:
                d3_label = text[16:18]
                break
        if d3_label:
            scene.play(d3_label.animate.set_color(SECONDARY_COLOR).scale(1.2)) 
            
        self.new_subsection(scene, "leaves", "data/sound/e6/slide2-6d.mp3")
        scene.play(Create(self.MPT.leaf1), Write(self.MPT.arrow2), run_time=1)
        scene.play(Create(self.MPT.leaf2), Write(self.MPT.arrow4), run_time=1)
        scene.play(Create(self.MPT.leaf3), Write(self.MPT.arrow6), run_time=1)
        scene.play(Create(self.MPT.leaf4), Write(self.MPT.arrow7), run_time=1)
            
        self.new_subsection(scene, "4 level mpt")
        scene.wait(2.5)
        scene.play(Indicate(self.MPT.extension2, color = SECONDARY_COLOR, scale_factor=1.1))
        scene.play(Indicate(self.MPT.branch1, color = SECONDARY_COLOR, scale_factor=1.1))
        leaves = [self.MPT.leaf1, self.MPT.leaf2, self.MPT.leaf3, self.MPT.leaf4]
        for i in range(4):
            scene.play(Indicate(leaves[i], color = SECONDARY_COLOR, scale_factor=1.1), run_time=0.4)
            
        scene.wait(1)
        scene.play(Indicate(self.MPT.leaf1.field_group[0], color = SECONDARY_COLOR), Indicate(self.worldState.keys_table.get_rows()[0], color = PRIMARY_COLOR, scale_factor=1.5))
        scene.wait(1)
        scene.play(Indicate(self.MPT.leaf1.field_group[1], color = SECONDARY_COLOR), Indicate(self.worldState.values_table.get_rows()[0], color = PRIMARY_COLOR))
        
        self.new_subsection(scene, "Simplified world state", "data/sound/e6/slide2-6d.mp3")
     
        path0 = [self.MPT.branch1.get_child_slot("1"), self.MPT.leaf1.field_group[0]]
        for item in path0:
            scene.play(Indicate(item, color = PRIMARY_COLOR), run_time=0.5)
            item.generate_target()
            item.target.set_color(PRIMARY_COLOR)
            scene.play(MoveToTarget(item), run_time=0.5)
        
    