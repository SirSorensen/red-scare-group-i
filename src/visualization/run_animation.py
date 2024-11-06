import sys
import pathlib
from manim import *
from manim.utils.file_ops import open_media_file
from graph_animate import GraphAnimation

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        input_lines = file.readlines()
    return [line.strip() for line in input_lines]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        print("Usage: python run_animation.py <file_name>")
        sys.exit(1)

    config.output_file = f"{file_name}-manim"
    # config.frame_size = (800, 800) # if we want to change the frame size
    
    # bugs out by some reason
    # if 'save' in sys.argv:
    #     config.save_last_frame = True
    
    root = pathlib.Path(__file__).resolve().parents[1]
    
    scene = GraphAnimation(file_name)
    scene.render()

    open_media_file(scene.renderer.file_writer)
