from Gallery_of_Graphs.graph_interface import IGraph
from Utils.Longest_Path.longest_path import Longest_Path


class Longest_Path_Tree(Longest_Path):
    def __init__(self, g : IGraph):
        super().__init__(g)
        self.longest_path_tree(g.node_colours, g.node_amount, g.edges)

    def build_tree_graph(self, N : int, edges : list[list[int]]) -> list[int]:
        tree_graph = [[] for _ in range(N)]
        visited_edges = set()

        for u in range(N):
            for v in edges[u]:
                if (u, v) not in visited_edges and (v, u) not in visited_edges:
                    tree_graph[u].append(v)
                    tree_graph[v].append(u)
                    visited_edges.add((u, v))

        return tree_graph

    def dfs(self, node : int, red_count : int, tree_graph : list[int], node_colours : list[bool]):
        self.visited[node] = True
        self.dist[node] = red_count

        for neighbor in tree_graph[node]:
            if not self.visited[neighbor]:
                self.dfs(neighbor, node, tree_graph, node_colours)

    def longest_path_tree(self, node_colours : list[bool], N : int, edges : list[list[int]]):
        tree_graph = self.build_tree_graph(N, edges)
        self.dfs(0, -1, tree_graph, node_colours)
