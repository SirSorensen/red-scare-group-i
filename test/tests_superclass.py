import sys
import unittest

sys.path.append('../src')
from Gallery_of_Graphs.graph import Graph
from Utils.graph_factory import construct_graph

class UnitTests(unittest.TestCase):
    def test_example(self):
        ...

    def test_individuals(self):
        ...

    def test_word_graphs(self):
        ...

    def test_grids(self):
        ...
    
    def test_walls(self):
        ...

    def test_ski(self):
        ...

    def test_increase(self):
        ...

    ###     Helper functions     ###
    def _act_assert(self, file_name, expected):
        # Arrange
        g : Graph = construct_graph(file_name)

        # Act
        actual = self._solve(g)

        # Arrange
        self.assertEqual(actual, expected, self._get_failure_str(file_name, actual, expected, g))
    
    def _solve(self, g : Graph):
        ...
    
    def _get_failure_str(self, file_name, actual, expected, g):
        return f"n\n{file_name} gave {actual} but should have given {expected}.\n\nGraph details:\n{g}"

if __name__ == '__main__':
    unittest.main()