
import re
from Gallery_of_Graphs.grid import Grid
from Gallery_of_Graphs.increase import Increase
from Gallery_of_Graphs.ski import Ski
from Gallery_of_Graphs.wall import Wall
from Gallery_of_Graphs.word_graph import WordGraph
from Gallery_of_Graphs.graph import Graph



def construct_graph(file_name) -> Graph:
    file_path = f'../data/{file_name}.txt'
    with open(file_path, "r") as file:  
        input_lines = file.read().splitlines()
 
    # Regex match case has taken inspiration from https://stackoverflow.com/a/72538070
    pattern = re.compile(
        r"""(?P<grid>grid-\d+-\d+)|(?P<increase>increase-n\d+-\d+)|(?P<ski>ski-\w+)|(?P<wall>wall-\w-\d+)|(?P<word>(?:rusty|common)-\d+-\d+)"""
    )
    
    mo = pattern.fullmatch(file_name)
    if mo is not None:
        match mo.lastgroup:
            case 'grid':
                return Grid(input_lines)
            case 'increase':
                return Increase(input_lines)
            case 'ski':
                return Ski(input_lines)
            case 'wall':
                return Wall(input_lines)
            case 'word':
                return WordGraph(input_lines)
            case _:
                return Graph(input_lines)
    else:
        return Graph(input_lines)
