# Translated to python from https://algs4.cs.princeton.edu/44sp/DijkstraSP.java.html

import sys
import heapdict
from Gallery_of_Graphs.graph_interface import IGraph

class Dijkstra:
    def __init__(self, G : IGraph, red_weight = 1):
        self.distTo = [sys.maxsize for _ in range(G.node_amount)]
        self.distTo[G.start] = red_weight if G.node_colours[G.start] else 0

        self.edgeTo : list = [None]*G.node_amount
        self.pq : heapdict.heapdict = heapdict.heapdict()
        self.G = G
        self.red_weight = red_weight

        self.dijkstra()

    def dijkstra(self):
        self.pq[self.G.start] = self.distTo[self.G.start]
        while len(self.pq.keys()) > 0:
            (k, _) = self.pq.popitem()
            for w in self.G.edges[k]:
                self.relax(k, w)
    
    # relax edge e and update pq if changed
    # source = edge's source vertex
    # dest = edge's destination vertex
    def relax(self, source : int, dest : int):
        weight = self.calc_weight(dest)
        potential_new_weight = self.distTo[source] + weight
        if (self.distTo[dest] > potential_new_weight):
            self.distTo[dest] = potential_new_weight
            self.edgeTo[dest] = (source, dest, weight)
            self.pq[dest] = potential_new_weight

    # Return red_weight if dest is red, 0 if black
    def calc_weight(self, dest : int) -> int:
        return int(self.G.node_colours[dest])*self.red_weight
    
    def get_dist(self, v : int) -> int:
        dist = self.distTo[v]
        if dist == sys.maxsize:
            return -1
        else:
            return dist
    
    def get_path(self, v : int) -> list[int]:
        if self.edgeTo[v] is None:
            return []
        
        path = [v]
        while path[-1] != self.G.start:
            (source, _, _) = self.edgeTo[path[-1]]
            if source in path:
                return path
            path.append(source)
        return path
    
    def path_to_str(self, v : int) -> str:
        path_strs = self.G.ids_to_nodes(self.get_path(v))
        path_strs.reverse()
        return ' -> '.join(path_strs)

