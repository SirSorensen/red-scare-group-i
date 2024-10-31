import re
import sys
import pathlib
import logging
from Gallery_of_Graphs.grid import Grid
from Gallery_of_Graphs.increase import Increase
from Gallery_of_Graphs.ski import Ski
from Gallery_of_Graphs.wall import Wall
from Gallery_of_Graphs.word_graph import WordGraph
from Gallery_of_Graphs.graph import Graph

logging.basicConfig(level=logging.DEBUG)


def construct_graph(file_name) -> Graph:
    root = pathlib.Path(__file__).resolve().parent.parent.parent
    path = root / 'data' / f'{file_name}.txt'
    
    if 'debug' in sys.argv:
        logging.debug(f"Path: {path}")
    
    with open(path, "r") as file:  
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
