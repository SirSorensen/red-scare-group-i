

class Graph:
    def __init__(self, input_lines : list[str]):
        # node_amount = n = number of nodes
        # edge_amount = m = number of edges
        # red_amount = number of red nodes
        self.node_amount, self.edge_amount, self.red_amount = map(int, input_lines[0].split())

        # start = s = index of starting node
        # end = t = index of ending node
        self.start, self.end = map(int, input_lines[1].split())

        node_inputs = input_lines[2:2+self.node_amount]
        self.node_colours = [(s[-1] == '*') for s in node_inputs]
        
        
        self.edges = [[] for _ in range(self.edge_amount)]
        edge_inputs = [s.split() for s in input_lines[3+self.node_amount:]]
        for input in edge_inputs:
            e_s = int(input[0])
            e_t = int(input[2])
            arrow = input[1]
            if arrow == "--":
                self.edges[e_s].append(e_t)
                self.edges[e_t].append(e_s)
            elif arrow == "->":
                self.edges[e_s].append(e_t)
            elif arrow == "<-": # Does not seem to happen ever
                self.edges[e_t].append(e_s)
            else:
                raise ValueError("Edge arrow not recognised.")

    def __str__(self) -> str:
        edges_str = ""
        for i in range(self.edge_amount):
            for dest_node in self.edges[i]:
                edges_str += f"\n   {i} -> {dest_node}"
        
        s = f"This graph has {self.node_amount} nodes, {self.edge_amount} edges, and {self.red_amount} red nodes.\n"
        s += f"Node colours (True if red, False if black) :\n   {self.node_colours}\n"
        s += f"Edges : {edges_str}"
        return s
        


    