import os
import networkx as nx
from pathlib import Path

directory = '../../../data'

def print_result(filename, property, value):
    print(f"{filename:<25} {property}: {value}")

def check_graph_bipartite(filename, graph):
    property = 'bipartite'
    bipartite = nx.is_bipartite(graph)
    print_result(filename, property, bipartite)

def check_graph_acyclic(filename, graph):
    is_directed = graph.is_directed()
    if is_directed:
        property = 'directed acyclic'
        acyclic = nx.is_directed_acyclic_graph(graph)
    else:
        property = 'acyclic'
        acyclic = not bool(nx.cycle_basis(graph))
    print_result(filename, property, acyclic)

def check_graph_connected(filename, graph):
    is_directed = graph.is_directed()
    if is_directed:
        property = 'strongly connected'
        is_connected = nx.is_strongly_connected(graph)
    else:
        property = 'connected'
        is_connected = nx.is_connected(graph)
    print_result(filename, property, is_connected)

def check_graph_planarity(filename, graph):
    property = 'planarity'
    planarity, _ = nx.check_planarity(graph)
    print_result(filename, property, planarity)

def create_graph_from_file(filename):
    vertices = []
    edges = []
    cardinality_R = 0

    with open(filename, 'r') as f:
        first_line = f.readline().strip()
        vertices_no, edges_no, cardinality = map(int, first_line.split())
        cardinality_R = cardinality

        s, t = f.readline().strip().split()
        
        for _ in range(vertices_no):
            line = f.readline().strip()
            if line.endswith(" *"):
                vertex_name = line[:-2].strip()
            else:
                vertex_name = line.strip()
            vertices.append(vertex_name)
        
        for _ in range(edges_no):
            line = f.readline().strip()
            if "->" in line:
                u, v = map(str.strip, line.split("->"))
                edges.append((u, v, True))  # True = directed
            elif "--" in line:
                u, v = map(str.strip, line.split("--"))
                edges.append((u, v, False))  # False = undirected

    is_directed = any(edge[2] for edge in edges)

    graph = nx.DiGraph() if is_directed else nx.Graph()

    for vertex in vertices:
        graph.add_node(vertex)

    for u, v, directed in edges:
        if directed:
            graph.add_edge(u, v)  # Directed edge for DiGraph
        else:
            graph.add_edge(u, v)  # Undirected edge for Graph
    
    return graph, s, t, cardinality_R

if __name__ == '__main__':
    base_path = Path(__file__).resolve().parent
    directory = base_path / "../../data"
    directory = directory.resolve()

    graphs = []

    if not directory.is_dir():
        raise FileNotFoundError(f"Directory not found: {directory}")

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):  # Make sure it's a file, not a subdirectory
            graph, s, t, cardinality_R = create_graph_from_file(f)
            graphs.append((filename, graph))

    """
    for (filename, graph) in graphs:
        check_graph_bipartite(filename, graph)

    for (filename, graph) in graphs:
        check_graph_acyclic(filename, graph)

    for (filename, graph) in graphs:
        check_graph_connected(filename, graph)
    """
    for (filename, graph) in graphs:
        check_graph_planarity(filename, graph)
        

