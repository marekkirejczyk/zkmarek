import networkx as nx
from manim import Graph


class VerkleTree(Graph):
    def __init__(self):
        G = nx.Graph()
        G.add_node("ROOT")
        for i in range(5):
            G.add_node("Child_%i" % i)
            G.add_node("Grandchild_%i" % i)
            G.add_node("Greatgrandchild_%i" % i)
            G.add_edge("ROOT", "Child_%i" % i)
            G.add_edge("Child_0", "Grandchild_%i" % i)
            G.add_edge("Grandchild_1", "Greatgrandchild_%i" % i)
        super().__init__(list(G.nodes),
                         list(G.edges),
                         layout="tree",
                         root_vertex="ROOT")
