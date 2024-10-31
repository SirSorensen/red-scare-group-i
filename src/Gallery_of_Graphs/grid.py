import math
from Gallery_of_Graphs.graph import Graph

"""
    The Grid graphs consist of $N^2$ vertices that represent integer coordinates $(x,y)$ for $x,y ∈ {0, ..., N-1}$.
    Each vertex $(x,y)$ is connected to $(x-1,y)$, $(x,y-1)$, and $(x-1,y-1)$, provided that these vertices exist.
    The red vertices form a maze-like structure in the graph:
    Every second row is red, except for the top- or bottommost vertex, alternatingly.
    There is a unique $s,t$-path avoiding all red vertices, and a shortest alternating path following the diagonal.

    Grid graphs of various sizes are represented by "grid-$N$-0".
    Each of these graphs comes with two variants.
    In "grid-$N$-1", some random red vertices have turned non-red (so there are `holes' in the hedges).
    In "grid-$N$-2", some random non-red vertices have turned red (so some passages are blocked).
"""

class Grid(Graph):
    def __init__(self, input_lines : list[str]):
        super().__init__(input_lines)
    
    def node_to_id(self, s : str) -> tuple[int, int]:
        # In case side_length has not been init yet
        if not hasattr(int, 'side_length'):
            self.side_length = int(math.sqrt(self.node_amount))

        (a, b) = map(int, s.split('_'))
        return b + a*self.side_length

    def ids_to_nodes(self, node_ids : list[int]):
        originals = []
        for i in range(len(node_ids)):
            _id = node_ids[i]
            y = _id//self.side_length
            x = _id%self.side_length
            originals.append(f"{x}_{y}")
            if self.node_colours[_id]:
                originals[-1] = f"*{originals[-1]}*"
        return originals
