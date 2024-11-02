import pathlib
import sys

path = str(pathlib.Path(__file__).resolve().parents[1])

sys.path.append(path)

from manim import *
from Gallery_of_Graphs.graph import Graph as CustomGraph
from Utils.graph_factory import construct_graph

class GraphAnimation(Scene):
    def __init__(self, file_path, **kwargs):
        super().__init__(**kwargs)
        self.file_name = file_path
    
    def construct(self):
        custom_graph = construct_graph(self.file_name)

        vertices = [str(i) for i in range(custom_graph.node_amount)]
        edges = [
            (str(e_s), str(e_t))
            for e_s in range(custom_graph.node_amount)
            for e_t in custom_graph.edges[e_s]
        ]
        root_node = custom_graph.start
        end_node = custom_graph.end
        # constants.DEFAULT_FONT_SIZE = 10
        
        g = Graph(vertices, edges, labels=True, layout="kamada_kawai", layout_scale=4.5)
        
        g = g.scale_to_fit_height(config.frame_height - 0.5)
        
        # print(f"frame width: {config.frame_width}")
        # print(f"frame height: {config.frame_height}")
        # print(f"graph width: {g.width}")
        # print(f"graph height: {g.height}")
        
        self.play(Create(Text(self.file_name).scale(0.8).to_edge(UL)))
        self.play(Create(g), run_time=5, lag_ratio=0.1)

        self.wait(2)
