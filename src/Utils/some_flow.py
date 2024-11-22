import copy
from collections import deque, defaultdict
from Gallery_of_Graphs.graph_interface import IGraph


def bfs(source: int, sink: int, parent: dict, cap: dict, flow: dict, adjList: dict) -> bool:
    visited = set()
    queue = deque([source])
    visited.add(source)

    while queue:
        current = queue.popleft()
        for neighbor in adjList[current]:
            if neighbor not in visited and cap[current][neighbor] - flow[current][neighbor] > 0:
                parent[neighbor] = current
                visited.add(neighbor)
                if neighbor == sink:
                    return True
                queue.append(neighbor)
    return False

#Inspired by https://www.w3schools.com/dsa/dsa_algo_graphs_edmondskarp.php
def edmonds_karp(start, end, cap, flow, adjList) -> int:
    source = start
    sink = end
    parent = {}
    max_flow = 0

    while bfs(source, sink, parent, cap, flow, adjList):
        path_flow = float('Inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, cap[parent[s]][s] - flow[parent[s]][s])
            s = parent[s]
        v = sink
        while v != source:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = parent[v]
        max_flow += path_flow
    return max_flow

class some_flow:
    def __init__(self, G : IGraph):
        self.graph = G
        self.capacity = defaultdict(lambda: defaultdict(int))
        self.flow = defaultdict(lambda: defaultdict(int))
        self.adj_list = defaultdict(list)

        # Self Edges
        for u in range(G.node_amount):
            self.capacity[u][u + self.graph.node_amount] = 1
            self.adj_list[u].append(u + self.graph.node_amount)

        # Add edges to initial capacity & adjacency-list
        for u in range(len(G.edges)):
            for v in G.edges[u]:
                self.capacity[u + self.graph.node_amount][v] = 1
                self.adj_list[u + self.graph.node_amount].append(v)
                # Add reverse edge for residual graph
                self.adj_list[v].append(u + self.graph.node_amount)

        # Append super-source (N*2) to start
        self.capacity[G.node_amount*2][G.start + self.graph.node_amount] = 1
        self.adj_list[G.node_amount*2].append(G.start + self.graph.node_amount)

        # Append super-source (N*2) to end
        self.capacity[G.node_amount*2][G.end + self.graph.node_amount] = 1
        self.adj_list[G.node_amount*2].append(G.end + self.graph.node_amount)

    def some(self) -> bool:
        reds = []
        for i in range(self.graph.node_amount):
            if self.graph.node_colours[i]:
                reds.append(i)

        # If either start or end is red - bfs from start to end
        if self.graph.start in reds or self.graph.end in reds:
            return bfs(self.graph.start, self.graph.end, {}, self.capacity, self.flow, self.adj_list)

        for red in reds:
            # Create clean state for unique run of max-flow algo.
            flow_state = copy.deepcopy(self.flow)
            flow_network = copy.deepcopy(self.capacity)
            adj_list = copy.deepcopy(self.adj_list)

            # Add sink to red node w. cap 2.
            flow_network[red][(self.graph.node_amount*2) + 1] = 2
            adj_list[red].append((self.graph.node_amount*2) + 1)

            if edmonds_karp((self.graph.node_amount*2), red, flow_network, flow_state, adj_list) == 2:
                return True

        return False