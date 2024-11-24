# Translated to python from https://algs4.cs.princeton.edu/41graph/DepthFirstPaths.java.html

from Gallery_of_Graphs.graph_interface import IGraph

class DepthFirstPaths:
    def __init__(self, G : IGraph):
        self.marked : list[bool] = [False]*G.node_amount
        self.edgeTo : list[int] = [-1]*G.node_amount
        self.s : int = G.start
        self.dfs(G, self.s)
    
    
    def dfs(self, G : IGraph, s : int):
        stack = []
        self.marked[s] = True
        stack.append(s)
        while (len(stack) > 0):
            v : int = stack.pop()
            for w in G.edges[v]:
                if not self.marked[w]:
                    self.edgeTo[w] = v
                    self.marked[w] = True
                    stack.append(w)


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
    


    def calc_red(self, t : int, node_colours : list[bool]) -> int:
        parent : int = self.edgeTo[t]
        if parent == -1:
            return -1
        
        dist = int(node_colours[t])

        while parent != self.s:
            dist += int(node_colours[parent])
            parent = self.edgeTo[parent]

        return dist + int(node_colours[self.s])