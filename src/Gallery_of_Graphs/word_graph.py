from Gallery_of_Graphs.graph import Graph

"""
    In the word graphs, each vertex represents a five-letter word of English.
    For $k ∈ {1,2}$, an edge joins $u$ and $v$ if the corresponding words are anagrams, or if they differ in exactly $k$ positions.
    For instance ``begin'' and ``binge'' are neighbours, and so are ``turns'' and ``terns'' for $k=1$.

    The word graphs  come in two flavours.
    The *rusty word* graphs are guaranteed to include ``begin,'' ``ender,'' and ``rusty.''
    The vertex corresponding to ``rusty'' is coloured red, no other vertices are red.

    The filenames are "rusty-$k$-$n$".
"""

class WordGraph(Graph):
    def __init__(self, input_lines : list[str]):
        self.node_ids : dict[str, int] = {}
        super().__init__(input_lines)
    
    def node_to_id(self, node_str : str):
        node_id = self.node_ids.get(node_str)
        if node_id is None:
            node_id = len(self.node_ids)
            self.node_ids[node_str] = node_id
        return node_id
    
    def ids_to_nodes(self, node_ids : list[int]):
        rev_dict = {v:k for (k,v) in self.node_ids.items()}
        originals = [rev_dict[node_id] for node_id in node_ids]
        for i in range(len(node_ids)):
            _id = node_ids[i]
            if self.node_colours[_id]:
                originals[i] = f"*{originals[i]}*"
        return originals