import sys
import unittest

from tests_superclass import UnitTests

sys.path.append('../src')
from Gallery_of_Graphs.graph import Graph
from Utils.graph_factory import construct_graph
from Utils.negative_dijkstra import NegativeDijkstra

class SomeTests(UnitTests):
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
        self.solutionType = 'Some'
        return g.solve_some()

    def _get_failure_str(self, file_name, actual, expected, g):
        return f"\n\n{file_name} gave {actual} but should have given {expected}.\nPath found = {SomeTests._get_path(g)}\nDistances found = \n{SomeTests._get_distTo(g)}\n\nGraph details:\n{g}"
    
    def _get_path(g : Graph):
        return NegativeDijkstra(g).path_to_str(g.end)
    
    def _get_distTo(g : Graph):
        dij = NegativeDijkstra(g)
        node_ids = [_id for _id in range(g.node_amount)]
        node_originals = g.ids_to_nodes(node_ids)
        distTo = [str(dist) if dist != sys.maxsize else '_infinite_' for dist in dij.distTo]
        return '\n'.join([f"    - {distTo[_id]} distance to {node_originals[_id]}" for _id in node_ids])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)