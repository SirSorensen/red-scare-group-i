from Gallery_of_Graphs.graph_interface import IGraph
from Utils.Longest_Path.longest_path import Longest_Path


class Longest_Path_Tree(Longest_Path):
    def __init__(self, g : IGraph):
        super().__init__(g)
        self.parent = [-1]*g.node_amount

        self.stack.append(g.start)
        self.visited[g.start] = True
        self.dfs(g.edges, g.node_colours)



    def dfs(self, tree_graph : list[int], node_colours : list[bool]):
        while len(self.stack) > 0:
            node = self.stack.pop()

            for neighbor in tree_graph[node]:
                if not self.visited[neighbor]:
                    self.visited[neighbor] = True
                    self.parent[neighbor] = node
                    self.dist[neighbor] = self.calc_red(neighbor, node_colours)
                    self.stack.append(neighbor)
    
    def calc_red(self, node_index : int, node_colours : list[bool]) -> int:
        parent_reds : int = self.dist[self.parent[node_index]]
        if parent_reds < 0:
            raise ValueError("Parent has under 0 red nodes in path!")
        return parent_reds + int(node_colours[node_index])

