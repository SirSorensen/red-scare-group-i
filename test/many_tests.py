import sys
import unittest

from tests_superclass import UnitTests

sys.path.append('../src')
from Gallery_of_Graphs.graph import Graph

class ManyTests(UnitTests):
    def test_example(self):
        self._act_assert('G-ex', 2)

    def test_individuals(self):
        self._act_assert('P3-0', 1)
        self._act_assert('P3-1', 0)
        self._act_assert('K3-0', 1)
        self._act_assert('K3-1', 1)
        self._act_assert('K3-2', 0)

    def test_word_graphs(self):
        self._act_assert('rusty-1-17', 1)
        self._act_assert('common-1-20', -1)

    def test_grids(self):
        self._act_assert('grid-5-0', 8)
    
    def test_walls(self):
        self._act_assert('wall-p-1', 1)
        self._act_assert('wall-p-3', 1)
        self._act_assert('wall-z-3', 0)
        self._act_assert('wall-n-2', 0)

    def test_ski(self):
        self._act_assert('ski-illustration', 1)

    def test_increase(self):
        self._act_assert('increase-n8-1', 2)
        self._act_assert('increase-n8-2', 1)

    
    ###     Helper functions     ###
    def _solve(self, g : Graph):
        return g.solve_many()

if __name__ == '__main__':
    unittest.main()