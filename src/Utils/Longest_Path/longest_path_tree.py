from Gallery_of_Graphs.graph_interface import IGraph
from Utils.Longest_Path.longest_path import Longest_Path


class Longest_Path_Tree(Longest_Path):
    def __init__(self, g : IGraph):
        super().__init__(g)
        self.parent = [-1]*g.node_amount
        self.dfs(g.edges)
        self.calc_reds(g.node_amount, g.node_colours)



    def dfs(self, tree_graph : list[int]):
        self.stack.append(0)
        self.visited[0] = True

        while len(self.stack) > 0:
            node = self.stack.pop()

            for neighbor in tree_graph[node]:
                if not self.visited[neighbor]:
                    self.visited[neighbor] = True
                    self.parent[neighbor] = node
                    self.stack.append(neighbor)

    def calc_reds(self, N, node_colours : list[bool]):
        for node_index in range(N):
            reds = int(node_colours[node_index])
            cur_parent = self.parent[node_index]
            while cur_parent != -1:
                reds += int(node_colours[cur_parent])
                cur_parent = self.parent[cur_parent]
            self.dist[node_index] = reds






