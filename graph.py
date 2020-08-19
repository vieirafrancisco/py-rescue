from settings import *

def memset(keys, value=False):
    intr = {}
    for key in keys:
        intr[key] = value
    return intr

class GraphControl:
    def __init__(self):
        self.graph = None

    def update(self, block_group):
        self.graph = Graph()
        # add nodes
        for block in block_group.matrix:
            self.graph.add_node(block.pos)
        # create edges
        for block in block_group.matrix:
            x, y = block.pos
            directions = filter(
                lambda pos: 0 <= pos[0] < COLUMNS and 0 <= pos[1] < ROWS,
                    [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
            ) 
            for ax, ay in directions:
                adjacent_block = block_group.get_block_by_position(ax, ay)
                if adjacent_block.color == block.color:
                    self.graph.create_edge(block.pos, adjacent_block.pos)

    def event_update(self, mx, my):
        result = []
        group = self.graph.dfs((mx, my))
        if len(group) > 1:
            for x, y in group:
                result.append((x, y))
        return result

class Graph:
    def __init__(self):
        self.graph = {}
        self.visited = {}

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

    def create_edge(self, n1, n2):
        self.add_nodes([n1, n2])
        if n1 not in self.graph[n2]:
            self.graph[n1].append(n2)
            self.graph[n2].append(n1)

    def add_nodes(self, node_list):
        for node in node_list:
            self.add_node(node)

    def add_node(self, node):
        if not self.has_node(node):
            self.graph[node] = []

    def get_adjacent(self, node):
        if self.has_node(node):
            return self.graph[node]
        raise Exception(f"Node {node} doesn't exist!")

    def dfs(self, v):
        if self.is_empty:
            raise Exception("Graph not has nodes!")
        self.visited = memset(self.graph.keys())
        stack = []
        return self.dfs_util(v, stack)

    def dfs_util(self, v, stack):
        self.visited[v] = True
        stack.append(v)
        for u in self.graph[v]:
            if not self.visited[u]:
                self.dfs_util(u, stack)
        return stack