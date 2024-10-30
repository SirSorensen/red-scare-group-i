# Translated to python from https://algs4.cs.princeton.edu/44sp/DijkstraSP.java.html

import heapdict

class Dijkstra:
    def __init__(self, s : int, t : int, vertex_amount : int, edges_from : list[list[int]], node_colours : list[bool]):
        self.s = s
        self.t = t
        self.edges_from = edges_from
        self.node_colours = node_colours

        max_weight = 1.0
        for v in range(vertex_amount):
            for dest in edges_from[v]:
                max_weight += self.calc_weight(dest)

        self.distTo = [max_weight for _ in range(vertex_amount)]
        self.distTo[s] = 0.0

        self.edgeTo : list = [None]*vertex_amount
        self.pq : heapdict.heapdict = heapdict.heapdict()
        self.dijkstra()

    def dijkstra(self):

        # relax vertices in order of distance from s
        self.pq[self.s] = self.distTo[self.s]
        while len(self.pq.keys()) > 0:
            (k, weight) = self.pq.popitem()
            for w in self.edges_from[k]:
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

    
    def calc_weight(self, dest : int) -> int:
        if self.node_colours[dest]:
            return 1
        else:
            return 0
    
    def get_dist(self, v : int) -> float:
        return self.distTo[v]
    
    def get_path(self, v : int) -> list[int]:
        path = [v]
        while path[-1] != self.s:
            (source, dest, weight) = self.edgeTo[path[-1]]
            path.append(source)
        return path
    
    def path_to_str(self, v : int) -> str:
        path_str = [str(x) for x in self.get_path(v)]
        path_str.reverse()
        return ' -> '.join(path_str)

