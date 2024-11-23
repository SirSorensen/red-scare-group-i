import sys
import unittest
import pathlib

src = pathlib.Path(__file__).resolve().parent.parent / 'src'

sys.path.append(str(src))
from Gallery_of_Graphs.graph import Graph
from Utils.graph_factory import construct_graph

results = {}

class UnitTests(unittest.TestCase):

    def test_directed_cyclic(self):
        ...

    def test_directed_acyclic(self):
        ...

    def test_undirected_cyclic(self):
        ...
    
    def test_undirected_acyclic(self):
        ...

    ###     Helper functions     ###
    def _act_assert(self, file_name, expected):
        # Arrange
        g : Graph = construct_graph(file_name)

        # Act
        actual = self._solve(g)
        
        self.expected = expected
        self.actual = actual
        self.file = file_name

        if 'list' in sys.argv:
            results[file_name] = [actual, expected]
            solution_type = self.solutionType if hasattr(self, 'solutionType') else ''
            print(f"{solution_type} {file_name}; Actual: {actual}   Expected: {expected}.")
        
        # Arrange
        self.assertEqual(actual, expected, self._get_failure_str(file_name, actual, expected, g))

    
    def _get_failure_str(self, file_name, actual, expected, g):
        return f"n\n{file_name} gave {actual} but should have given {expected}.\n\nGraph details:\n{g}"

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)