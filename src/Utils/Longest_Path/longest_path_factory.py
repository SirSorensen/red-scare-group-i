
from Gallery_of_Graphs.graph_interface import IGraph
from Utils.Longest_Path.longest_path_directed_graph import Longest_Path_Directed_Graph
from Utils.Longest_Path.longest_path_tree import Longest_Path_Tree
from Utils.Longest_Path.longest_path import Longest_Path


def gen_longest_path(g : IGraph) -> Longest_Path:
        if g.is_directed:
            return Longest_Path_Directed_Graph(g)
        elif is_acyclic_and_connected(g.node_amount, g.edges):
            return Longest_Path_Tree(g)
        else:
            return Longest_Path(g, True)

def is_acyclic_and_connected(N, edges):
    visited = [False] * N

    def is_connected():
        stack = [0]
        seen = set()
        while stack:
            node = stack.pop()
            if node in seen:
                continue
            seen.add(node)
            for neighbor in edges[node]:
                if neighbor not in seen:
                    stack.append(neighbor)
        return len(seen) == N

    def dfs_cycle_detection_undirected(node, parent):
        visited[node] = True
        for neighbor in edges[node]:
            if not visited[neighbor]:
                if dfs_cycle_detection_undirected(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    if dfs_cycle_detection_undirected(0, -1):
        return False

    if not is_connected():
        return False

    return True



