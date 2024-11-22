from Gallery_of_Graphs.graph_interface import IGraph
from Utils.Longest_Path.longest_path import Longest_Path


class Longest_Path_Tree(Longest_Path):
    def __init__(self, g : IGraph):
        super().__init__(g)
        self.dfs(g.edges)



    def dfs(self, tree_graph : list[int]):
        self.stack.append(0)
        self.visited[0] = True

        while len(self.stack) > 0:
            node = self.stack.pop()

            for neighbor in tree_graph[node]:
                if not self.visited[neighbor]:
                    self.visited[neighbor] = True
                    self.dist[neighbor] = node
                    self.stack.append(neighbor)






