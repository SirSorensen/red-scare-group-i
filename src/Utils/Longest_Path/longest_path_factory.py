
from collections import deque
from Gallery_of_Graphs.graph_interface import IGraph
from Utils.Longest_Path.longest_path_directed_graph import Longest_Path_Directed_Graph
from Utils.Longest_Path.longest_path_tree import Longest_Path_Tree
from Utils.Longest_Path.longest_path import Longest_Path

def longest_path_result(g : IGraph) -> str:
    if g.is_directed and not cycle_detection_directed(g.node_amount, g.edges):
        return Longest_Path_Directed_Graph(g).dist[g.end]
    elif not g.is_directed and not dfs_cycle_detection_undirected([False] * g.node_amount, 0, -1, g.edges):
        return Longest_Path_Tree(g).dist[g.end]
    else:
        return "?"


def dfs_cycle_detection_undirected(visited, node, parent, edges):
    visited[node] = True
    for neighbor in edges[node]:
        if not visited[neighbor]:
            if dfs_cycle_detection_undirected(visited, neighbor, node, edges):
                return True
        elif neighbor != parent:
            return True
    return False

# Cycle detection algorithm for directed graphs, taken from https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
def cycle_detection_directed(V, adj):
    in_degree = [0] * V
    q = deque()
    visited = 0

    for u in range(V):
        for v in adj[u]:
            in_degree[v] += 1

    for u in range(V):
        if in_degree[u] == 0:
            q.append(u)

    while q:
        u = q.popleft()
        visited += 1

        for v in adj[u]:
            in_degree[v] -= 1
            
            if in_degree[v] == 0:
                q.append(v)

    return visited != V


