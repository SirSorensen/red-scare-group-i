from Gallery_of_Graphs.graph_interface import IGraph

class Longest_Path:
	def __init__(self, g : IGraph, graphIsSupported = True):
		self.stack = []
		self.visited = [False] * g.node_amount
		self.dist = [-1] * g.node_amount
		self.dist[g.start] = int(g.node_colours[g.start])
		self.graphIsSupported = graphIsSupported