from Gallery_of_Graphs.graph import Graph


file_name = 'G-ex'
file_path = f'../data/{file_name}.txt'
file = open(file_path, "r") 
input_lines = file.read().splitlines()
g = Graph(input_lines)

print(g)