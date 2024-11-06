import re
import sys
import pathlib
import logging
from Gallery_of_Graphs.graph import Graph

logging.basicConfig(level=logging.DEBUG)


def construct_graph(file_name) -> Graph:
    root = pathlib.Path(__file__).resolve().parent.parent.parent
    path = root / 'data' / f'{file_name}.txt'
    
    if 'debug' in sys.argv:
        logging.debug(f"Path: {path}")
    
    with open(path, "r") as file:  
        input_lines = file.read().splitlines()
 
    return Graph(input_lines)
