import sys
import networkx as nx
import matplotlib.pyplot as plt
import pathlib

def read_graph_from_file(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    
    node_count = int(lines[0].split()[0])
    start, end = lines[1].split()
    
    edges = []
    red_nodes = set()
    for line in lines:
        if '--' in line:
            nodes = line.split('--')
            edges.append((nodes[0].strip(), nodes[1].strip()))
            edges.append((nodes[1].strip(), nodes[0].strip()))
        elif '->' in line:
            nodes = line.split('->')
            edges.append((nodes[0].strip(), nodes[1].strip()))
        elif '*' in line:
            node = line.split()[0]
            red_nodes.add(node.strip())
    
    return edges, red_nodes, node_count, start, end

def draw_graph(edges, red_nodes, node_count, start, end):
    G = nx.Graph()
    G.add_edges_from(edges)
    
    n = int(node_count ** 0.5)
    
    pos = {f"{i}_{j}": (i, j) for i in range(n) for j in range(n)}
    node_colors = ['orange' if node in red_nodes and node == start else
                   'purple' if node in red_nodes and node == end else
                   'red' if node in red_nodes else 
                   'green' if node == start else 
                   'blue' if node == end else
                   'skyblue' for node in G.nodes()]
    
    # Calculate figure size dynamically
    fig_size = max(5, n)
    plt.figure(figsize=(fig_size, fig_size))
    
    # Adjust font size dynamically
    font_size = 8 # max(8, 200 // n)
    
    nx.draw(G, pos, with_labels=True, node_size=700, node_color=node_colors, font_size=font_size, font_color='black', font_weight='bold')

if __name__ == "__main__":  
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        print("Usage: python grid_draw.py <file_name>")
        sys.exit(1)
    
    root = pathlib.Path(__file__).resolve().parents[2]
    filepath = root / 'data' / f'{file_name}.txt'
    
    edges, red_nodes, node_count, start, end = read_graph_from_file(filepath)
    draw_graph(edges, red_nodes, node_count, start, end)
    
    plt.savefig(root / 'media' / 'images' / f'{file_name}.png')
    
    if 'show' in sys.argv:
        plt.show()
