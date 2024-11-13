import sys
import unittest

from tests_superclass import UnitTests

sys.path.append('../src')
from Gallery_of_Graphs.graph import Graph

class AlternateTests(UnitTests):

    def test_directed_cyclic(self):
        self._act_assert('K3-2 copy', False)

    def test_directed_acyclic(self):
        self._act_assert('K3-1', True)
        self._act_assert('K3-2', False)
        self._act_assert('ski-illustration', False)
        self._act_assert('increase-n8-1', True)
        self._act_assert('increase-n8-2', True)

    def test_udirected_cyclic(self):
        self._act_assert('G-ex', True)
        self._act_assert('K3-0', True)
        self._act_assert('rusty-1-17', False)
        self._act_assert('grid-5-0', True)
        self._act_assert('wall-p-1', False)
        self._act_assert('wall-p-3', False)
        self._act_assert('wall-z-3', False)
        self._act_assert('wall-n-2', False)

    def test_udirected_acyclic(self):
        self._act_assert('P3-0', True)
        self._act_assert('P3-1', False)
        self._act_assert('common-1-20', False)
        
    ### Helper methods ###
    def _solve(self, g : Graph):
        return g.solve_alternate()


if __name__ == '__main__':
    unittest.main()