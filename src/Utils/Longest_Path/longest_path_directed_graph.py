# Original code from https://www.geeksforgeeks.org/find-longest-path-directed-acyclic-graph/
	# This code is contributed to GeeksForGeeks by mohit kumar 29.

class Longest_Path_Directed_Graph:
	def __init__(self, N, s, edges, node_colours):
		self.stack = []
		self.visited =[False] * N
		self.dist = [-1] * N

		processed_graph = self.preprocess(N, edges, s, node_colours)
		self.dist = self.longest_path(processed_graph, edges, node_colours)


	def preprocess(self, N, edges, s, node_colours):
		dist = [-10**9] * N
		dist[s] = int(node_colours[s])

		for i in range(N):
			if not self.visited[i]:
				self.topological_sort_util(edges, i)

		return dist

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

			if (dist[u] != 10**9):
				for i in edges[u]:

					val = int(node_colours[i])
					cur_dist = dist[u] + val

					if (dist[i] < cur_dist):
						dist[i] = cur_dist
		return dist





