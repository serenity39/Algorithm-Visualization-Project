import networkx as nx


class DiGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_node(self, node):
        self.graph.add_node(node)

    def add_edge(self, from_node, to_node, weight):
        self.graph.add_edge(from_node, to_node, weight=weight)

    def get_graph(self):
        return self.graph
