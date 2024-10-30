""" 
    We consider a graph $G$ to have vertex set $V(G)$ and edge set $E(G)$.
    The graph can be directed or undirected.
    We only consider simple (no multiple edges between any pair of vertices) and unweighted graphs.
    Every graph has two specified vertices $s,t ∈ V(G)$ called the *start* and *end* vertices.
    Every graph has a subset $R ⊆ V(G)$ of *red* vertices. ($R$ can include $s$ and $t$)
    An (s,t)-path is a sequence of distinct vertices $v_1, ..., v_l$ such that $v_1=s$, $v_l=t$, and $v_i->v_{i+1} ∈ E(G)$ for each $i ∈ {1, ..., l-1}$.
    The *length* of such a path is $l-1$. (The number of edges)
    Note that this definition requires the vertices on a path to be distinct, this is sometimes called a *simple* path.
"""

class Graph:
    def __init__(self, input_lines : list[str]):
        # node_amount = |V(G)| = number of nodes
        # edge_amount = |E(G)| = number of edges
        # red_amount = |R| = number of red nodes
        self.node_amount, self.edge_amount, self.red_amount = map(int, input_lines[0].split())

        # start = s = index of starting node
        # end = t = index of ending node
        self.start, self.end = map(int, input_lines[1].split())

        node_inputs = input_lines[2:2+self.node_amount]
        self.node_colours = [(s[-1] == '*') for s in node_inputs]
        
        self.edges = [[] for _ in range(self.edge_amount)]
        edge_inputs = [s.split() for s in input_lines[3+self.node_amount:]]
        for input in edge_inputs:
            e_s = int(input[0])
            e_t = int(input[2])
            arrow = input[1]
            if arrow == "--":
                self.edges[e_s].append(e_t)
                self.edges[e_t].append(e_s)
            elif arrow == "->":
                self.edges[e_s].append(e_t)
            elif arrow == "<-": # Does not seem to happen ever
                self.edges[e_t].append(e_s)
            else:
                raise ValueError("Edge arrow not recognised.")

    def __str__(self) -> str:
        edges_str = ""
        for i in range(self.edge_amount):
            for dest_node in self.edges[i]:
                edges_str += f"\n   {i} -> {dest_node}"
        
        s = f"This graph has {self.node_amount} nodes, {self.edge_amount} edges, and {self.red_amount} red nodes.\n"
        s += f"Node colours (True if red, False if black) :\n   {self.node_colours}\n"
        s += f"Edges : {edges_str}"
        return s
        
    #### The problems we want solved for each graph are the following: ####
    """
        None:
        Return the length of a shortest (s,t)-path internally avoiding $R$.
        To be precise, let $P$ be the set of $s,t$-paths $v_1, ..., v_l$ such that $v_i ∉ R$ if $1<i<l$.
        Let $l(p)$ denote the length of a path $p$.
        Return $min{ l(p) : p ∈ P }$.
        If no such path exists, return `-1'.
        Note that the edge $st$, if it exists, is an (s,t)-path with $l=2$.
        Thus, if $s->t ∈ E(G)$ then the answer is 1, no matter the colour of $s$ or $t$.
    """
    def solve_none():
        ...

    """
        Some:
        Return `true' if there is a path from $s$ to $t$ that includes at least one vertex from $R$.
        Otherwise, return `false.'
    """
    def solve_some():
        ...
    
    """
        Many:
        Return the maximum number of red vertices on any path from $s$ to $t$.
        To be precise, let $P$ be the set of (s,t)-paths and let $r(p)$ denote the number of red vertices on a path $p$.
        Return $max{ r(p) : p ∈ P }$.
        If no path from $s$ to $t$ exists, return `-1'.
    """
    def solve_many():
        ...
    
    """
        Few:
        Return the minimum number of red vertices on any path from $s$ to $t$.
        To be precise, let $P$ be the set of (s,t)-paths and let $r(p)$ denote the number of red vertices  on a path $p$.
        Return $min{ r(p) : p ∈ P }$.
        If no path from $s$ to $t$ exists, return `-1'.
    """
    def solve_few():
        ...
    
    """
        Alternate:
        Return `true' if there is a path from $s$ to $t$ that alternates between red and non-red vertices.
        To be precise, a path $v_1, ..., v_l$ is *alternating* if for each $i ∈ {1, ..., l-1}$, exactly one endpoint of the edge $v_i--v_{i+1}$ is red.
        Otherwise, return `false.'
    """
    def solve_alternate():
        ...
    


    