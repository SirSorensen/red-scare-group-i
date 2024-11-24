from Gallery_of_Graphs.graph_interface import IGraph

class Longest_Path:
	def __init__(self, g : IGraph, graphIsSupported = True):
		self.stack = []
		self.visited = [False] * g.node_amount
		self.dist = [-1] * g.node_amount
		self.dist[g.start] = int(g.node_colours[g.start])
		self.graphIsSupported = graphIsSupported

	def calc_red(self, node_index : int, parent_index : int, node_colours : list[bool]) -> int:
		parent_reds : int = self.dist[parent_index]
		if parent_reds < 0:
			raise ValueError("Parent has under 0 red nodes in path!")
		return parent_reds + int(node_colours[node_index])