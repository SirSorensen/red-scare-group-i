import sys
import unittest

from tests_superclass import UnitTests

sys.path.append('../src')
from Gallery_of_Graphs.graph import Graph

class ManyTests(UnitTests):

    def test_directed_acyclic(self):
        self._act_assert('K3-1', 1)
        self._act_assert('K3-2', 0)
        self._act_assert('ski-illustration', 1)
        self._act_assert('ski-level3-1', 3)
        self._act_assert('ski-level5-3', 0)
        self._act_assert('increase-n8-1', 2)
        self._act_assert('increase-n8-2', 1)

    def test_undirected_acyclic(self):
        self._act_assert('P3-0', 1)
        self._act_assert('P3-1', 0)

    def test_cyclic(self):
        self._act_assert('common-1-20', '?')
        self._act_assert('common-1-50', '?')


    ###     Helper functions     ###
    def _solve(self, g : Graph):
        self.solutionType = 'Many'
        return g.solve_many()

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)