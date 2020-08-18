def memset(keys, value=False):
    intr = {}
    for key in keys:
        intr[key] = value
    return intr

class Graph:
    def __init__(self):
        self.graph = {}
        self.visited = {}
        self.group = []

    @property
    def is_empty(self):
        if len(self.graph.keys()) > 0:
            return False
        else:
            return True

    def has_node(self, node):
        if node in self.graph.keys():
            return True
        else:
            return False

    def add_node(self, node):
        self.graph[node] = []

    def remove_node(self, node):
        ...

    def create_edge(self, node1, node2):
        if not self.has_node(node1):
            self.graph[node1] = []
        if not self.has_node(node2):
            self.graph[node2] = []
        if node1 not in self.graph[node2]:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)

    def remove_edge(self, node1, node2):
        ...

    def get_adjacent(self, node):
        if self.has_node(node):
            return self.graph[node]
        raise Exception(f"Node {node} doesn't exist!")

    def dfs(self, v):
        if self.is_empty:
            raise Exception("Graph not has nodes!")
        self.visited = memset(self.graph.keys())
        self.group = []
        self.dfs_util(v)

    def dfs_util(self, v):
        self.visited[v] = True
        self.group.append(v)
        for u in self.graph[v]:
            if not self.visited[u]:
                self.dfs_util(u)