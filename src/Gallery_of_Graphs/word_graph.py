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
        self.node_dict : dict[str, int] = {}
        self.node_dict_size = 0
        super().__init__(input_lines)
    
    def node_to_int(self, s : str) -> tuple[int, int]:
        cached = self.node_dict.get(s)
        if cached is not None:
            return cached
        else:
            to_be_cached = self.node_dict_size
            self.node_dict[s] = to_be_cached
            self.node_dict_size += 1
            return to_be_cached
