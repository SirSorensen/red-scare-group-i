from Utils.DFS import DepthFirstPaths
from Gallery_of_Graphs.graph_interface import IGraph
from Utils.Longest_Path.longest_path import Longest_Path


class Longest_Path_Tree(Longest_Path):
    def __init__(self, g : IGraph):
        super().__init__(g)
        self.parent = [-1]*g.node_amount

        dfs = DepthFirstPaths(g)
        self.dist = [-1]*g.node_amount
        self.dist[g.end] = dfs.calc_red(g.end, g.node_colours)
