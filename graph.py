class Graph:
    def __init__(self):
        self.graph = {}

    def has_node(self, node):
        if node in self.graph.keys():
            return True
        else:
            return False

    def add_node(self, node):
        self.graph[node] = []

    def create_edge(self, node1, node2):
        if not self.has_node(node1):
            self.graph[node1] = []
        if not self.has_node(node2):
            self.graph[node2] = []
        if node1 not in self.graph[node2]:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)

    def get_adjacent(self, node):
        if self.has_node(node):
            return self.graph[node]
        raise Exception(f"Node {node} doesn't exist!")