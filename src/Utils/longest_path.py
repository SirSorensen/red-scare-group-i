# From https://www.geeksforgeeks.org/find-longest-path-directed-acyclic-graph/
	# This code is contributed to GeeksForGeeks by mohit kumar 29.
# A recursive function used by longestPath. See below 
# link for details 
# https:#www.geeksforgeeks.org/topological-sorting/ 

class Longest_Path:
	def __init__(self, N, s, t, edges, node_colours):
		self.table, self.visited = [], [False for i in range(N)] 
		
		s = 0
		processed_graph = self.preprocess(N, edges, s, node_colours)
		self.dist = self.longest_path(processed_graph, edges, node_colours)
		
	def preprocess(self, N, edges, s, node_colours):
		dist = [-10**9 for _ in range(N)]  

		for i in range(N):
			if (self.visited[i] == False): 
				self.topological_sort_util(edges, i) 

		if node_colours[s]:
			dist[s] = 1
		else:
			dist[s] = 0
		return dist


	def topological_sort_util(self, edges, n): 
		self.visited[n] = True

		for i in edges[n]: 
			if (not self.visited[i]): 
				self.topological_sort_util(edges,i) 

		self.table.append(n) 

	def longest_path(self, dist, edges, node_colours): 

		while (len(self.table) > 0): 
			
			u = self.table[-1] 

			del self.table[-1] 

			if (dist[u] != 10**9): 
				for i in edges[u]: 
					
					if node_colours[i]:
						val = 1
					else: 
						val = 0

					if (dist[i] < dist[u] + val): 
						dist[i] = dist[u] + val 
		return dist