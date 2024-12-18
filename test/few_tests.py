import sys
import unittest

from tests_superclass import UnitTests

sys.path.append('../src')
from Gallery_of_Graphs.graph import Graph
from Utils.graph_factory import construct_graph
from Utils.dijkstra import Dijkstra

class FewTests(UnitTests):
    def test_directed_cyclic(self):
        self._act_assert('K3-2 copy', 0)

    def test_directed_acyclic(self):
        self._act_assert('K3-1', 0)
        self._act_assert('K3-2', 0)
        self._act_assert('ski-illustration', 0)
        self._act_assert('increase-n8-1', 1)
        self._act_assert('increase-n8-2', 1)

    def test_undirected_cyclic(self):
        self._act_assert('G-ex', 0)
        self._act_assert('K3-0', 0)
        self._act_assert('rusty-1-17', 0)
        self._act_assert('grid-5-0', 0)
        self._act_assert('wall-p-1', 0)
        self._act_assert('wall-p-3', 0)
        self._act_assert('wall-z-3', 0)
        self._act_assert('wall-n-2', 0)

    def test_undirected_acyclic(self):
        self._act_assert('P3-0', 1)
        self._act_assert('P3-1', 0)
        self._act_assert('common-1-20', -1)

    
    ###     Helper functions     ###
    def _solve(self, g : Graph):
        self.solutionType = 'Few'
        return g.solve_few()
    
    def _get_failure_str(self, file_name, actual, expected, g):
        return f"\n\n{file_name} gave {actual} but should have given {expected}.\nPath found = {FewTests._get_path(g)}\nDistances found = \n{FewTests._get_distTo(g)}\n\nGraph details:\n{g}"
    
    def _get_path(g : Graph):
        return Dijkstra(g).path_to_str(g.end)
    
    def _get_distTo(g : Graph):
        dij = Dijkstra(g)
        node_ids = [_id for _id in range(g.node_amount)]
        node_originals = g.ids_to_nodes(node_ids)
        distTo = [str(dist) if dist != sys.maxsize else '_infinite_' for dist in dij.distTo]
        return '\n'.join([f"    - {distTo[_id]} distance to {node_originals[_id]}" for _id in node_ids])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)