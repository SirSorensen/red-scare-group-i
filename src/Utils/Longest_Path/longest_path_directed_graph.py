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
	def topological_sort_util(self, edges, n):
		self.visited[n] = True

		for i in edges[n]:
			if (not self.visited[i]):
				self.topological_sort_util(edges,i)

		self.stack.append(n)

	def longest_path(self, dist, edges, node_colours):

		while (len(self.stack) > 0):

			u = self.stack.pop()

			if (dist[u] != -1):
				for i in edges[u]:

					cur_dist = self.calc_red(i, u, node_colours)

					if (dist[i] < cur_dist):
						dist[i] = cur_dist
		return dist





