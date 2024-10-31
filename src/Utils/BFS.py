# Translated to python from https://algs4.cs.princeton.edu/41graph/BreadthFirstPaths.java.html

from Gallery_of_Graphs.graph_interface import IGraph
from queue import Queue

class BreadthFirstPaths:
    def __init__(self, G : IGraph, skip_red = False):
        self.marked : list[bool] = [False]*G.node_amount
        self.edgeTo : list[int] = [-1]*G.node_amount
        self.s : int = G.start
        self.bfs(G, self.s, skip_red)
    
    
    def bfs(self, G : IGraph, s : int, skip_red : bool):
        if skip_red and G.node_colours[s]:
            return
        
        queue = Queue()
        self.marked[s] = True
        queue.put(s)
        while (not queue.empty()):
            v : int = queue.get()
            for w in G.edges[v]:
                if not self.marked[w] and (skip_red and not G.node_colours[w]):
                    self.edgeTo[w] = v
                    self.marked[w] = True
                    queue.put(w)

    def hasPathTo(self, v : int) -> bool:
        return self.marked[v]
    
    
    def pathTo(self, v: int) -> list[int]:
        if not self.hasPathTo(v):
            return None
        path = []
        x = v
        while x != -1:
            path.append(x)
            x = self.edgeTo[x]
        path.reverse()
        return path


    def pathLength(self, v: int) -> int:
        path = self.pathTo(v)
        if path is None:
            return -1
        return len(path) - 1