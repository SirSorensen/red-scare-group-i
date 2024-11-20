from Utils.Longest_Path.longest_path_directed_graph import Longest_Path_Directed_Graph
from Utils.Longest_Path.longest_path_tree import Longest_Path_Tree

class Longest_Path:
	def __init__(self, N, s, t, edges, node_colours, is_directed):
            self.stack = []
            self.visited = [False] * N
            self.dist = [-1] * N 
            self.graphIsNotSupported = False 

            if is_directed:
                self.dist = Longest_Path_Directed_Graph(N, s, edges, node_colours).dist
            elif is_acyclic_and_connected(self, N, edges):		
                self.dist = Longest_Path_Tree(N, edges, node_colours, t).dist
            else:
                self.graphIsNotSupported = True  

def is_acyclic_and_connected(self, N, edges):
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



