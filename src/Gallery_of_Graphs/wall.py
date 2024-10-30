from Gallery_of_Graphs.graph import Graph

"""
    The Wall graphs are a family consisting of $N$ overlapping 8-cycles called *bricks$.
    The bricks are laid in a wall of height 2, with various intervals of overlap.
    Each wall has a single red vertex $w$, the rightmost vertex at the same level as vertex $0$.
    These graphs are interesting instances for finding paths from $s$ to $t$ through the red vertex.
    The should help you avoid some obvious pitfalls when developing an algorithm for the problem *Some$.

    The Walls with overlap 1, called "brick-1-$N$", allow an $s,t$-path through $w$.

    The Walls with overlap 0, called "brick-0-$N$", allow a walk from $s$ to $t$ through $w$, but this walk will use $N-2$ vertices twice. 
    In particular, such a walk it not a path, and your algorithm for Problem *Some$ should not be fooled by it.

    The walls with negative overlap, called "brick-n-$N$" also allow a walk from $s$ to $t$ through $w$, but this walk would use $N-2$ edges twice.
    Again, such walk is not a path.
"""

class Wall(Graph):
    def __init__(self, input_lines : list[str]):
        super().__init__(input_lines)