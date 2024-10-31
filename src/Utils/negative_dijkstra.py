# Translated to python from https://algs4.cs.princeton.edu/44sp/DijkstraSP.java.html

import sys
import heapdict
from Gallery_of_Graphs.graph_interface import IGraph
from Utils.dijkstra import Dijkstra

class NegativeDijkstra(Dijkstra):
    def __init__(self, G : IGraph):
        super().__init__(G, -1)

    def dijkstra(self):
        self.pq[self.G.start] = self.distTo[self.G.start]
        while len(self.pq.keys()) > 0:
            (k, _) = self.pq.popitem()
            if k != self.G.end:
                for w in self.G.edges[k]:
                    if not self.marked(k, w):
                        self.relax(k, w)
    
    def marked(self, source, dest):
        path = self.get_path(source)
        return dest in path

    def get_dist(self, v : int) -> int:
        dist = self.distTo[v]
        if dist == sys.maxsize:
            return 1
        else:
            return dist

