import sys
import unittest

from tests_superclass import UnitTests

sys.path.append('../src')
from Gallery_of_Graphs.graph import Graph

class SomeTests(UnitTests):

    def test_directed_acyclic(self):
        self._act_assert('K3-1', True)
        self._act_assert('K3-2', False)
        self._act_assert('ski-illustration', True)
        self._act_assert('ski-level3-1', True)
        self._act_assert('ski-level5-3', False)
        self._act_assert('increase-n8-1', True)
        self._act_assert('increase-n8-2', True)
    
    def test_undirected_cyclic(self):
        self._act_assert('G-ex', True)
        self._act_assert('K3-0', True)
        self._act_assert('rusty-1-17', True)
        self._act_assert('grid-5-0', True)
        self._act_assert('wall-p-1', True)
        self._act_assert('wall-p-3', True)
        self._act_assert('wall-z-3', False)
        self._act_assert('wall-n-2', False)

        self._act_assert('common-1-100.txt', False)
        self._act_assert('dodecahedron.txt', True)
        self._act_assert('gnm-10-15-0.txt', True)
        self._act_assert('gnm-10-15-1.txt', True)
        self._act_assert('gnm-10-20-0.txt', True)
        self._act_assert('gnm-10-20-1.txt', True)
        self._act_assert('grid-5-1', True)
        self._act_assert('grid-5-2', True)
        self._act_assert('smallworld-3-0', True)
        self._act_assert('smallworld-3-1', True)
        self._act_assert('wall-p-2', True)
        self._act_assert('wall-z-1', True)
        self._act_assert('wall-z-2', False)
        self._act_assert('wall-n-1', True)
        self._act_assert('wall-n-3', False)

    def test_udirected_acyclic(self): 
        self._act_assert('P3-0', True)
        self._act_assert('P3-1', False)
        self._act_assert('common-1-20', False)
        self._act_assert('common-1-50', False)

    ### Helper methods ###
    def _solve(self, g : Graph):
        self.solutionType = 'Some'
        return g.solve_some()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)