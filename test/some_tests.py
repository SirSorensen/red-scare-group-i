import sys
import unittest

from tests_interface import TestsInterface

sys.path.append('../src')
from Gallery_of_Graphs.graph import Graph

class SomeTests(TestsInterface):
    def test_example(self):
        self._act_assert('G-ex', True)

    def test_individuals(self):
        self._act_assert('P3-0', True)
        self._act_assert('P3-1', False)
        self._act_assert('K3-0', True)
        self._act_assert('K3-1', True)
        self._act_assert('K3-2', False)

    def test_word_graphs(self):
        self._act_assert('rusty-1-17', True)
        self._act_assert('common-1-20', False)

    def test_grids(self):
        self._act_assert('grid-5-0', True)
    
    def test_walls(self):
        self._act_assert('wall-p-1', True)
        self._act_assert('wall-p-3', True)
        self._act_assert('wall-z-3', False)
        self._act_assert('wall-n-2', False)

    def test_ski(self):
        self._act_assert('ski-illustration', True)

    def test_increase(self):
        self._act_assert('increase-n8-1', True)
        self._act_assert('increase-n8-2', True)

    ### Helper methods ###
    def _solve(self, g : Graph):
        return g.solve_some()


if __name__ == '__main__':
    unittest.main()