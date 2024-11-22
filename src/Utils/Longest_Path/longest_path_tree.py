from Gallery_of_Graphs.graph_interface import IGraph
from Utils.Longest_Path.longest_path import Longest_Path


class Longest_Path_Tree(Longest_Path):
    def __init__(self, g : IGraph):
        super().__init__(g)
        self.dfs(0, -1, g.edges, g.node_colours)


    def dfs(self, node : int, red_count : int, tree_graph : list[int], node_colours : list[bool]):
        self.visited[node] = True
        self.dist[node] = red_count

        for neighbor in tree_graph[node]:
            if not self.visited[neighbor]:
                self.dfs(neighbor, node, tree_graph, node_colours)
        
