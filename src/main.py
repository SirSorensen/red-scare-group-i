from Utils.graph_factory import *
from Utils.result_printer import *

# uses 'G-ex' as default file name if no argument is given
file_name = 'G-ex' if len(sys.argv) < 2 else sys.argv[1]
print_solution(file_name)


### Outcomment if you want to print out all results: ###
#print_all_solution(print_to_file = True)
#print_latex_table(print_to_file = True)