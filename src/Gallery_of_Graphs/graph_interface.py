class IGraph:
    def __init__(self, input_lines : list[str]):
        self.node_amount : int
        self.edge_amount : int
        self.red_amount : int        
        self.node_colours : list[bool]
        self.start : int
        self.end : int
        self.edges : list[list[int]]

    def __str__(self) -> str:
        pass
        
    def solve_none(self) -> int:
        pass

    def solve_some(self) -> bool:
        pass

    def solve_many(self) -> int:
        pass

    def solve_few(self) -> int:
        pass

    def solve_alternate(self) -> bool:
        pass
    
    def node_to_id(self, node_str) -> int:
        pass
        
    def ids_to_nodes(self, node_id : int) -> list[str]:
        pass
        
