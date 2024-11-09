from Utils.graph_factory import *
from Gallery_of_Graphs.graph import Graph

# uses 'G-ex' as default file name if no argument is given
file_name = 'G-ex' if len(sys.argv) < 2 else sys.argv[1]

g : Graph = construct_graph(file_name)

print(g)

g.solve_many()