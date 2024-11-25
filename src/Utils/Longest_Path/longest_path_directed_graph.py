# Original code from https://www.geeksforgeeks.org/find-longest-path-directed-acyclic-graph/
	# This code is contributed to GeeksForGeeks by mohit kumar 29.

from Gallery_of_Graphs.graph_interface import IGraph
from Utils.Longest_Path.longest_path import Longest_Path


class Longest_Path_Directed_Graph(Longest_Path):
	def __init__(self, g : IGraph):
		super().__init__(g)
		
		self.preprocess(g.node_amount, g.edges)
		self.dist = self.longest_path(self.dist, g.edges, g.node_colours)


	def preprocess(self, N, edges):
		for i in range(N):
			if not self.visited[i]:
				self.topological_sort_util(edges, i)

	#  May yield better performance with Kahn's topological sort
	def topological_sort_util(self, edges, node_index):
		self.visited[node_index] = True

		for neighbor in edges[node_index]:
			if not self.visited[neighbor]:
				self.topological_sort_util(edges, neighbor)
		
		self.stack.append(node_index)


	def longest_path(self, dist, edges, node_colours):

		while (len(self.stack) > 0):

			v = self.stack.pop()

			if (dist[v] != -1):
				for u in edges[v]:
					cur_dist = self.calc_red(u, v, node_colours)

					if (dist[u] < cur_dist):
						dist[u] = cur_dist
		return dist
	
	def calc_red(self, node_index : int, parent_index : int, node_colours : list[bool]) -> int:
		parent_reds : int = self.dist[parent_index]
		if parent_reds < 0:
			raise ValueError("Parent has under 0 red nodes in path!")
		return parent_reds + int(node_colours[node_index])





