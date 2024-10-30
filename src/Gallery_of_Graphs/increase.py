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
        super().__init__(input_lines)