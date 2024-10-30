from graph import Graph

"""
    SkiFree is an ancient computer game by Chris Pirih, part of the Microsoft Entertainment Pack in 1991, and going back to VT100 VAX/VMS terminals, ultimately inspired by Activision's *Skiing* for the Atari 2600 console.

    Time to show you can handle yourself off-pist. Get from the start to the goal, avoiding the trees, dogs rocks etc.
    Beware of the dreaded Yeti who is told to lurk at the red nodes of the mountain and will certainly chase you down and eat you if you pass him.

    In each level, the player moves down, and either one step left or right.
    (Some moves are blocked by obstacles.)
"""

class Ski(Graph):
    def __init__(self, input_lines : list[str]):
        super().__init__(input_lines)