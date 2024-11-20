from Utils.graph_factory import *
from Gallery_of_Graphs.graph import Graph
from Utils.result_printer import *

# uses 'G-ex' as default file name if no argument is given
file_name = 'G-ex' if len(sys.argv) < 2 else sys.argv[1]

print_all_solution(print_to_file = True)