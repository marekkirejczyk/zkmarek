from manim import *

class MerkleTree16Children(Scene):
    def construct(self):
        root_node = Text("Merkle Root", font_size=32, color=WHITE).move_to(UP * 3)
        
        level_1_nodes = VGroup(*[Text(f"Node 1.{i+1}", font_size=24, color=WHITE).next_to(root_node, DOWN, buff=0.5) for i in range(16)])
        
        level_2_nodes = VGroup(*[Text(f"Node 2.{i+1}", font_size=18, color=WHITE).next_to(level_1_nodes[0], DOWN, buff=0.5) for i in range(16)])
        
        level_3_nodes = VGroup(*[Text(f"Node 3.{i+1}", font_size=16, color=WHITE).next_to(level_2_nodes[0], DOWN, buff=0.5) for i in range(16)])

        arrows = []
        for node in level_1_nodes:
            arrows.append(Arrow(start=root_node.get_bottom(), end=node.get_top(), color=WHITE))
        
        for node in level_2_nodes:
            arrows.append(Arrow(start=level_1_nodes[0].get_bottom(), end=node.get_top(), color=WHITE))
        
        for node in level_3_nodes:
            arrows.append(Arrow(start=level_2_nodes[0].get_bottom(), end=node.get_top(), color=WHITE))

        self.play(Create(root_node))
        self.play(LaggedStartMap(Create, level_1_nodes, lag_ratio=0.1))
        self.play(LaggedStartMap(Create, arrows, lag_ratio=0.1))
        self.play(LaggedStartMap(Create, level_2_nodes, lag_ratio=0.1))
        self.play(LaggedStartMap(Create, level_3_nodes, lag_ratio=0.1))

        self.wait(2)
