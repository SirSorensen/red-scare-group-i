from Gallery_of_Graphs.graph import Graph

"""
    Each *Increase* graph is generated from a sequence $a_1, ..., a_n$ of unique integers with $0 α_i ≤ 2n$.
    (The random process is this: Pick a subset of size $n$ from ${0, ..., 2n}$ and arrange the elements in random order.)
    We set $s=α_1$ and $t=α_n$.
    Odd numbers are red.
    There is an edge from  $α_i$ to $α_j$ if $i<j$ and $α_i<α_j$.
"""

class Increase(Graph):
    def __init__(self, input_lines : list[str]):
        self.node_ids = {}
        super().__init__(input_lines)
    
    # Helper functions for specific graph-types
    def node_to_id(self, node_str) -> int:
        node_val = int(node_str)
        node_id = self.node_ids.get(node_val)
        if node_id is None:
            node_id = len(self.node_ids)
            self.node_ids[node_val] = node_id
        return node_id
    
    def ids_to_nodes(self, node_ids : list[int]):
        rev_dict = {v:k for (k,v) in self.node_ids.items()}
        originals = [str(rev_dict[node_id]) for node_id in node_ids]
        for i in range(len(node_ids)):
            _id = node_ids[i]
            if self.node_colours[_id]:
                originals[i] = f"*{originals[i]}*"
        return originals