# Translated to python from https://algs4.cs.princeton.edu/41graph/BreadthFirstPaths.java.html

from Gallery_of_Graphs.graph import Graph
from queue import Queue

class BreadthFirstPaths:
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
            for w in G.edges[v]:
                if not self.marked[w]:
                    self.edgeTo[w] = v
                    self.marked[w] = True
                    queue.put(w)

    def hasPathTo(self, v : int) -> bool:
        return self.marked[v]