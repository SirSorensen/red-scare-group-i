from Gallery_of_Graphs.graph_interface import IGraph
from Utils.Longest_Path.longest_path import Longest_Path


class Longest_Path_Tree(Longest_Path):
    def __init__(self, g : IGraph):
        super().__init__(g)
        self.dist = self.longest_path_tree(g.node_colours, g.node_amount, g.edges)

    def build_tree_graph(self, N, edges):
        tree_graph = [[] for _ in range(N)]
        visited_edges = set()

        for u in range(N):
            for v in edges[u]:
                if (u, v) not in visited_edges and (v, u) not in visited_edges:
                    tree_graph[u].append(v)
                    tree_graph[v].append(u)
                    visited_edges.add((u, v))

        return tree_graph

    def dfs(self, node, parent, red_count, tree_graph, node_colours):
        self.visited[node] = True
        self.dist[node] = red_count

        for neighbor in tree_graph[node]:
            if not self.visited[neighbor]:
                is_red = 1 if node_colours[neighbor] == 1 else 0
                self.dfs(neighbor, node, red_count + is_red, tree_graph, node_colours)

    def longest_path_tree(self, node_colours, N, edges):
        tree_graph = self.build_tree_graph(N, edges)

        self.visited = [False] * N
        self.dfs(0, -1, 1 if node_colours[0] == 1 else 0, tree_graph, node_colours)

        return self.dist
