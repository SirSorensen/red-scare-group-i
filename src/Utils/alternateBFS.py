from Gallery_of_Graphs.graph import Graph
from queue import Queue

class AlternateBreadthFirstPaths:
    def __init__(self, G : Graph):
        self.marked : list[bool] = [False]*G.node_amount
        self.edgeTo : list[int] = [0]*G.node_amount
        self.s : int = G.start
        self.bfs(G, self.s)
    
    
    def bfs(self, G : Graph, s : int):
        queue = Queue()
        self.marked[s] = True
        queue.put(s)
        while (not queue.empty()):
            v : int = queue.get()
            color : bool = G.node_colours[v]
            for w in G.edges[v]:
                if not self.marked[w] and G.node_colours[w] != color:
                    self.edgeTo[w] = v
                    self.marked[w] = True
                    queue.put(w)

    def hasPathTo(self, v : int) -> bool:
        return self.marked[v]